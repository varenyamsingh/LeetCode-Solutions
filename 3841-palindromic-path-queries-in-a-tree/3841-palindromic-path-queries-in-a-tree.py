
class Solution:
    def palindromePath(self, n, edges, s, queries):
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        parent = [-1] * n
        depth = [0] * n
        order = [0]
        parent[0] = 0

        for u in order:
            for v in adj[u]:
                if v == parent[u]:
                    continue
                parent[v] = u
                depth[v] = depth[u] + 1
                order.append(v)

        size = [1] * n
        heavy = [-1] * n

        for u in reversed(order):
            best = 0
            for v in adj[u]:
                if parent[v] == u:
                    size[u] += size[v]
                    if size[v] > best:
                        best = size[v]
                        heavy[u] = v

        head = [0] * n
        pos = [0] * n
        timer = 0
        stack = [(0, 0)]

        while stack:
            u, h = stack.pop()

            while u != -1:
                head[u] = h
                pos[u] = timer
                timer += 1

                for v in adj[u]:
                    if parent[v] == u and v != heavy[u]:
                        stack.append((v, v))

                u = heavy[u]

        base = [0] * n
        chars = list(s)

        for u in range(n):
            base[pos[u]] = 1 << (ord(chars[u]) - 97)

        seg_size = 1
        while seg_size < n:
            seg_size *= 2

        tree = [0] * (2 * seg_size)

        for i in range(n):
            tree[seg_size + i] = base[i]

        for i in range(seg_size - 1, 0, -1):
            tree[i] = tree[2 * i] ^ tree[2 * i + 1]

        def update(u, c):
            chars[u] = c
            i = seg_size + pos[u]
            tree[i] = 1 << (ord(c) - 97)

            i //= 2
            while i:
                tree[i] = tree[2 * i] ^ tree[2 * i + 1]
                i //= 2

        def range_xor(l, r):
            l += seg_size
            r += seg_size
            result = 0

            while l <= r:
                if l & 1:
                    result ^= tree[l]
                    l += 1

                if not (r & 1):
                    result ^= tree[r]
                    r -= 1

                l //= 2
                r //= 2

            return result

        def path_xor(u, v):
            result = 0

            while head[u] != head[v]:
                if depth[head[u]] < depth[head[v]]:
                    u, v = v, u

                result ^= range_xor(pos[head[u]], pos[u])
                u = parent[head[u]]

            if depth[u] > depth[v]:
                u, v = v, u

            result ^= range_xor(pos[u], pos[v])
            return result

        answer = []

        for q in queries:
            parts = q.split()

            if parts[0] == "update":
                update(int(parts[1]), parts[2])
            else:
                u = int(parts[1])
                v = int(parts[2])

                mask = path_xor(u, v)
                answer.append((mask & (mask - 1)) == 0)

        return answer
