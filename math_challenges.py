import random
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
        return True
    else:
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
        return True
    else:
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
    answer = int(input("Math Challenge: Find the nearest prime to "+ str(n) + ".\nYour answer: "))
    if answer==nearest_prime(n):
        print("Correct! You win a key.")
        return True
    else:
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
   answer = int(input("Your answer: "))
   if answer == sol:
       print("Correct answer! You've won a key.")
       return True

   else:
       return False

def math_challenge():
    keys=0
    challenge=random.randint(1,4)
    if challenge==1:
        if math_challenge_factorial():
            keys +=1
    elif challenge==2:
        if math_challenge_equation():
            keys += 1
    elif challenge==3:
        if math_challenge_prime():
            keys += 1
    elif challenge==4:
        if math_roulette_challenge():
            keys += 1
