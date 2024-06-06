# def greeting (name):
#     print('hello',name)

# print(greeting('ali'))
# print(greeting)

# sayHello =greeting
# print(sayHello)
# print(greeting)

# del sayHello
# print(sayHello)
# print(greeting)



def factorial (number):
    if not isinstance(number,int):
        raise TypeError('Number must be an integer ')
    
    if not number >=0:
        raise ValueError('number must be zero or possitive')



    def inner_factorial(number):
        if number <=1:
            return 1
        
        return number * inner_factorial(number-1)
    return inner_factorial(number)


try:
    print(factorial(input('faktoryelini almak istediginiz sayiyi giriniz....')))
except Exception as ex:
    print(ex)