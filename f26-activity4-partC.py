# Complete the TODOs using the Python concepts introduced in class.
# Run this file to check your result.  

# DG8002 - F26 - Activity 4
# Author Name: Stephan Kozak
# Date: October 8, 2026

# SCENARIO
# A weather station has recorded temperatures over seven days. 
# Your task is to examine the data and produce a short weather report.

#                 M   T   W  Th  F   Sa  Su
temperatures  = [18, 22, 25, 19, 27, 24, 16]

# TODO 0: Create the variables you need for total temperature, # of days above 23 degrees, and hottest day
totalTemperature = 0
daysAbove23 = 0
hottestDay = -1

# TODO 1: Iterate through every recorded temperature
for temperature in temperatures:
    
    # TODO 2: Print the recorded temperature
    print(f"Recorded Temperature: {temperature} degrees C")
    
    # TODO 3: Add the temperature to total
    totalTemperature += temperature
    
    # TODO 4: If temperature is above 23, add 1 to the day counter
    if temperature > 23:
        daysAbove23 += 1
        
# TODO 5: Calculate and print the average temeprature for the week.
averageTemperature = totalTemperature / len(temperatures)
print(f"Average Temperature: {averageTemperature:.2f}")
        
# TODO 6: Print how many days exceeded 23 degrees
print(f"Days Above 23: {daysAbove23}")

# TODO 7: Print the -> index <- of the highest temperature.
highestTemperature = max(temperatures)
hottestDay = temperatures.index(highestTemperature)
print(f"Highest Temperature Index: {hottestDay}")

# EXPECTED OUTPUT
# Average Temperature: 21.57
# Days Above 23:  3
# Highest Temperature Index: 5  


