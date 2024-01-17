import random
print("Welcome to Dice GAme")
dice_outcome_list=[]
max_roll=0
sum=0
while max_roll<5:
    number=int(input("Enter 1 to Roll the Dice and 0 to exit:"))


    if number==1:
        print("ROLLING THE DICE")
        dice_value=random.randint(1,6)
        print(f'The Outcome is {dice_value}')
        sum+=dice_value
        dice_outcome_list.append(dice_value)
        max_roll+=1

    elif number==0:
        break
    else:
        print("Invalid Input")


print(f'The Total Value of all Outcome is {sum}')