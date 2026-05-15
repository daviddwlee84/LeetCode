package categories

import "testing"

func TestPickCategory(t *testing.T) {
	cases := []struct {
		name string
		tags []string
		want string
	}{
		{"empty falls back", nil, "AdHoc"},
		{"unknown tag falls back", []string{"Greedy", "Two Pointers"}, "AdHoc"},
		{"linked list wins over hash", []string{"Hash Table", "Linked List"}, "LinkedList"},
		{"BST is tree", []string{"Binary Search Tree"}, "BinaryTree"},
		{"DFS is graph", []string{"Depth-First Search", "Recursion"}, "Graph"},
		{"DP wins", []string{"Dynamic Programming", "Array"}, "DynamicProgramming"},
		{"bitmask -> bit manipulation", []string{"Bitmask"}, "BitManipulation"},
		{"binary search -> Search", []string{"Binary Search"}, "Search"},
		{"matrix -> array", []string{"Matrix"}, "Array"},
		{"hash table only -> array", []string{"Hash Table"}, "Array"},
		{"string + array -> string (first match)", []string{"String", "Array"}, "String"},
		{"math wins over array", []string{"Math", "Array"}, "Math"},
		{"trie -> string", []string{"Trie"}, "String"},
		{"interactive", []string{"Interactive"}, "Interactive"},
		{"design", []string{"Design"}, "Design"},
		{"case insensitive", []string{"binary search"}, "Search"},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			got := PickCategory(c.tags)
			if got != c.want {
				t.Errorf("PickCategory(%v) = %q, want %q", c.tags, got, c.want)
			}
		})
	}
}
