'''
sensors = {"모터온도":78, "진동": 0.5}
print(sensors["모터온도"])      #78
sensors["압력"]=95
sensors["모터온도"]=80
print(sensors)

print(sensors.get("유량",0))  #0 (없으면 기본값)
print("진동" in sensors)    #True
'''

'''
a={"온도": 23}
b={"풍속": 44}
a.update(b)
print("갱신된 딕셔너리",a)
del a["온도"]
print("센서수:",len(a))
'''

#sensors={"온도":23,"압력":95}
#avg=sum(sensors.values())/len(sensors)

##for key, value in sensors.items():
  #  if value> avg:
 #       print("최대값 센서:",key)

#a={'온도','진동','압력'}
#b={78,0.5,95}
#a=dict(zip(a,b))

#for name, value in a.items():
#    print(name,value)

#a={"온도":55,"압력":88,"진동":44}
#b={"온도":60,"압력":60,"진동":10}
#c={}
#for key, value in a.items():
#    if value>b[key]:
#        c[key]=value
 #       print("경고센서:",value)
        
  # 실습 5
#valuues={"온도":95, "진동":0.5,"압력":88}
#limits={"온도":90, "진동":1.0,"압력":90}
#warning=[]

#for name, value in values.items()

# 실습 6
'''
plant = {
    "1번모터": {"온도":78, "상태": "정상"},
    "2번펌프": {"압력":95, "상태":"경고"}
}

for name, info in plant.items():
    if info["상태"]=="경고":
        print(f"{name} 점검필요")
'''

#실습 7
#rows={"온도":78, "압력":95,"진동":0.5}
#sensors={}
#for row in rows:
#    name,value=row.split(",")
#    sensors[name]=float(value)
#print(sensors)



# 실습 8
sensors = {"온도": 95, "압력": 96}
limits = {"온도": 90, "압력": 90}

# values() 이용한 평균
avg = sum(sensors.values()) / len(sensors)
print("평균:", round(avg, 1))

# items() 순회 -> 임계값 비교 -> 초과한 값은 셋에 담기(키 값 담기)
danger = set()
for name, v in sensors.items():
    if v > limits[name]:     # 1. 들여쓰기(공백 4칸)를 맞춰야 합니다.
        danger.add(name)     # 2. 오타 수정: dnager -> danger (들여쓰기도 적용)

# 셋 정렬하여 출력
print("위험 센서:", sorted(danger))  # 3. 오타 수정: dager -> danger


