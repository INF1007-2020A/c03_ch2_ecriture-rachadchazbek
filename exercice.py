
def my_fuction1(vect1,vect2):
    variable = 0
    for i in range(0,len(vect1)):
        variable += vect1[i] * vect2[i]
    if variable ==0:
        return "orthogonal"
    else:
        return "non orthogonal"


def my_function2(a):
    somme = 0
    m = 0
    for i in range(0,len(a)):
        if a[i] < 0:
            continue
        else:
            somme += a[i]
            m += 1
    resultat = somme/m
    return resultat



def my_fuction3(x):
    i100 = 0
    i20 = 0
    i10 = 0
    i5 = 0
    i1 = 0
    while (x>=100):
        x= x - 100
        i100 = i100 + 1
    while (x>=20):
        x = x -20
        i20 = i20 + 1
    while x >= 10:
        x = x - 10
        i10 = i10 + 1
    while x >= 5:
        x = x - 5
        i5 = i5 + 1
    while x >= 1:
        x = x-1
        i1 = i1+1
    return (f"biullets de 100: {i100}, billets de 20: {i20}, billets de 10: {i10}, billets de 5: {i5}, billets de 1: {i1} ")





