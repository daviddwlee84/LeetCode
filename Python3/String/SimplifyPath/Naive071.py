class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        for item in path.split('/'):
            if item in ['.', '']:
                continue
            elif item == '..':
                if stack:
                    # "/../"
                    stack.pop()
            else:
                stack.append(item)

        return '/' + '/'.join(stack)
