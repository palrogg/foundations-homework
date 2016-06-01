# Paul Ronga
# Wednesday, May 5, 2016
# Homework 2

# 1) Make a list of the following numbers: 22, 90, 0, -10, 3, 22, and 48
numbers = [22, 90, 0, -10, 3, 22, 48]

# 1) Display the number of elements in the list
print("Array length:", len(numbers))

# 2) Display the 4th element of this list.
print("4th:", numbers[3])

# 3) Display the sum of the 2nd and 4th element of the list.
print("Sum:", numbers[1] + numbers[3])

# 4) Display the 2nd-largest value in the list.
print("2nd-largest:", sorted(numbers, reverse=True)[1])

# 5) Display the last element of the original unsorted list
print("Last:", numbers[len(numbers)-1])

# 6) For each number, display a number:
    #if your original number is less than 10, multiply it by thirty.
        #If it's also even, add six.
    #If it's greater than 50 subtract ten.
    #If it's not negative ten, subtract one.
    #(For example: 2 is less than 10, so 2 * 30 = 60, 2 is also even, so 60 + 6 = 66, 2 is not negative ten, so 66 - 1 = 65.)

print("\n~~~~ Begin if-else ~~~~")

newNumbers = []

for number in numbers:
    printnumber = number
    if number < 10:
        printnumber *= 30
        if number % 2 == 0:
            printnumber += 6
    if number > 50:
        printnumber -= 10
    if number != -10:
        printnumber -= 1
    print(number, "->", printnumber)
    newNumbers.append(printnumber)

print("~~~~ End if-else ~~~~\n")

# 7) Sum the result of each of the numbers divided by two.
theSum = 0
for number in numbers:
    theSum += number/2
print("The sum is:", theSum)

theSum2 = 0
for newNumber in newNumbers:
    theSum2 += newNumber/2

print("The sum of each of the previously computed numbers divided by two is:", theSum2)

# DICTIONARIES
print("\n#### DICTIONARIES ####\n")

# 8) ... Define a dictionary called movie that works with the following code.
#print("My favorite movie is", movie['title'], "which was released in", movie['year'], "and was directed by", movie['director'])

movie = {"title":"The Fearless Vampire Killers", "year":1967, "director":"Roman Polanski"}

# 9) Add entries to the movie dictionary for budget and revenue (you'll use code like movie['budget'] = 1000), and print out the difference between the two.
movie['budget'] = 500
movie['revenue'] = 900000
print("Difference: ", movie['revenue'] - movie['budget'])

# 10) If the movie cost more to make than it made in theaters, print "It was a flop".
#If the film's revenue was more than five times the amount it cost to make, print "That was a good investment."
if movie['budget'] > movie['revenue']:
    print("It was a flop")
elif movie['revenue'] > 5 * movie['budget']:
    print("That was a good investment.")

# 11) Sometimes dictionaries are used to describe the same aspects of many different objects.
# Make ONE dictionary that describes the population of the boroughs of NYC.
# Manhattan has 1.6 million residents, Brooklyn has 2.6m, Bronx has 1.4m, Queens has 2.3m and Staten Island has 470,000.
# (Tip: keeping it all in either millions or thousands is a good idea)

boroughs_population = {"Manhattan":1600, "Brooklyn":2600, "Bronx":1400, "Queens":2300, "Staten Island":470}

# 12) Display the population of Brooklyn.
print("Brooklyn (thousands):", boroughs_population['Brooklyn'])

# 13) Display the combined population of all five boroughs.
theSum = 0
for borough, pop in boroughs_population.items():
    theSum += pop
print("The sum is (thousands):", theSum)

# 14) Display what percent of NYC's population lives in Manhattan.
manhattan_percentage = boroughs_population["Manhattan"]/theSum*100
print("%.2f" % (manhattan_percentage) + "% of NYC’s population lives in Manhattan.")
