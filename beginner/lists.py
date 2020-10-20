lucky_numbers = [1,2,3,3,4]
friends = ["Kevin","Karen","Jim"]
friends[0] = "Mike"
friends.append("Creed")
friends.insert(2,"Oscar")
friends.remove("Jim")
friends.clear()
friends.extend(lucky_numbers)
friends.pop()
print(friends)
print(friends.index(1))
print(friends.count(3))

newfriends = ["Kevin","Karen","Jim","Creed","Pam","Mike"]
newfriends.sort()
print(newfriends)
newnewfriends = newfriends.copy()
newnewfriends.reverse()
print(newnewfriends)