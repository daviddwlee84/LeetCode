class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []

        for item in path.split('/'):
            if item == '' or item == '.':
                continue
            elif item == '..':
                if stack:
                    stack.pop()
            else:
                stack.append(item)

        if not stack:
            return '/'

        ans = ''
        for item in stack:
            ans += f'/{item}'
        return ans
