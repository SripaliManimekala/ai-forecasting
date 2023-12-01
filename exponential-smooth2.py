# Assuming you have a list of true sales data for the first 12 months
true_sales_data = [100, 120, 90, 110, 105, 95, 115, 125, 130, 120, 140, 150]

# Set the smoothing factor (alpha)
alpha = 0.2

# Use exponential smoothing to predict the next 12 months iteratively
predicted_values = true_sales_data.copy()  # Initialize with the true sales data

for _ in range(12):
    next_prediction = alpha * true_sales_data[-1] + (1 - alpha) * predicted_values[-1]
    predicted_values.append(next_prediction)

print("True Sales Data:", true_sales_data)
print("Predicted Sales Data:", predicted_values[-12:])
