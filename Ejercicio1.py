def torre_hanoi(a_1,a_2,a_3,n):
    if n>0:
        torre_hanoi(a_1,a_2,a_3,n-1)
        print("Mover disco de la", a_1, "a la", a_2)
        torre_hanoi(a_3,a_2,a_1,n-1)

torre_hanoi("primera aguja", "segunda aguja", "tercera aguja", 74)