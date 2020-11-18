#### MUST Have pizza.py in same directory to use ####
#This is a simple pizza shop business application I wrote in my introductory python course
#Currently I'm taking CS313E, data structures and algorithms, and I have some more
#complex programs on my github, but this program is probably more
#relevant to the content I would teach as a Tynker Python Tutor.

#imports the pizza.py module
import pizza

def main():

    #initalizes some pizzas as seed data
    pizza1 = pizza.Pizza("PEPPERONI GLUTEN FREE", 40, 15.99, "Corn	and Rice")
    pizza2 = pizza.Pizza("CHEESE", 50, 9.99, "Wheat")
    pizza3 = pizza.Pizza("MUSHROOM", 60, 11.99, "Multi-grain")
    pizza4 = pizza.Pizza("PEPPERONI", 70, 12.00, "Multi-grain")

    pizza_list = []

    pizza_list.append(pizza1)
    pizza_list.append(pizza2)
    pizza_list.append(pizza3)
    pizza_list.append(pizza4)

    #initializes a loop control variable
    choice = ""

    #continues as long as the user does not enter 'Q'
    while choice != "Q":

        #try except to test for errors in user input
        try:

            #calls the display_menu function which prints the menu
            display_menu()

            #prompts the user for a choice and updates the loop control variable
            choice = input("Please enter your choice: ")
            choice = choice.upper()

            #handles for if the user enters an invalid character
            while choice != "A" and choice != "B" and choice != "C" and choice != "Q":
                choice = input("Invalid choice! Please re-enter: ")
                choice = choice.upper()

            #prints pizzas if choice is A
            if choice == "A":

                printAllPizzas(pizza_list)

            #allows user to change the price for the pizza if choice is B
            elif choice == "B":

                #gets the type of pizza and the new price
                pizzaType = input("Please enter the pizza type: ")
                pizzaType = pizzaType.upper()
                newPrice = float(input("Please enter the price of pizza: "))

                #calls the updatePrice function 
                typeCheck = updatePrice(pizza_list, pizzaType, newPrice)

                #if pizza is not found outputs an error prompts user for a new choice
                if typeCheck == 0:
                    print("Error! The program could not find that pizza type!")

            #allows user to view the crust information for a pizza
            elif choice == "C":

                pizzaType = input("Please enter the pizza type: ")
                pizzaType = pizzaType.upper()
                typeCheck = outputPizzaCrust(pizza_list, pizzaType)

                #same as before prints an error if pizza is not found
                if typeCheck == 0:
                    print("Error! The program could not find that pizza type!")

            #if user choice is Q will end the program   
            else:

                break

        #catches input errors for if the user doesn't enter a valid number
        except ValueError:

            print("Next time enter a number instead of a string!")

        #catches any other possible issues
        except Exception as err:

            print("Exception handling section, system message :", err)

#function that just prints out a simple menu
def display_menu():
    print('')
    print("Welcome to Pizza P")
    print("=" *12)
    print("A: Output information for all pizzas")
    print("B: Set a new price for a pizza")
    print("C: Output crust information for a specific pizza")
    print("Q: Quit the program")

#function that prints the pizzas
def printAllPizzas(pList):

    for items in pList:
        print(items)
        print('')

#function that updates the price of a selected pizza, returns 0 if that pizza is not found
def updatePrice(pList, pType, pPrice):
    
    count = 0
    for items in pList:
        check = items.get_pizza_type()
        if check == pType:
            items.set_price(pPrice)
            break
        count += 1
    if count == len(pList):
        return 0

def outputPizzaCrust(pList, pType):

    count = 0
    for items in pList:
        check = items.get_pizza_type()
        if check == pType:
            print("The type of crust for", items.get_pizza_type(), "is", items.get_crust())
            break
        count += 1
    if count == len(pList):
            return 0
main()


