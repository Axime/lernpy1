iter = 20
import random
import time

for i in range(iter):
    print(f"Iteration:{i}")
    for l in range(iter):
        print(f"{random.randint(0, l)} ", end="")
    print("")