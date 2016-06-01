# Paul Ronga
# 2016-05-23
# Homework 1

# 1. Prompt the user for their year of birth
year_of_birth = input("What's your year of birth? ")

#Additionally, if someone gives you a year in the future, try asking them again (assume they'll do it right the second time).
while int(year_of_birth) > 2016:
    year_of_birth = input("What's your _real_ year of birth? ")

# 2. How old they are
age = 2016 - int(year_of_birth)
print("Your age is approximately", age, "years old.")

# 3. How many times their heart has beaten -> let's say it beats 42 million times in a year
print("Your heart has beaten", age*42000000, "times.")

# 4. How many times a blue whale's heart has beaten > "A blue whale’s heart beats six times a minute" > 3155760
print("A blue whale's heart has beaten", age*3155760, "times.")

# 5. How many times a rabbit's heart has beaten
# 6. If the answer to (5) is more than a billion, say "XXX billion" instead of the very long raw number
rabbit_beats = age * 70956000 # 135 * 60 * 24 * 365
if rabbit_beats > 1000000000:
    print("A rabbit's heart has beaten",int(rabbit_beats / 1000000000), "billion times.")
else:
    print("A rabbit's heart has beaten", rabbit_beats, "times.")

# 7. How old they are in Venus years > "A year on Venus is 0.62 as long as an Earth year."
print("Your age is approximately", age/0.62, "Venus years old.")

# 8. How old they are in Neptune years > "a year on Neptune is 60,190 days or 164.79 years"
print("Your age is approximately", age/164.79, "Neptune years old.")

# 9. Whether they are the same age as you, older or younger
# 10. If older or younger, how many years difference
age_diff = age - 26

if age_diff == 0:
    print("You have the same age as me!")
elif age_diff < 0:
    print("You seem to be", -age_diff, "years younger than me.")
else:
    print("You are", age_diff, "years older than me.")

# 11. If they were born in an even or odd year
if int(year_of_birth) % 2 == 0:
    print("You were born in an even year.")
else:
    print("You were born in an odd year.")

# 12. How many times the Pittsburgh Steelers have won the Superbowl since their birth.
superbowl_wins = [1974, 1975, 1978, 1979, 2005, 2008]
wins_count = 0
for win in superbowl_wins:
    if int(year_of_birth) <= win:
        wins_count += 1
print("The Pittsburgh Steelers have won the Superbowl", wins_count, "times since your birth.")

# 13. Which US President was in office when they were born (FDR onward)
presidents = {'1789-1797':'George Washington', '1797-1801':'John Adams', '1801-1809':'Thomas Jefferson', '1809-1817':'James Madison', '1817-1825':'James Monroe', '1825-1829':'John Quincy Adams', '1829-1837':'Andrew Jackson', '1837-1841':'Martin Van Buren', '1841':'William H. Harrison', '1841-1845':'John Tyler',
'1841-1849':'James K. Polk', '1849-1850':'Zachary Taylor', '1850-1853':'Millard Fillmore', '1853-1857':'Franklin Pierce', '1857-1861':'James Buchanan', '1861-1865':'Abraham Lincoln', '1865-1869':'Andrew Johnson', '1869-1877':'Ulysses S. Grant', '1877-1881':'Rutherford B. Hayes', '1881':'James A. Garfield', '1881-1885':'Chester A. Arthur',
'1885-1889':'Grover Cleveland', '1889-1893':'Benjamin Harrison', '1893-1897':'Grover Cleveland', '1897-1901':'William McKinley', '1901-1909':'Theodore Roosevelt', '1909-1913':'William H. Taft', '1913-1921':'Woodrow Wilson', '1921-1923':'Warren G. Harding', '1923-1929':'Calvin Coolidge', '1929-1933':'Herbert Hoover', '1933-1945':'Franklin D. Roosevelt',
'1945-1953':'Harry S. Truman', '1953-1961':'Dwight D. Eisenhower', '1961-1963':'John F. Kennedy', '1963-1969':'Lyndon B. Johnson', '1969-1974':'Richard M. Nixon', '1974-1977':'Gerald R. Ford', '1977-1981':'Jimmy Carter', '1981-1989':'Ronald Reagan', '1989-1993':'George H. W. Bush', '1993-2001':'Bill Clinton', '2001-2009':'George W. Bush',
'2009-2016':'Barack Hussein Obama'}

president_found = 0
for year, president in presidents.items(): # and not iteritems, which was for Python 2
    dates = year.split("-")
    if len(dates) == 1: # this president didn't last long
        if dates [0] == year_of_birth:
            if president_found > 0:
                print("This same year,", president, "also started or finished a mandate.")
            else:
                print("US president", president, "was in office when you were born.")
            president_found += 1
            also = 'also'
    else:
        if dates[0] <= year_of_birth and dates[1] >= year_of_birth:
            if president_found > 0:
                print("This same year,", president, "also started or finished a mandate.")
            else:
                print("US president", president, "was in office when you were born.")
            president_found += 1

if president_found == 0:
    print("No president was found. Maybe you were born before the french revolution or you come from the future.")
