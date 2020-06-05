with open('dataset_3363_2.txt') as inf:
    cod = str(inf.readline()) #чтение из файла
    dnk = ('')
    n = cod[0]
    z = ('')
    for i in range(len(cod)):
        if not cod[i].isdigit(): #проверка на букву
            n = cod[i]
        elif i + 1 < len(cod) and not cod[i+1].isdigit(): #проверка на конец строки и проверка следующего символа - не должна быть цифра = конец цикла
            z += cod[i]
            z = int(z)
            dnk = dnk + n * z #запись промежуточного результата в переменную
            z = ('') #обнуление переменной
        else:
            z += cod[i] #символ: не буква, нет конца строки, следующий сивол - цифра, значит продолжаем цикл
with open('output.txt', 'w') as ouf: #запись в файл
    ouf.write(dnk)
