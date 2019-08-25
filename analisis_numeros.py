from collections import Counter
import sklearn
import numpy as np
from sklearn.datasets import load_digits

digits = load_digits()
nr_unos = 0

v_promedios = [0, 0, 0, 0, 0, 0, 0, 0]
v_s = [0, 0, 0, 0, 0, 0, 0, 0]
v_a = [np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([])]
v_stds = [0, 0, 0, 0, 0, 0, 0, 0]

h_promedios = [0, 0, 0, 0, 0, 0, 0, 0]
h_s = [0, 0, 0, 0, 0, 0, 0, 0]
h_a = [np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([]), np.array([])]
h_stds = [0, 0, 0, 0, 0, 0, 0, 0]

for i in range(len(digits.images)):
    if (digits.target[i] == 1):
        nr_unos += 1
        for x in range(8):
            # print("image nr: ", i)
            columna = digits.images[i].T[x]
            # print(digits.images[i].T[x])
            # print("suma columna: ", sum(columna))
            v_s[x] += sum(columna)
            v_a[x] = np.append(v_a[x], sum(columna))

for i in range(8):
    v_promedios[i] = v_s[i] / nr_unos
    # print("promedios[%d]: " %(i) , promedios[i])
    v_stds[i] = np.std(v_a[i])
    # print("stds[%d]: "%i, stds[i])
    # print()

for i in range(len(digits.images)):
    if (digits.target[i] == 1):
        nr_unos += 1
        for x in range(8):
            # print("image nr: ", i)
            fila = digits.images[i][x]
            # print(digits.images[i].T[x])
            # print("suma columna: ", sum(columna))
            h_s[x] += sum(fila)
            h_a[x] = np.append(h_a[x], sum(fila))

for i in range(8):
    h_promedios[i] = h_s[i] / nr_unos
    # print("promedios[%d]: " %(i) , promedios[i])
    h_stds[i] = np.std(h_a[i])
    # print("stds[%d]: "%i, stds[i])
    # print()

VP = 0
VN = 0
FP = 0
FN = 0
v_bitmaps = []
h_bitmaps = []

identificado = 0
for i in range(len(digits.images)):

    image = digits.images[i]
    v_sumas = [0, 0, 0, 0, 0, 0, 0, 0]
    h_sumas = [0, 0, 0, 0, 0, 0, 0, 0]
    v_bitmap = [0, 0, 0, 0, 0, 0, 0, 0]
    h_bitmap = [0, 0, 0, 0, 0, 0, 0, 0]

    for x in range(8):
        v_sumas[x] = sum(image.T[x])
    for x in range(8):
        h_sumas[x] = sum(image[x])
    if ((abs(v_sumas[0] - v_promedios[0]) < v_stds[0]
         and abs(v_sumas[1] - v_promedios[1]) < v_stds[1]
         and abs(v_sumas[2] - v_promedios[2]) < v_stds[2]
         and abs(v_sumas[3] - v_promedios[3]) < v_stds[3]
         and abs(v_sumas[4] - v_promedios[4]) < v_stds[4]
         and abs(v_sumas[5] - v_promedios[5]) < v_stds[5]
         and abs(v_sumas[6] - v_promedios[6]) < v_stds[6]
         and abs(v_sumas[7] - v_promedios[7]) < v_stds[7])
            or
            (abs(v_sumas[0] - v_promedios[0]) < v_stds[0]
             and abs(v_sumas[1] - v_promedios[1]) < v_stds[1]
             and abs(v_sumas[3] - v_promedios[3]) < v_stds[3]
             and abs(v_sumas[4] - v_promedios[4]) < v_stds[4]
             and abs(v_sumas[5] - v_promedios[5]) < v_stds[5]
             and abs(v_sumas[6] - v_promedios[6]) < v_stds[6]
             and abs(v_sumas[7] - v_promedios[7]) < v_stds[7])
            or
            (abs(v_sumas[0] - v_promedios[0]) < v_stds[0]
             and abs(v_sumas[1] - v_promedios[1]) < v_stds[1]
             and abs(v_sumas[2] - v_promedios[2]) < v_stds[2]
             and abs(v_sumas[4] - v_promedios[4]) < v_stds[4]
             and abs(v_sumas[6] - v_promedios[6]) < v_stds[6]
             and abs(v_sumas[7] - v_promedios[7]) < v_stds[7])
            or
            (abs(v_sumas[0] - v_promedios[0]) < v_stds[0]
             and abs(v_sumas[1] - v_promedios[1]) < v_stds[1]
             and abs(v_sumas[3] - v_promedios[3]) < v_stds[3]
             and abs(v_sumas[4] - v_promedios[4]) < v_stds[4]
             and abs(v_sumas[6] - v_promedios[6]) < v_stds[6]
             and abs(v_sumas[7] - v_promedios[7]) < v_stds[7])
             #or
             #(abs(v_sumas[0] - v_promedios[0]) < v_stds[0]
             #and abs(v_sumas[1] - v_promedios[1]) < v_stds[1]
             #and abs(v_sumas[2] - v_promedios[2]) < v_stds[2]
             #and abs(v_sumas[3] - v_promedios[3]) < v_stds[3]
             #and abs(v_sumas[5] - v_promedios[5]) < v_stds[5])
            #or
             #abs(h_sumas[7] - h_promedios[7]) < h_stds[7]

    ):
        if (digits.target[i] == 1):
            VP += 1
        else:
            FP += 1
    elif (digits.target[i] == 1):
        for x in range(8):
            if (abs((v_sumas[x] - v_promedios[x])) < v_stds[x]):
                v_bitmap[x] = 1
        # print(bitmap)
        v_bitmaps.append(v_bitmap)
        for x in range(8):
            if (abs((h_sumas[x] - h_promedios[x])) < h_stds[x]):
                h_bitmap[x] = 1
        # print(bitmap)
        h_bitmaps.append(h_bitmap)
        # pl.gray() # Queremos las imágenes en grises
        # pl.matshow(digits.images[i]) # Imprimir una imagen dada
        FN += 1
    else:
        VN += 1

# print(bitmaps)

print(Counter(map(tuple,v_bitmaps)))
print(Counter(map(tuple,h_bitmaps)))


print("nr unos: ", nr_unos, " VP: ", VP, " FP: ", FP, "FN: ", FN, " VN: ", VN)
print()
print("Accuracy: ", 100 * (VP + VN) / (VP + VN + FP + FN))
print("Precision: ", 100 * (VP / (VP + FP)))
print("Recall: ", 100 * (VP / (VP + FN)))
print("Especificidad: ", 100 * (VN / (VN + FP)))