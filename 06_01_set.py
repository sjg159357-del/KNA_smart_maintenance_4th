# 셋 _ 중복 자동 제거, 순서 없음
# 형식: {값1, 값2} 또는 Set(리스트)
# -빈 셋 set()
#logs = ["S01","S02","S01","S03"]
#unique_logs= set(logs)
#print(unique_logs)  #셋은 순서가 없어 인덱싱 불가
#print(sorted(unique_logs))               #['S01','S02','S03']

# 1. 변수명 'alerts'로 수정 및 "S01," 뒤의 불필요한 콤마 제거
#alerts = {"S01", "S02"}

# 2. "S03" 추가
#alerts.add("S03")
#print(alerts)

# 3. 중복된 값 "S02" 추가 (세트는 중복을 허용하지 않음)
#alerts.add("S02")
#print(alerts)

# 4. 'priint' 오탈자 수정 및 포함 여부 확인
#print("S02" in alerts)

#print("===실습4===")
#ID=["S01","S02","S03","S04"]
#ID_ture=set(ID)
#print(sorted(ID_ture))
#print(len(sorted(ID_ture)))

#집합 연산 -union(전체) / intersection(공통)/ difference(차이)
#line_a= {"S01","S02","S03"}
#line_b = {"S03","S04"}
#print(line_a.union(line_b))
#print(line_a.intersection(line_b))
#print(line_a.difference(line_b))

#A={"A01","A02","A03","A04"}
#B={"A01","A02","A06","A07"}
#print("공통:",A.union(B))
#print("A만:",A.intersection(B))
#print("B만:",B.difference(A))

todayID_1={"D01","D02","D03"}
D_1ID_2={"D01","D06","D11"}
print("신규이상:",todayID_1.difference(D_1ID_2))
print("지속이상:",todayID_1.intersection(D_1ID_2))
