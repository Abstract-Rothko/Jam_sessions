# Phoebe's Adventure

print("Welcome to Phoebe's Adventure.")

play = input("Do you wish to play?\n(Yes/No) ").lower()
if play == "yes":
    print("Let's play then~!")
    print(" ")
    print("Meet Phoebe Erin Class, a ten year-old who's quite self-conscious. It's after school and she needs to get home safely.\nKindly assist.")
    print("...")
    print(" ")
    #Adventure begins
    leave = input("Phoebe just left the Academy and needs to pick a direction. Which one do you suggest?\n(Up/Down) ").lower()
    
    # Normal Route
    if leave == "up":
        hill = input("As she walks up the street, Phoebe notices that Avery, the dog, is growling at her, bearing all its teeth.\nAvery is notorious for his bites and it's making her nervous. Should she:\n1) Keep her pace and ignore Avery\n2) Run as fast as she can ")
        if hill == "1":
            print("Avery's growling intensifies as Phoebe walked, but as soon as she passed his yard – Avery stopped.\nHe ignored her afterwards.")
            print("Phew~!")
            crossroads = input("After breathing a sigh of relief, Phoebe reaches her next crossroad. Which way do you suggest?\n(Left/Right) ").lower()
            if crossroads == "left":
                print("Phoebe turns left and continues her journey.")
                friend = input("Whilst walking, in the distance, she could see Friendly. What should she do?\n(Talk/Ignore) ").lower()
                if friend == "talk":
                    print("Friendly kills Phoebe.\nYou lose.")
                elif friend == "ignore":
                    print("Friendly notices Phoebe and waves with a gentle smile. After realizing he was being ignored, he went on about his day.")
                    street = input("After some distance, Phoebe reaches a street that looks familiar.\nHowever, she does not know if it will take her home. Should she take that chance?\n(Yes/No) ").lower()
                    if street == "yes":
                        print("Phoebe decides to walk down the familiar-looking street.")
                        doubt = input("After what feels like a long, quiet walk – Phoebe gets less and less confident in her decision. Maybe she was confused. Should she:\n1) Continue with her journey?\n2) Go back to where she started? ").lower()
                        if doubt == "1":
                            print("Taking in a deep breath, Phoebe decides to continue with her journey.\nAfter turning another corner, she could see her home in the distance.\nShe made it.\nTHE END ★ ")
                        elif doubt == "2":
                            print("Phoebe loses confidence in her sense of direction andvgets lost on the way back.\nYou lose")
                        else:
                            print("That answer is not accepted. You lose :( ")
                    elif street == "no":
                        print("Phoebe gets lost.\nYou lose.")
                    else:
                        print("That answer is not accepted.\nYou lose :( ")
                else:
                    print("That answer is not accepted. You lose :( ")
            elif crossroads == "right":
                print("Phoebe turns right and continues her journey.")
                car = input("A car suddenly stops next to Phoebe. A stranger offers a lift. Should she accept?\n(Yes/No) ").lower()
                if car == "yes":
                    print("Phoebe gets kidnapped.\nDon't talk to strangers. You lose.")
                elif car == "no":
                    print("Phoebe declines the offer and continues walking.")
                    actual = input("She runs into Jodie, her class friend, who proposes that Phoebe stay at her place until her dad picks her up. Should she accept?\n(Yes/No) ").lower()
                    if actual == "yes":
                        print("Phoebe stays at Jodie's until her dad picks her up. After a good scolding, Phoebe promises never to wander off again.\nTHE END XD")
                    elif actual == "no":
                        print("Phoebe declines Jodie's proposal and pushes forward on her journey.\She gets lost. You lose.")
                    else:
                        print("That answer is not accepted. You lose :( ")
                else:
                    print("That answer is not accepted. You lose :( ")
            else:
                print("That answer is not accepted. You lose :( ")
        elif hill == "2":
            print("Avery gives chase and catches up to Phoebe. You lose.")
        else:
            print("That answer is not accepted. You lose :( ")
    
    # Fantasy Route
    elif leave == "down":
     route = input("As Phoebe travelled down the street, she came across three routes. Which one should she choose?\n(Left/Right/Straight)  ").lower()
     if route == "left":
         print("Phoebe turns left and continues her journey.")
         print("Rain begins to pour lightly, casting a mist-like environment.")
         laces = input("'Oh?' Her shoe laces had come undone. Should she:\n1) Tie them or\n2) Continue? ")
         if laces == "1":
             print("Phoebe ties her shoelaces before continuing with her adventure.")
             friend = input("Whilst walking, in the distance, she could see Friendly. What should she do?\n(Talk/Ignore) ").lower()
             if friend == "ignore":
                 print("Friendly notices Phoebe and waves with a gentle smile. After realizing he was being ignored, he went on about his day.")
                 portal = input("After some distance, a magic portal appears in front Phoebe. Should she enter?\n(Yes/No) ").lower()
                 if portal == "no":
                     print("The portal feels unusual, Phoebe thought. She decides to continue her journey rather than investigate.")
                     voice = input("Faintly, Phoebe felt her ears tingle at the sound of someone singing in the rain. It was heavenly, but also sounded sad. Should she investigate?\n(Yes/No) ").lower()
                     if voice == "yes":
                         print("Following the sound of the beautiful voice, Phoebe managed to locate the source—it was a rain siren!!\nYou Lose")
                     elif voice == "no":
                         print("Slapping her cheeks, Phoebe convinced herself to focus. She continued on her journey and finally made it to the end. She really made it home!\nTHE END XD")
                     else:
                         print("That answer is not accepted. You lose :( ")
                 elif portal == "yes":
                     print("Phoebe gets tranported to the OtherWorld.\nYou Lose.")
                 else:
                     print("That answer is not accepted. You lose :( ")
             elif friend == "talk":
                 print("Friendly kills Phoebe.\nYou Lose.")
             else:
                 print("That answer is not accepted. You lose :( ")
         elif laces == "2":
             print("It can wait, Phoebe mused. She was better off picking up the pace before the started to pour—Ah!")
             print("Phoebe tripped, not even five steps later.")
             print("This fall had been truly bad. She had fallen into another world")
             print("Sunny skies. Green clouds. Blue plants.")
             egg = input("In front of her was an egg. Should she take it?\n(Yes/No) ").lower()
             if egg == "yes":
                 print("Phoebe decides to take the egg with her.")
                 bird = input("A giant bird-like creature appears before Phoebe with a saddle. It will giver her a ride, in exchange for the egg.\n(Yes/No) ").lower()
                 if bird == "yes":
                     print("The creature takes Phoebe on its saddle, flaps its powerful wings, then takes flight. Phoebe's unsure how exactly the creature knew, but it flew her to another portal which lead to her home, allowing her to arrive safely.\nTHE END ★")
                 elif bird == "no":
                     print("Phoebe refuses and decides to walk the journey by herself. Who knows if that creature was trying to trick her not")
                     flag = input("'!' — Suddenly, a large object fell from the sky in front of her. It was the bird-like creature. Should she investigate?\n(Yes/No) ").lower()
                     if flag == "yes":
                         print("A dimension-warping dragon appears.\nEveryone dies.")
                     elif flag == "no":
                         print("A dimension-warping dragon appears.\nEveryone dies.")
                     else:
                         print("That answer is not accepted. You lose :( ")
                 else:
                     print("That answer is not accepted. You lose :( ")
             elif egg == "no":
                 print("Phoebe gets carried off by a giant bird-like creature for being in its territory.\nYou Lose.")
             else:
                 print("That answer is not accepted. You lose :( ")
         else:
             print("That answer is not accepted. You lose :( ")
     elif route == "right":
         print("Phoebe turns right and continues her journey.")
         rain = input("As she walks, it suddenly begins to pour. Should she look for shelter?\n(Yes/No) ").lower()
         if rain == "yes":
             print("Phoebe decides to sit at a nearby bus stop until the heavy rains subsided a little. How long that would be, shw did not know, but the covering did help if only a little.")
             cat = input("Mr. Timothy the Cat suddenly appeared next to Phoebe and struck up a conversation. Should she:\n1) Have a conversation with Mr. Timothy or \n2) Ignore him and sit in silence? ")
             if cat == "1":
                 print("Phoebe and Mr. Timothy have a conversation about a range of topics and, after hearing her plight, he hands her an umbrella and chuckles. Aftwerwards, he disappears.")
                 umbrella = input("The rain subsides a little and now she has an umbrella. Should Phoebe continue her journey?\n(Yes/No) ").lower()
                 if umbrella == "yes":
                     print("And so, Phoebe continued her journey")
                     nymph = input("After walking and singing to herself for quite a while, a rain spirit suddenly manifested in front of her. 'Let me show you the way, little one,' it said. What should be Phoebe's response?\n(Yes/No) ").lower()
                     if nymph == "no":
                         print("Phoebe politely declines the offer, and continues on her journey.")
                         print("Before she had even realized it, she had already made it home!\nTHE END ★")
                     elif nymp == "yes":
                         print("After accepting the rain spirit's proposal, Phoebe get's transported to the Spirit World and only returns in 16 years. You lose.")
                     else:
                         print("That answer is not accepted. You lose :( ")
                 elif umbrella == "no":
                     print("After waiting a couple more minutes, a bus showed up. Phoebe took the bus home.\nTHE END XD ")
                 else:
                     print("That answer is not accepted. You lose :( ")
             elif cat == "2":
                 print("After an awkward silence, Mr. Timothy disappears. The rain continues pouring until nightfall.\nYou lose.")
             else:
                 print("That answer is not accepted. You lose:( ")
         elif rain == "no":
             print("Due to rapid change in temperature, Phoebe suddenly goes into shock and collapses.\nYou lose.")
         else:
             print("That answer is not accepted. You lose :( ")
     elif route == "straight":
         print("Wrong choice. You lose.")
     else:
         print("That answer isn't accepted. You lose :( ")
    else:
        print("That answer isn't accepted. You lose :( ")
elif play == "no":
    print("Maybe next time~!")
else:
    quit()