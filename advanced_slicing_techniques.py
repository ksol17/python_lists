# Task 1

temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

second_week_temperatures = temperatures[7:15]

print(second_week_temperatures)

# Task 2

above_100_temperatures = []
for temp in temperatures:
    if temp > 100:
        above_100_temperatures.append(temp)
print(above_100_temperatures)