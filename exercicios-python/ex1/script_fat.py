#Função fatorial com recursividade.
""" def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*fatorial(n-1) 
        
"""
#Função fatorial não recursiva.
"""def fatorial(n):
    fat = 1
    if n == 0 or n == 1:
        return fat
    else:
        for x in range(2, n + 1):
               fat = fat*x
        return fat
"""