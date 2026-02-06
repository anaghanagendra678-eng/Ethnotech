# List of favorite fruits
fruits = ["apple", "banana", "apple", "orange", "banana", "apple"]

# Empty dictionary to store counts
fruit_count = {}

# Count each fruit
for fruit in fruits:
    if fruit in fruit_count:
        fruit_count[fruit] += 1
    else:
        fruit_count[fruit] = 1

# Print results
print("Favorite Fruit Count:")
for fruit, count in fruit_count.items():
    print(fruit, ":", count)

print()

# List of test scores
scores = [78, 85, 90, 66, 88, 92, 74]

# Calculate values
highest = max(scores)
lowest = min(scores)
average = sum(scores) / len(scores)

# Print results
print("Test Score Analysis")
print("Highest Score:", highest)
print("Lowest Score:", lowest)
print("Average Score:", average)

print()

# Days of the week
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Temperatures for each day
temperatures = [30, 32, 31, 29, 33, 34, 28]

# Find hottest and coldest temperatures
hottest_temp = max(temperatures)
coldest_temp = min(temperatures)

# Find the day for hottest and coldest
hottest_day = days[temperatures.index(hottest_temp)]
coldest_day = days[temperatures.index(coldest_temp)]

# Print results
print("Weekly Weather Report")
print("Hottest Day:", hottest_day, "-", hottest_temp, "°C")
print("Coldest Day:", coldest_day, "-", coldest_temp, "°C")

print()

# List of pets owned by classmates
pets = ["dog", "cat", "dog", "bird", "cat", "dog", "fish"]

# Empty dictionary to store pet counts
pet_count = {}

# Count each pet
for pet in pets:
    if pet in pet_count:
        pet_count[pet] += 1
    else:
        pet_count[pet] = 1

# Print results
print("Pet Survey Results:")
for pet, count in pet_count.items():
    print(pet, ":", count)

print()

# Number of guesses taken by players
guesses = [4, 6, 3, 5, 2, 4, 6]

# Calculate statistics
best = min(guesses)
worst = max(guesses)
average = sum(guesses) / len(guesses)

# Print results
print("Number Guess Game Analysis")
print("Best Performance (least guesses):", best)
print("Worst Performance (most guesses):", worst)
print("Average Guesses:", average)

print()

# Minutes watched each day
watch_time = [45, 60, 30, 90, 50, 70, 40]

# Calculate total and average
total_time = sum(watch_time)
average_time = total_time / len(watch_time)

# Print results
print("YouTube Watch Time Report")
print("Total Minutes Watched:", total_time)
print("Average Minutes per Day:", average_time)

print()

# List of votes
votes = ["pizza", "burger", "pizza", "pizza", "burger", "pasta", "pizza"]

# Dictionary to count votes
vote_count = {}

# Count each vote
for vote in votes:
    if vote in vote_count:
        vote_count[vote] += 1
    else:
        vote_count[vote] = 1

# Find the winner
winner = max(vote_count, key=vote_count.get)

# Print results
print("Voting Results:")
for food, count in vote_count.items():
    print(food, ":", count)

print("Winner is:", winner)

print()

import random

# Number of times to roll the dice
rolls = 100

# Empty dictionary to store counts
dice_count = {}

# Roll the dice
for i in range(rolls):
    number = random.randint(1, 6)
    if number in dice_count:
        dice_count[number] += 1
    else:
        dice_count[number] = 1

# Print results
print("Dice Roll Results:")
for number in sorted(dice_count):
    print("Number", number, ":", dice_count[number])

print()

# Pocket money received each week
money = [50, 75, 60, 100, 80, 90]

# Calculate values
highest = max(money)
lowest = min(money)
average = sum(money) / len(money)

# Print results
print("Pocket Money Report")
print("Highest Amount:", highest)
print("Lowest Amount:", lowest)
print("Average Amount:", average)

print()

# List of favorite colors
colors = ["red", "blue", "green", "blue", "red", "yellow", "blue", "green"]

# Dictionary to count colors
color_count = {}

# Count each color
for color in colors:
    if color in color_count:
        color_count[color] += 1
    else:
        color_count[color] = 1

# Print results
print("Favorite Colors Count:")
for color, count in color_count.items():
    print(color, ":", count)

print()
