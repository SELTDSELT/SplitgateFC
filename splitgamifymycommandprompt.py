import random
import time
print("\n" * 100)
import random

chars = [
    "a", "b", "c", "d", "e", "f", "g",
    "h", "i", "j", "k", "l", "m", "n",
    "o", "p", "q", "r", "s", "t", "u",
    "v", "w", "x", "y", "z",
    "0", "1", "2", "3", "4",
    "5", "6", "7", "8", "9"
]

result = (
    random.choice(chars) +
    random.choice(chars) +
    random.choice(chars) + "-" +
    random.choice(chars) +
    random.choice(chars) +
    random.choice(chars)
)


print("Created by NotDaBenjamin (!!creator)")
print("© 2026 Super Evil Laboratory That Does Super Evil Laboratory Things")
print("Use !!help for a list of commands")
print("Check out my other stupid bullshit projects at https://github.com/SELTDSELT\n")
print("This is not a violation of the 1047 Games or Splitgates TOS, as you must test codes manually (also it has like a 1 in 10 million chance of actually getting a working code.)\n\n")

def run():
    q = input("")
    if q.lower() == "!!pull":
        print("\n" * 100)
        result = (
            random.choice(chars) +
            random.choice(chars) +
            random.choice(chars) + "-" +
            random.choice(chars) +
            random.choice(chars) +
            random.choice(chars)
            )
        print(f"{result.upper()}")
        input("Press enter to exit")
        print("\n" * 100)
        run()
    
    elif q.lower() == "!!mine":
        r = input("Entering mining mode will stop the command prompt tab from being useable, so you must open a new tab to start. Press Y to continue, or N to cancel\n")
        if r.lower() == "y":
            print("\n")
            print("Please type py mine/script.py to start mining.")
        elif r.lower() == "n":
            print("\n" * 100)
            run()
        else:
            print("\n" * 100)
            print("Unknown Command, type !!help for a list of commands")
            run()
    elif q.lower() == "!!uncapmine":
        r = input("Entering mining mode will stop the command prompt tab from being useable, so you must open a new tab to start. Press Y to continue, or N to cancel\n")
        if r.lower() == "y":
            print("\n" * 100)
            print("Please type py mine/lscript.py to start mining.")
        elif r.lower() == "n":
            print("\n")
            run()
        else:
            print("\n" * 100)
            print("Unknown Command, type !!help for a list of commands")
            run()
    elif q.lower() == "!!uncappull":
        print("\n" * 100)
        result = (
            random.choice(chars) +
            random.choice(chars) +
            random.choice(chars) + "-" +
            random.choice(chars) +
            random.choice(chars) +
            random.choice(chars)
            )
        print(f"{result}")
        input("Press enter to exit")
        print("\n" * 100)
        run()
    elif q.lower() == "!!exit":
        print("")
    elif q.lower() == "!!clear":
        print("\n" * 100)
        run()
    elif q.lower() == "!!help":
        print("\n" * 100)
        print("!!pull - Pulls a random friend code")
        print("!!uncappull - Pulls a random friend code without capital letters")
        print("!!mine - Mine for friend codes")
        print("!!uncapmine - Mines for friend codes without capital letters")
        print("!!help - Shows this message")
        print("!!clear - Clears the console")
        print("!!exit - Exits the program")
        print("!!creator - Me :D")
        print("!!version - Shows the version information")
        input("Press enter to exit")
        print("\n" * 100)
        run()
    elif q.lower() == "!!creator":
        print("\n" * 100)
        print("Created by NotDaBenjamin\n\nWebsite: https://notdabenjamin.neocities.org\nGitHub: https://github.com/NotDaBenjamin\nBluesky: https://bsky.app/profile/notdabenjamin.neocities.org\nAll Links: https://linktr.ee/NotDaBenjamin\n\nAll hobby projects, or projects I do in my free time away from work (Including this one :D) can be found here: https://github.com/SELTDSELT")
        input("Press enter to exit")
        print("\n" * 100)
        run()
    elif q.lower() == "!!version":
        print("\n" * 100)
        print("Version: 1.0")
        input("Press enter to exit")
        print("\n" * 100)
        run()
    else:
        print("\n" * 100)
        print("Unknown Command, type !!help for a list of commands")
        run()
    
run()