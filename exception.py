#poo=5/0
#print(poo)
'''try:
    num=10
    deno=0
    
    result=num/deno
    
    print(result)
except:
    print("error:deno cannot b 0")'''



'''try:
    even_nos=[2,4,6,8]
    print(even_nos[2]/0)
except ZeroDivisionError:
    print("den cannot b zero")
except IndexError:
    print("index out of bound")'''



'''try:
    num=int(input("enter a no"))
    assert num%2==0#used for debugging code
except:
    print("not an even")
else:
    reciprocal=1/num
    print(reciprocal)'''



try:
    num=10
    deno=0
    
    result=num/deno
except:
    print("denomiantor cannot b 0");
finally:
    print("this is finally block")