from random import *
from time import sleep as wait


def RandomDictItem(Dict):
    RDI = list(Dict)[randint(0,len(list(Dict))-1)]
    return RDI,Dict[RDI]

Quotes = {"A Christmas Carol" : {
    "Scrooge's introduction" : [
        '"a squeezing, wrenching, grasping, scraping, clutching, covetous old sinner"',
        '"he was a tight-fisted hand at the grindstone"',
        '"solitary as an oyster"'
        ]
    }
}

LitName,LitCont = RandomDictItem(Quotes)

ThemeChar,ThemeCharAns = RandomDictItem(LitCont)

print("In " + LitName + ", give three quotes about " + ThemeChar + ".")

for i in range(0,3):
    input()

print("Alright. Here are some examples which you could've used:")

for i in ThemeCharAns:
    wait(0.5)
    print(i)
