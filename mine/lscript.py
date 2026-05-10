import random
import time


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
chance = 0



print("Created by NotDaBenjamin")
print("© 2026 Super Evil Laboratory That Does Super Evil Laboratory Things")
print("Use !!help for a list of commands")
print("Check out my other stupid bullshit projects at https://github.com/SELTDSELT\n\n")

def mine():
    result = (
    random.choice(chars) +
    random.choice(chars) +
    random.choice(chars) + "-" +
    random.choice(chars) +
    random.choice(chars) +
    random.choice(chars)
)
    global chance
    chance = chance + 1
    print(f"{chance}$ {result}")
    time.sleep(0.5)
    mine()
mine()