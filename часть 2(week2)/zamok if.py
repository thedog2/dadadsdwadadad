a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
if (a<=d and b<=e) or (a<=e and b<=d):
    print('Yes')
elif (c<=d and b<=e)or(c<=e and b<=d):
    print('Yes')
elif(c<=d and a<=e)or(c<=e and a<=d):
    print('Yes')
else:
    print('No')
