from hero import Hero

if __name__ == "__main__":
    # If you run this file from the terminal
    # this block is executed.
    my_hero = Hero("Grace Hopper", 200)
    other_hero = Hero("Wonder Woman",100)
    print(my_hero.fight(other_hero.name))