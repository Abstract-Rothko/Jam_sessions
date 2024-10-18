# Inner Conflicts of a Teenage Degenerate

# Background context
print("Meet Parker Aaron Class. \nHe's 16 years old, an average teenager who's defining trait is the fact the he's an avid trap-rock listener.")
print("Everyday is relatively boring with normal problems, normal solutions and normal outcomes.")
print("...")
print("Normal. Normal. Normal.")
print("If he continued living like this, then perhaps—just maybe, he can finally be a regular person... but that was a story for another time.")
print("In today's story, Parker had run into a bit of a problem.")

# Suggest to play
print("He needs a higher power to help guide his decisions")
play = input("Will you help?\n(Yes/No) ").lower()

if play == "yes":
    print("Alright, let's access his brain!")
elif play == "no":
    print("Welp, maybe next time~!")
    quit()
else:
    print("That answer is not accepted.")
    quit()

# Storyline begins
print(" ")
print("Answer simply with a 'yes' or 'no'.")
print(" ")
choice = input("You find a dirty magazine on your way to school.\nDo you pick it up? ").lower()
if choice == "no":
    print(" ")
    chance = input("Are you sure?\nWhen are you getting a chance like this again?\nDon't you want the magazine? ").lower()
    if chance == "no":
        print(" ")
        spring = input("Even though it's a spring edition?\nThose usually have a wide variety of—No, No, No!\nYou should NOT investigate.\nRight? ").lower()
        if spring == "no":
            print(" ")
            century = input("It's the 21st century. \nNo one reads magazines anymore–even though this one, even at a glace, is still in great condition!\nAren't you curious at all? ").lower()
            if century == "no":
                print(" ")
                first = input("It won't hurt just to read a couple of pages.\nYou can toss the book afterwards—no judgement.\nWhat do you say? ").lower()
                if first == "no":
                    print(" ")
                    cover = input("One of the people on the cover looks familiar, but you need a closer look.\nInvestigate? ").lower()
                    if cover == "no":
                        print(" ")
                        one = input("Take a look around first.\nDo you want to see if anyone's watching you first? ").lower()
                        if one == "no":
                            print(" ")
                            growth = input("You're a growing teenager, these conflicted feelings are normal.\nEveryone has met the same challenges.\nWill you take the magazine? ").lower()
                            if growth == "no":
                                print(" ")
                                regret = input("You might come to regret this later. Are you sure? ").lower()
                                if regret == "no":
                                    print(" ")
                                    crush = input("On your way to school, you run into your crush walking in the opposite direction.\nYou give each other an awkward greeting, smile, then continue walking.\nWill you turn back and strike a conversation? ").lower()
                                    if crush == "no":
                                        print(" ")
                                        print("As you sneak a last glance at them, you clearly see how they pick up the dirty magazine and dart off.\nThe End :-)")
                                    elif crush == "yes":
                                        print("As you turn to talk to them, you clearly see how they pick up the dirty magazine and dart off.\nThe End :-)")
                                    else:
                                        print("That answer is not accepted. You lose :-(")
                                elif regret == "yes":
                                    print("Begrudgingly, embarrassingly–you end up taking the magazine with you.\nWhether you agree or not, you win ;-)")
                                else:
                                    print("That answer is not accepted. You Lose :-( ")
                            elif growth == "yes":
                                print("Oof! Bad timing! Your secret enemy just took a picture of you with a dirty magazine. This will used against you!\You Lose! :-(")
                            else:
                                print("That answer is not accepted.\nYou Lose :-(")
                        elif one == "yes":
                            print("An elderly person makes eye-contact. After smiling softly, they give you a thumbs up. You end up leaving the magazine out of sheer embarrassment.\nYou lose ;-( ")
                        else:
                            print("That answer is not accepted. You lose ;-(")
                    elif cover == "yes":
                        print("Turns out that it's [redacted], your neighbour and a recent college graduate. The next Sunday dinner is going to be very awkward.\nYou... Win?")
                    else:
                        print("That answer is not accepted. You lose :-( ")
                elif first == "yes":
                    print("Big mistake. You enjoyed it more than you thought you would and out of desire - a very horny one - the magazine is tossed into your bag.\nYou lose :-(")
                else:
                    print("That answer is not accepted. You lose :-(")
            elif century == "yes":
                print("This will actually be your very first physical copy of a magazine. There's a first time for everything.\nYou win ;-)")
            else:
                print("That answer is not accepted. You lose ;-( ")
        elif spring == "yes":
            print("It really is a spring edition!\nThese editions are renowned for their variety of articles on the history of the three sizes.\nThis is gonna be good!\nYou Win ;-)")
        else:
            print("That answer is not accepted. You Lose :-( ")
    elif chance == "yes":
        print("After some hesitance, you pick up the dirty magazine. There's this strange feeling that someone saw you do it, but other than that, you go about your day unperturbed.\nYou Win ;-) ")
    else:
        print("That answer is not accepted. You lose :-( ")
elif choice == "yes":
    print("You pick it up and place it inside your bag, then go about your day.\nZero consequences.\nYou Win ;-)")
else:
    print("That answer is not accepted. You lose :-(")
