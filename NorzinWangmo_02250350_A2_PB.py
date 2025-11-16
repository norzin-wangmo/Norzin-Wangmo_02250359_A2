from typing import List, Tuple

def bubble_sort_names(names: List[str]) -> List[str]:
    arr = names[:]  # copy
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j].lower() > arr[j + 1].lower():
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def insertion_sort_scores(scores: List[int]) -> List[int]:
    arr = scores[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def quick_sort_prices(prices: List[int]) -> Tuple[List[int], int]:
    arr = prices[:]
    call_count = 0

    def quicksort(lo: int, hi: int):
        nonlocal call_count
        call_count += 1  
        if lo >= hi:
            return
        p = partition(lo, hi)
        quicksort(lo, p - 1)
        quicksort(p + 1, hi)

    def partition(lo: int, hi: int) -> int:
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        return i + 1

    if len(arr) > 0:
        quicksort(0, len(arr) - 1)
    return arr, call_count

def show_sort_menu():
    print("=== Sorting Algorithms Menu ===")
    print("Select a sorting operation (1-4):")
    print("1. Bubble Sort - Sort Student Names")
    print("2. Insertion Sort - Sort Test Scores")
    print("3. Quick Sort - Sort Book Prices")
    print("4. Exit program")

def main():
    student_names = ["Kado", "Bobchu", "Zamu", "Nado", "Lemo", "CheyChey", "Bumchu",
                     "Sangay", "Tashi", "Buthri", "Kunzang", "Jigme", "Kinley", "Tobden", "Peday"]

    test_scores = [78, 45, 92, 67, 88, 54, 73, 82, 91, 59, 76, 85, 48, 93, 71, 89, 57, 80, 69, 62]

    book_prices = [450, 230, 678, 125, 890, 320, 540, 275, 710, 95, 410, 605, 335, 120, 999]

    while True:
        show_sort_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print(f"Original: {student_names}")
            print("Performing Bubble Sort...")
            sorted_names = bubble_sort_names(student_names)
            print(f"Sorted: {sorted_names}\n")

        elif choice == "2":
            print(f"Original scores: {test_scores}")
            print("Performing Insertion Sort...")
            sorted_scores = insertion_sort_scores(test_scores)
            print(f"Sorted scores: {sorted_scores}")
            top5 = list(reversed(sorted_scores))[:5]
            print("Top 5 Scores:")
            for rank, score in enumerate(top5, start=1):
                print(f"{rank}. {score}")
            print()

        elif choice == "3":
            print(f"Original prices: {book_prices}")
            print("Performing Quick Sort...")
            sorted_prices, calls = quick_sort_prices(book_prices)
            print(f"Sorted prices: {sorted_prices}")
            print(f"Recursive calls: {calls}\n")

        elif choice == "4":
            print("Thank you for using the sorting program!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, 3, or 4.\n")

        again = input("Would you like to perform another sort? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the sorting program!")
            break

if __name__ == "__main__":
    main()
