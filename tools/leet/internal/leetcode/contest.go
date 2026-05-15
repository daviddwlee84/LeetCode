package leetcode

import (
	"context"
	"encoding/json"
	"fmt"
	"strconv"
	"strings"
)

// LatestContestNumber returns the most recent weekly or biweekly contest
// number. We hit the contest list page's API endpoint (no auth required).
//
// Implementation note: LeetCode exposes /contest/api/info?slug= for known
// slugs but listing is via the contest schedule. We use a pragmatic approach:
// fetch the upcoming contest list and look at the latest numbered slug.
func (c *Client) LatestContestNumber(ctx context.Context, kind string) (int, error) {
	// GraphQL query for contest history / upcoming.
	const q = `query upcomingContests {
  upcomingContests { title titleSlug startTime }
  brightTitle: pastContests { data { title titleSlug } }
}`
	var data struct {
		Upcoming []struct {
			Title     string `json:"title"`
			TitleSlug string `json:"titleSlug"`
		} `json:"upcomingContests"`
	}
	// We don't strictly need the past-contest slot; ignore errors there.
	_ = c.gql(ctx, q, "upcomingContests", nil, &data)

	prefix := "weekly-contest-"
	if kind == "biweekly" {
		prefix = "biweekly-contest-"
	}
	best := 0
	for _, u := range data.Upcoming {
		if !strings.HasPrefix(u.TitleSlug, prefix) {
			continue
		}
		n, err := strconv.Atoi(strings.TrimPrefix(u.TitleSlug, prefix))
		if err != nil {
			continue
		}
		if n > best {
			best = n
		}
	}
	if best > 0 {
		// "Upcoming" — caller probably wants the most recent finished one.
		// Subtract one biweekly = 2 weeks back; weekly = 1 week back.
		return best - 1, nil
	}
	return 0, fmt.Errorf("could not determine latest %s contest from API; pass an explicit number", kind)
}

// Contest fetches contest metadata + each problem's full Question payload.
func (c *Client) Contest(ctx context.Context, slug string) (Contest, error) {
	contest := Contest{Slug: slug, Kind: "weekly"}
	if strings.HasPrefix(slug, "biweekly-contest-") {
		contest.Kind = "biweekly"
		nstr := strings.TrimPrefix(slug, "biweekly-contest-")
		if n, err := strconv.Atoi(nstr); err == nil {
			contest.Number = n
		}
	} else if strings.HasPrefix(slug, "weekly-contest-") {
		nstr := strings.TrimPrefix(slug, "weekly-contest-")
		if n, err := strconv.Atoi(nstr); err == nil {
			contest.Number = n
		}
	}

	// REST endpoint: /contest/api/info/{slug}/ — public JSON.
	resp, err := c.http.R().
		SetContext(ctx).
		Get("/contest/api/info/" + slug + "/")
	if err != nil {
		return contest, err
	}
	if !resp.IsSuccess() {
		return contest, fmt.Errorf("contest info HTTP %d", resp.StatusCode())
	}
	var info struct {
		Contest struct {
			Title     string `json:"title"`
			TitleSlug string `json:"title_slug"`
		} `json:"contest"`
		Questions []struct {
			Title     string `json:"title"`
			TitleSlug string `json:"title_slug"`
		} `json:"questions"`
	}
	if err := json.Unmarshal(resp.Body(), &info); err != nil {
		return contest, fmt.Errorf("parse contest info: %w", err)
	}
	contest.Title = info.Contest.Title
	if contest.Title == "" {
		contest.Title = slug
	}

	for i, qmeta := range info.Questions {
		entry := ContestEntry{
			Index: i + 1,
			Slug:  qmeta.TitleSlug,
			Title: qmeta.Title,
		}
		// Best-effort fetch of full question data — public queries succeed
		// only after the contest starts; before that, skip silently.
		if q, err := c.QuestionData(ctx, qmeta.TitleSlug); err == nil {
			entry.Question = q
		}
		contest.Problems = append(contest.Problems, entry)
	}
	if len(contest.Problems) == 0 {
		return contest, fmt.Errorf("contest %s returned 0 problems (may not have started yet)", slug)
	}
	return contest, nil
}
