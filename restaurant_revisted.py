from queue import Queue
from collections import namedtuple

class MenuItem:
    def __init__(self, name: str, price: float):
        self.name = name
        self.price = price

    def calculate_price(self, quantity: int) -> float:
        return self.price * quantity
    
    def menu_to_dict(self):
        return{
            "name": self.name, 
            "price": self.price
        }
    
class Beverage(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)
  
    def set_size(self, size:str):
        self.__size = size

    def get_size(self:str):
        return self.__size

    def set_bottle_type(self, bottle_type):
        self.__bottle_type = bottle_type

    def get_bottle_type(self):
        return self.__bottle_type

    def with_ice(self, answer) -> str:
        if answer == "yes":
            return f"your {self.name} is with ice"
        elif answer == "no":
            return f"your {self.name} is without ice"


class Apetizer(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_sauce(self, sauce:str):
        self.__sauce = sauce

    def get_sauce(self):
        return self.__sauce


class Dessert(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_flavour(self, flavour:str):
        self.__flavour = flavour

    def get_flavour(self):
        return self.__flavour


class MainPlate(MenuItem):
    def __init__(self, name, price):
        super().__init__(name, price)

    def set_accompaniment1(self, accompaniment_1:str):
        self.__accompaniment1 = accompaniment_1

    def get_accompaniment1(self):
        return self.__accompaniment1

    def set_accompaniment2(self, accompaniment_2:str):
        self.__accompaniment2 = accompaniment_2

    def get_accompaniment2(self):
        return self.__accompaniment2


class Order:
    def __init__(self, number):
        self.number = number
        self.order = []

    def add_items(self, menu_item: MenuItem, quantity: int) -> list:
        prod = namedtuple (f"Orden{self.number}",["prducto","cantidad"]) ##Aqui esta la named tuple, la uso para añadir los objetos al menu
        product= prod( 
            menu_item,
            quantity        
        )
        self.order.append(product)

    def show_order(self) -> list:
        return [(item[0].name, item[1]) for item in self.order]

    def calculate_total_price(self) -> float:
        total_bill = 0
        total_quantity = 0

        main_plate_names = []
        for item, quantity in self.order:
            if isinstance(item, MainPlate):
                main_plate_names.append(item.name)

        for menu_item, quantity in self.order:
            price = menu_item.calculate_price(quantity)

            if "Hamburger"in main_plate_names and isinstance(menu_item, Beverage):
                price *= 0.9  # 10% Discount on beverages

            if "Fried chicken" in main_plate_names and isinstance(menu_item, Dessert):
                price *= 0.95  # 5% Discount on desserts

            total_bill += price
            total_quantity += quantity

        if total_quantity >= 10:
            total_bill *= 0.97  # 3% discount if the order has 10 items or more

        return total_bill
    
    def create_new_menu(self):
        self.menu={}

    def add_items_to_menu(self):
        product_type = input("Cual tipo de producto (Beverage, Apetizer, Dessert, MainPlate): ")

        name = input("Enter name: ")
        price = float(input("Enter price: "))

        if product_type == "Beverage":
            item = Beverage(name, price)

        elif product_type == "Apetizer":
            item = Apetizer(name, price)

        elif product_type == "Dessert":
            item = Dessert(name, price)

        elif product_type == "MainPlate":
            item = MainPlate(name, price)

        self.menu[name] = item

        return self.menu
    
    def update_menu_items(self):
        name=input("Cual es el nombre del producto que quieres modificar")
        price=input("cual es el nuevo precio")
        if name in self.menu.keys():
            price = float(input("Nuevo precio: "))
            self.menu[name]["price"] = price
            print("Actualizado")

        else: 
            print("No existe el elemento")

    def delete_menu_items(self):
        name=input("Cual item quieres remover")
        if name in self.menu.keys():
            p=self.menu.pop(name)
            print (f"Se eleminio {p}")
        
        else:
            "No existe el elemento "

class Manage_orders:
    def __init__(self):
        self.list_orders=[]

    
    def add_list_orders(self, order:Order):
        self.list_orders.append(order)


    def manage_order(self):
        cola_fifo=Queue(maxsize=15)
        for order in self.list_orders:
            cola_fifo.put(order)
        
        if cola_fifo.full():
            print("La cola esta llena, por favor esperar")
        
        while not cola_fifo.empty():
            order_removida=cola_fifo.get()
            print ("Enviando orden a cocina ",order_removida.show_order())

class Payment:
    def __init__(self, bill):
        self.bill = bill

    def pay(self):
        pass


class Card_Payment(Payment):
    def __init__(self, bill):
        super().__init__(bill)
       
    def set_number_card(self, number_card: str):
        self.__number_card = number_card
    
    def set_cvv(self, cvv: int):
        self.__cvv = cvv
    
    def pay(self):
        return f"Thanks for paying {self.bill} with the card ending with {self.__number_card[-4:]}"


class Money_Payment(Payment):
    def __init__(self, bill):
        super().__init__(bill)
     
    def set_amount(self, amount: float):
        self.__amount = amount
    
    def get_amount(self):
        return self.__amount
    
    def pay(self):
        if self.__amount >= self.bill:
            return f"Thanks for paying {self.bill}, here is your change {self.__amount - self.bill}"
        else:
            return "You don't have enough money :///"
            
# 🥤 Drinksn
coke = Beverage("Coca-cola", 2.5)
coke.set_size("medium")
coke.set_bottle_type("plastic")

water = Beverage("Water", 1.5)
water.set_size("large")
water.set_bottle_type("glass")

juice = Beverage("Orange juice", 3.0)
juice.set_size("small")
juice.set_bottle_type("tetra pak")

iced_tea =Beverage("Iced tea", 2.0)
iced_tea.set_size("medium")
iced_tea.set_bottle_type("plastic")

# 🍟 Appetizers
fries = Apetizer("French fries", 3.0)
fries.set_sauce("Ketchup")

wings = Apetizer("Wings", 4.5)
wings.set_sauce("BBQ")

nuggets = Apetizer("Nuggets", 3.5)
nuggets.set_sauce("Mustard")

salad = Apetizer("Mixed salad", 3.0)
salad.set_sauce("Ranch")

# 🍽️ Main Courses
hamburger = MainPlate("Hamburger", 6.0)
hamburger.set_accompaniment1("French fries")
hamburger.set_accompaniment2("Salad")

fried_chicken = MainPlate("Fried chicken", 7.0)
fried_chicken.set_accompaniment1("Mashed potatoes")
fried_chicken.set_accompaniment2("Corn")

lasagna = MainPlate("Lasagna", 8.0)
lasagna.set_accompaniment1("Garlic bread")
lasagna.set_accompaniment2("Green salad")

steak = MainPlate("Steak", 9.5)
steak.set_accompaniment1("Rice")
steak.set_accompaniment2("Sautéed potatoes")

# 🍰 Desserts
ice_cream = Dessert("Ice cream", 2.0)
ice_cream.set_flavour("Vanilla")

chocolate_cake = Dessert("Chocolate cake", 2.5)
chocolate_cake.set_flavour("Chocolate")

flan = Dessert("Flan", 2.2)
flan.set_flavour("Caramel")

brownie = Dessert("Brownie", 2.8)
brownie.set_flavour("Walnut")


# Create an order
order_1 = Order(number=1)

# Add items
order_1.add_items(juice, 2)         # Juice (Drink)
order_1.add_items(nuggets, 2)       # Nuggets (Appetizer)
order_1.add_items(ice_cream, 2)     # Ice cream (Dessert)
order_1.add_items(water, 2)         # Water (Drink)

order2= Order(2)
order2.add_items(ice_cream, 2)

order3= Order(3)
order3.add_items(hamburger,6)

print(order_1.calculate_total_price())

Manage_orders1=Manage_orders()

Manage_orders1.add_list_orders(order_1)
Manage_orders1.add_list_orders(order2)
Manage_orders1.add_list_orders(order3)
Manage_orders1.manage_order()


