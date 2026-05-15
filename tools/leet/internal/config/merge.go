package config

// Merge overlays `over` onto `base`. Non-zero fields in `over` win;
// zero/empty fields in `over` leave `base` untouched. For slice fields
// (Categories, CategoryPriority, StrategyKinds) a non-nil `over` slice
// REPLACES `base` — we don't try to concatenate, because the priority
// order is significant and concatenation would silently change behavior.
//
// Layouts merge field-by-field: an override that fills in only
// `solution_pattern` for "legacy" keeps the other legacy fields intact.
func Merge(base *Config, over Config) {
	if over.DefaultLayout != "" {
		base.DefaultLayout = over.DefaultLayout
	}
	if over.Layout != "" {
		base.Layout = over.Layout
	}
	if over.AuthFile != "" {
		base.AuthFile = over.AuthFile
	}
	if over.Categories != nil {
		base.Categories = over.Categories
	}
	if over.FallbackCategory != "" {
		base.FallbackCategory = over.FallbackCategory
	}
	if over.CategoryPriority != nil {
		base.CategoryPriority = over.CategoryPriority
	}

	mergeLayout(&base.Layouts.Legacy, over.Layouts.Legacy)
	mergeLayout(&base.Layouts.Structured, over.Layouts.Structured)
	mergePaths(&base.Paths, over.Paths)
}

func mergeLayout(base *LayoutSpec, over LayoutSpec) {
	if over.FolderPattern != "" {
		base.FolderPattern = over.FolderPattern
	}
	if over.CategoryCase != "" {
		base.CategoryCase = over.CategoryCase
	}
	if over.SolutionPattern != "" {
		base.SolutionPattern = over.SolutionPattern
	}
	if over.TestPattern != "" {
		base.TestPattern = over.TestPattern
	}
	if over.NotePattern != "" {
		base.NotePattern = over.NotePattern
	}
	if over.TestImport != "" {
		base.TestImport = over.TestImport
	}
	if over.TestStyle != "" {
		base.TestStyle = over.TestStyle
	}
	if over.MetaFile != "" {
		base.MetaFile = over.MetaFile
	}
	if over.StrategyKinds != nil {
		base.StrategyKinds = over.StrategyKinds
	}
}

func mergePaths(base *PathsConfig, over PathsConfig) {
	if over.Python != "" {
		base.Python = over.Python
	}
	if over.Contest != "" {
		base.Contest = over.Contest
	}
	if over.JavaScript != "" {
		base.JavaScript = over.JavaScript
	}
	if over.Cpp != "" {
		base.Cpp = over.Cpp
	}
}
