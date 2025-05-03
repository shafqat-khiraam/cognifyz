import random

def space_adventure():
    print("Welcome, Captain of the Nebula Voyager!")
    print("As captain of this fine vessel, you are responsible for the safety of your crew and the success of our mission. Today, we embark on an exciting journey to explore the unknown reaches of the galaxy.")
    
    print("\nYour ship's sensors detect a faint distress signal from a nearby planet. The crew is tense, awaiting your command. Do you:")
    print("1. Investigate the signal and potentially help those in need")
    print("2. Play it safe and continue on your current course")
    
    choice1 = input("Enter 1 or 2: ")
    
    if choice1 == "1":
        print("\nYou decide to investigate. As the ship descends through the planet's atmosphere, your heart races. The surface is barren, except for a crashed alien vessel. The scene is eerily quiet.")
        print("Do you:")
        print("1. Approach the wreck and search for survivors")
        print("2. Stay cautious and examine the ship from a distance")
        
        choice2 = input("Enter 1 or 2: ")
        
        if choice2 == "1":
            print("\nYou find alien survivors trapped inside the wreckage. Their eyes plead for help. They look fragile, but there's something odd about their silence.")
            print("Do you:")
            print("1. Offer medical assistance and bring them on board")
            print("2. Stay alert; it could be a trap")
            
            choice3 = input("Enter 1 or 2: ")
            
            if choice3 == "1":
                print("\nYou tend to the injured aliens, and in gratitude, they share advanced technology with your crew. You've forged a new intergalactic alliance!")
            elif choice3 == "2":
                print("\nYour instincts were correct! The aliens reveal their true intentions and attack, but thanks to your caution, you're able to defend your ship and escape. Disaster averted!")
        
        elif choice2 == "2":
            print("\nFrom a distance, you notice strange energy readings coming from the ship. Before you can react, the wreckage explodes, sending shockwaves through the area.")
            print("Do you:")
            print("1. Rush back to your ship and flee the planet")
            print("2. Investigate the source of the explosion")
            
            choice3 = input("Enter 1 or 2: ")
            
            if choice3 == "1":
                print("\nYou manage to escape just in time, but something feels wrong. As your ship departs, you realize the energy blast altered your ship’s systems, and a mysterious force is now tracking you...")
            elif choice3 == "2":
                print("\nInvestigating further, you discover ancient alien technology beneath the surface. Your crew unlocks new secrets that could change the fate of humanity.")
    
    elif choice1 == "2":
        print("\nYou decide to ignore the distress signal. As you sail through the stars, the crew questions your decision. Just as you think all is calm, an anomaly appears on the radar—an unstable wormhole. The ship rattles violently.")
        print("Do you:")
        print("1. Steer into the wormhole to explore the unknown")
        print("2. Avoid the anomaly and find a safer route")
        
        choice2 = input("Enter 1 or 2: ")
        
        if choice2 == "1":
            print("\nThe wormhole pulls you in, twisting time and space. When you emerge on the other side, you're in an entirely new galaxy—untouched and full of possibilities. You've opened the door to a new frontier!")
        elif choice2 == "2":
            print("\nYou manage to avoid the wormhole, but the ship sustains damage in the process. Systems fail one by one, and soon, you’re left drifting through space, waiting for a miracle.")
    
    print("\nThank you for playing the Space Exploration Adventure, Captain! Your choices have shaped the fate of your mission. Until next time!")
    
space_adventure()
