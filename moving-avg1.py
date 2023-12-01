N, W, K= map(int,input().split())

data = list(map(int,input().split()))

next_data_point = sum(data[-W:])/W

print(next_data_point)