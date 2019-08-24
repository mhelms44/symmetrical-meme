import sys
import os
import logging
import random

logfile = open('logtest.out', 'w')

logging.basicConfig(filename='logtest.out', level=logging.INFO)

def main_menu():
    logging.debug('Loading main menu')
    print("Welcome to the intro screen.")
    print("Select your option")
    print("1. New Game")
    print("2. Options")
    print("3. Exit Game")
    introChoice = input("1, 2, or 3?")
    if introChoice == '1':
        print("You selected new game")
        newgame()
    elif introChoice == '2':
        print("You selected options")
        options()
    elif introChoice == '3':
        print("You selected exit")
        exit_choice()
    else:
        print("I'm not sure what you want. Try again.")
        main_menu()

def exit_choice():
    print("Quitting...")
    logging.info('User initated exit. Goodbye.')
    exit(0)

def newgame():
    print("Launching a new game...")
    print("What is your name?")
    char_name = input("> ")
    char_create(char_name)

def options():
    print("Not a whole lot of options yet either")
    logging.info("Options selected, no support yet.")
    main_menu()

def intro():
    logging.info('Booting up game')
    logging.info('Launching main menu')
    print("Launching...")
    main_menu()

def char_create(char_name):
    print(f"Your character's name is: {char_name}")
    print("What will your character class be?")
    char_classes = ["warrior","ranger","mage"]
    for i in char_classes:
        print(f"{i}")
    char_class_choice = input("Pick your class: >")
    
    if char_class_choice == 'warrior':
        print(f"You picked {char_class_choice}")
        choose_starter_item(char_name, char_class_choice)

    elif char_class_choice == 'ranger':
        print(f"You picked {char_class_choice}")
        choose_starter_item(char_name, char_class_choice)

    elif char_class_choice == 'mage':
        print(f"You picked {char_class_choice}")
        choose_starter_item(char_name, char_class_choice)
    
    else:
        print("you failed, try again!")
        char_create(char_name)

def choose_starter_item(char_name, char_class_choice):
    print("Pick your starter item.")
    starter_item = ["master key","water of revival","pumpkin seed", "5 blackfire bombs"]
    for i in starter_item:
        print(f"{i}")
    starter_item_choice = input("Select your item: ")
    if starter_item_choice == 'master key':
        print(f"You picked {starter_item_choice}")
        print(f"Your character is {char_name} and your class is {char_class_choice}")
        start_game(char_name, char_class_choice, starter_item_choice)
    
    elif starter_item_choice == 'water of revival':
        print(f"You picked {starter_item_choice}")
        print(f"Your character is {char_name} and your class is {char_class_choice}")
        start_game(char_name, char_class_choice, starter_item_choice)
    
    elif starter_item_choice == 'pumpkin seed':
        print(f"You picked {starter_item_choice}")
        print(f"Your character is {char_name} and your class is {char_class_choice}")
        start_game(char_name, char_class_choice, starter_item_choice)
    
    elif starter_item_choice == '5 blackfire bombs':
        print(f"You picked {starter_item_choice}")
        print(f"Your character is {char_name} and your class is {char_class_choice}")
        start_game(char_name, char_class_choice, starter_item_choice)

    else:
        print("You didn't even try did you?")
        choose_starter_item(char_name, char_class_choice)

def fight_sequence(char_name, char_health, npc_health, char_atk, npc_atk, char_class_choice, starter_item_choice):
    while char_health > 1 and npc_health > 1:
        npc_health -= char_atk
        print(f"{char_name} attacks!")
        print(f"{char_name} does {char_atk} damage!")
        print(f"NPC now has {npc_health} health!")
        input("Press enter to continue")
        if npc_health <=0:
            print(f"{char_name} killed the NPC!")
            victory(char_name, char_class_choice, starter_item_choice)
        char_health -= npc_atk
        print("NPC attacks!")
        print(f"NPC does {npc_atk} damage!")
        print(f"{char_name} now has {char_health} health!")
        input("Press enter to continue")
        if char_health <=0:
            print(f"{char_name} is dead!")
            dead(char_name, char_class_choice, starter_item_choice)

def start_game(char_name, char_class_choice, starter_item_choice):
    char_health = random.randrange(50, 80)
    npc_health = random.randrange(20, 60)
    char_atk = random.randrange(5, 30)
    npc_atk = random.randrange(3, 45)
    print("The game is now starting")
    print(f"{char_name} walks into the dark tunnel from their cell, an undead approaches.")
    fight_sequence(char_name, char_health, npc_health, char_atk, npc_atk, char_class_choice, starter_item_choice)

def victory(char_name, char_class_choice, starter_item_choice):
    print("You slayed!")
    print("1. Rematch\n2. New Game\n3. Exit")
    choice = input("> ")
    if choice == '1':
        start_game(char_name, char_class_choice, starter_item_choice)
    elif choice == '2':
        main_menu()
    elif choice == '3':
        exit(0)
    else:
        print("Don't let the victory go to your head, you still suck.")
        dead(char_name, char_class_choice, starter_item_choice)
        

def dead(char_name, char_class_choice, starter_item_choice):
    print(f"{char_name} has died!")
    print("Do you want to try again, start a new game, or exit the game?")
    print("1. Continue\n2. New Game\n3. Exit")
    choice = input("> ")
    if choice == '1':
        start_game(char_name, char_class_choice, starter_item_choice)
    elif choice == '2':
        main_menu()
    elif choice == '3':
        exit(0)
    else:
        print("You're so bad you can't even enter a valid choice.")
        dead(char_name, char_class_choice, starter_item_choice)

intro()