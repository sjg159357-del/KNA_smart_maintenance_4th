# f-stirng - 문자열 안에 변수 바로 끼우기
# 형식: f"~~~ {변수}~~"

#name = "홍길동"
#age = 25
#print(f'{name}님은 {age}살입니다')
# 숫자도 str 변환 없이 바로 들어감
#print(f'온도: {25.5}')
# 중괄호 안에 계산식 가능
hours =3
#print(f'{hours * 60}분')
# 소수점 자리수 조정
# 형식: {값(변수):.2f} -> 소수점 둘째 자리까지 (자동 반올림)
#value =25.34567
#print(f'측정값: {value:.2f}')
#print(f'측정값: {value:.1f}')

#a= '설비 PUMP-A'
#b= '온도 87도'
#print(f'{a,b}')

#print('실습2')
#a=87 
#b=87
#c=87
#print(f'평균{(a+b+c)/3}')

#print('실습3')
#observ= 87.456

#print(f' {observ:.1f}')
#print(f' {observ:.2f}')

#v='5,senosor_2,WARNING,0.78912'

#v1=v.strip().split(',')
#print(f'센서{v1[1]}상태{v1[2]}f' {v1[3]:.2f}'')

 #실습 4
#raw =" 5, sensor_2 , WARNIN , 0.78912 " 
    
#parts = raw.strip().split(',')
#sid = parts[1].strip()
#status=parts[2].strip().lower()
#value = float(parts[3].strip())

#print(f"[센서 {sid}] 상태 {status}, 측정값 {value:.2f}")

# 값 바꾸기 / in 존재 확인
# 형식: 리스트[번호] = 새 값 / 값 in 리스트
#nums=[25,26,24,28,27]
#nums[2] = 99
#print(nums)

#print("모터" in machines)

# 값 추가 - append, insert, extend
# 형식: 리스트.append(값) / 리스트.insert(위치, 값) / 리스트.extend(다른 리스트)
#data = [25, 26, 24]
#data.append(28)           #[25, 26, 24, 28]
#data.insert(1,99)        #[25. 99, 26, 24, 28]
#data.extend([30,31])     #[25, 99, 26, 24, 28, 30, 31]
#print(data)

#print("---실습6---")
#tem=[25,26,240,28,27] 

#print(240 in tem)
#print(tem.index(240))

#tem[2]=24
#print(240 in tem)

print("실습7")

b=[]
b.append(30)
b.insert(0,28)
b.extend([31,32])
print(b)




#값 삭제 -remove, pop, del
# 형식: 리스트.remove(값)/꺼낸 값 =리스트.pop(위치)/del 리스트[위치]
d = [25, 26, 24, 28, 27]
d.remove(24)
print(d)          #[25, 26, 28, 27]
got = d.pop(1) 
print(got, d) #26 [25,28, 27]
del d[0]
print(d)         #[28, 27]

# 정렬, 탐색 -sort,reverse / count, index
# 형식:리스트.sort()   .reverse()  . count(값)    .index(값)
#i=[27, 24, 30, 22, 26]
#i.sort()
#i.sort(reverse=True)
#i.reverse
#print(i)
#r=["정상", "이상", "정상", "정상", "이상"]
#print(r.count("정상"), r.index("이상"))             #3 1


#print("===실습 8===")

#number=[1,2,3,4,5,6]

#number.remove(3)
#print(number)

print("===실습9===")

hp=[3,5,9,2,4]

hp.sort()
print(hp)
print(hp.count(3),hp.index(3))

