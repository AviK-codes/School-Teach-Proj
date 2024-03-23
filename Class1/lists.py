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

f = [x**2 for x in range(1,11)]
print(f)

v=f[-3:]
print(v)
