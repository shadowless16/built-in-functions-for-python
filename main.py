food1 = input("Enter your first favorite food: ")
food2 = input("Enter your second favorite food: ")
food3 = input("Enter your third favorite food: ")

favorite_foods = [food1, food2, food3]

print("\nYour current list of favorite foods:")
print(favorite_foods)

print("which of the following would like to use ? \n 1)append \n 2)clear \n 3)copy \n 4)count \n 5)Extend \n 6) index \n 7)insert \n 8)pop \n 9)remove \n 10)reverse \n 11)sort  ")

choice = int(input("Enter your choice? "))

if choice == 1:
    new_food = input("Enter the food to append: ")
    favorite_foods.append(new_food)
    print("List of favorite foods")
    print(favorite_foods)
elif choice == 2:
    favorite_foods.clear()
    print("List of favorite foods")
elif choice == 3:
    v2 = favorite_foods.copy()
    print(v2)
elif choice == 4: 
    count = favorite_foods.count("yam")
    print(count)
elif choice == 5:
    additional_foods = input("Enter additional foods separated by commas: ").split(',')
    favorite_foods.extend(additional_foods)
    print("\nExtended list of favorite foods:")
    print(favorite_foods)
elif choice == 6:
    fav_food = favorite_foods.index("yam")
    print(fav_food)
elif choice == 7:
    favorite_foods.insert(1, "eba")
    print(favorite_foods)
elif choice == 8:
    favorite_foods.pop(1)
    print(favorite_foods)
elif choice == 9:
    favorite_foods.remove("rice")
    print(favorite_foods)
elif choice == 10:
    favorite_foods.reverse()
    print(favorite_foods)
elif choice == 11:
    favorite_foods.sort()
    print(favorite_foods)
else:
    print("\nInvalid choice!")