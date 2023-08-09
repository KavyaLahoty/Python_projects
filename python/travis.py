known_users = ["Alice" , "Bob" , "Claire" , "Dan" , "Emma" , "Fred" , "Georgie" , "Harry"]

while True:
    print("Hi! I'm Travis")
    name = input("What is your name?:").strip().capitalize()

    if name in known_users:
       print("Hello{}!.".format(name))
       remove = input("Would you like to be removed from the system?(y/n):").lower()
       if remove == "y":
           
           known_users.remove(name)
           

        
    else:
        
        print("Hmmmm I don't think we've met {}".format(name))
        add_me = input("Would you like to be added to the system(y/n):").strip().lower()
        if add_me == "y":
             known_users.append(name)
        elif add_me == "n":
            print("Alright, see you later alligator!!")
               
