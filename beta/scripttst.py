import random
import time


chars = "abcdefghijklmnopqrstuvwxyz0123456789"


result = "".join(random.choice(chars) for _ in range(3))
result += "-"
result += "".join(random.choice(chars) for _ in range(3))




print("Created by NotDaBenjamin")
print("© 2026 Super Evil Laboratory That Does Super Evil Laboratory Things")
print("Use !!help for a list of commands")
print("Check out my other stupid bullshit projects at https://github.com/SELTDSELT\n\n")

def mine():
    print(result.upper())
    time.sleep(0.5)
    mine()
mine()