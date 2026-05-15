// Package categories maps LeetCode topic tags to the directory layout this
// repo has used since 2018:
//
//	Python3/{Category}/{ProblemName}/
//
// The priority table now lives in internal/config (see defaults.go). This
// package is a thin shim that PickFromConfig uses; PickCategory remains as a
// zero-config helper for callers (and existing tests) that want the
// built-in defaults.
package categories

import (
	"strings"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/config"
)

// Fallback is the category folder used when no priority entry matches.
// Kept exported for backward compatibility with any external callers.
const Fallback = "AdHoc"

// PickFromConfig walks cfg.CategoryPriority in order; the first entry whose
// tag substring matches one of the provided LeetCode tags wins. Returns
// cfg.FallbackCategory (or "AdHoc" if empty) when nothing matches.
func PickFromConfig(cfg config.Config, tags []string) string {
	fallback := cfg.FallbackCategory
	if fallback == "" {
		fallback = Fallback
	}
	if len(tags) == 0 {
		return fallback
	}
	lower := make([]string, len(tags))
	for i, t := range tags {
		lower[i] = strings.ToLower(strings.TrimSpace(t))
	}
	for _, p := range cfg.CategoryPriority {
		needle := strings.ToLower(p.Tag)
		for _, t := range lower {
			if strings.Contains(t, needle) {
				return p.Dir
			}
		}
	}
	return fallback
}

// PickCategory is a thin wrapper using built-in defaults. Existing Phase 1
// callers stay working without threading a Config through.
func PickCategory(tags []string) string {
	return PickFromConfig(config.Defaults(), tags)
}
