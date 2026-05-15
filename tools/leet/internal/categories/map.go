// Package categories maps LeetCode topic tags to the directory layout this
// repo has used since 2018:
//
//	Python3/{Category}/{ProblemName}/
//
// The repo's 12 historical categories are: Array, BinaryTree, BitManipulation,
// Design, DynamicProgramming, Graph, Interactive, LinkedList, Math, Search,
// String, AdHoc.
package categories

import "strings"

const Fallback = "AdHoc"

// priority is intentionally ordered. PickCategory walks problem tags in the
// order LeetCode returns them, but for each tag it consults this list — the
// first table entry whose tag substring matches wins. This means stronger
// signals (e.g. "Linked List") beat weaker ones ("Hash Table") when a problem
// has both, which matches how the user has historically filed problems.
var priority = []struct{ Tag, Dir string }{
	{"Linked List", "LinkedList"},
	{"Binary Search Tree", "BinaryTree"},
	{"Binary Tree", "BinaryTree"},
	{"Tree", "BinaryTree"},
	{"Graph", "Graph"},
	{"Depth-First Search", "Graph"},
	{"Breadth-First Search", "Graph"},
	{"Topological Sort", "Graph"},
	{"Union Find", "Graph"},
	{"Dynamic Programming", "DynamicProgramming"},
	{"Memoization", "DynamicProgramming"},
	{"Bit Manipulation", "BitManipulation"},
	{"Bitmask", "BitManipulation"},
	{"Binary Search", "Search"},
	{"Math", "Math"},
	{"Number Theory", "Math"},
	{"Geometry", "Math"},
	{"Combinatorics", "Math"},
	{"Design", "Design"},
	{"Linked List Design", "Design"},
	{"Interactive", "Interactive"},
	{"String", "String"},
	{"String Matching", "String"},
	{"Trie", "String"},
	{"Array", "Array"},
	{"Matrix", "Array"},
	{"Hash Table", "Array"},
	{"Hash Function", "Array"},
}

// PickCategory chooses a folder for a problem given LeetCode's topic tags.
//
// Algorithm: walk the priority table in order; for each entry, check if any
// of the input tags contains that entry's tag (case-insensitive). The first
// priority entry with a hit wins. This means structural categories like
// "Linked List" or "Binary Tree" beat looser auxiliary tags like "Hash
// Table" regardless of which order LeetCode happened to list them in.
//
// Returns Fallback ("AdHoc") if nothing matches — covers greedy / two
// pointer / backtracking problems that don't have a dedicated folder.
func PickCategory(tags []string) string {
	if len(tags) == 0 {
		return Fallback
	}
	lower := make([]string, len(tags))
	for i, t := range tags {
		lower[i] = strings.ToLower(strings.TrimSpace(t))
	}
	for _, p := range priority {
		needle := strings.ToLower(p.Tag)
		for _, t := range lower {
			if strings.Contains(t, needle) {
				return p.Dir
			}
		}
	}
	return Fallback
}
