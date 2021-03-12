# lists are a collections of items in a particular order
# in python [] brackets represents a list
# example of lists
bicycles = ["portugal", "greece", "england", "italy", "france", "spain"]
print(bicycles)

# accessing elements in a list
print(bicycles[0].title(), bicycles[1].upper())

# Using individual values from a list
cars = ['ferrari', 'lamborghini', 'aston martin']
message = f"My first car will be an {cars[2].title()}!"
print(message)

# exercises. printing the same message to all of my friends
names = ['leandro', 'dumilde', 'kailany', 'liliany', 'lourdes', 'ndona']
message_to_all = "I will never forget you "

print(message_to_all + names[0].title())
print(message_to_all + names[1].title())
print(message_to_all + names[2].title())
print(message_to_all + names[3].title())
print(message_to_all + names[4].title())
print(message_to_all + names[5].title())

# favorite mode of transportation - exercises
carros = ['Mercedes-Benz Sl 65 AMG','Lexus LFA','McLaren MP4-12C','Porsche 918 Spyder Concept','Lamborghini Aventador']
print(f"I will own a {carros[-1]} before 2026")
print(f"I'm going to give a {carros[1]} to my mum")
print(f"My wife loves {carros[0]}")
print(f"My kids shall love {carros[2]}")