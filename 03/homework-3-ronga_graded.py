#Grade: 14/14 

#LISTS
#
# 1) Make a list called "countries" - it should contain seven different countries and NOT be in alphabetical order
# let's select the smallest by population:
countries = ['Pitcairn', 'Cocos Islands', 'Holy See', 'Tokelau', 'Niue', 'Svalbard', 'Christmas Island']

# 2) Using a for loop, print each element of the list
for country in countries:
    print(country)

# 3) Sort the list permanently.
countries.sort()

# 4) Display the first element of the list
print('First element [after sort()]:', countries[0])

# 5) Display the second-to-last element of the list using a line of code that will work no matter what the size of the list is (hint: len will be helpful)
print('Second-to-last element [after sort()]:', countries[len(countries)-2])

# 6) Delete one of the countries from the list using its name (we didn't learn this in class).
countries.remove('Svalbard')

# 7) Using a for loop, print each element of the list again, which should now be one element shorter.
for country in countries:
    print(country)

# DICTIONARIES
#
# These will require LATITUDE and LONGITUDE. You can ask Google for latitude and longitude by typing in *coordinates of CITYNAME*. You can also use http://itouchmap.com/latlong.html. Store the latitude and longitude without the N/S/E/W - if the latitude is S, make it negative. If the longitude is W, make it negative. See here for explanation: https://answers.yahoo.com/question/index?qid=20080211182008AAMdUe8
#
# 1) Make a dictionary called 'tree' that responds to 'name', 'species', 'age', 'location_name', 'latitude' and 'longitude'. Pick a tree from here: https://en.wikipedia.org/wiki/List_of_trees
tree = {"name":"Mingo Oak", "species":"oak", "age":577, "location_name":"Mingo", "latitude":37.819400, "longitude":-82.067083}

# 2) Print the sentence "{name} is a {years old} tree that is in {location_name}"
print(tree["name"], "is a", tree["age"], "tree that was in", tree["location_name"])

# 3) The coordinates of New York City are 40.7128° N, 74.0059° W. Check to see if the tree is south of NYC, and print "The tree {name} in {location} is south of NYC" if it is. If it isn't, print "The tree {name} in {location} is north of NYC"
position = ""
if tree["latitude"] > 40.7128:
    print("The tree", tree['name'], "in", tree['location_name'], "is north of NYC")
else:
    print("The tree", tree['name'], "in", tree['location_name'], "is south of NYC")

# 4) Ask the user how old they are. If they are older than the tree, display "you are {XXX} years older than {name}." If they are younger than the tree, display "{name} was {XXX} years old when you were born."
user_age = input("How old are you? \n ~> ")

# Never trust users
try:
   user_age_int = int(user_age)
except ValueError:
   print("Next time, please type your age as an integer! I choosed 13 years old for you.")
   user_age_int = 13

age_diff = tree['age'] - user_age_int
if(age_diff > 0):
    print(tree['name'], "was", age_diff, "years old when you were born.")
elif(age_diff < 0):
    print("You are", -age_diff, "years older than", tree['name'])
else:
    print("You have the same age as the tree!")

#
# LISTS OF DICTIONARIES
#
# 1) Make a list of dictionaries of five places across the world - (1) Moscow, (2) Tehran, (3) Falkland Islands, (4) Seoul, and (5) Santiago.
# Each dictionary should include each city's name and latitude/longitude (see note above).

# SELECT CONCAT('"name":"', name, '", "latitude":', latitude, ', "longitude":', longitude) FROM city WHERE name in ('Moskva', 'Tehran', 'Falkland Islands', 'Seoul', 'Santiago');
places = [
    {"name":"Moskow", "latitude":55.75, "longitude":37.62},
    {"name":"Tehran", "latitude":35.7, "longitude":51.42},
    {"name":"Falkland Islands", "latitude":-52.22, "longitude":-59.90},  # lat 51°40′ – 53°00′ S % lng 57°40′ – 62°00′ W
    {"name":"Seoul", "latitude":37.57, "longitude":126.97},
    {"name":"Santiago", "latitude":-33.45, "longitude":-70.67}
]

# 2) Loop through the list, printing each city's name and whether it is above or below the equator (How do you know? Think hard about the latitude.). When you get to the Falkland Islands, also display the message "The Falkland Islands are a biogeographical part of the mild Antarctic zone," which is a sentence I stole from Wikipedia.
for place in places:
    belowOrAbove = ("below", "above")[place["latitude"] > 0]    # this is bad. (false, true)[condition]
    print(place["name"], "is", belowOrAbove, "the equator.")
    if place["name"] == "Falkland Islands":
        print("The Falkland Islands are a biogeographical part of the mild Antarctic zone.")

# 3) Loop through the list, printing whether each city is north of south of your tree from the previous section.
for place in places:
    belowOrAboveTree = ("south", "north")[place["latitude"] > tree["latitude"]]
    print(place["name"], "is", belowOrAboveTree, "of the tree.")
