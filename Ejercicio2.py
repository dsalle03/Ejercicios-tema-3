def determinante(matriz):
    suma = (matriz[0][0]*matriz[1][1]*matriz[2][2])+(matriz[1][0]*matriz[2][1]*matriz[0][2])+(matriz[2][0]*matriz[0][1]*matriz[1][2])
    resta = (-matriz[0][2]*matriz[1][1]*matriz[2][0])-(matriz[1][2]*matriz[2][1]*matriz[0][0])-(matriz[2][2]*matriz[0][1]*matriz[1][0])
    return suma + resta

print("El determinante de la matriz 3x3 es", determinante([[9,2,7],[4,5,1],[2,6,4]]))


