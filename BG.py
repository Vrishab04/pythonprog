file_path="poorvi.txt"
try:
    with open(file_path,"r")as file:
        content=file.read()
        print(content)
except Exception as e:
    print(f"an error occured:{e}")
finally:
    print("closing the file")