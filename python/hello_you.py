#ask user for name

name = input(" What is your name? ")



#ask user for age

age = input("What is your age? ")


# ask user for city
city = input("Which city do you live in? ")


#ask user for hobby

hobby = input("What do you love doing? ")


 # create output text




string = "Your name is {} and you are {} years old. You live in {} and you love {}"
output = string.format(name,age,city,hobby)



#print output to screen

print(output)
