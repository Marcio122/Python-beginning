# using variables in a string
name = "ada"
last_name = "love"
full_name = f'{name} {last_name}'
print(full_name)

# using f-strings to compose messages
name = "ada"
last_name = "love"
full_name = f"Hello, {name} {last_name}!"
print(full_name.title())

first_name = "alex"
last_name  = "geoveti"
full_name = f"{first_name} {last_name}"
print(f"Hi, {full_name.title()}!")

# You can also use f-strings to compose a message, and then assign the entire message to a variable:
first_name = "geo"
last_name = "bri"
full_name = f" {first_name} {last_name}"
message = f"Hello,{full_name.title()}."
print(message)