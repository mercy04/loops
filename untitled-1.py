age=int(input("enter your age=>"))

if age < 3:
    print("toddler")             # 30 < 3 = false
    
elif age > 20 and age < 30:      # 30 > 20 =  true and 30 = false ----- true and false --- false
    print("your in your 20's")
                                 # 30 >= 30 = true and 30 < 40 = true ----- false and true --- false
elif age >= 30 and age < 40:
    print("your in your 30's")
    
