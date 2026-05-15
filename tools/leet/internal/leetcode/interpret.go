package leetcode

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"strconv"
)

// InterpretSolution hits the LeetCode "Run" endpoint
// (POST /problems/{slug}/interpret_solution/). Unlike Submit, this does
// NOT count toward the user's submission stats — it just runs the code
// against `dataInput` and returns stdout + expected stdout, exactly like
// the "Run" button in the LeetCode UI.
//
// dataInput should be the raw newline-separated input LeetCode expects
// (e.g. for Two Sum: "[2,7,11,15]\n9"). Pass an empty string to use the
// problem's default sample test case.
//
// Returns an opaque submission_id to feed into PollResult.
func (c *Client) InterpretSolution(ctx context.Context, slug, lang, code, dataInput string) (string, error) {
	if c.creds.Empty() {
		return "", errors.New("interpret requires auth — run 'leet auth'")
	}

	// Need question_id (numeric) for the POST body.
	q, err := c.QuestionData(ctx, slug)
	if err != nil {
		return "", err
	}
	qid, _ := strconv.Atoi(q.QuestionID)

	// If caller didn't supply input, fall back to LeetCode's sample test
	// case (the same string the "Run" button starts with).
	if dataInput == "" {
		dataInput = q.ExampleTestcases
	}

	body := map[string]any{
		"lang":        lang,
		"question_id": qid,
		"typed_code":  code,
		"data_input":  dataInput,
		"judge_type":  "small",
	}
	resp, err := c.http.R().
		SetContext(ctx).
		SetHeader("Referer", baseURL+"/problems/"+slug+"/").
		SetBody(body).
		Post("/problems/" + slug + "/interpret_solution/")
	if err != nil {
		return "", err
	}
	if resp.StatusCode() == 401 || resp.StatusCode() == 403 {
		return "", fmt.Errorf("interpret auth rejected (HTTP %d) — re-run 'leet auth'", resp.StatusCode())
	}
	if !resp.IsSuccess() {
		return "", fmt.Errorf("interpret HTTP %d: %s", resp.StatusCode(), truncate(resp.String(), 200))
	}
	// LeetCode returns {"interpret_id": "..."} or {"interpret_expected_id": "..."}
	// depending on the slug; older accounts get just {"submission_id": ...}.
	var data struct {
		InterpretID  json.Number `json:"interpret_id"`
		SubmissionID json.Number `json:"submission_id"`
	}
	if err := json.Unmarshal(resp.Body(), &data); err != nil {
		return "", fmt.Errorf("parse interpret response: %w", err)
	}
	id := data.InterpretID.String()
	if id == "" {
		id = data.SubmissionID.String()
	}
	if id == "" {
		return "", fmt.Errorf("no interpret_id in response: %s", truncate(resp.String(), 200))
	}
	return id, nil
}
