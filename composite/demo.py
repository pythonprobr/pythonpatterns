from menu import Menu, MenuItem

pancake_house_menu = Menu("PANCAKE HOUSE MENU", "Breakfast")
diner_menu = Menu("DINER MENU", "Lunch")
cafe_menu = Menu("CAFE MENU", "Dinner")
dessert_menu = Menu("DESSERT MENU", "Dessert of course!")
coffee_menu = Menu("COFFEE MENU", "Stuff to go with your afternoon coffee")

all_menus = Menu("ALL MENUS", "All menus combined")

all_menus.append(pancake_house_menu)
all_menus.append(diner_menu)
all_menus.append(cafe_menu)

pancake_house_menu.append(MenuItem(
	"K&B's Pancake Breakfast",
	"Pancakes with scrambled eggs, and toast",
	True,
	2.99))
pancake_house_menu.append(MenuItem(
	"Regular Pancake Breakfast",
	"Pancakes with fried eggs, sausage",
	False,
	2.99))
pancake_house_menu.append(MenuItem(
	"Blueberry Pancakes",
	"Pancakes made with fresh blueberries, and blueberry syrup",
	True,
	3.49))
pancake_house_menu.append(MenuItem(
	"Waffles",
	"Waffles, with your choice of blueberries or strawberries",
	True,
	3.59))

diner_menu.append(MenuItem(
	"Vegetarian BLT",
	"(Fakin') Bacon with lettuce & tomato on whole wheat",
	True,
	2.99))
diner_menu.append(MenuItem(
	"BLT",
	"Bacon with lettuce & tomato on whole wheat",
	False,
	2.99))
diner_menu.append(MenuItem(
	"Soup of the day",
	"A bowl of the soup of the day, with a side of potato salad",
	False,
	3.29))
diner_menu.append(MenuItem(
	"Hotdog",
	"A hot dog, with saurkraut, relish, onions, topped with cheese",
	False,
	3.05))
diner_menu.append(MenuItem(
	"Steamed Veggies and Brown Rice",
	"Steamed vegetables over brown rice",
	True,
	3.99))

diner_menu.append(MenuItem(
	"Pasta",
	"Spaghetti with Marinara Sauce, and a slice of sourdough bread",
	True,
	3.89))

diner_menu.append(dessert_menu)

dessert_menu.append(MenuItem(
	"Apple Pie",
	"Apple pie with a flakey crust, topped with vanilla icecream",
	True,
	1.59))

dessert_menu.append(MenuItem(
	"Cheesecake",
	"Creamy New York cheesecake, with a chocolate graham crust",
	True,
	1.99))
dessert_menu.append(MenuItem(
	"Sorbet",
	"A scoop of raspberry and a scoop of lime",
	True,
	1.89))

cafe_menu.append(MenuItem(
	"Veggie Burger and Air Fries",
	"Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
	True,
	3.99))
cafe_menu.append(MenuItem(
	"Soup of the day",
	"A cup of the soup of the day, with a side salad",
	False,
	3.69))
cafe_menu.append(MenuItem(
	"Burrito",
	"A large burrito, with whole pinto beans, salsa, guacamole",
	True,
	4.29))

cafe_menu.append(coffee_menu)

coffee_menu.append(MenuItem(
	"Coffee Cake",
	"Crumbly cake topped with cinnamon and walnuts",
	True,
	1.59))
coffee_menu.append(MenuItem(
	"Bagel",
	"Flavors include sesame, poppyseed, cinnamon raisin, pumpkin",
	False,
	0.69))
coffee_menu.append(MenuItem(
	"Biscotti",
	"Three almond or hazelnut biscotti cookies",
	True,
	0.89))

class Garconete:

	def __init__(self, menu):
		self.menu = menu

	def display_menu(self):
		self.menu.display()

jane = Garconete(all_menus)

jane.display_menu()
