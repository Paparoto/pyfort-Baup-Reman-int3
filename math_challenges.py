import random
import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)

def math_challenge_factorial():
    n = random.randint(1,10)
    answer=int(input("Math Challenge: Calculate the factorial of " + str(n) + ".\nYour answer: "))
    if answer==factorial(n):
        print("Correct! You win a key.")
        time.sleep(0.5)
        return True
    else:
        print("Wrong")
        time.sleep(0.5)
        return False



def  solve_linear_equation():
    a = random.randint(1,10)
    b = random.randint(1,10)
    x = -b/a
    return {'a': a,'b': b,'x': x}


def math_challenge_equation():
    sol = solve_linear_equation()
    answer = int(input(("Math Challenge: Solve the equation " + str(sol["a"]) +"x + " + str(sol["b"]) + " = 0.\nWhat is the value of x: ")))
    if answer == sol["x"]:
        print("Correct! You win a key.")
        time.sleep(0.5)
        return True
    else:
        print("Wrong")
        time.sleep(0.5)
        return False



def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

def nearest_prime(n):
    while True:
        if is_prime(n):
            return n
        n=n+1

def math_challenge_prime():
    n= random.randint(10,20)
    answer = int(input("Math Challenge: Find the nearest greatest prime (including this exact number) to "+ str(n) + ".\nYour answer: "))
    time.sleep(1)
    if answer==nearest_prime(n):
        print("Correct! You win a key.")
        time.sleep(0.5)
        return True
    else:
        print("Wrong")
        time.sleep(0.5)
        return False



def math_roulette_challenge():
   roul=[]
   sol = 0
   for i in range(1,6):
       roul.append(random.randint(1,20))
   f = random.randint(1,3)
   for elem in roul:
        if f == 1:
            sol += elem
            x = 'addition'
        elif f == 2:
            if sol>0:
                sol*=elem
            else:
                sol=elem
            x = 'multiplication'
        elif f == 3:
            sol -= elem
            x = 'subtraction'
   print("Numbers on the roulette:",roul)
   print("Calculate the result by combining these numbers with",x)
   answer=0
   try :
       answer = int(input("Your answer: "))
   except:
       print("We interpretated your answer as 0")
   time.sleep(1.5)
   if answer == sol:
       print("Correct! You win a key.")
       time.sleep(0.5)
       return True
   else:
       print("Wrong")
       time.sleep(0.5)
       return False

def math_challenge():
    challenge=random.randint(1,4)
    if challenge==1:
        if math_challenge_factorial():
            return True
    elif challenge==2:
        if math_challenge_equation():
            return True
    elif challenge==3:
        if math_challenge_prime():
            return True
    elif challenge==4:
        if math_roulette_challenge():
            return True
    return False
