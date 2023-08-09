students = {
    "male": ["Tom", "Charlie" , "Harry" , "Frank"],
    "female":["Sarah" , "Huda" , "Samantha" , "Emily" , "Elizabeth"]
    }

for key in students.keys():
    for item in students[key]:
        if "a" in item:
            print(item)
