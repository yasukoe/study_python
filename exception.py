# Exception

class MyException(Exception):
    pass



def div(a,b):
    try:
        if(b<0):
            raise MyException("not minus")
        print(a/b)
    except ZeroDivisionError: #Python word
        print("not by zero")
    except MyException as e:
        print(e)
    else:
        print('no exception')
    finally:
        print('--end--')

div(10,3)
div(10,0)
div(10,-3)
