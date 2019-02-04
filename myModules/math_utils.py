from myModules.models import Student


def average_grade(roster):
    class_sum = 0
    for i in range(10):
        class_sum = class_sum + Student.get_grade(roster[i])

    class_average = class_sum / 10

    return class_average

