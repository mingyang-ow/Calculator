
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

global endofcal
endofcal = False

operation = {
"+" : add,
 "-" : sub,
 "*" : mul,
 "/" : div,   
}

num1 = int(input("Please enter your first number "))
num2 = int(input("Please enter your second number "))
for opt in operation:
        print(opt)
    
opt_symbol = input("Please key in the operation you will like to use ")
answer = operation[opt_symbol](n1 = num1, n2= num2)
print(f"{num1} {opt_symbol} {num2} = {answer}")
cont = input("Would like you to continue operating on the answer or stop the calculation ").lower()

def subcal(n3,n4):
    
    for opt in operation:
        print(opt)
    
    nopt_symbol = input("Please key in the operation you will like to use ")

    new_answer = operation[nopt_symbol](n1 = answer,n2 = num3)
    
    print(f"{answer} {nopt_symbol} {num3} = {new_answer} ")
    
if cont == "no":
    endofcal
    endofcal = True
while not endofcal:
    num3 = int(input("Please enter your next number "))
    subcal(num3,answer) 
    new_answer = answer
    cont = input("Would like you to continue operating on the answer or stop the calculation. Yes or No").lower()
    if cont == "no":
        endofcal
        endofcal = True
    