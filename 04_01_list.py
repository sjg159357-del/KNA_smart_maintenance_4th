# 리스트
#형식: 이름= [값1, 값2, ...]
#- 리스트는 여러 값을 '순서대로' 한 이름에 담는다.

temps =[25, 26, 24, 28, 27]               #숫자 리스트
machines = ["펌프", "모터", "압축기"]
mixed = ["펌프", 87, True]      # 종류가 달라도 한 리스트에 담을 수 있음

print(len(temps))      #5
print(len([]))         #0


print("====실습2====")

list=[25,26,24,27,26,55]
#print(list)
#print(len(list))

#list_1=[]
#print(list_1)
#print(len(list_1))

#print(list[0],list[2],list[-1])

#list[0]=33
#list[5]=22
#print(list[0]+list[5],(list[0]+list[5]/2))

#print("===실습4===")
#temp=[22,24,27,28,30,21,3,18,33,83]
#print(temp[0:3],temp[3:6],len(temp[0:3]))

print("===실습5===")

e=[3,4,5,6,5,4,6,7,8,7,5,3]
first=e[0:6]
second=e[6:]
print(first)
print(second)
print(len(first),len(second))



# 실습 8
#temps=[25,26,999,24,28,26]
#temps.remove(999)
#print(temps)
#x= temps.pop(1)
#print(X)
#del temps[0]
#print(temps)

# 실습 9
temps =[27,24,30,22,26,24,28]
temps.sort()
print(temps)
temps.reverse()
print(temps)
print(temps.count(24))
print(temps.index(24))
