N, alpha = map(float, input().split())
data = [float(input()) for _ in range(int(N))]
data_smoothed=[data[0]]

for i in range(int(N)):
    smoothed_value = alpha * data[i] + (1 - alpha) * data_smoothed[i-1]
    data_smoothed.append(smoothed_value)

print(data)
print(data_smoothed)
