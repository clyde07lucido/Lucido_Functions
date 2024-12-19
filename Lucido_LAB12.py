print("Welcome to KFC!")

menu = ["8-PC Bucket Meal", "2-PC Fully Loaded Meal", "Chicken Cheese Burger Combo", "Large Shots Combo", "Coke Float"]
price = [805, 275, 145, 130, 55]
total = 0

def display_menu(menu, price):
            for i in range(len(menu)):
                print(f"{i+1}. {menu[i]}: ₱{price[i]}")

while True:
        print("Enter the number of the item you want to order. Enter 'done' to finish.")
        display_menu(menu, price)

        choice = input("\nEnter your choice: ").strip()

        if choice.lower() == 'done':
            break
        elif choice.isdigit():  
            choice = int(choice)
            if 1 <= choice <= len(menu): 
                    total += price[choice - 1]
                    print(f"\nAdded {menu[choice - 1]} to your order. Total: ₱{total}")
            else:
                    print(f"\nInvalid choice. Please select a valid menu item. Total: ₱{total}")
        else:
                print(f"\nInvalid input. Please enter a number or 'done'. Total: ₱{total}")

print(f"\nYour total amount to pay: ₱{total}")

while True:
    fee = int(input("Enter your amount to pay: ₱"))
    change = fee - total

    if fee >= total:
        print(f"\nChange: ₱{change}")
        break
    else:
        print(f"\nYour money is not enough. Please pay at least ₱{total}")

print("Thank you for your order. Come back again to KFC!")