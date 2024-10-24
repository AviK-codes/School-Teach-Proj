print(5 * 6)
print(5*"cat")
my_cat = 5*"cat"
print(my_cat)
print(my_cat.upper())

my_cat = "My cat is saying \"I like eating mice\"    aaaa"
my_dog = "Rex"
print(my_cat)
print(my_cat.upper())
print(my_cat.title())
print(my_cat.count("a"))
print(my_cat.strip("a"))
print(my_cat.find("mice"))
print(my_cat.replace("mice", "birds"))
print(my_dog.isalpha())
print(my_dog.islower())
print(my_dog.lstrip())

word = "python"
print(word.center(10))  # Output:   python
print(word.center(16))  # Output:     python

file_name = "document.txt"

if file_name.startswith("document"):
    print("This is a document file.")
if file_name.endswith(".txt"):
    print("This is a text file.")

#my_score=input()
#print(f"My test score is {my_score}")
