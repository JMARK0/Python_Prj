#This project aims build a Guess the number game between computer, whichever player wins picks randon number within 
#..mentioned limit other player as to GuessIt ,accordingly Point table will updated 
import random as rd

def Guess(num) :
    random_number =rd.randint(1,num) #random that should be guessed
    print(random_number)
    guess_num =0
    while guess_num !=random_number:
        if(guess_num > random_number):
            print(f"{guess_num} is greater ,Try again")
            guess_num =Guessor('H',guess_num,num)
        elif(guess_num < random_number):
            print(f"{guess_num} is Lower ,Try again")
            guess_num =Guessor('L', guess_num,num)
    print (f'Yay!! You won the game by guessing the correct number {random_number}')

    
def  Guessor (feedback,guess_num,limit):
    if(feedback =='H'):
        return rd.randint(1,guess_num-1)
    elif(feedback == 'L'):
        return rd.randint(guess_num+1,limit)


Guess(int(input('Referee !! Please Enter the limit number : ')))