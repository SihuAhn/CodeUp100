frontNum, backNum = input().split("-")
num = ("%06d" %int(frontNum)+ "%07d" %int(backNum)).replace(" ", "")
print(num)

#frontNum, backNum = input().split("-")
#print(frontNum+backNum)
