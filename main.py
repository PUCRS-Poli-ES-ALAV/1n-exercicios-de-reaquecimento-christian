def mult(num1, num2):
    if(num1==0):
        return 0
    else:
        return num2+(mult((num1-1), num2))
    

def sum(num1, num2):
    if(num1 == 0 and num2 == 0):
        return 0
    elif(num1 == 0):
        return 1+(sum(num1, num2-1))
    else:
        return 1+(sum(num1-1, num2))
    

def frac(num):
    if(num == 0):
        return 0
    else:
        return 1/num + frac(num-1)
    

def invert(string):
    if(string == ""):
        return ""
    else:
        return string[-1] + invert(string[:-1])

def F(num):
    if(num == 1):
        return 1
    elif(num == 2):
        return 2
    else:
        return 2 * F(num-1) + 3 * F(num-2)
    
def A(m, n):
    if(m == 0):
        return n+1
    elif(n == 0):
        return A(m-1, 1)
    else:
        return A(m-1, A(m, n-1))
    
    
def multVet(vet):
    if(len(vet) == 0):
        return 1
    else:
        return vet[-1] * multVet(vet[:-1])

def sumVet(vet):
    if(len(vet) == 0):
        return 0
    else:
        return vet[-1] + sumVet(vet[:-1])
    

def palindromeCheck(string):
    if(string == ""):
        return True
    elif(string[0] == string[-1]):
        return palindromeCheck(string[1:-1])
    elif(len(string) == 1):
        return True
    else:
        return False
    


print("A seguir multiplicacao de 4 e 7")
print(mult(4,7))

print("A seguir a soma de 5 e 9")
print(sum(5,9))

print("A seguir somatorio de fracao ate 1/9")
print(frac(9))

print("Inversao da string batata")
print(invert("batata"))

print("Funcao F para 7")
print(F(3))

print("Funcao Ackerman para 5 e 6")
print(A(3,4))

print("Multiplicacao do vetor [2,5,4,3,8,8]")
print(multVet([2,5,4,3,8,8]))

print("Soma do vetor [6,4,3,9,8]")
print(sumVet([6,4,3,9,8]))

print("Verifica de arara eh palindrome")
print(palindromeCheck("arara"))

print("Verifica de abacate eh palindrome")
print(palindromeCheck("abacate"))
