def get_age_and_name():
    name=input("what is your name: ")
    year=int(input("what is your birth year: "))
    age = 2019 - year
    get_output(age, year, name)

def get_output(age, year, name):
    print("Your name is " + name + "and I think your age is ")
    print(age)
    
        

get_age_and_name()
