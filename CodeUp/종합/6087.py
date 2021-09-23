// 3의 배수는 통과

// 1부터 입력한 정수까지 1씩 증가시켜 출력하는 프로그램을 작성하되, 3의 배수인 경우는 출력하지 않도록 만들어보자
// 조건문이나 반복문의 코드블록 안에서 continue 가 실행되면, 반복 블록 안에 있는 나머지 부분을 실행하지 않고, 다음 반복 단계로 넘어간다

n = int(input())

for i in range(1, n+1): 
  if i%3==0: 
    continue        // 다음 반복 단계로 넘어간다
  print(i, end=' ') // i가 짝수가 아닐 때만 실행된다
