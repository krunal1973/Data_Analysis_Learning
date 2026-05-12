for i in range(5):
    print(i)


for i in range(1,11):
    print(i)


sports = ["Cricket", "Football", "Hockey"]

for sport in sports:
    print(sport)


count=1

while count <=5: 
    print(count)
    count += 1

for i in range (1,11):

    if i %2 == 0:
        print(i)



for i in range(1,5):

    for j in range (1,5):
        print(i,j)


for i in range (1,4):

    for j in range(i):
        print("*", end=" ")
    print()



password=""

while password != "secret":
    password = input("Enter the password: ")
    
print("Access granted!")

count = 1
total=0
while count <=5:
     total = total + count
     count +=1
print(total)