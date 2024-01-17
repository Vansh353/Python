print("Welcome To BMI Calculator")
print("This BMI Calculator is for Both the System(Kg and cm) or (Pound and feet)")
name=input("Enter Your Name: ")
temp=1

while temp:
    
    Weight_system=int(input("\n 0) Imperial System(Pounds and Inches) \n 1) Metric Unit(Kg and Cm) \n Enter Your Weight System : "))
    flag=1
    if Weight_system==1:

        while flag:
            try :
                weight=float(input("Enter your Weight(Kgs): "))
                height=float(input("Enter your height(Cm): "))
                flag=0
            
            except ValueError:
                print("You are entering another input rather than numbers")  

        height=height/100
        bmi= (weight)/(height*height)
        
        if bmi<18.5:
            print(f"{name}, your report is Underweight. BMI: %.2f" % bmi)
            break 
       

        elif bmi>=18.5 and bmi<25:
            print(f"{name} your report is Normal BMI: %.2f" % bmi )
            break 

        elif bmi>=25 and bmi<30:
            print(f"{name} your report is Overweight BMI: %.2f" % bmi)
            break 

        elif bmi>=30:
            print(f"{name} your report is Obesity BMI: %.2f" % bmi)
            break 


        else:
            print("Invalid")
            break 

    elif Weight_system==0:

        while flag:
            try:
                
                weight=float(input("Enter your Weight(Pound): "))
                height=float(input("Enter your height(Feets): "))
                height_1=float(input("Enter your height(Inches): "))
                flag=0

            except:
                print("You are entering another input rather than numbers")
        height=height*30.48
        height_1=height_1*2.54
        height=height+height_1
        weight=weight*0.454
        height=height/100
        bmi= (weight)/(height*height)
        
        if bmi<18.5:
            print(f"{name}, your report is Underweight. BMI: %.2f" % bmi)
            break 
        elif bmi>=18.5 and bmi<25:
            print(f"{name} your report is Normal BMI: %.2f" % bmi )
            break 

        elif bmi>=25 and bmi<30:
            print(f"{name} your report is Overweight BMI: %.2f" % bmi)
            break 

        elif bmi>=30:
            print(f"{name} your report is Obesity BMI: %.2f" % bmi)
            break 


        else:
            print("Invalid")
            break 
    


    else:
        print(" Invalid Input!! Enter Correct Input either 1 or 0)")
        temp=1