# Sets (unordered, unindexed & does NOT allow duplicates)

# Using set() to create a set
# languages = set()

# Using curly braces allows you to initialize the set with values
# languages = { 'english', 'mandarin chinese', 'spanish', 'english', 'spanish', 'portugese' }


# ********* Practice: Showroom & Junkyard *********

# Create an empty set named showroom.

showroom = set()

# Add four of your favorite car model names to the set.

showroom = {'Mustang', 'Porche', 'Tesla', 'Toyata'}

# Print the length of your set.

print(len(showroom))

# Pick one of the items in your show room and add it to the set again.

showroom.add('Mustang')

# Print your showroom. Notice how there's still only one instance of that model in there.

print(showroom)

# Using update(), add two more car models to your showroom with another set.

showroom2 = set() 
showroom2 = {'Camaro', 'Mazda'}

showroom.update(showroom2) # Update showroom using showroom2 as the argument
print(showroom)

# You've sold one of your cars. Remove it from the set with the discard() method.

showroom.discard('Camaro')
print(showroom)
