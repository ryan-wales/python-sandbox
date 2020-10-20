friends = ["Jim","Pam","Kevin"]
for friend in friends:
    print(friend)

print("========")

for index in range(len(friends)):
    print(friends[index])


for index in range(5):
    if index == 0:
        print("first iteration")
    else:
        print("Not first")