

try:    # try block
    a=int(input())
    b=int(input())
    print(a+b)
except Exception as e:  # e to show the actual mistake
    print("Give only Integer Value",e)


