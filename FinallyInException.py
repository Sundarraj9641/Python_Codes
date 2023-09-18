try:    # try block
    a=int(input())
    b=int(input())
    print(a+b)
    
except ValueError as e:  # value error (Int, str, char)
    print("Give only Integer Value",e)

except TypeError as e:  # type error (+, -, *, /)
    print("Check the operation",e)

except Exception as e:  # It handle all types of error
    print("Check the operation",e)

finally:    # It will execute even exception was occurred or not
    print("It will execute even exception was occurred or not")




    

    


    
