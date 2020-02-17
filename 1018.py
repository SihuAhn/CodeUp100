list = input().split()
for i in range(len(list)):
    if list[i] is int:
        print(int(list[i]))
    else:
        print(list[i])
        
 #모범 소스    
# h,m=input().split(':');
# print(int(h), int(m), sep=':');
