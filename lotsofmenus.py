from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantappmenusource.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# create a user
User1 = User(name="Radhika", email="radhika740@gmail.com", picture='http://ragamuffinsbazaar.co.uk/wp-content/uploads/2014/10/RS-Logo-Outline.png')
session.add(User1)
session.commit()

#Menu for Tex Foods
restaurant1 = Restaurant(user_id=1, name = "Tex Foods")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "French Fries", description = "with garlic and parmesan", price = "$2.99", course = "Appetizer", restaurant = restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken Burger", description = "Juicy grilled chicken patty with tomato mayo and lettuce", price = "$5.50", course = "Entree", restaurant = restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Chocolate Cake", description = "fresh baked and served with ice cream", price = "$3.99", course = "Dessert", restaurant = restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Sirloin Burger", description = "Made with grade A beef", price = "$7.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Root Beer", description = "16oz of refreshing goodness", price = "$1.99", course = "Beverage", restaurant = restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name = "Iced Tea", description = "with Lemon", price = "$.99", course = "Beverage", restaurant = restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name = "Grilled Cheese Sandwich", description = "On texas toast with American Cheese", price = "$3.49", course = "Entree", restaurant = restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name = "Veggie Burger", description = "Made with freshest of ingredients and home grown spices", price = "$5.99", course = "Entree", restaurant = restaurant1)

session.add(menuItem8)
session.commit()




#Menu for Ching Thai
restaurant2 = Restaurant(user_id=1, name = "Ching Thai")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Chicken Stir Fry", description = "with your choice of noodles vegetables and sauces", price = "$7.99", course = "Entree", restaurant = restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Peking Duck", description = " a famous duck dish from Beijing[1] that has been prepared since the imperial era. The meat is prized for its thin, crisp skin, with authentic versions of the dish serving mostly the skin and little meat, sliced in front of the diners by the cook", price = "$25", course = "Entree", restaurant = restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Spicy Tuna Roll", description = "Tuna Roll with spices", price = "$9.99", course = "Appetizer", restaurant = restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Nepali Momo ", description = "Special Nepali Momo", price = "$15", course = "Entree", restaurant = restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Beef Noodle Soup", description = "Beef Noodle soup", price = "$7.99", course = "Appetizer", restaurant = restaurant2)

session.add(menuItem5)
session.commit()




#Menu for Viechina
restaurant3 = Restaurant(user_id=1, name = "Viechina")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Pho", description = "a Vietnamese noodle soup consisting of broth, linguine-shaped rice noodles called banh pho, a few herbs, and meat.", price = "$7.99", course = "Appetizer", restaurant = restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chinese Dumplings", description = "a common Chinese dumpling which generally consists of minced meat and finely chopped vegetables wrapped into a piece of dough skin. The skin can be either thin and elastic or thicker.", price = "$8.99", course = "Entree", restaurant = restaurant3)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Gyoza", description = "The most prominent differences between Japanese-style gyoza and Chinese-style jiaozi are the rich garlic flavor, which is less noticeable in the Chinese version, the light seasoning of Japanese gyoza with salt and soy sauce, and the fact that gyoza wrappers are much thinner", price = "$12", course = "Entree", restaurant = restaurant3)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Stinky Tofu", description = "Taiwanese dish, deep fried fermented tofu served with pickled cabbage.", price = "$9.99", course = "Entree", restaurant = restaurant3)
session.add(menuItem4)
session.commit()



#Menu for Best Thai
restaurant4 = Restaurant(user_id=1, name = "Best Thai")

session.add(restaurant4)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Tres Leches Cake", description = "Rich, luscious sponge cake soaked in sweet milk and topped with vanilla bean whipped cream and strawberries.", price = "$8.99", course = "Dessert", restaurant = restaurant4)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Mushroom risotto", description = "Portabello mushrooms in a creamy risotto", price = "$7.99", course = "Entree", restaurant = restaurant4)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Honey Boba Shaved Snow", description = "Milk snow layered with honey boba, jasmine tea jelly, grass jelly, caramel, cream, and freshly made mochi", price = "$9.99", course = "Beverage", restaurant = restaurant4)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Cauliflower Manchurian", description = "Golden fried cauliflower florets in a midly spiced soya,garlic sauce cooked with fresh cilantro, celery, chilies,ginger & green onions", price = "$8.99",    course="Appetizer", restaurant = restaurant4)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Aloo Gobi Burrito", description = "Vegan goodness. Burrito filled with rice, garbanzo beans, curry sauce, potatoes (aloo), fried cauliflower (gobi) and chutney. Nom Nom", price = "$9.99", course = "Entree", restaurant = restaurant4)

session.add(menuItem5)
session.commit()




#Menu for Jony's Restaurant
restaurant5 = Restaurant(user_id=1, name = "Jony\'s Restaurant ")

session.add(restaurant5)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Shellfish Tower", description = "A Grilled Shellfish with spiced Onions.", price = "$7.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken and Rice", description = "A Deep fried chicken with cup of white rice.", price = "$10.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Mom's Spaghetti", description = "A spaghetti with mild species init.", price = "$8.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Chocolate Icecream", description = "A chocolate Icecream.", price = "$6.99", course = "Dessert", restaurant = restaurant5)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Tonkatsu Ramen", description = "Noodles in a delicious pork-based broth with a soft-boiled egg", price = "$7.99", course = "Entree", restaurant = restaurant5)

session.add(menuItem5)
session.commit()




#Menu for Tex Mex
restaurant6 = Restaurant(user_id=1, name = "Tex Mex")

session.add(restaurant6)
session.commit()


menuItem1 = MenuItem(user_id=1, name = "Lamb Curry", description = "Slow cook that thang in a pool of tomatoes, onions and al those tasty Indian spices.", price = "$11.99", course = "Entree", restaurant = restaurant6)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken Marsala", description = "Chicken cooked in Marsala wine sauce with mushrooms", price = "$9.99", course = "Entree", restaurant = restaurant6)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Potstickers", description = "Delicious chicken and veggies encapsulated in fried dough.", price = "$11.99", course = "Appetizer", restaurant = restaurant6)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Cheese cake", description = "A cheese cake with the toppings of choclate fillings and cherries", price = "$7.99", course = "Dessert", restaurant = restaurant6)

session.add(menuItem4)
session.commit()




#Menu for Halal Point
restaurant7 = Restaurant(user_id=1, name = "Halal point ")

session.add(restaurant7)
session.commit()

menuItem1 = MenuItem(user_id=1, name = "Mutton Biryani", description = "A Fully cooked mutton with Tomatoes, onions and a cooked birayni rice.", price = "$7.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name = "Chicken Tikka Masala", description = "Boiled chicken and gravy of onions and species.", price = "$8.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name = "Egg noodles", description = "A boiled noodles with egg.", price = "$9.99", course = "Entree", restaurant = restaurant7)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name = "Mango Lassi", description = "A Lassi added with Mango pulp Milk and sugar.", price = "$4.99", course = "Beverage", restaurant = restaurant7)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name = "Gulab Jammon", description = "A deep fried Jammon with sugar syrup init.", price = "$4.99", course = "Dessert", restaurant = restaurant7)

session.add(menuItem5)
session.commit()

#Creating User2 and adding a restaurant for him.
User2 = User(name="Vaijayanth", email="vaijayanth.raghavan@gmail.com", picture='http://ragamuffinsbazaar.co.uk/wp-content/uploads/2014/10/RS-Logo-Outline.png')
session.add(User2)
session.commit()

#Menu for VJ Bistro
restaurant8 = Restaurant(user_id=2, name = "VJ Bistro ")

session.add(restaurant8)
session.commit()

menuItem1 = MenuItem(user_id=2, name = "Falafel Plate", description = "Falafel with pita and hummus", price = "$6.99", course = "Entree", restaurant = restaurant8)

session.add(menuItem1)
session.commit()

print "added menu items!"
