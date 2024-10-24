users = {
    0: {"name": "Hero"},
    1: {"name": "Dunn"},
    2: {"name": "Sue"},
    3: {"name": "Chi"},
    4: {"name": "Thor"},
    5: {"name": "Clive"},
    6: {"name": "Hicks"},
    7: {"name": "Devin"},
    8: {"name": "Kate"},
    9: {"name": "Klein"}
}

friendships_pairs = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
                     (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

friendships = {users[user]["name"]: [] for user in users}
print(friendships)

for i,j in friendships_pairs:
    friendships[users[i]["name"]].append(users[j]["name"])
    friendships[users[j]["name"]].append(users[i]["name"])

print(friendships)