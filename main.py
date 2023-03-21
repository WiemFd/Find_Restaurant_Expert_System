import colorama  # Python Library to Print Colored Text 
#import freeze , unfreeze 
#import forezendict 
from colorama import Fore, Style
colorama.init(autoreset=True) 
from restaurant import Hungry #import class Hungry from restaurant.py
restaurants_list = [] # define empty list of restaurants 
description = {} #define empty descriptions set
location = {} #define empty locations set 



def preprocess(): # function to load information from .txt files into variables 

    #global restaurants_list, description, location
    restaurants = open("restaurants.txt") #open "restaurants.txt" file
    restaurants_t = restaurants.read() # read "restaurants.txt" file
    restaurants_list = restaurants_t.split("\n") # Split "restaurants.txt" file into a list where each word is a list item or a res
    restaurants.close() #close "restaurants.txt" file

    for res in restaurants_list: # loop list of restaurants 

        resto_s_file = open("description/" + res + ".txt") # open description files 
        resto_s_data = resto_s_file.read()# read description files
        description[res] = resto_s_data # restaurant and its description
        resto_s_file.close() #close description files

        resto_s_file = open("location/" + res + ".txt") # open treatment files 
        resto_s_data = resto_s_file.read() #read treatment files
        location[res] = resto_s_data # restaurant and its location
        resto_s_file.close() # close treatement files


def get_details(res): # function to display more details about the restaurant
    return description[res] # return restaurant description


def get_locations(res): # function to display the restaurant location
    return location[res] # return restaurant location


#driver function
if __name__ == "__main__":
    preprocess() # call function preprocess
    #creating instance from the class object Hungry
    engine = Hungry(get_locations, get_details)
    #loop to keep running the code until user says no when asked for another choice
    while 1:
        engine.reset() # reset choice
        engine.run() # run code
        print(Fore.LIGHTCYAN_EX+Style.BRIGHT+"               Would you like to make other choices ? Reply yes or no") # ask for another choice
        if input() == "no": # if choice=no, exit from program else run the code again for a new restaurant choice
            exit()
