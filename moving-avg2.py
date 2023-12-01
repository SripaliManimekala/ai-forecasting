N, W, K= map(int,input().split())
# data =[]
# for i in range(N):
#     data_point = int(input())
#     data.append(data_point)
data = [float(input()) for _ in range(N)]

for i in range(K):
    data.append(sum(data[-W:])/W)

print(data)