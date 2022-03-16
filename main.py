import os, random
from datetime import date

def getwordletoday():
  t = str(date.today())
  t = t.replace('-',' ').split()
  start = date(2022,2,22)
  today = date(int(t[0]),int(t[1]),int(t[2]))
  delt = today-start
  startw = 'thorn'  
  file = open('words.txt','r').read().split()
  num = file.index(startw)

  return file[num+delt.days]

words = open('words.txt','r').read().split()
#secretword = random.choice(words)
secretword = getwordletoday() #for testing correct wordle of the day
firstguess = 'audio'
turn = 0
guess = ''

correct_position = ['_','_','_','_','_']
correct_letter = []
incorrect_letter = []
already_guessed = []

guessed = [
  [],
  [],
  [],
  [],
  [],
  []
]

def getBoard():
  os.system('clear')
  for i in guessed:
    print(*i) if ''.join(i) != '' else print('\033[1;37;40m_ '*5)

def bestBotGuess(original, turn):
  scoretracker = {}
  if original == '': # checks for firstguess
    return firstguess
  # checks if not guess = firstguess
  if correct_position == ['_','_','_','_','_']: # checks if there is correct letter pos
    for i in words:
      current_word_score = 0
      if i in already_guessed:
        current_word_score = 0
      else: 
        if len(set(i)) == len(i):
          current_word_score += 20
        else:
          current_word_score -= 30
        for j in i:
          if j in correct_letter:
            current_word_score += 20
          if j in incorrect_letter:
            current_word_score = 0
      scoretracker[i] = current_word_score
    values = scoretracker.values()
    index = list(scoretracker.values()).index(max(values)) # gets index
    return list(scoretracker.keys())[index] # returns best guess
  else:
    for i in words:
      current_word_score = 0
      if i in already_guessed: #checks if word is already guessed
        current_word_score = 0
      else:
        if len(set(i)) == len(i):
          current_word_score += 20
        else:
          current_word_score -= 30
        for j in range(len(i)):
          if i[j] == correct_position[j]:
            current_word_score += 40
          elif i[j] in correct_letter:
            if i[j] == original[j]: # checks if correct word but not lettering is not used again in next guess
              current_word_score -= 20
            if i[j] in correct_position: # checks if letter already in correct position
              current_word_score -= 10
            else:
              current_word_score += 20
          elif i[j] in incorrect_letter:
            current_word_score = 0
      scoretracker[i] = current_word_score
    values = scoretracker.values()
    index = list(scoretracker.values()).index(max(values)) #gets index
    return list(scoretracker.keys())[index] #returns best guess

while True:
  getBoard()
  if turn == 6:
    print('\033[1;37;40mThe secret word was',secretword)
    break
  input()
  guess = bestBotGuess(guess, turn)
  if guess == secretword:
    for i in range(len(guess)): guessed[turn].append('\033[1;30;42m'+guess[i])
    getBoard()
    print('\033[1;37;40mYou Win!')
    break
  if guess in words:
    for i in range(len(guess)):
      if guess[i] == secretword[i]: 
        guessed[turn].append('\033[1;30;42m'+guess[i])
        correct_position[i] = guess[i]
      elif guess[i] in secretword: 
        guessed[turn].append('\033[1;30;43m'+guess[i])
        if not(guess[i] in correct_letter):
          correct_letter.append(guess[i])
      else:
        guessed[turn].append('\033[1;37;40m'+guess[i])
        incorrect_letter.append(guess[i])
    already_guessed.append(guess)
    turn += 1
