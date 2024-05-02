def average(arr):
    distinct_heights = set(arr) 
    total_height = sum(distinct_heights)
    num_distinct_heights = len(distinct_heights)
    avg = total_height / num_distinct_heights 
    return round(avg, 3) 

n = int(input()) 
heights = list(map(int, input().split()))
print(average(heights))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)