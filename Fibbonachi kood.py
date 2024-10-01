# on vaja lisada kaks tagavara arvu, sest muidu tekib error
tagavara = {0: 0, 1: 1}


def fibonacci(n):
    if n not in tagavara:
        tagavara[n] = fibonacci(n-1) + fibonacci(n-2)
    return tagavara[n]

nr = int(input("Sisestage arv: "))
vastus = fibonacci(nr)
print(f"Fibbonaci väärtus numbriga {nr} on {vastus}")