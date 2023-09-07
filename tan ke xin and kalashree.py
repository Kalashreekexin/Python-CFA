#!/usr/bin/env python

import random

def main():
 """Start a music guesssing game ."""
print("Guess the music!")

instruments = [
        "Guitar",
        "Drum",
        "Violin",
        "Triangle",
        "Gong",
        "Flute",
        "Piano",
        "Tabla" ]


x = random.choice(instruments)

score = 100
chances = 0
while(chances<=5):
    print(f'YOU HAVE {5-chances} CHANCES LEFT')
    guess_instruments = str(input('Guess the instruments:'))

    if(x == guess_instruments):
        print(f'Congratulation, You Got It. Score :{score-5*chances}')
        break
    elif(x > guess_instruments):
        print('Hint:Choose another Instruments')
    else:
        print('Hint : Try again')
        print("YOU MAY CHOOSE THE ANSWER FROM HERE",instruments) 
        chances = chances + 1

    if x == guess_instruments:
        print("You guessed{}.Congratulation you go it right!".format (guess_instruments))
    else:
        print("Oops!! You lost ,ran out of your chances.")

main()