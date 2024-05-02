import itertools

def modify_string(s):
    result = []
    for key, group in itertools.groupby(s):
        count = len(list(group))
        result.append((count, int(key)))
    return result

s = input().strip()

modified_string = modify_string(s)
print(*modified_string)
