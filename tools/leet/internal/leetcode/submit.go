package leetcode

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"strconv"
	"time"
)

// Submit POSTs code to /problems/{slug}/submit/ and returns the submission ID.
// Auth (LEETCODE_SESSION + csrftoken) is required.
func (c *Client) Submit(ctx context.Context, slug, lang, code string) (string, error) {
	if c.creds.Empty() {
		return "", errors.New("submit requires auth — run 'leet auth'")
	}

	// We need the numeric questionId to construct the submit body.
	q, err := c.QuestionData(ctx, slug)
	if err != nil {
		return "", err
	}
	qid, _ := strconv.Atoi(q.QuestionID)

	body := map[string]any{
		"lang":        lang,
		"question_id": qid,
		"typed_code":  code,
	}
	resp, err := c.http.R().
		SetContext(ctx).
		SetHeader("Referer", baseURL+"/problems/"+slug+"/").
		SetBody(body).
		Post("/problems/" + slug + "/submit/")
	if err != nil {
		return "", err
	}
	if resp.StatusCode() == 401 || resp.StatusCode() == 403 {
		return "", fmt.Errorf("submit auth rejected (HTTP %d) — re-run 'leet auth'", resp.StatusCode())
	}
	if !resp.IsSuccess() {
		return "", fmt.Errorf("submit HTTP %d: %s", resp.StatusCode(), truncate(resp.String(), 200))
	}
	var data struct {
		SubmissionID json.Number `json:"submission_id"`
	}
	if err := json.Unmarshal(resp.Body(), &data); err != nil {
		return "", fmt.Errorf("parse submit response: %w", err)
	}
	if data.SubmissionID == "" {
		return "", fmt.Errorf("no submission_id in response: %s", truncate(resp.String(), 200))
	}
	return data.SubmissionID.String(), nil
}

// PollResult polls /submissions/detail/{id}/check/ until state == "SUCCESS"
// or timeout. Polling interval starts at 600ms and backs off to 2s.
func (c *Client) PollResult(ctx context.Context, submissionID string) (SubmitResult, error) {
	deadline := time.Now().Add(60 * time.Second)
	delay := 600 * time.Millisecond
	for {
		select {
		case <-ctx.Done():
			return SubmitResult{}, ctx.Err()
		default:
		}
		resp, err := c.http.R().
			SetContext(ctx).
			Get("/submissions/detail/" + submissionID + "/check/")
		if err != nil {
			return SubmitResult{}, err
		}
		if !resp.IsSuccess() {
			return SubmitResult{}, fmt.Errorf("check HTTP %d", resp.StatusCode())
		}
		var r SubmitResult
		if err := json.Unmarshal(resp.Body(), &r); err != nil {
			return SubmitResult{}, fmt.Errorf("decode check: %w", err)
		}
		if r.State == "SUCCESS" || r.StatusMsg != "" && r.State == "" {
			return r, nil
		}
		if time.Now().After(deadline) {
			return SubmitResult{}, fmt.Errorf("submission %s still pending after timeout", submissionID)
		}
		time.Sleep(delay)
		if delay < 2*time.Second {
			delay = delay * 3 / 2
		}
	}
}
