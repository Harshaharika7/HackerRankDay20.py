if __name__ == '__main__':
  
    n = int(input().strip())
    a = list(map(int, input().rstrip().split()))

    # Write your code here
    num_swaps = 0

    for i in range(n):
        for j in range(n - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                num_swaps += 1

        # If no elements were swapped during a traversal, stop
        if num_swaps == 0:
            break

    print(f"Array is sorted in {num_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
