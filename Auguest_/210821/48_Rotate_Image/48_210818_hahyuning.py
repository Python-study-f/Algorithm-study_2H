class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        p_size = min(n, m) // 2
        partitions = []

        for k in range(p_size):
            tmp = []
            # 윗변
            for j in range(k, m - k):
                tmp.append(matrix[k][j])
            # 오른변
            for i in range(k + 1, n - 1 - k):
                tmp.append(matrix[i][m - 1 - k])
            # 아랫변
            for j in range(m - 1 - k, k, -1):
                tmp.append(matrix[n - 1 - k][j])
            # 왼변
            for i in range(n - 1 - k, k, -1):
                tmp.append(matrix[i][k])

            partitions.append(tmp)

        for k in range(p_size):
            tmp = partitions[k]
            t_size = len(tmp)
            t_idx = -(n - 1 - 2 * k)

            # 윗변
            for j in range(k, m - k):
                matrix[k][j] = tmp[t_idx]
                t_idx = (t_idx + 1) % t_size
            # 오른변
            for i in range(k + 1, n - 1 - k):
                matrix[i][m - 1 - k] = tmp[t_idx]
                t_idx = (t_idx + 1) % t_size
            # 아랫변
            for j in range(m - 1 - k, k, -1):
                matrix[n - 1 - k][j] = tmp[t_idx]
                t_idx = (t_idx + 1) % t_size
            # 왼변
            for i in range(n - 1 - k, k, -1):
                matrix[i][k] = tmp[t_idx]
                t_idx = (t_idx + 1) % t_size

        return matrix