import time


def bubble_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def insertion_sort(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key

    end_time = time.time()
    execution_time = end_time - start_time

    return arr, execution_time


def print_iterations(arr, iterations=5):
    print("Iterasi Pertama:")
    for i in range(iterations):
        print(arr[i], end=" ")
    print("\n")

    print("Iterasi Terakhir:")
    for i in range(len(arr) - iterations, len(arr)):
        print(arr[i], end=" ")
    print("\n")


def print_analysis():
    print("Worst Case: Bubble Sort and Insertion Sort memiliki kompleksitas waktu O(n^2).")
    print("Best Case (Bubble Sort): Jika array sudah terurut secara menaik, kompleksitas waktu menjadi O(n).")
    print("Best Case (Insertion Sort): Jika array sudah terurut secara menurun, kompleksitas waktu menjadi O(n).")
    print("Average Case: Bubble Sort dan Insertion Sort memiliki kompleksitas waktu O(n^2).\n")


def main():
    arr = [12, 99, 62, 15, 20, 95, 39, 48, 3, 24, 8, 43, 74, 19, 97, 33, 49, 68, 55, 33,
           90, 90, 7, 26, 85, 46, 39, 40, 9, 36, 60, 64, 89, 31, 25, 71, 21, 23, 63, 84,
           32, 5, 3, 44, 21, 10, 21, 17, 50, 2, 36, 53, 79, 54, 19, 88, 1, 32, 31, 15, 6,
           3, 1, 40, 22, 43, 18, 1, 77, 9, 59, 40, 7, 41, 81]

    print("Sebelum pengurutan:")
    print(arr)
    print("\n")

    choice = input("Pilih metode pengurutan (bubble/insertion): ")

    if choice == "bubble":
        sorted_arr, execution_time = bubble_sort(arr.copy())
    elif choice == "insertion":
        sorted_arr, execution_time = insertion_sort(arr.copy())
    else:
        print("Pilihan tidak valid.")
        return

    print("Setelah pengurutan:")
    print(sorted)
