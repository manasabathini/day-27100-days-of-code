import random,os, time

def rollTheDice(side):
  result = random.randint(1,side)
  return result

def health():
  healthStat = (rollTheDice(6) * rollTheDice(12)/2) +10
  return healthStat

def stregth():
  strengthStat = ((rollTheDice(6)+rollTheDice(8))/2)+12
  return strengthStat 

while True:
  print("Character Builder")
  print()
  name = input("Name your legend: \n ")
  type = input("Character Type [Human, Elf, wizard, Orca] :\n ")
  print()
  print(name)
  print("Health: ", + health())
  print("stregth: ", stregth())
  print()
  print("May your name go down in Legend…")
  print()
  again = input("Again?:\n")
  if again == "No" or again == "no":
    break
  time.sleep(1)
  os.system("clear")
