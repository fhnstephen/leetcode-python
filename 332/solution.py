from queue import PriorityQueue
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
      edges = {}
      for ticket in tickets:
        if not ticket[0] in edges:
          edges[ticket[0]] = PriorityQueue()
        edges[ticket[0]].put(ticket[1])
      ans = []
      def dfs(x = 'JFK'):
        if x in edges:
          edge = edges[x]
          while not edge.empty():
            next_edge = edge.get()
            dfs(next_edge)
        ans.append(x)
      dfs()
      ans.reverse()
      return ans
