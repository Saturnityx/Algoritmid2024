#võtame hetkel kindlad raamatud mis meil on
raamatud = [31, 25, 10, 5, 20, 30, 15, 40, 45, 100, 1, 12]
def bubble_sort(raamatud):

    #Kasutan bubble sorti, et raamatud oleksid väiksemast suuremani
    for n in range(len(raamatud) - 1, 0, -1):

        for i in range(n):
            if raamatud[i] > raamatud[i + 1]:

                swapped = True
                raamatud[i], raamatud[i + 1] = raamatud[i + 1], raamatud[i]
#Sorteerime listi, enne raamatu pikkuste vaatlust
bubble_sort(raamatud)

#Eemaldame raamatud, mis on üle 30cm pikkad
for x in raamatud:
    if 31 in raamatud:
        raamatud.pop(-1)
    
#Kui pikkad raamatud meil riiulisse lähevad
print("Raamatu riiulisse lähevad raamatud pikkusega:")
print(raamatud)
