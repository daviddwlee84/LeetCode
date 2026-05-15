package main

import (
	"fmt"
	"os"

	"github.com/daviddwlee84/LeetCode/tools/leet/internal/cli"
)

func main() {
	if err := cli.Root().Execute(); err != nil {
		fmt.Fprintln(os.Stderr, "leet:", err)
		os.Exit(1)
	}
}
