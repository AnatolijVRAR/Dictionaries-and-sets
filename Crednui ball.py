gredes = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Jonny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

gredes_m = [sum(gredes[0])/len(gredes[0]),
            sum(gredes[1])/len(gredes[1]),
            sum(gredes[2])/len(gredes[2]),
            sum(gredes[3])/len(gredes[3]),
            sum(gredes[4])/len(gredes[4])]

students_sort = sorted((students))

dict1 = dict(zip(students_sort, gredes_m))
print(dict1)
