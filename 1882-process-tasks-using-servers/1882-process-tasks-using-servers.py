import heapq

class Solution:
    def assignTasks(self, servers, tasks):
        available = [(w, i) for i, w in enumerate(servers)]
        heapq.heapify(available)

        busy = []
        ans = []
        time = 0

        for j, task in enumerate(tasks):

            time = max(time, j)

            # Release servers that have completed their tasks
            while busy and busy[0][0] <= time:
                end, w, i = heapq.heappop(busy)
                heapq.heappush(available, (w, i))

            # If all servers are busy, jump forward in time
            if not available:
                time = busy[0][0]

                while busy and busy[0][0] <= time:
                    end, w, i = heapq.heappop(busy)
                    heapq.heappush(available, (w, i))

            # Select server with minimum weight, then index
            w, i = heapq.heappop(available)

            ans.append(i)

            # Server becomes free after processing this task
            heapq.heappush(busy, (time + task, w, i))

        return ans