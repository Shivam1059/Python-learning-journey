#variale create

a = 1234  #intiger data type
b1 = complex(5,7)
a1 = 345
print(a)
print(a + a1)
print(a + b1) # complex number 

b = "Harry" #string datatype decleartion for using double code
print(b)

c = True
print(c)

d = None

g = 3.345

#type of datatype
print("The type of a is: ",type(a))
print("The type of a is: ",type(b))
print("The type of a is: ",type(c))
print("The type of a is: ",type(d))
print("The type of a is: ",type(d))
print("The type of a is: ",type(g))


#list: list is collection of diffrent datatype of items, and list is muteable
list1 = [2,4,6,8,3,[-2,4],["apple","mango"],[4.56,-78]]
print(list1)

#Tupel : tupel is collecction of different datatype of item , and it is inmuteable
tupel = (("mango","banana"),(2,4),(4.56,-98))
print(tupel)

#dict : dicsnery is collection of key valueper , and it is muteable,and dicsnery is also a map datatype
dic1 = {
 "name" : "shivam ahiwar",
 "age" : 18,
 "city": "Indore",
 "hight" : 5.3
}
print(dic1)
print(dic1["name"]) #keyvalue pare
print(dic1["name"][3]) #indexing
