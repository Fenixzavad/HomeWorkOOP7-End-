import copy
import Classes
import Zoo


def showAll():
    for i in range(len(Zoo.Zoo.all)):
        print(f"{i+1}) {Zoo.Zoo.all[i]}")


def showInfo(num):
    print(f"{num-1}) {Zoo.Zoo.all[num-1]}")
    if (isinstance(Zoo.Zoo.all[num-1], Classes.Home)):
        Zoo.Zoo.all[num-1].caressing()
    if (isinstance(Zoo.Zoo.all[num-1], Classes.DogTraning)):
        Zoo.Zoo.all[num-1].traning()
    if (isinstance(Zoo.Zoo.all[num-1], Classes.BirdFly)):
        Zoo.Zoo.all[num-1].birdFly()


def sayAll():
    for i in range(len(Zoo.Zoo.all)):
        Zoo.Zoo.all[i].animalSay()


def sayAnimal(num):
    Zoo.Zoo.all[num-1].animalSay()


def addAnimal(num):
    match num:
        case 1:
            addCat()
        case 2:
            addTiger()
        case 3:
            addDog()
        case 4:
            addWolf()
        case 5:
            addChicken()
        case 6:
            addStork()


def addCat():
    name = "Кот"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    name2 = input("Кличка: ")
    breed = input("Порода: ")
    vaccination = input("Наличие прививки: ")
    color = input("Цвет: ")
    date = input("Дата рождения: ")
    wool = input("Наличие шерсти: ")
    animal = Classes.Cat(name, height, weight, colorEye,
                         name2, breed, vaccination, color, date, wool)
    Zoo.Zoo.all.append(copy.copy(animal))


def addTiger():
    name = "Тигр"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    place = input("Ареал обитания: ")
    date = input("Дата обнаружения: ")
    animal = Classes.Tiger(name, height, weight, colorEye, place, date)
    Zoo.Zoo.all.append(copy.copy(animal))


def addDog():
    name = "Собака"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    name2 = input("Кличка: ")
    breed = input("Порода: ")
    vaccination = input("Наличие прививки: ")
    color = input("Цвет: ")
    date = input("Дата рождения: ")
    wool = input("Наличие шерсти: ")
    animal = Classes.Dog(name, height, weight, colorEye,
                         name2, breed, vaccination, color, date, wool)
    Zoo.Zoo.all.append(copy.copy(animal))


def addWolf():
    name = "Волк"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    place = input("Ареал обитания: ")
    date = input("Дата обнаружения: ")
    leader = bool(input("Вожак стаи? True/False: "))
    animal = Classes.Wolf(name, height, weight, colorEye, place, date, leader)
    Zoo.Zoo.all.append(copy.copy(animal))


def addChicken():
    name = "Курица"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    fly = 0
    animal = Classes.Chicken(name, height, weight, colorEye, fly)
    Zoo.Zoo.all.append(copy.copy(animal))


def addStork():
    name = "Аист"
    height = int(input("Рост: "))
    weight = int(input("Вес: "))
    colorEye = input("Цвет глаз: ")
    fly = int(input("Высота полета: "))
    animal = Classes.Stork(name, height, weight, colorEye, fly)
    Zoo.Zoo.all.append(copy.copy(animal))


def deleteAnimal(num):
    Zoo.Zoo.all.pop(num-1)