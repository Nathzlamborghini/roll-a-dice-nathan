import random
import string
from tkinter import N, Y
yesorno = input(str("Do you want to roll the dice? Yes=y, and No=n"))

while yesorno == "y":
    no = random.randint(1,6)
    if no == 1:
        print("[-----]")
        print("[     ]")
        print("[  0  ]")
        print("[     ]")
        print("[-----]")
    elif no == 2:
        print("[-----]")
        print("[    0]")
        print("[     ]")
        print("[0    ]")
        print("[-----]")
    elif no == 3:
        print("[-----]")
        print("[    0]")
        print("[  0  ]")
        print("[0    ]")
        print("[-----]")
    elif no == 4:
        print("[-----]")
        print("[0   0]")
        print("[     ]")
        print("[0   0]")
        print("[-----]")
    elif no == 5:
        print("[-----]")
        print("[0   0]")
        print("[  0  ]")
        print("[0   0]")
        print("[-----]")
    elif no == 6:
        print("[-----]")
        print("[0   0]")
        print("[0   0]")
        print("[0   0]")
        print("[-----]")
    doucontinue = input(str("Do you want to continue? Yes=y, and No=n"))
    if doucontinue == "n":
        exit()

    