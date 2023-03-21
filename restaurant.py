from experta import * #Experta is a Python library for building expert systems strongly inspired by CLIPS.
import colorama  #Python Library to Print Colored Text 
from colorama import Fore, Style
colorama.init(autoreset=True) 

class Hungry(KnowledgeEngine): #create a class

#define constractor
    def __init__(self, get_locations, get_details): #define init 
        self.get_details = get_details # define get_details function
        self.get_locations = get_locations # define get_locations function
        KnowledgeEngine.__init__(self) # assignment to knowledgeEngine

    #code giving instructions on how to use the Expert System
    @DefFacts() 
    def _initial_action(self):
        print("")
        print(Fore.RED+Style.BRIGHT+"------------------------------------- Find a Restaurant in Tunisia -------------------------------------") # print the main objective of the project 
        print("")
        print(Fore.LIGHTGREEN_EX+"                  Are you hungry or do you want something to drink?    ")  
        print("")
        print(Fore.MAGENTA+"       We are here to help you enjoy your time by choosing the right restaurant to go.   ") 
        print("")
        print(Fore.LIGHTYELLOW_EX+ "       So Let's turn the minutes into moments ! Time to start :D ==> Reply yes or no ") # how to reply
        print("")
        yield Fact(action="eating") # send a value "eating" back to the call

    #taking various input from user

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Expensive=W())), salience=13)  
    def choice_0(self): 
        self.declare(Fact(Expensive=input(Fore.CYAN+"                              Expensive => "+Fore.LIGHTWHITE_EX))) #declare choice N°=0

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Chic=W())), salience=12)
    def choice_1(self):
        self.declare(Fact(Chic=input(Fore.CYAN+"                              Chic => "+Fore.LIGHTWHITE_EX))) #declare choice N°=1
    
    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Traditional=W())), salience=11)
    def choice_2(self):
        self.declare(Fact(Traditional=input(Fore.CYAN+"                              Traditional => "+Fore.LIGHTWHITE_EX))) #declare choice N°=2

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Full_Service=W())), salience=10)
    def choice_3(self):
        self.declare(Fact(Full_Service=input(Fore.CYAN+"                              Full Service => "+Fore.LIGHTWHITE_EX))) #declare choice N°=3

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Quick_Service=W())), salience=9)
    def choice_4(self):
        self.declare(Fact(Quick_Service=input(Fore.CYAN+"                              Quick Service => "+Fore.LIGHTWHITE_EX))) #declare choice N°=4

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Savoury_Dishes=W())), salience=8)
    def choice_5(self):
        self.declare(Fact(Savoury_Dishes=input(Fore.CYAN+"                              Savoury Dishes => "+Fore.LIGHTWHITE_EX)))  #declare choice N°=5

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Sweet_Dishes=W())), salience=7)
    def choice_6(self):
        self.declare(Fact(Sweet_Dishes=input(Fore.CYAN+"                              Sweet Dishes => "+Fore.LIGHTWHITE_EX))) #declare choice N°=6

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Tunisian_Cuisine=W())), salience=6)
    def choice_7(self):
        self.declare(Fact(Tunisian_Cuisine=input(Fore.CYAN+"                              Tunisian Cuisine => "+Fore.LIGHTWHITE_EX))) #declare choice N°=7

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Italian_Cuisine=W())), salience=5)
    def choice_8(self):
        self.declare(Fact(Italian_Cuisine=input(Fore.CYAN+"                              Italian Cuisine => "+Fore.LIGHTWHITE_EX))) #declare choice N°=8
    
    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Korean_Cuisine=W())), salience=4)
    def choice_9(self):
        self.declare(Fact(Korean_Cuisine=input(Fore.CYAN+"                              Korean Cuisine => "+Fore.LIGHTWHITE_EX))) #declare choice N°=9

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Mexican_Cuisine=W())), salience=3)
    def choice_10(self):
        self.declare(Fact(Mexican_Cuisine=input(Fore.CYAN+"                              Mexican Cuisine => "+Fore.LIGHTWHITE_EX))) #declare choice N°=10

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Turkish_Cuisine=W())), salience=2)
    def choice_11(self):
        self.declare(Fact(Turkish_Cuisine=input(Fore.CYAN+"                              Turkish Cuisine => "+Fore.LIGHTWHITE_EX))) #declare choice N°=11

    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Home_delivery=W())), salience=1)
    def choice_12(self):
        self.declare(Fact(Home_delivery=input(Fore.CYAN+"                              Home delivery => "+Fore.LIGHTWHITE_EX))) #declare choice N°=12
    
    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Access_Wifi=W())), salience=0)
    def choice_13(self):
        self.declare(Fact(Access_Wifi=input(Fore.CYAN+"                              Access Wifi => "+Fore.LIGHTWHITE_EX))) #declare choice N°=13
    
    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Outside_Seating=W())), salience=-1)
    def choice_14(self):
        self.declare(Fact(Outside_Seating=input(Fore.CYAN+"                              Outside Seating => "+Fore.LIGHTWHITE_EX))) #declare choice N°=14
    
    # a rule contains return value of DefFacts , a choice noum that can not be matched with any value and the priority of the rule 
    @Rule(Fact(action="eating"), NOT(Fact(Sea_view=W())), salience=-2)
    def choice_15(self):
        self.declare(Fact(Sea_view=input(Fore.CYAN+"                              Sea view => "+Fore.LIGHTWHITE_EX))) #declare choice N°=15

    #different rules checking for each restaurant match

