// 3 6 9 게임의 왕이 되자

// 만약 3, 6, 9 가 들어간 수를 자신이 불러야 하는 상황이라면, 수를 부르는 대신 "박수(X)" 를 쳐야 한다

n = int(input())

for i in range(1, n+1) :
  if i%10==3 or i%10==6 or i%10==9 :
    print("X", end=' ')
  else :
    print(i, end=' ')
