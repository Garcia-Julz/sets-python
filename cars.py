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


# Now create another set of cars in a variable junkyard. Someone who owns a junkyard full of old cars has approached you about buying the entire inventory. In the new set, add some different cars, but also add a few that are the same as in the showroom set.

junkyard = set()

junkyard = {'Ford', 'Honda', 'Kia', 'Scion', 'Mustang', 'Porche'}

# Use the intersection method to see which cars exist in both the showroom and that junkyard.

dup_validator = junkyard.intersection(showroom)
print(dup_validator)

# Now you're ready to buy the cars in the junkyard. Use the union method to combine the junkyard into your showroom.

junkyard = junkyard.union(showroom)
print(junkyard)

# Use the discard() method to remove any cars that you acquired from the junkyard that you do not want in your showroom.

# ONE METHOD CAN BE THIS WAY WITH Discard()
# junkyard.discard('Ford')
# junkyard.discard('Honda')
# junkyard.discard('Kia')

# LEARNED THIS IS COOL WAY TO DO MULTIPLE OBJECTS AT ONCE difference_update()
junkyard.difference_update({'Ford', 'Honda', 'Kia'})
print(junkyard)