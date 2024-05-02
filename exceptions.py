def main():
    t = int(input())  # Number of test cases
    for _ in range(t):
        try:
            a, b = map(int, input().split())
            result = a // b  # Integer division
            print(result)
        except ZeroDivisionError as e:
            print(f"Error Code: {e}")
        except ValueError as e:
            print(f"Error Code: {e}")

if __name__ == "__main__":
    main()
