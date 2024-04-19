fileptr=("poorvi.txt","r")

if fileptr:
    print("opened")
    
fileptr=open("poorvi.txt","a")#append
fileptr.write("mango")






if fileptr:
    print("opened succes")
fileptr.close()
    