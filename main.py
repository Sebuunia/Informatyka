from character import Warrior
from character import Gnom
from character import Mag
from character import Archer
import random
global name

def battle(hero, enemy):
    print(f"\n{hero.name} is fighting against {enemy.name}!\n")
    
    while hero.health > 0 and enemy.health > 0:
        turn = random.choice([hero, enemy])
        
        if turn == hero:
            print(f"{hero.name} attacks {enemy.name}!")
            hero.attack(enemy)
        else:
            print(f"{enemy.name} attacks {hero.name}!")
            enemy.attack(hero)
        
        print(f"{hero.name} - Health: {hero.health}")
        print(f"{enemy.name} - Health: {enemy.health}\n")
    
    if hero.health > 0:
        print(f"{hero.name} wins the battle!")
        hero.damage += 5 
        print(f"{hero.name} gains +5 damage! New damage: {hero.damage}\n")
        return True
    else:
        print("+----------------------------------------------------+")
        print(f"{hero.name} lost the battle... Game Over!")
        print("+----------------------------------------------------+")
        return False


print("+----------------------------------------------------+")
print("+------------------DragonRPG-v0.0.1------------------+")
print("+----------------------------------------------------+")
while True:
    print("1. New Game")
    print("2. About")
    print("3. Character History")
    print("4. Quit Game")
    print("+----------------------------------------------------+")
    operator = input(">")

    if operator == "1":
        print("")
        name = input("Enter your nickname: ")
        print("")
        print("+----------------------------------------------------+")
        print("> What class do you want to choose?")
        print("+----------------------------------------------------+")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("+----------------------------------------------------+")
        choose = input(">")
        if choose == "1":
            print("")
            print("+----------------------------------------------------+")
            print("Warrior: ")
            print("+----------------------------------------------------+")
            hero = Warrior(name, health=100, damage=10)
            print(f"Name: {name}")
            print(f"Health: {hero.health}")
            print(f"Damage: {hero.damage}")
            print("+-----------------------------------------------------+")
            gnom = Gnom()
            if not battle(hero, gnom):
                print("Game Over")
                break
            else:
                print("Proceeding to the next challenge...")
            print("+-----------------------------------------------------+")
        elif choose == "2":
            print("")
            print("+----------------------------------------------------+")
            print("Mag: ")
            print("+----------------------------------------------------+")
            hero = Mag(name, health=80, damage=8)
            print(f"Name: {name}")
            print(f"Health: {hero.health}")
            print(f"Damage: {hero.damage}")
            print("+-----------------------------------------------------+")
            gnom = Gnom()
            if not battle(hero, gnom):
                print("Game Over")
                break
            else:
                print("Proceeding to the next challenge...")
            print("+-----------------------------------------------------+")
        elif choose == "3":
            print("")
            print("+----------------------------------------------------+")
            print("Archer: ")
            print("+----------------------------------------------------+")
            hero = Archer(name, health=40, damage=9)
            print(f"Name: {name}")
            print(f"Health: {hero.health}")
            print(f"Damage: {hero.damage}")
            print("+-----------------------------------------------------+")
            print("You met a gnome on your way! The fight begins!")
            print("+-----------------------------------------------------+")
            gnom = Gnom()
            if not battle(hero, gnom):
                print("Game Over")
                break
            else:
                print("Proceeding to the next challenge...")
            print("+-----------------------------------------------------+")


    elif operator == "2":
        print("+-----------------------------------------------------+")
        print("> About DragonRPG")
        print("+-----------------------------------------------------+")
        print("DragonRPG was created for long-term")
        print("computer science work.")
        print("It was designed without much thought and for fun")
        print("DragonRPG was developed by me: Sebastian K......")
        print("If you find any bugs in the game just DM me on Discord")
        print("My username is sebusiekpolakpl")
        print("+-----------------------------------------------------+")

    elif operator == "3":
        print("+-----------------------------------------------------+")
        print("1. Warrior")
        print("2. Mage")
        print("3. Archer")
        print("+-----------------------------------------------------+")
        hist = input(">")

        if hist == "1":
            print("+-----------------------------------------------------+")
            print("The warrior, whose heart beat to the rhythm of battle, stood on the front lines, unafraid of any enemy.")
            print("His sword, which he had fought with since his youth, was as strong as his will.")
            print("After each battle, wounded yet unyielding, he returned to his village to rest and prepare for the next clash.")
            print("+-----------------------------------------------------+")
        elif hist == "2":
            print("+-----------------------------------------------------+")
            print("The mage, master of arcane arts, spent his days in the library studying forgotten spells and magical rituals.")
            print("His power grew with each passing day, but he knew that true strength lay not in spells, but in the ability to control his own emotions.")
            print("When the time came to face the darkness, his magic became the key to saving the world.")
            print("+-----------------------------------------------------+")
        elif hist == "3":
            print("+-----------------------------------------------------+")
            print("The archer, unknown in most villages, could hit a target no one else could see.")
            print("His arrows were as swift as the wind, and his accuracy legendary, making him an invaluable ally on the battlefield.")
            print("Yet despite his fame, deep down he preferred the solitude of the forests, where he could find peace among nature.")
            print("+-----------------------------------------------------+")
    elif operator == "4":
        break