from typing import List

def process_data(data: List[int]) -> int:
    total = 0
    for item in data:
        total += item
    return total

def main():
    data = [1, 2, 3, 4, 5]
    result = process_data(data)
    print(f"Total: {result}")

if __name__ == "__main__":
    main()