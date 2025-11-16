from typing import List, Tuple

def linear_search(student_ids: List[int], target: int) -> Tuple[int, int]:
    comparisons = 0
    for i, sid in enumerate(student_ids):
        comparisons += 1
        if sid == target:
            return i + 1, comparisons  
    return -1, comparisons

def binary_search(scores: List[int], target: int) -> Tuple[int, int]:
    left, right = 0, len(scores) - 1
    comparisons = 0
    while left <= right:
        mid = (left + right) // 2
        comparisons += 1
        if scores[mid] == target:
            return mid + 1, comparisons 
        elif scores[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1, comparisons

def show_search_menu():
    print("=== Searching Algorithms Menu ===")
    print("Select a search operation (1-3):")
    print("1. Linear Search - Find Student ID")
    print("2. Binary Search - Find Score")
    print("3. Exit program")

def main():
    student_ids = [1000, 1001, 1010, 1005, 1046, 1070, 1024, 1039, 1017, 1002,
                   1025, 1031, 1056, 1093, 1084, 1066, 1007, 1018, 1029, 1090]
    sorted_scores = [34, 41, 47, 73, 78, 61, 65, 87, 81, 84, 89, 98, 95, 91, 99,
                     110, 100, 109, 170, 125]

    while True:
        show_search_menu()
        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            print(f"Searching in the list: {student_ids}")
            try:
                target = int(input("Enter Student ID to search: ").strip())
            except ValueError:
                print("Please enter a valid integer Student ID.\n")
                continue
            pos, comps = linear_search(student_ids, target)
            if pos != -1:
                print(f"Result: Student ID {target} found at position {pos} Comparisons made: {comps}\n")
            else:
                print(f"Result: Student ID {target} not found. Comparisons made: {comps}\n")

        elif choice == "2":
            print(f"Sorted scores: {sorted_scores}")
            try:
                target = int(input("Enter score to search: ").strip())
            except ValueError:
                print("Please enter a valid integer score.\n")
                continue
            pos, comps = binary_search(sorted_scores, target)
            if pos != -1:
                print(f"Result: Score {target} found at position {pos} Comparisons made: {comps}\n")
            else:
                print(f"Result: Score {target} not found. Comparisons made: {comps}\n")

        elif choice == "3":
            print("Thank you for using the search program!")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.\n")

        again = input("Would you like to perform another search? (y/n): ").strip().lower()
        if again != 'y':
            print("Thank you for using the search program!")
            break

if __name__ == "__main__":
    main()

