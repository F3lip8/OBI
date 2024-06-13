N, K = [int(i) for i in input().split()]

A = [int(j) for j in input().split()]
A.sort(reverse=True)

print(A[K - 1])