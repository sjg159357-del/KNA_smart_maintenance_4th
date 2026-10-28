# 튜플
# 형식: (값1, 값2, 값3,.....)
# - 좌표, (이름, 값) 처럼 짝지어진 값을 하나로 묶을 때
#sensor=("모터온도",78)
#print(sensor)             #('모터온도',78)
#one =(78,)                #값이 한개라도, 표시해야할  튜플로 인지
#not_tuple=(78)
#print(type(one), type(not_tuple))          #<class 'tuple'> <class 'int'>

# 튜플 인덱싱, 슬라이싱
#s= ("모터온도",78,"C")
#print(s[0],s[-1])
#readings = (78,80,79,95,77)
#print(readings[1:4])

#  튜플 언패킹 - 한 번에 변수로 분리
# 형식: 변수1, 변수2=튜플 (변수 개수가 튜블 값 개수와 일치)
#name, value =sensor

#sensor=("모터온도",78)
#print(sensor)
#print(sensor[0],sensor[1])

#a=sensor[0]
#b=sensor[1]
#print(a, b)

#튜플 리스트+반복문(언패킹)
# - (이름, 값) 튜플들을 리스트로 모아 for 순회하면 여름, 값이 자동 분리
#sensors = [("모터온도",78),("펌프압력", 95)]
#for s in sensors:
 #   print(s)
  #  if value > 90:
   #     print(name, "경고")


# 중첩 튜플
#sensors = ("모터온도",78,(3,5))
#print(sensors[2][0])

# 튜플 리스트 정렬
sensors = [(78, "모터온도"), (95, "베어링진동"), (32, "펌프압력")]

# 오타 수정: sesors -> sensors
hot = sorted(sensors, reverse=True)

print(hot)
