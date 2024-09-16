"""
One Piece Quiz

The plan is to develop a game that asks 20 One Piece-related questions and score how well the questions are answered.
"""

print("Greetings! Welcome to my One Piece Quiz.")

# The desire to play

play = input("Would you like to play? ").lower()
score = 0

if play != "yes":
    print("Maybe next time...")
    quit()
else:
    print("Okay! Let's Pla~ay!")

# 1.

protagonist = input("Who is the protagonist of One Piece? ").lower()

if protagonist == "monkey d. luffy":
    score += 1
    print("Correct!")
elif protagonist == "luffy":
    score += .5
    print("Correct!")
else:
    print("Incorrect!")

# 2.

childhood = input("What is the name of Roronoa Zoro's childhood friend? ").lower()

if childhood != "kuina":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 3.

age = input("On which island did Nami fall sick with the 'Five-day Disease'? ").lower()

if age != "little garden":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 4.

dad = input("What is the name of Usopp's so-called father? ").lower()

if dad != "yassop":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 5.

restuarant = input("What is the name of the restuarant that Sanji used to work at? ").lower()

if restuarant != "baratie":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 6.

food = input("What is Tony Tony Chopper's favourite food? ").lower()

if food != "cotton candy":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 7.

real_name = input("What is Franky's real name? ").lower()

if real_name != "cutty flam":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    

# 8. 
giant = input("What is the name of the giant that used to take care of Nico Robin? ").lower()

if giant == "jaguar d. saul":
    score += 1
    print("Correct!")
elif giant == "saul":
    score += .5
    print("Correct!")
else:
    print("Incorrect!")
    

# 9.
surname = input("What is Vivi's last name? ").lower()

if surname != "nefertari":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    

# 10. 
song = input("Name the song that Brooke is always singing. ").lower()

if song != "bink's sake":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")


# 11.

crew = input("True or False. Jinbe was a former member of the Sun Pirates. ").lower()

if crew != "true":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    

# 12.

seven = input("Name one of the Seven Warlords. ").lower()
warlords = ['crocodile', 'dracule mihawk', 'hanafuda', 'donquixote doflamingo', 'trafalgar law', 'boa hancock', 'bartholomew kuma', 'buggy', 'gecko moria', 'edward weevil', 'jinbe', 'marshall d. teach']

if seven not in warlords:
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 13
alias = input("What is Doflamingo's alias used in the underworld? ").lower()

if alias != "joker":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 14.

member = input("Name one of the Worst Generation members. ").lower()
worst = ['monkey d. luffy', 'roronoa zoro', 'killer', 'eustass kidd', 'trafalgar law', 'jewelry bonney', 'capone bege', 'scratchman apoo', 'x drake', 'marshall d. teach', 'basil hawkins', 'urouge']

if member not in worst:
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 15.

scabbards = input("Name one of the Red Scabbards. ").lower()
red = ["kin'emon", "denjiro", "kikunojo", "nekomamushi", "kawamatsu", "ashura doji", "raizo", "inuarashi", "kanjuro"]

if scabbards not in red:
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

# 16.

island = input("After the Wano Arc, which island was removed from existence by Imu? ").lower()

if island != "lulusia":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    
# 17.
aspect = input("What aspect does York represent of Vegapunk? ").lower()

if aspect != "greed":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    
# 18.
elephant = input("What is the name of the giant elephant that carries zou? ").lower()

if elephant != "zunesha":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    

# 19.
ship = input("What is the name of Blackbeard's ship? ").lower()

if ship != "saber of xebec":
    print("Incorrect!")
else:
    score += 1
    print("Correct!")
    

# 20.
epithets = input("Name one of the epithets used by the admirals. ").lower()
admirals = ['aokiji', 'kizaru', 'akainu', 'fujitora', 'ryokugyu']

if epithets not in admirals:
    print("Incorrect!")
else:
    score += 1
    print("Correct!")

total_score = round((score/20) * 100, 2)    
tot_score_percentage = f"You have achieved a total score of {total_score}%"

print(tot_score_percentage)
if total_score == 100.00:
    print("Congratulations! You beat the quiz! Colour me impressed!")
else:
    print("Good Job!")