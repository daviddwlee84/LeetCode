class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path_list = path.split('/')

        for curr_path in path_list:
            if curr_path == '' or curr_path == '.':
                continue
            elif curr_path == '..':
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(curr_path)

        return '/' + '/'.join(stack)

# Runtime: 24 ms, faster than 97.99% of Python3 online submissions for Simplify Path.
# Memory Usage: 12.7 MB, less than 100.00% of Python3 online submissions for Simplify Path.
