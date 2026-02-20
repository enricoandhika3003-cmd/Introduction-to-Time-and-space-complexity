#Best Choice:
#Applies only one formula; No loops
def art(n):
    return int(n*(n+1)/2)

print(art(10))

#Loop runs from 1 to n
def art2(n):
    sum=0
    
    for i in range(1, n+1):
        sum+=i
    return sum

print(art2(10))

#2 Loops, Inner based off of Outer Loop
def art3(n):
    sum=0
    
    for i in range(1, n+1):
        for j in range(1, i+1):
            sum+=1
    return sum

print(art3(10))