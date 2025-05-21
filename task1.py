import random
import time
import pandas as pd
import matplotlib.pyplot as plt


# Рандомізований QuickSort
def randomized_quick_sort(arr: list) -> list:
    # Якщо масив має менше ніж два елементи, він уже відсортований
    if len(arr) < 2:
        return arr

    # Вибираємо випадковий індекс для опорного елемента
    pivot_index = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_index]

    # Розділяємо масив на три частини: менші, рівні та більші за опорний елемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


# Детермінований QuickSort
def deterministic_quick_sort(arr: list) -> list:
    # Якщо масив порожній або містить один елемент, повертаємо його
    if len(arr) < 2:
        return arr
    
    # Вибираємо середній елемент як опорний
    pivot_index = len(arr) // 2
    pivot = arr[pivot_index]

    # Розділяємо масив на три частини: менші, рівні та більші за опорний елемент
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    # Рекурсивно сортуємо ліву і праву частини, а потім об'єднуємо
    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


# Функція для вимірювання часу
def measure_time(sort_function: callable, arr: list, repeats=5) -> float:
    total_time = 0
    for _ in range(repeats):
        copied_array = arr.copy()
        start_time = time.time()
        sort_function(copied_array)
        total_time += time.time() - start_time
    return total_time / repeats

# Функція для побудови графіка
def plot_results(results):
    sizes = [result["Розмір масиву"] for result in results]
    deterministic_times = [result["Детермінований QuickSort"] for result in results]
    randomized_times = [result["Рандомізований QuickSort"] for result in results]

    plt.plot(sizes, deterministic_times, label="Детермінований QuickSort")
    plt.plot(sizes, randomized_times, label="Рандомізований QuickSort")
    plt.xlabel("Розмір масиву")
    plt.ylabel("Середній час виконання (секунди)")
    plt.title("Порівняння рандомізованого і детермінованого QuickSort")
    plt.legend()
    plt.grid()
    plt.show()


def main():
    # Тестування
    sizes = [10_000, 50_000, 100_000, 500_000]
    results = []

    for size in sizes:
        array = [random.randint(0, 100_000) for _ in range(size)]
        time_deterministic = measure_time(deterministic_quick_sort, array)
        time_randomized = measure_time(randomized_quick_sort, array)

        print(f"\nРозмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {time_randomized:.4f} секунд")
        print(f"   Детермінований QuickSort: {time_deterministic:.4f} секунд")

        results.append(
            {
                "Розмір масиву": size,
                "Рандомізований QuickSort": time_randomized,
                "Детермінований QuickSort": time_deterministic,
            }
        )

    df_results = pd.DataFrame(results)
    plot_results(results)

if __name__ == "__main__":
    main()
