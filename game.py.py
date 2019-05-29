#Есть список со словам “rock”, “scissors”, “paper”.
#Создайте прототип игры камень-ножницы-бумага с компьютером,
# в основе которой будет находится функции random.choice и input()

from random import choice

def igra(comp, user):
    if comp == user:
        print("Ничья")

    if user == "paper":
        if comp == "scissors":
            print("comp win")
        elif comp == "rock":
            print("user win")

    if user == "rock":
         if comp == "scissors":
             print("user win")
         elif comp == "paper":
             print("comp win")

    if user == "scissors":
        if comp == "paper":
            print("user win")
        elif comp == "rock":
            print("comp win")

game = ["rock", "scissors", "paper"]
comp = choice(game)
user = input("Введите вариант;")
igra(comp, user)
print(comp)
