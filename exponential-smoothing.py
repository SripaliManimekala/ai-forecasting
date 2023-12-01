N, alpha, K = map(float, input().split())
data = [float(input()) for _ in range(int(N))]
data_smoothed=[data[0]]

for i in range(K):
    smoothed_value = alpha * data[i] + (1 - alpha) * data_smoothed[i]
    data_smoothed.append(smoothed_value)

print(data)
print(data_smoothed)
