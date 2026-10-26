
#Разбиваем точки на соответствующие им кластеры
clustersA=[[],[]]
for s in open('27A.txt'):
    x,y = [float(c) for c in s.split()]
    if x>3:
        clustersA[0].append([x,y])
    else:
        clustersA[1].append([x,y])

#Сравниваем количество точек в массиве с каличеством точек в файле вручную
print(len(clustersA[0])+len(clustersA[1]))


#Функция для рассчёта расстояния между точек
def dist(p1,p2):
    x1,y1,x2,y2 = *p1, *p2
    return ((x2-x1)**2+(y2-y1)**2)**0.5

#Функция нахождения центроида в кластере
def center(kl):
    m=[]
    for p in kl:
        sm = sum(dist(p,p1) for p1 in kl)
        m.append([sm,p])
    return min(m)[1]

#Центроиды кластера
centerA = [center(kl) for kl in clustersA]
