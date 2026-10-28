# 딕셔너리
# 형식: {키: 값, 키: 값} -키는 문자열
# -리스트는 번호(인덱스)로 찾지만 딕셔너리는 이름(키)으로 찾는다
#sensors ={"모터온도": 78, "진동":0.5}
#print(sensors)
#print(sensors["모터온도"])
#print(type(sensors))       #<class 'dict'>
#print(sensors["유량"])             #key Error-> 없는키를 조회 시 에러

# 추가/ 수정/ 삭제
# 형식: 딕셔너리[키] =값 (없는 키 - 추가, 있는 키 - 수정)
# 형식: (삭제) del 딕셔너리[키]

#sensors = {"펌프압력": 50, "진동": 12}  # 예시를 위해 초기 딕셔너리 생성

#sensors["펌프압력"] = 95  # 추가 (또는 기존 값 수정)
#sensors["모터온도"] = 80  # 수정 (또는 새로운 키-값 추가#)
# del sensors["진동"]    # 삭제 (현재는 주석 처리됨)
# print(sensors)

# get() / in 연산자 사용법
# 형식: 딕셔너리.get(키, 기본값) / 키 in 딕셔너리

#print(sensors.get("유량"))        # None (괄호 누락 수정)
#print(sensors.get("유량", 0))     # 0

#print("모터온도" in sensors)      # True (앞쪽 불필요한 공백 제거)
#print(80 in sensors)            # False (sensrs 오타 수정 및 값 검색 특성)
'''
sensors={"모터온도":78,"진동":0.5}

print(sensors["모터온도"])
sensors["모터온도"]=95
print(sensors["모터온도"])
sensors["모터온도"]=78
print(sensors["모터온도"])
print(sensors.get("유량",0))
print(0 in sensors)

# keys/values/ items /len
sensors={"모터온도":78, "진동":0.5}
print(list(sensors.keys())/len(sensors))

print(list(sensors.vlaues()))
avg=sum(sensors.values())
print(avg)
'''
#for name, value in  sensors.items():
 #   print(name, value)

#for k in sensors.keys()
# for v in sensors.values()

#update - 여러 항목 한번에 갱신(키가 있으면 수정, 없으면 추가)
#d={"온도":78}
#d.update({"온도":80,})

# zip: 센서명 - 값 매핑하기
names=["온도","진동","압력"]
values=[78,0.5,95]
sensors =dict(zip(names,values))
print(sensors)

# 딕셔너리의 값에  리스트/딕셔너리  - 중첩 딕셔너리
plant={
    "1번모터":{"온도":78, "상태": "정상"},
    "2번펌프":{"압력":95, "상태": "경고"}
}

print(plant["2번펌프"]["압력"])    # 95



























