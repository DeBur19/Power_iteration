import random

outFile = open('Матрицы1000.txt', 'w', encoding='utf8')
for i in range(100):
    print(100, file=outFile)
    for j in range(100):
        for k in range(100):
            print(random.uniform(0, 100), file=outFile, end=' ')
        print(file=outFile)
outFile.close()
