# dicsnary in python

info = {
  "name":"shivam ahirwar",
  "age": 18,
  "en-no":"0832IT221059",
  "branch":"IT"
}

info["name"] = "apna college"
print(info)

# null_dict 
null_dict = {}
null_dict["name"] = "cdgi"
print(null_dict)

# nested dicsnary

student = {
  "name" : "Shivam ahiirwar",
  "sub"  : {
    "phy": 97,
    "chem" : 98,
    "math" : 100
  }
}

print(student)
print(student["sub"])
print(student["sub"]["math"])

#update value in dic
new_dict = {"city": "Indore"}
student.update(new_dict)

#pritn dic all key values
print(student.values)

#pritn dic all item values
print(student.items())

#shorts
print(student.keys())
print(len(student.keys()))

#convert dict into list
print(list(student.keys()))