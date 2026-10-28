# 실습 1
#temps = [25,32,28,35,19,31,27]
#for t in temps:
 #if t>=30:
 #   print("고온:",t)

# 실습 2
#hours= [3,8,12,6,10,4,9]
#for h in hours:
 #   if h >=5 and h<=10:
  #      print(h)
# 최대, 최소
#temps=[25,32,28,36,27,31]
#biggest = temps[0]
#for t in temps:
 #  if t> biggest:
  #    biggest =t
#print(biggest)

# 빈 리스트 채우기
#tmeps=[25,26,24,28]
#doubled = []
#for t in temps:
 #   doubled.append(t*2)
#print(doubled)       #[50,64,56,72,54,62]

#print("====실습3====")
#temps=[25,32,28,36,27,31,24]
#total=0
#count=0
#for t in temps:
    #if t > 30: 
#     total +=t
#     count+=1
#   print("고온 평균:", total/count)

#print("===실습4===")
#temps=[32,35,31,33]
#go=[]
#for t in temps:
#   if t>30:
#       go.append(t)
#print(temps)
#print(go,'/갯수',len(go))

#print("===실습5===")
#f=[33,34,35,66]
#c=[]
#for t in f:
#    c.append(t*1.8+32)
#print(f)
#print(c)

# 중첩 리스트 -리스트 안에 리스트
#- 표(행,열)처럼 한 줄에 여러 값이 묶인 데이터. 바깥 반복은 '행', 안쪽 인덱스로 '열'
#rows = [["펌프",25],["모터",32],["압축기",28]]
#for row in rows:
 #   print(row[0], "온도", row[1])

#print("===실습6===")

#temps = [25, 32, 28, 35, 27, 31, 24, 33, 29, 36]

# 1. 누적할 변수와 빈 리스트(hot)를 반복문 "밖"에서 초기화합니다.
#total = 0
#hot = []

# 2. 첫 번째 for문: 전체 합계를 구하고, 30도 초과 데이터를 hot 리스트에 담습니다.
#for t in temps:
 #   total += t  # 오타 수정: totoal += 5 -> total += t (원래 온도를 더해야 함)

  #  if t > 30:
   #     hot.append(t)

# 3. 두 번째 for문: 고온 리스트(hot)의 합계를 구합니다. (첫 번째 for문이 완전히 끝난 뒤 실행)
#hot_total = 0
#for h in hot:
 #   hot_total += h

# 4. 결과 출력: 모든 계산이 끝난 후 최종 결과를 딱 한 번만 출력합니다.
#print("전체 평균:", total / len(temps))
#print("고온 평균:", hot_total / len(hot))





