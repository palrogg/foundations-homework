import time, datetime
import pandas as pd

# 1) tiny functions

def depth_to_words(depth): # will describe the earthquake's depth
    depth = int(depth)
    if depth < 70:
        return 'shallow'
    elif depth >= 70 and depth < 300:
        return 'intermediate'
    elif depth >= 300:
        return 'deep'
    return 'undetermined'

def magnitude_to_words(magnitude):  # will describe the earthquake's power
    magnitude = float(magnitude)
    if magnitude < 4:
        return 'easily ignored'
    elif magnitude < 6:
        return 'moderate'
    elif magnitude < 7:
        return 'strong'
    elif magnitude < 8:
        return 'major'
    elif magnitude < 9:
        return 'huge'
    elif magnitude >= 9:
        return 'very destructive'
    return 'undetermined'

def day_in_words(timestamp): # should be the day of the week
    return time.strftime('%A', timestamp) # Am I lazy?

def time_in_words(timestamp): # should be "morning", "afternoon", "evening" or "night"
    hour = int(time.strftime('%H', timestamp))
    if hour < 6 or hour >= 23:
        return "night"
    elif hour < 12:
        return "morning"
    elif hour < 18:
        return "afternoon"
    elif hour < 23:
        return "evening"
    return 'undetermined'

def date_in_words(timestamp): #should be "Monthname day", e.g. "June 22"
    return time.strftime('%B %d', timestamp)


# 2) sentence

earthquake = {
      'rms': '1.85',
      'updated': '2014-06-11T05:22:21.596Z',
      'type': 'earthquake',
      'magType': 'mwp',
      'longitude': '-136.6561',
      'gap': '48',
      'depth': '10',
      'dmin': '0.811',
      'mag': '5.7',
      'time': '2014-06-04T11:58:58.200Z',
      'latitude': '59.0001',
      'place': '73km WSW of Haines, Alaska',
      'net': 'us',
      'nst': '',
      'id': 'usc000rauc'}

def eq_to_sentence(earthquake):
    timestamp = time.strptime(earthquake['time'][:-5], '%Y-%m-%dT%H:%M:%S')
    sentence = ''
    if depth_to_words(earthquake['depth'])[:1] in 'aeiou':
        sentence = "An "
    else:
        sentence = "A "
    sentence += depth_to_words(earthquake['depth']) + ", " + magnitude_to_words(earthquake['mag'])
    sentence += " earthquake was reported " + day_in_words(timestamp) + " " + time_in_words(timestamp)
    sentence += " on " + date_in_words(timestamp) + ", "+ earthquake['place'] + "."
    return sentence

print(eq_to_sentence(earthquake))


# 3) bulk delivery

df = pd.read_csv('http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.csv')

def getPOSIX(timestamp):
    return datetime.datetime.strptime(timestamp[:-5], '%Y-%m-%dT%H:%M:%S')

date_from = datetime.datetime.now() - datetime.timedelta(days=30)

lastmonth = df[(df['time'].apply(getPOSIX) > date_from) & (df['mag'] > 4.0)]

earthquakes = lastmonth.to_dict('records')
for event in earthquakes:
    print(eq_to_sentence(event))



# 4) other bits

lastmonth_full = df[(df['time'].apply(getPOSIX) > date_from)]

events = lastmonth_full.to_dict('records')

def other_to_sentence(event):
    timestamp = time.strptime(event['time'][:-5], '%Y-%m-%dT%H:%M:%S')
    return "There was also a magnitude " + str(event['mag']) + " " + event['type'] + " on " + date_in_words(timestamp) + ", " + event['place'] + "."

for event in events:
    if event['type'] != 'earthquake':
        print(other_to_sentence(event))
    else:
        if event['mag'] > 4.0:
            print(eq_to_sentence(event))
