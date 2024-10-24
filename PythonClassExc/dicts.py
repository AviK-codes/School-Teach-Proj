dicta = {"yoav": "football", "yosi": "basketball", "haim": "swimming"}
print(dicta["yosi"])

dicta = [{"name": "boris", "age": 45, "location": "moscow"}, {"name": "dima", "age": 34, "location": "kiev"}]
print(dict)
for i in dicta:
    print(i["name"] + " is leaving in:")
    print(i["location"])
    print(f"{i["name"]} is leaving in {i["location"]}")
    if i["location"] == "moscow":
        print("he is in Russia")

sports = {'John': 'Football', 'Mike': 'Basketball', 'Yariv': 'Swimming', 'Liana': 'Running', 'Eitan': 'Bicycle'}
print(sports)
print(sports['John'])
print(sports['Yariv'])
sports['John'] = "Jogging"
print(sports)
del sports['Mike']
print(sports)
sports.update({"Hila" : "Surfing"})

print("\nprint key and values:")
for k, v in sports.items():
    print(k, v)

print("\nprint the values:")
for v in sports.values():
    print(v)

print("\nprint the keys:")
for k in sports:
    print(k)