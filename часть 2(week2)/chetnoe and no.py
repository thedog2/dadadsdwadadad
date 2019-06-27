a=int(input())
b=int(input())
c=int(input())
if (a%2==0 and b%2!=0) or (a%2!=0 and b%2==0):
    print('Yes')
elif(a%2==0 and c%2!=0) or (a%2!=0 and c%2==0):
    print('Yes')
elif(b%2==0 and c%2!=0) or (b%2!=0 and c%2==0):
    print('Yes')
else:
    print('No')
