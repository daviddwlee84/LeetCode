// Package leetcode is a minimal client for the unofficial LeetCode GraphQL +
// REST submit endpoint. We intentionally keep it thin — the user's repo
// stays the source of truth, this just fetches problem data and ferries
// submissions.
package leetcode

import (
	"context"
	"encoding/json"
	"errors"
	"fmt"
	"net/http"
	"strconv"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/auth"
	"github.com/go-resty/resty/v2"
)

const (
	baseURL = "https://leetcode.com"
	gqlURL  = baseURL + "/graphql"
	ua      = "leet-cli/0.1 (+https://github.com/daviddwlee84/LeetCode)"
)

type Client struct {
	http  *resty.Client
	creds auth.Credentials
}

// NewClient returns a configured client. Missing creds are OK for public
// queries (daily, questionData) but submit/userStatus will fail.
func NewClient(c auth.Credentials) *Client {
	r := resty.New().
		SetBaseURL(baseURL).
		SetHeader("User-Agent", ua).
		SetHeader("Referer", baseURL+"/").
		SetHeader("Origin", baseURL).
		SetHeader("Content-Type", "application/json")
	cli := &Client{http: r, creds: c}
	cli.applyCookies()
	return cli
}

func (c *Client) applyCookies() {
	if c.creds.Empty() {
		return
	}
	c.http.SetCookies([]*http.Cookie{
		{Name: "LEETCODE_SESSION", Value: c.creds.Session, Domain: ".leetcode.com", Path: "/"},
		{Name: "csrftoken", Value: c.creds.CSRF, Domain: ".leetcode.com", Path: "/"},
	})
	c.http.SetHeader("X-Csrftoken", c.creds.CSRF)
}

type gqlEnvelope struct {
	Data   json.RawMessage  `json:"data"`
	Errors []map[string]any `json:"errors,omitempty"`
}

func (c *Client) gql(ctx context.Context, query, opName string, vars map[string]any, out any) error {
	body := map[string]any{
		"query":         query,
		"operationName": opName,
		"variables":     vars,
	}
	resp, err := c.http.R().
		SetContext(ctx).
		SetBody(body).
		Post(gqlURL)
	if err != nil {
		return err
	}
	if resp.StatusCode() == 401 || resp.StatusCode() == 403 {
		return fmt.Errorf("auth rejected (HTTP %d) — re-run 'leet auth'", resp.StatusCode())
	}
	if !resp.IsSuccess() {
		return fmt.Errorf("graphql HTTP %d: %s", resp.StatusCode(), truncate(resp.String(), 200))
	}
	var env gqlEnvelope
	if err := json.Unmarshal(resp.Body(), &env); err != nil {
		return fmt.Errorf("decode envelope: %w", err)
	}
	if len(env.Errors) > 0 {
		return fmt.Errorf("graphql errors: %v", env.Errors)
	}
	return json.Unmarshal(env.Data, out)
}

// DailyChallenge returns today's daily problem.
func (c *Client) DailyChallenge(ctx context.Context) (Question, error) {
	var data struct {
		Active struct {
			Date     string   `json:"date"`
			Link     string   `json:"link"`
			Question Question `json:"question"`
		} `json:"activeDailyCodingChallengeQuestion"`
	}
	if err := c.gql(ctx, queryDailyChallenge, "questionOfToday", nil, &data); err != nil {
		return Question{}, err
	}
	if data.Active.Question.TitleSlug == "" {
		return Question{}, errors.New("daily challenge response missing question")
	}
	return data.Active.Question, nil
}

// QuestionData fetches a single problem by titleSlug.
func (c *Client) QuestionData(ctx context.Context, slug string) (Question, error) {
	var data struct {
		Question Question `json:"question"`
	}
	err := c.gql(ctx, queryQuestionData, "questionData", map[string]any{"titleSlug": slug}, &data)
	if err != nil {
		return Question{}, err
	}
	if data.Question.TitleSlug == "" {
		return Question{}, fmt.Errorf("question %q not found", slug)
	}
	return data.Question, nil
}

// UserStatus returns the auth state.
func (c *Client) UserStatus(ctx context.Context) (UserStatus, error) {
	var data struct {
		UserStatus UserStatus `json:"userStatus"`
	}
	err := c.gql(ctx, queryUserStatus, "globalData", nil, &data)
	return data.UserStatus, err
}

// QuestionSlugByID searches the problemset list for a given frontend ID and
// returns its titleSlug. We use a narrow filter so the response is small.
func (c *Client) QuestionSlugByID(ctx context.Context, id int) (string, error) {
	var data struct {
		List struct {
			Questions []struct {
				TitleSlug          string `json:"titleSlug"`
				QuestionFrontendID string `json:"questionFrontendId"`
			} `json:"questions"`
		} `json:"problemsetQuestionList"`
	}
	vars := map[string]any{
		"categorySlug": "",
		"limit":        5,
		"skip":         0,
		"filters": map[string]any{
			"searchKeywords": strconv.Itoa(id),
		},
	}
	if err := c.gql(ctx, queryQuestionTitleByID, "problemsetQuestionList", vars, &data); err != nil {
		return "", err
	}
	want := strconv.Itoa(id)
	for _, q := range data.List.Questions {
		if q.QuestionFrontendID == want {
			return q.TitleSlug, nil
		}
	}
	return "", fmt.Errorf("no question with frontend ID %d found", id)
}

func truncate(s string, n int) string {
	if len(s) <= n {
		return s
	}
	return s[:n] + "…"
}
