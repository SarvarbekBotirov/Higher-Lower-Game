from gc import get_referents
from art import logo, vs
from game_data import data
import random
#Logo higher lower game
print(logo)

#creating first random person from data
first_person = data[random.randint(0,len(data)-1)]
print(f"Compare A: {first_person['name']}, a {first_person['description']}, from {first_person['country']}")
#second logo
print(vs)

#creating second random person from data
second_person = data[random.randint(0,len(data)-1)]
print(f"Compare B: {second_person['name']}, a {second_person['description']}, from {second_person['country']}")

#getting users answer
user_guess = input("Who has more followers? Type \"A\" or \"B\": ").lower()

count = 0


if user_guess == "a" and first_person['follower_count'] > second_person['follower_count']:
    count += 1
elif user_guess == "b" and first_person['follower_count'] < second_person['follower_count']:
    count += 1
print(count)
    

#comparison logic

    