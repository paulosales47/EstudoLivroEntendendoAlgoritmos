import time

def fatorial(valor):
    if(valor == 1):
        return 1
    else:
        return valor * fatorial(valor - 1);


def fatorial_tail(valor, total = 1):
    if(valor == 0):
        return total
    else:
        return fatorial_tail(valor - 1, valor * total)


print(fatorial(995))
print(fatorial_tail(995))