#Rule for Chili's restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="yes"),
        Fact(Chic="yes"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="yes"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_1(self):
        self.declare(Fact(restaurant="Chilis"))

    #Rule for Club Grill Citroen restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="yes"),
        Fact(Chic="yes"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="yes"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_2(self):
        self.declare(Fact(restaurant="Club_Grill_Citroen"))

     #Rule for Crepe Factory restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="no"),
        Fact(Chic="no"),
        Fact(Traditional="no"),
        Fact(Full_Service="no"),
        Fact(Quick_Service="yes"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_9(self):
        self.declare(Fact(restaurant="Crepes_Factory"))

    #Rule for Trattoria Crock Pizza restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="no"),
        Fact(Chic="no"),
        Fact(Traditional="no"),
        Fact(Full_Service="no"),
        Fact(Quick_Service="yes"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="no"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="yes"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="no"),
        Fact(Outside_Seating="no"),
        Fact(Sea_view="no")
    )
    def restaurant_3(self):
        self.declare(Fact(restaurant="Trattoria_Crock_Pizza"))

    #Rule for Lebambou restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="yes"),
        Fact(Chic="yes"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="no"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="yes"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_4(self):
        self.declare(Fact(restaurant="Le_bambou"))

    #Rule for El Ali restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="yes"),
        Fact(Chic="no"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="yes"),
        Fact(Italian_Cuisine="yes"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="no"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="no"),
        Fact(Sea_view="no")
    )
    def restaurant_5(self):
        self.declare(Fact(restaurant="El_Ali"))

    #Rule for Soltana restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="no"),
        Fact(Chic="no"),
        Fact(Traditional="yes"),
        Fact(Full_Service="no"),
        Fact(Quick_Service="yes"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="no"),
        Fact(Tunisian_Cuisine="yes"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="no"),
        Fact(Access_Wifi="no"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_6(self):
        self.declare(Fact(restaurant="Soltana"))

    #Rule for Le Safran restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="yes"),
        Fact(Chic="yes"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="yes"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="yes")
    )
    def restaurant_7(self):
        self.declare(Fact(restaurant="Le_Safran"))

    #Rule for YoYo food restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="no"),
        Fact(Chic="yes"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_8(self):
        self.declare(Fact(restaurant="YoYo_food"))
    
   

    #Rule for Farm Ranch restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="no"),
        Fact(Chic="no"),
        Fact(Traditional="no"),
        Fact(Full_Service="yes"),
        Fact(Quick_Service="no"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="yes"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_10(self):
        self.declare(Fact(restaurant="Farm_Ranch"))
    
    #Rule for Echemi restaurant
    @Rule(
        Fact(action="eating"),
        Fact(Expensive="no"),
        Fact(Chic="yes"),
        Fact(Traditional="no"),
        Fact(Full_Service="no"),
        Fact(Quick_Service="yes"),
        Fact(Savoury_Dishes="yes"),
        Fact(Sweet_Dishes="no"),
        Fact(Tunisian_Cuisine="no"),
        Fact(Italian_Cuisine="no"),
        Fact(Korean_Cuisine="no"),
        Fact(Mexican_Cuisine="no"),
        Fact(Turkish_Cuisine="no"),
        Fact(Home_delivery="yes"),
        Fact(Access_Wifi="yes"),
        Fact(Outside_Seating="yes"),
        Fact(Sea_view="no")
    )
    def restaurant_11(self):
        self.declare(Fact(restaurant="Echemi"))

    #identify restaurant
    @Rule(Fact(action="eating"), Fact(restaurant=MATCH.restaurant), salience=-3)
    
    def restaurant(self, restaurant): 
        print("")
        id_restaurant = restaurant # restaurant noum 
        restaurant_details = self.get_details(id_restaurant) # restaurant details
        locations = self.get_locations(id_restaurant) # restaurant locations
        print("")
        print(Fore.RED+Style.BRIGHT+"------------- Your choices match %s ------------- \n" % (id_restaurant)) #display restaurant 
        print(Fore.GREEN+"A short description of the restaurant is given below :\n") # display restaurant description
        print(Fore.LIGHTWHITE_EX+Style.BRIGHT+restaurant_details + "\n")
        print(Fore.LIGHTMAGENTA_EX+"Locations: \n") # display locations
        print(Fore.LIGHTWHITE_EX+Style.BRIGHT+locations + "\n")
    
    # If no restaurant is found
    @Rule(
        Fact(action="eating"),
        Fact(Expensive=MATCH.Expensive),
        Fact(Chic=MATCH.Chic),
        Fact(Traditional=MATCH.Traditional),
        Fact(Full_Service=MATCH.Full_Service),
        Fact(Quick_Service=MATCH.Quick_Service),
        Fact(Savoury_Dishes=MATCH.Savoury_Dishes),
        Fact(Sweet_Dishes=MATCH.Sweet_Dishes),
        Fact(Tunisian_Cuisine=MATCH.Tunisian_Cuisine),
        Fact(Italian_Cuisine=MATCH.Italian_Cuisine),
        Fact(Korean_Cuisine=MATCH.Korean_Cuisine),
        Fact(Mexican_Cuisine=MATCH.Mexican_Cuisine),
        Fact(Turkish_Cuisine=MATCH.Turkish_Cuisine),
        Fact(Home_delivery=MATCH.Home_delivery),
        Fact(Access_Wifi=MATCH.Access_Wifi),
        Fact(Outside_Seating=MATCH.Outside_Seating),
        Fact(Sea_view=MATCH.Sea_view),
        NOT(Fact(restaurant=MATCH.restaurant)),
        salience=-4)

    def not_matched(self): 
        print(Fore.YELLOW+"\n          The system did not find a restaurant that matched your exact choices.\n")

    