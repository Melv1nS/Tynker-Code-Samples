
#defines pizza class
class Pizza:

    def __init__(self, pizza_type, inventory, price, crust):

        #defines private attributes of pizza class
        self.__pizza_type = pizza_type
        self.__inventory = inventory
        self.__price = price
        self.__crust = crust

    #get methods for pizza type
    def get_pizza_type(self):
        return self.__pizza_type
    #set method for pizza type
    def set_pizza_type(self, pizza_type):
        self.__pizza_type = pizza_type

    #get method for inventory
    def get_inventory(self):
        return self.__inventory

    #set method for inventory
    def set_inventory(self, inventory):

        #makes sure the number set for inventory is positive and > 0
        if inventory <= 0:
            print("You cannot set the inventory to negative or zero!")
        else:
            self.__inventory = inventory

    #get method for price
    def get_price(self):
        return self.__price

    #set method for price
    def set_price(self, price):

        #majes sure price isn't negative, 0, or > than 17.99
        if price <= 0:
            print("You cannot set the price to negative or zero!")
            
        elif price > 17.99:
            print("You cannot set the price greater than 17.99")

        else:
            self.__price = price

    #get method for crust
    def get_crust(self):
        return self.__crust

    #set method for crust
    def set_crust(self, crust):
        self.__crust = crust

    #__str__ method, defines what will be printed if a pizza object is printed. 
    def __str__(self):
        return "The pizza type is: " + str(self.__pizza_type) + "\nThe inventory is: " + \
               str(self.__inventory) + "\nThe price is: $" + str(format(self.__price, '.2f')) + "\nThe crust is: " \
               + str(self.__crust)

