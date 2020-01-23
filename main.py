import random, os, time

def clear():
  os.system("clear")

clear()

mainFile = open("main.he","r")

line = mainFile.readlines()
cline = -1

vars = {}

passIf = False
bruh = False

while not cline >= len(line) - 1:
  splitLine = line[cline].split()
  if splitLine == []:
    splitLine = ['null']  

  time.sleep(0.05)
  #print(splitLine)
  if splitLine[0] == "1" and passIf == False: # adding variables

      vars[splitLine[1]] = int(splitLine[2])

  if splitLine[0] == "2" and passIf == False: # printing vars

        print(vars.get(splitLine[1], ""))

  if splitLine[0] == "3" and passIf == False:
    if splitLine[4] == "+": 
      vars[splitLine[1]] = int(vars.get(splitLine[2],0)) + int(splitLine[3])
    if splitLine[4] == "-":
      vars[splitLine[1]] = int(vars.get(splitLine[2],0)) - int(splitLine[3])
    if splitLine[4] == "/":
      vars[splitLine[1]] = int(vars.get(splitLine[2],0)) / int(splitLine[3])
    if splitLine[4] == "*":
      vars[splitLine[1]] = int(vars.get(splitLine[2],0)) * int(splitLine[3])

  if splitLine[0] == "4" and passIf == False:
      cline = int(splitLine[1]) - 1
      if passIf == True:
        passIf = False

  if splitLine[0] == "5" and passIf == False:
    if splitLine[2] == '==':
      if vars.get(splitLine[1]) == int(splitLine[3]):
        passIf = False 
      else:
        passIf = True
      
    if splitLine[2] == "!=":
      if vars[splitLine[1]] != int(splitLine[3]):
        passIf = False
      else:
        passIf = True

  if passIf == True and not splitLine[0] == ".":
    pass
  elif passIf == True and splitLine[0] == ".":
    passIf = False

  cline = cline + 1
 