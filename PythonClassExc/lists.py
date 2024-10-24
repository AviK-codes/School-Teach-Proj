import random

a="aaa"
ls=["a", "b", "c"]
lista = [1, 5, 6, ls, 7, 8, a]
print(lista[3])
print(lista)

grocery_list = [5, "milk", 1, "bread", 1, "honey", 10, "bananas"]
print(grocery_list)
print(grocery_list[1])
print(grocery_list[0:4])
grocery_list[0:1] = [1, "butter"]
print(grocery_list)
shops_list = ["supersal", "rami_levi", "carrefour"]
shops_list.append("osher_ad")
another = "supertal"
shops_list.append(another)
buying_list = [shops_list, grocery_list]
print(buying_list)
del shops_list[0:2]
print(5*shops_list)
state=("power", "on", 220)
print(state)


a = ["aaa mmm kkk", "   bbb  ccc lll ", "ccc","wer","pp","aed"]
print(a[1].strip())
print(a[1].upper())
print(a[1].lower())
print(a[1].title())
a.remove("ccc")
print(a)
for x in a:
    print(x.strip().upper())
    print(x.lower())
    print(x.title())

#List Comprehensions:
#List comprehensions allow you to create new lists based
#on existing ones in a concise way.

f = [x**2 for x in range(1,11)]
print(f)

v=f[-3:]
print(v)

even_numbers = [num for num in range(1, 10) if num % 2 == 0]
print(even_numbers)
# Output: [2, 4, 6, 8]

numbers = [1, 2, 3, 4, 5, 6]
even_odd_list = ["Even" if i % 2 == 0 else "Odd" for i in numbers]
print(even_odd_list)
# Output: ['Odd', 'Even', 'Odd', 'Even', 'Odd', 'Even']

num_list = [y for y in range(100) if y % 2 == 0 if y % 5 == 0]
print(num_list)
# Output: [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]

word = "RED"
tripled_letters = [x * 3 for x in word]
print(tripled_letters)
# Output: ['RRR', 'EEE', 'DDD']

print(random.randrange(0, 10))
rnd = [random.randrange(0, 10)]
print(rnd)

abc = [random.randrange(0, 10) for i in range(10) ]
print("abd=",abc)

colors = ["red", "blue", "green"]
print(colors)
for color in colors:
    selection = colors.pop()
    print(selection)
selection = colors.pop()
print(selection)
print(colors)

a=['a','v','f','g']
a[0:2] = ['l',1,2]
print(a)

a="aaa"
ls=["a", "b", "c"]
lista = [1, 5, 6, ls, 7, 8, a]
print(lista[3][2])
print(lista)

a = [0, 1, 2, 3, 4, 5]

print(a[::2])   # [0, 2, 4] (every second element)
print(a[1::2])  # [1, 3, 5] (every second element, starting from index 1)
print(a[:3])    # [0, 1, 2] (first three elements)
print(a[3:])    # [3, 4, 5] (all elements from index 3 onwards)
print(a[::-1])  # [5, 4, 3, 2, 1, 0] (all elements backward)

colors = ["red", "blue", "green"]
print(colors)
for color in colors:
    selection = colors.pop()
    print(selection)

aa=[[1,2],[3,4],[5,6],[7,8]]
l =[item for sublist in aa for item in sublist if (item % 2) == 0]
print(l)

name1= "jojo"
nums=[1,2,3,4]
n1=[char for couples in zip(name1,nums) for char in couples]
print(n1)

m1=[]
for couples in zip(name1,nums):
    for char in couples:
        m1.append(char)
print(m1)


nn = [ i for x in zip("Jerusalem",[0,1,2,3,4,5,6,7]) for i in x]
print(nn)

lst=["yossi", "yaakov","miriam","zvulun"]
print([[l,word[::-1]] for word in lst for l in word[0]])

binary_strings = ['101', '110', '1001','101111001010']

decimal_values = [int(bin_str, 2) for bin_str in binary_strings]
print(decimal_values)

n = 7
primes = [x for x in range(2, n+1) if (x % y != 0 for y in range(2, int(x**0.5) + 1))]
print(primes)
print(int(n**0.5) + 1)
