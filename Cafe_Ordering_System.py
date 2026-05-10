# Restaurant Management System

#---Welcome message---

print(' ✨ Welcome to our Restaurant✨ ')
menu = {
        "SOUP🍲":{"Tomato": 120,
                 "Hot n Sour": 129,
                 "Lemon Coriander": 89,
                 "Mix Veg": 105,
                 "Cream Of Broccoli": 130,
                 "Sweet Corn": 95
                },
        "ITALIAN🍕":{"Penne in White Sauce": 180,
                   "Red Sauce Pasta": 130,
                   "Risotto": 135,
                   "Veg Paradise Pizza(Medium)": 200,
                   "Veg Creamy Pizza": 220,
                   "Lasagna": 250,
                   "Spaghetti Aglio e Olio": 270
                  },
        "Best of Asia🍜":{"Veg Sushi": 200,
                        "Japanese Ramen": 240,
                        "Kimchi & Bibimbap": 280,
                        "Thai Curry": 230,
                        "Manchurian": 150,
                        "Hakka Noodles": 180,
                        "Spring Roll": 190,
                        "Thai Dimsums(10 pc)": 200,
                        "Fried Rice": 220
                       },
        "Desi Indian🍽️":{"Phulka(2) with Panner butter/"
                        "Masala ": 240,
                       "Phulka(2) with Malai Kofta": 220,
                       "Dosa Sambar": 200,
                       "Idli(3) Sambar": 180,
                       "Pulao": 200,
                       "Biryani": 250,
                       "Vegetable Khichadi": 200
                         
                      },
        "Snacks🍟":{"French Fries":80,
                    "Samosa(pc)" :75,
                    "Crispy Corn":100,
                    "Saute Vegetable":120,
                    "Dahi Kachori": 80,
                    "Crispy Veg": 120
                    },
        "Beverages🍸":{"Tea": 60,
                     "Coffee":70,
                     "Cold Coffee": 120,
                     "Matcha": 150,
                     "Hot Chocolate": 110,
                     "Mineral Water": 40,
                    }
       }
#---printing the menu---

print(f'{"Menu":^30}')

for category in menu:
    print("\n" + category)
    print("-" * 30)

    for item, price in menu[category].items():
        print(f"{item} - Rs{price}")
print("-" * 30)
print()
print()



#---Order---

cart = {}  # A variable to store the order

while True:    ##since we don't know how many dishes customer will order 
    food_choice = input('Enter the food you want: ')

    for category in menu:
        if food_choice in menu[category]:
            price = menu[category][food_choice]
            Quantity = int(input("Enter the quantity: "))

            if food_choice in cart:
                cart[food_choice] += Quantity  ##if the food already exists 
                                               ##add the new quantity to it
            else:
                cart[food_choice] = Quantity  #if does not exist write the customer 
                                              #entered quantity
            print(f'{food_choice} added to cart')
            break
    else:
        print("\nSorry the dish is currently unavailable😔")

    order_more = input("Do you want to order more?" 
                        "(yes or no): ").lower()
    if order_more == "no":
        break

#---bill---

print("-" * 30)
print(f'{"Taste of Asia":^30}')
print(f'{"BILL":^30}')


total = 0
for item, qty in cart.items():  #accessing the value through it's key
    for category in menu:         #checking if item is available in menu or not
        if item in menu[category]:#if item is found
                price = menu[category][item]
                break
    total_bill = price * qty
    total += total_bill

    print(f'{item}...{price} x {qty}  Rs{total_bill}')

print()
print("-" * 30)
print(f'Total: Rs{total}')
print("-" * 30)
print()
print("Thank you for dining with us ✨")
