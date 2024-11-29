from unicodedata import digit

ur_name = input("Enter your name : ")

print("-"*50)
print(f"                    welcome , {ur_name}                  ")
print("-"*50)


TO_DO = {}




while True:
    print("-" * 50)
    print(f"                    TO-DO-LIST!                 ")
    print("-" * 50)
    print("Tasks              priority              Due-date")
    print()
    for key in TO_DO:
        print(f"{key} ", end="")
        for value in TO_DO[key]:
            print(F"              {value}" ,"    " , end="" )
        print()


    print()
    print("-" * 50)
    print(f"                    OPTIONS                  ")
    print("-" * 50)
    print("1- ADD \n2- REMOVE \n3- EDIT \n4- SAVE \n5- VIEW \n6- QUIT(q)")
    option = input("Enter your option :").lower()
    if option == "q":
        break
    while True:
        if option!= "add" and option != "remove" and option != "edit" and option != "save" and option != "view":
            print("Invalid Option")
            option = input("Enter your option :").lower()
        else:
            break
    if option == "add":
        num_task = int(input("Enter number of tasks you want to add:"))
        for i in range(num_task):
            name = input("Enter the Task Name : ").lower()
            while True:
                priority = input ("Enter the Task priority (High , Medium , Low): ").lower()
                if priority != "high" and priority != "medium" and priority != "low":
                    print("Invalid Priority")
                else:
                    break
            Due_Date = input ("Enter the Task Due-Date : ").lower()
            TO_DO[name] =  [priority , Due_Date]























