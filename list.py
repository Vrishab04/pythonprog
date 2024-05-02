if __name__ == '__main__':
 n=int(input())
name = input()
score = float(input())
students = []
for i in range(n):
    name = input()
    grade = float(input())
    students.append([name, grade])
students.sort(key=lambda x: x[1])
second_lowest_grade = None
for i in range(1, n):
    if students[i][1] != students[0][1]:
        second_lowest_grade = students[i][1]
        break
second_lowest_students = [name for name, score in students if score == second_lowest_grade]
second_lowest_students.sort()