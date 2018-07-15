'''
Dictionaries are similar to list, but they have key and values instead of one value
Curly brackets represent them and : is used to separate key and value
'''

ages={'Tony':20,'Bob':21,'Pat':30,'Sarah':40,'Jill':50}
print(ages)             # Print whole dictrionary
print(ages['Jill'])     # Print value for one key

# Loop through dicturionary and print
for i,j in ages.items():
    print(i+"'s age ",j)

ages['Pat']=32          # Update value for specific key
print(ages['Pat'])

del ages['Tony']        # Delete specific key information
print(ages)

print(len(ages))        # Get length of the dictionary
print(ages.keys())      # Get all keys in the dictionary
print(ages.values())    # Get all Values in the dictionary

ages2 = {'Anil':15,'Raj':25,'Sonu':45,'Kyle':55}
ages.update(ages2)      # Adds ages2 to ages
print(ages)

ages2.clear()           # Clears all dictionary contents
print(ages2)

del ages2               # Deletes the dictionary
print(ages2)            # This will generate error since it was deleted in above command


# Create a new dictrionary for stocks
stocks = {
    "AAPL": 100,
    "UAA": 17,
    "TSLA": 325.15,
    "ORCL": 52.35,
    "NFLX": 235.5,
    "CMG": 319.20
}

print(min(stocks)) # by default it sorts by key
print(max(stocks.keys())) # sort by key (explicitly)
print(min(stocks.values())) #  sort by value

print(sorted(stocks)) #by default it sorts all the keys
print(sorted(stocks.keys())) #sort all keys (explicitly)
print(sorted(stocks.values())) #sort all values

# you can also use zip function to switch key and values
zipped = zip(stocks.values(),stocks.keys())
print(sorted(zipped))

#Create another list
mktcap = [100,200,300,400,500,600]

#Zip three lists together and sort
zipped3 = zip(stocks.values(),stocks.keys(),mktcap)
print(sorted(zipped3))

flipped3 = zip(mktcap, stocks.values(),stocks.keys())
print(sorted(flipped3))
