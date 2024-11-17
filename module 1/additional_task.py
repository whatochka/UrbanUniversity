grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
students = sorted(list(students))
avarage_score_of_students = dict()

for index, name in enumerate(students):
    avarage_score_of_students[name] = sum(grades[index]) / len(grades[index])

print(avarage_score_of_students)
