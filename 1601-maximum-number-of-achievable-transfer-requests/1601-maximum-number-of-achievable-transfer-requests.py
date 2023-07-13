class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        
      table = [0] * n
      ans = 0
      m = len(requests)

      def bt(index, selected):
        nonlocal ans
        if index == m:
          if max(table) == 0:
            ans = max(ans, selected)
          return

        f, t = requests[index]
        # if select
        table[f] -= 1
        table[t] += 1
        bt(index + 1, selected + 1)
        table[f] += 1
        table[t] -= 1
        # if not select
        bt(index + 1, selected)
      bt(0, 0)
      return ans