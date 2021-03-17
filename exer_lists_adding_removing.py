# exercise 1
# . Guest List: If you could invite anyone, living or deceased, to dinner, who 
# would you invite? Make a list that includes at least three people you’d like to 
# invite to dinner. Then use your list to print a message to each person, inviting them to dinner.
dinner = ['tb joshua', 'shepherd bushiri', 'Harry']
print(f"\n\tCan we have a dinner today Prophet {dinner[0].title()}?")
print(f"\t{dinner[1].title()} can we have a dinner with you and your pastors?")
print(f"\tIt would be a pleasure to have a dinner with you my brother {dinner[2].title()}, do you want?")

# exercise 2 
# Changing Guest List
print(f"{dinner[1].title()} cannot go for dinner this month. ")
dinner[1] = 'daniel'
print(dinner)

print(f"Prophet {dinner[0].title().title()} do you confirm tonight?")
print(f"Brother {dinner[1].title()} do you confirm your presence?")
print(f"{dinner[2].title()} are you going to be here?")

# exercises 3
# more guests
print("Wow I found that there's more space here, let me call some guys around here")
dinner.insert(3,'Lina')
dinner.insert(4, 'Geovanna')
dinner.insert(5, 'Geoveti')
print(dinner)
dinner.append('Alexandre')
print(dinner)

print(f"You are welcome into this dinner {dinner[0].title()}.")
print(f"You are welcome into this dinner {dinner[1].title()}.")
print(f"You are welcome into this dinner {dinner[2].title()}.")
print(f"You are welcome into this dinner {dinner[3].title()}.")
print(f"You are welcome into this dinner {dinner[4].title()}.")
print(f"You are welcome into this dinner {dinner[5].title()}.")
print(f"You are welcome into this dinner {dinner[6].title()}.")

print("\nOhh damnn I invited many friends but I only have space for two people")
# time to pop()
alexandre_popped = dinner.pop()
print(f"I'm very sorry but we can't have a dinner tonight {alexandre_popped}.")

Geoveti = dinner.pop()
print(f"I'm very sorry but we can't have a  dinner tonight {Geoveti}.")

Geovanna = dinner.pop()
print(f"I'm very sorry little girl but we can't be together tonight {Geovanna}.")

Lina = dinner.pop()
print(f"I'm very sorry, but next time we will have a dinner Mrs {Lina}.")

Harry_popped = dinner.pop()
print(f"I'm very sorry {Harry_popped}, but next time we will be together.")

print(dinner)
print(f"{dinner[0].title()} and {dinner[1].title()} you all still invited to today's dinner")

del dinner[0]
print(dinner)

del dinner[0]
print(dinner)