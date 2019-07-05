# 752. Open the Lock

You have a lock in front of you with 4 circular wheels. Each wheel has 10 slots: `'0', '1', '2', '3', '4', '5', '6', '7', '8', '9'`. The wheels can rotate freely and wrap around: for example we can turn `'9'` to be `'0'`, or `'0'` to be `'9'`. Each move consists of turning one wheel one slot.

The lock initially starts at `'0000'`, a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, the wheels of the lock will stop turning and you will be unable to open it.

Given a `target` representing the value of the wheels that will unlock the lock, return the minimum total number of turns required to open the lock, or -1 if it is impossible.

**Example 1**:

```txt
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation:
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".
```

**Example 2**:

```txt
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation:
We can turn the last wheel in reverse to move from "0000" -> "0009".
```

**Example 3**:

```txt
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation:
We can't reach the target without getting stuck.
```

**Example 4**:

```txt
Input: deadends = ["0000"], target = "8888"
Output: -1
Note:
The length of deadends will be in the range [1, 500].
target will not be in the list deadends.
Every string in deadends and the string target will be a string of 4 digits from the 10,000 possibilities '0000' to '9999'.
```

## Solution

### BFS

## Other's solution

### Start from target and Early stop (fastest)

```py
class Solution:
    def openLock(self, deadends: 'List[str]', target: 'str') -> 'int':
        def dist(code):
            return sum(min(int(c), 10-int(c)) for c in code)

        def neighbors(code):
            temp = []
            for i in range(4):
                pre, x, sur = code[:i], int(code[i]), code[i:]
                temp.append( code[:i] + str((x - 1) % 10) + code[i + 1:])
                temp.append( code[:i] + str((x + 1) % 10) + code[i + 1:])
            return temp

        dead = set(deadends)
        if '0000' in dead or target in dead: return -1
        last_moves = set(neighbors(target)) - dead
        if not last_moves: return -1
        ans = dist(target)
        for code in last_moves:
            if dist(code) < ans: return ans
        return ans + 2
```

### BFS

```py
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if '0000' in dead:
            return -1
        neighbors = set(self.adjacent(target))
        if neighbors & dead == neighbors:
            return -1
        visited = set()
        queue = collections.deque(['0000'])
        visited.add('0000')
        step = 0
        while queue:
            step += 1
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur == target:
                    return step - 1
                for n in self.adjacent(cur):
                    if n in dead or n in visited:
                        continue
                    queue.append(n)
                    visited.add(n)

    def adjacent(self, cur):
        res = []
        for i in range(4):
            left, mid, right = cur[:i], int(cur[i]), cur[i+1:]
            for m in [(mid + 1) % 10, (mid - 1) % 10]:
                res.append(left + str(m) + right)
        return res
```

```java
class Solution {
    public int openLock(String[] deadends, String target) {
        Queue<String> q = new LinkedList<>();
        Set<String> deads = new HashSet<>(Arrays.asList(deadends));
        Set<String> visited = new HashSet<>();
        q.offer("0000");
        visited.add("0000");
        int level = 0;
        while(!q.isEmpty()) {
            int size = q.size();
            for(int n = 0; n < size; n++) {
                String s = q.poll();
                if(deads.contains(s)) continue;
                if(s.equals(target)) return level;

                for(int i = 0; i < 4; i++) { // all 4 positions, go one number above, one below
                    char c = s.charAt(i);
                    String prefix = s.substring(0, i), postfix = s.substring(i + 1);
                    addToQueue(q, getNextValue(s, c, prefix, postfix, true), visited, deads);
                    addToQueue(q, getNextValue(s, c, prefix, postfix, false), visited, deads);
                }
            }
            level ++;
        }
        return -1;
    }

    private String getNextValue(String s, char c, String prefix, String postfix, boolean previous) {
        if(previous) return  prefix + (c == '9' ? 0 : c - '0' + 1) + postfix;
        return prefix + (c == '0' ? 9 : c - '0' - 1) + postfix;
    }
    private void addToQueue(Queue<String> q, String str, Set<String> visited, Set<String> deads) {
        if(!visited.contains(str) && !deads.contains(str)) {
            q.offer(str);
            visited.add(str);
        }
    }
}
```
