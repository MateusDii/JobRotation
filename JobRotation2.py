#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fibonacci(num):
    """
    Função que calcula a sequência de Fibonacci até o número informado e retorna uma lista com os valores.
    """
    fib_seq = [0, 1]
    while fib_seq[-1] < num:
        next_num = fib_seq[-1] + fib_seq[-2]
        fib_seq.append(next_num)
    return fib_seq

def verifica_fibonacci(num):
    """
    Função que verifica se um número pertence à sequência de Fibonacci.
    """
    fib_seq = fibonacci(num)
    if num in fib_seq:
        return f"{num} pertence à sequência de Fibonacci!"
    else:
        return f"{num} não pertence à sequência de Fibonacci."


numero = int(input("Digite um número: "))
print(verifica_fibonacci(numero))


# In[ ]:




