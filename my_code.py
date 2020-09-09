# Complete the function below calculate your age after different numbers of years.

def age_now(x):
    # My age now
    print(f"I am currently {x} years old.\n")

def age_1(y):
    # My age next year
    print(f"Next year I'll be {y+1} years old.\n")

def age_10(z):
    # My age in 10 years
    print(f"In 10 years, I'll be {z+10}!\n")

def age_50(q):
    # My age in 50 years!
    print(f"In 50 years, I'll be {q+50}! Wow!\n")




if __name__ == '__main__':

    age = (int(input("how old are you?")))   # change this number to your current age

 

    age_now(age)   # run function age_now with argument age
    age_1(age)    # run function age_1 with argument age
    age_10(age)    # run function age_10 with argument age
    age_50(age)    # run function age_50 with argument age
