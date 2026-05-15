package config

// Defaults returns the built-in baseline config. These values are what
// Phase 1 hardcoded; the priority table here was previously in
// internal/categories/map.go.
//
// IMPORTANT: keep this in sync with the historical conventions of this
// repo. Tests in this package (and the smoke test in Phase 2.B3) assert
// that loading config in a repo with no `.leet/config.toml` produces
// exactly the same scaffolding as Phase 1 did.
func Defaults() Config {
	return Config{
		DefaultLayout:    "legacy", // safest default — preserves 2018 behavior
		AuthFile:         "",       // resolves via store.go's UserConfigDir if empty
		Categories:       defaultCategories(),
		FallbackCategory: "AdHoc",
		CategoryPriority: defaultPriority(),
		Layouts: LayoutMap{
			Legacy:     legacyLayout(),
			Structured: structuredLayout(),
		},
		Paths: PathsConfig{
			Python:     "Python3",
			Contest:    "Contest/LeetCodeWeeklyContest",
			JavaScript: "JavaScript",
			Cpp:        "Cpp",
		},
	}
}

func defaultCategories() []string {
	return []string{
		"Array",
		"BinaryTree",
		"BitManipulation",
		"Design",
		"DynamicProgramming",
		"Graph",
		"Interactive",
		"LinkedList",
		"Math",
		"Search",
		"String",
		"AdHoc",
	}
}

// defaultPriority preserves the order Phase 1 used (see Phase 1's
// internal/categories/map.go — moved here intact so behavior is identical).
func defaultPriority() []TagDirEntry {
	return []TagDirEntry{
		{Tag: "Linked List", Dir: "LinkedList"},
		{Tag: "Binary Search Tree", Dir: "BinaryTree"},
		{Tag: "Binary Tree", Dir: "BinaryTree"},
		{Tag: "Tree", Dir: "BinaryTree"},
		{Tag: "Graph", Dir: "Graph"},
		{Tag: "Depth-First Search", Dir: "Graph"},
		{Tag: "Breadth-First Search", Dir: "Graph"},
		{Tag: "Topological Sort", Dir: "Graph"},
		{Tag: "Union Find", Dir: "Graph"},
		{Tag: "Dynamic Programming", Dir: "DynamicProgramming"},
		{Tag: "Memoization", Dir: "DynamicProgramming"},
		{Tag: "Bit Manipulation", Dir: "BitManipulation"},
		{Tag: "Bitmask", Dir: "BitManipulation"},
		{Tag: "Binary Search", Dir: "Search"},
		{Tag: "Math", Dir: "Math"},
		{Tag: "Number Theory", Dir: "Math"},
		{Tag: "Geometry", Dir: "Math"},
		{Tag: "Combinatorics", Dir: "Math"},
		{Tag: "Design", Dir: "Design"},
		{Tag: "Linked List Design", Dir: "Design"},
		{Tag: "Interactive", Dir: "Interactive"},
		{Tag: "String", Dir: "String"},
		{Tag: "String Matching", Dir: "String"},
		{Tag: "Trie", Dir: "String"},
		{Tag: "Array", Dir: "Array"},
		{Tag: "Matrix", Dir: "Array"},
		{Tag: "Hash Table", Dir: "Array"},
		{Tag: "Hash Function", Dir: "Array"},
	}
}

func legacyLayout() LayoutSpec {
	return LayoutSpec{
		FolderPattern:   "{title_pascal}",
		CategoryCase:    "", // preserve (PascalCase as stored in Categories)
		SolutionPattern: "{strategy}{id}.py",
		TestPattern:     "test_{id}.py",
		NotePattern:     "Note{id}.md",
		TestImport:      "from {strategy}{id} import Solution as {strategy}",
		TestStyle:       "per_strategy",
		MetaFile:        "",
	}
}

func structuredLayout() LayoutSpec {
	return LayoutSpec{
		FolderPattern:   "{title_kebab}",
		CategoryCase:    "lower",
		SolutionPattern: "{strategy_snake}.py",
		TestPattern:     "test.py",
		NotePattern:     "README.md",
		TestImport:      "from {strategy_snake} import Solution as {strategy_camel}",
		TestStyle:       "parametrize",
		MetaFile:        "meta.json",
		StrategyKinds:   []string{"own", "reference", "archive"},
	}
}
