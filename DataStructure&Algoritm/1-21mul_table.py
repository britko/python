# 1~12까지 8을 건너뛰고 출력하기2

for i in range(1, 10):
    for j in range(1, 10):
        print(f'{i*j:3}', end=' ') # j:3 <- i와 j를 3자리로 출력하기 위해 :3을 사용
    print()