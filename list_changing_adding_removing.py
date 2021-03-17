# Changing, Adding and removing elements in a list

# lists will always be a dynamic
# In changing elements we modify
# modifying elements in a list: this sintax is similar to accessing elements in a list
motor = [' Neiman Marcus Limited Edition Fighter', 'Ducati Panigale V2', 'KTM 790 Adventure R', 'Harley-Davidson Street Glide']
print(motor)

motor[0] = 'Zero SR/S'
print(motor)

# adding elements  to a list \ adding elements to a list is very important
# let's see if u wanna add more registered users on your website
# So in adding elements to a list we have many ways of adding them, and one of these elements are: appending
# appending elements is one of the easy ways for you to add elements on your list
# when you append the element, the element goes as the last item of the list
# using the same list we have here, we're going to append an element to the list
# On adding we append() and insert() 

motor = [' Neiman Marcus Limited Edition Fighter', 'Ducati Panigale V2', 'KTM 790 Adventure R', 'Harley-Davidson Street Glide']
print(motor)

motor.append('Zero SR/S')
print(motor)


#the append method makes lists become dynamically, we can start a list without any element and then start appending

body = []
body.append('head')
body.append('chest')
body.append('ears')

print(body)
# this way of working with lists is very cool, and is one of the best way to collect data

# You can add a new element at any position in your list by using insert() method

languages = ['Python', 'JavaScript', 'Flutter']
languages.insert(2, 'C++')
print(languages)

# removing elements from a list
# removing elements using the del statement
# If I know the position of an element that I want to remove I can use the del statement

laptops = ['hp', 'dell', 'acer', 'asus']
print(laptops)

del laptops[0]
print(laptops)

# You can remove an item from any position in a list using the del statement if you know its index
del laptops[1]
print(laptops)
# In both examples, you can no longer access the value that was removed from the list after the del statement is used.

# removing an item using the pop() method
# the pop method lets you remove the item from the list, but it let you work with item
# first of all this method removes the last item, further I'm going to learn how to pop at any position
# Let's pop a list
laptops = ['hp', 'dell', 'acer', 'asus']
print(laptops)
popped_laptop = laptops.pop()
print(laptops)
print(popped_laptop)

# One little exercise
country = ['USA', 'UK', 'Dubai', 'france']
print(country)

last_country = country.pop()
print(country)
print(f"The last place I lived was in {last_country.title()}")

# Popping Items from any Position in a List
country = ['USA', 'UK', 'Dubai', 'france']
popped_country = country.pop(0)
print(f"I'm going to live and be a resident in {popped_country}!")

# removing an item by his value
# this method is very useful in cases when you dont know the exact position of the value
# but if you know the value then you can use de remove() method that you're about to see
medias = ['facebook', 'instagram', 'twitter', 'whatsApp']
medias.remove('whatsApp')
print(medias)
# challenge - try to remove an item and explain why did you remove
medias = ['facebook', 'instagram', 'twitter', 'whatsApp']
social = 'whatsApp'
medias.remove(social)
print(medias)
print(f"We removed {social} from our list because of some technical issues.")
