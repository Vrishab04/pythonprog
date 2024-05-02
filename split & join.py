def split_and_join(line):
a = str(input("this is a string"))
a = a.split(" ")  
print(a)  
a = "-".join(a)
print(a)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)