import random
print("WElcome to Guessing game")
flag=1

while flag:

    flag=int(input("enter 1 to play the game 0 to exit: "))
    if flag==1:
        print("Enter the Range:")
        lower_range=int(input("Enter the lower range: "))
        upper_range=int(input("Enter the upper range: "))
        Guess_counter=0
        if(lower_range<upper_range):
            random_number=random.randint(lower_range,upper_range)
          

            print("Lets start the guessing game")
            guess=0
            while guess<3:


                n=int(input("Enter your Number: "))

                if n>upper_range:
                    print("Out of Range")

                elif n<lower_range:
                    print("Out of range")
                    

                elif n>random_number:
                    print("Try again! Too High ")
                    
                    guess=guess+1
                    Guess_counter=Guess_counter+1
                    

                elif n<random_number:
                    print("Try again! Too Low")
                    guess=guess+1
                    Guess_counter=Guess_counter+1
                

                elif n==random_number:
                    Guess_counter=Guess_counter+1
                    print(f'Congrats You Guess the right Number  with {Guess_counter} guesses')

            

                    break
        else:
            print("Invalid Range")

    elif flag==0:
        print("Bye Bye")

    else:
        print("invalid input ")

        
                