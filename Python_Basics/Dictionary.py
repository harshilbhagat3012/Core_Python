#group of key & value pairs
#mutable
book = {"Book" : "Kafka on Shore", "Author" : "Murakami"}
print(book)
print(type(book))

print(book.get("Author"))
print(book["Book"])

print(book.keys())
print(book.values())

book["Author"] = "Haruki Murakami"
print(book)

#for Author in Book:
 #   print("Key:", Author)

#book.pop()
print(book)
#del car["Book"]
#compare dictionaries with == & !=


# Adding a value to the dictionary at run time which we will use in future frame works

dict = {}

dict["firstname"] = "Harshil"
dict["lastname"] = "Bhagat"
dict["gender"] = "Male"
print(dict)
print(dict["firstname"])
print(dict["lastname"])
print(dict["gender"])


#My name would be changed to harshil bhagat