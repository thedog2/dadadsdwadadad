N=int(input())
h= N % (60 * 24) // 60
m = N % 60
print(h,':',m)
