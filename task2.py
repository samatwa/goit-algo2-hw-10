# Визначення класу Teacher
class Teacher:
    def __init__(
        self,
        first_name: str,
        last_name: str,
        age: int,
        email: str,
        can_teach_subjects: set[str],
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.can_teach_subjects = can_teach_subjects
        self.assigned_subjects = set()


# Функція для створення розкладу
def create_schedule(
    subjects: set[str], teachers: list[Teacher]
) -> list[Teacher] | None:
    # Перевіряємо граничні випадки
    if not subjects:
        return []  # Порожній розклад, якщо немає предметів

    if not teachers:
        return None  # Неможливо створити розклад без викладачів

    uncovered_subjects = set(subjects)
    available_teachers = teachers.copy()
    schedule = []

    while uncovered_subjects:
        best_teacher = None
        best_covered = set()

        for teacher in available_teachers:
            covered = teacher.can_teach_subjects & uncovered_subjects

            if len(covered) > len(best_covered) or (
                len(covered) == len(best_covered)
                and best_teacher
                and teacher.age < best_teacher.age
            ):
                best_teacher = teacher
                best_covered = covered

        if not best_teacher or not best_covered:
            return None  # Не можна покрити всі предмети

        # Додаємо викладача до розкладу і оновлюємо його призначені предмети
        best_teacher.assigned_subjects = best_covered
        schedule.append(best_teacher)

        # # Оновлюємо непокриті предмети і доступних викладачів
        uncovered_subjects -= best_covered
        available_teachers.remove(best_teacher)

    return schedule


# Основна частина
if __name__ == "__main__":
    # Множина предметів
    subjects = {"Математика", "Фізика", "Хімія", "Інформатика", "Біологія"}

    # Створення списку викладачів
    teachers = [
        Teacher(
            "Олександр",
            "Іваненко",
            45,
            "o.ivanenko@example.com",
            {"Математика", "Фізика"},
        ),
        Teacher("Марія", "Петренко", 38, "m.petrenko@example.com", {"Хімія"}),
        Teacher(
            "Сергій",
            "Коваленко",
            50,
            "s.kovalenko@example.com",
            {"Інформатика", "Математика"},
        ),
        Teacher(
            "Наталія", "Шевченко", 29, "n.shevchenko@example.com", {"Біологія", "Хімія"}
        ),
        Teacher(
            "Дмитро",
            "Бондаренко",
            35,
            "d.bondarenko@example.com",
            {"Фізика", "Інформатика"},
        ),
        Teacher("Олена", "Гриценко", 42, "o.grytsenko@example.com", {"Біологія"}),
    ]

    # Виклик функції створення розкладу
    schedule = create_schedule(subjects, teachers)

    # Виведення результату
    if schedule:
        print("Розклад занять:")
        for teacher in schedule:
            print(
                f"{teacher.first_name} {teacher.last_name}, {teacher.age} років, email: {teacher.email}"
            )
            print(
                f"   Викладає предмети: {', '.join(sorted(teacher.assigned_subjects))}\n"
            )
    else:
        print("Неможливо покрити всі предмети наявними викладачами.")
