from myModules.models import Student
from myModules.math_utils import average_grade


class __main__():
    list = []

    list.append(Student("Brian", 90))
    list.append(Student("Chris", 92))
    list.append(Student("Ray", 91))
    list.append(Student("Anna", 85))
    list.append(Student("Aoife", 80))
    list.append(Student("Ana", 95))
    list.append(Student("Will", 87))
    list.append(Student("Max", 84))
    list.append(Student("Karen", 80))
    list.append(Student("Liam", 100))

    print(average_grade(list))
