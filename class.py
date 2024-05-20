# # class 

# class Person :
#     # class attributes
#     address = ' no informaton'



#     # object attributes
#     # constructor(yapici metod)
#     def __init__(self, name , year):





#         # object attributes
#         self.name = name
#         self.year = year
#     # instance methods

#     def intro(self):
#         print('hello there.I am '+self.name)

#     # instance methods

#     def calculateage(self):
#         return 2019 - self.year

# # object(instance)

# p1 = Person(name='ali',year=1990)
# p2 = Person(name='yagmur',year=1859)


# p1.intro()
# p2.intro()

# print(f'adim: {p1.name} ve yasim: {p1.calculateage()}')
# print(f'adim: {p2.name} ve yasim: {p2.calculateage()}')



# print(p1)
# print(p2)
# print(type(p1))
# print(type(p2))
# print(p1==p2)

# # uptading
# p1.name='ahmet'
# p1.address='kocaeli'



# accessing object attributes
# print(f'name: {p1.name} year: {p1.year} address:{p1.address}')
# print(f'name: {p1.name} year: {p2.year}')





class Circle :
    # class object attribute
    pi = 3.14

    def __init__(self, yaricap=1) :
        self.yaricap = yaricap


    # methods
    def cevre_hesapla(self):
        return 2*self.pi*self.yaricap
    
    def alan_hesapla(self):
        return self.pi*(self.yaricap**2)
    
c1 = Circle()  #yaricap = 1 
c2 = Circle(5) 

print(f'c1 : alan = { c1.alan_hesapla()} cevre = {c1.cevre_hesapla()}')
print(f'c1 : alan = { c2.alan_hesapla()} cevre = {c2.cevre_hesapla()}')