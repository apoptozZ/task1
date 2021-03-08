#Задача 1: Вам подаются на вход два вектора a и b в трехмерном пространстве.
          #Реализуйте их скалярное произведение без помощи numpy.

def no_numpy_scalar(a, b):
    result = 0
    for i, j in zip(a, b):
        result += (i * j)
    return result

