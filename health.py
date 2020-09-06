import random

health = 50
#to set mode we use difficulty
difficulty = 3
#to get integer value use int called casting to convert one data type to other
potion_health = int(random.randint(25,50)/difficulty)
health = health + potion_health
print(health)
