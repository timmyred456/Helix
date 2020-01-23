import random, os, time, sys

def clear():
  os.system("clear")

clear()

mainFile = open("main.hx","r")

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

textBuffer = []


showCurrent = False


while not cline >= len(line):
  splitLine = line[cline].split()
  if splitLine == []:
    splitLine = ['null']  


  if showCurrent == True:
    print(str(splitLine))

  time.sleep(0.001)
  #print(splitLine)
  if splitLine[0] == "1" and passIf == False: # adding variables
      vars[splitLine[1]] = smartInt(splitLine[2])

  if splitLine[0] == "2" and passIf == False: # printing vars
      try:
        if splitLine[2] == "1":
          sys.stdout.write(str(smartInt(splitLine[1])))
        elif splitLine[2] == "2":
          print(chr(smartInt(splitLine[1])))
        elif splitLine[2] == "3":
          sys.stdout.write(str(chr(smartInt(splitLine[1]))))
        elif splitLine[2] == "4":
          pass
      except:
        print(smartInt(splitLine[1]))
        

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
      cline = smartInt(splitLine[1])
      
  if splitLine[0] == "5" and passIf == False:
    if splitLine[2] == '==':
      if smartInt(splitLine[1]) == smartInt(splitLine[3]):
        passIf = False 
      else:
        passIf = True
      
    if splitLine[2] == "!=":
      if smartInt(splitLine[1]) != smartInt(splitLine[3]):
        passIf = False
      else:
        passIf = True

  if passIf == True and not splitLine[0] == ".":
    pass
  elif passIf == True and splitLine[0] == ".":
    passIf = False

  cline = cline + 1
 