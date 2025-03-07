def calculate_temperature(T, T0, T1, C0, C1):
    # Convert C0 and C1 to actual Celsius values
    C0 = C0 / 8.0
    C1 = C1 / 8.0

    # Use linear interpolation formula
    temperature = C0 + (T - T0) * (C1 - C0) / (T1 - T0)

    return round(temperature, 1)  # Round to 1 decimal place

# Read input
num_sensors = int(input())
results = []

for _ in range(num_sensors):
    T, T0, T1, C0, C1 = map(int, input().split())
    results.append(calculate_temperature(T, T0, T1, C0, C1))

# Print the results
for result in results:
    print(result)