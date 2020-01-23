import random, os, time

def clear():
  os.system("clear")

clear()

mainFile = open("main.he","r")

line = mainFile.readlines()
cline = 0

vars = {}

passIf = False
bruh = False

def checkInt(lineC):
  if '1,' in lineC:
    return True
  else:
    return False

def smartInt(lineC):
  if '1,' in lineC:
    return int(vars.get(lineC.replace("1,",""),1))
  else:
    return int(lineC)

while not cline >= len(line) - 1:
  splitLine = line[cline].split()
  if splitLine == []:
    splitLine = ['null']  

  time.sleep(0.1)
  #print(splitLine)
  if splitLine[0] == "1" and passIf == False: # adding variables

      vars[splitLine[1]] = int(splitLine[2])

  if splitLine[0] == "2" and passIf == False: # printing vars

        print(vars.get(splitLine[1], ""))

  if splitLine[0] == "3" and passIf == False:
    if splitLine[3] == "+": 
      vars[splitLine[1]] = smartInt(splitLine[2]) + smartInt(splitLine[4])
    if splitLine[3] == "-":
      vars[splitLine[1]] = smartInt(splitLine[2]) - smartInt(splitLine[4])
    if splitLine[3] == "/":
      vars[splitLine[1]] = smartInt(splitLine[2]) / smartInt(splitLine[4])
    if splitLine[3] == "*":
      vars[splitLine[1]] = smartInt(splitLine[2]) * smartInt(splitLine[4])

  if splitLine[0] == "4" and passIf == False:
      cline = smartInt(splitLine[1]) - 1
      
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
 