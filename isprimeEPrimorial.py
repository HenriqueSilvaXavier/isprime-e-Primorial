def isprime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True
    
    
print("O primorial (n#) é produto de todos numeros primos antecessores ou iguais a n")
n=1     
list=[]
p=1
número= int(input("Digite um número: "))
for n in range(0, número+1):
      if isprime(n)==True:
       p=p*n
print("O primorial de {} é {}.".format(n, p))