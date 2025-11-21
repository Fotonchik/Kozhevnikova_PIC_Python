from mygroup import groupmates


def print_students(students):
    print("Имя".ljust(15), "Фамилия".ljust(10), "Экзамены".ljust(30), "Оценки".ljust(20), "Средний балл")
    print("-" * 100)
    for student in students:
        avg_grade = sum(student["оценки"]) / len(student["оценки"])
        print(student["имя"].ljust(15), 
              student["фамилия"].ljust(10), 
              str(student["экзамены"]).ljust(30), 
              str(student["оценки"]).ljust(20),
              f"{avg_grade:.2f}")


def filter_students_by_avg(students, min_avg):
    """
    Фильтрует студентов по средней оценке.
    Возвращает список студентов с средним баллом выше min_avg.
    """
    filtered = []
    for student in students:
        avg_grade = sum(student["оценки"]) / len(student["оценки"])
        if avg_grade > min_avg:
            filtered.append(student)
    return filtered


def main():
    print("=" * 100)
    print("Список всех студентов группы:")
    print("=" * 100)
    print_students(groupmates)
    
    print("\n" + "=" * 100)
    threshold = float(input("Введите минимальный средний балл для фильтрации: "))
    print("=" * 100)
    
    filtered_students = filter_students_by_avg(groupmates, threshold)
    
    if filtered_students:
        print(f"\nСтуденты с средним баллом выше {threshold:.2f}:")
        print("=" * 100)
        print_students(filtered_students)
    else:
        print(f"\nСтудентов с средним баллом выше {threshold:.2f} не найдено.")


if __name__ == "__main__":
    main()


