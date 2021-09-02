# 다이나믹 프로그래밍 (동적 계획법)
# 메모리를 적절히 사용하여 수행 시간 효율성을 향상
# 이미 계산된 결과는 별도의 메모리에 저장하여 다시 계산하지 않도록 한다.
# 최적 부분 구조
#   - 큰 문제를 작은 문제로 나눌 수 있으며, 작은 문제 답을 모아 큰 문제를 해결
# 중복 되는 부분 문제
#   - 동일한 작은 문제를 반복적으로 해결
# 상향식과 하향식 방법으로 구현 가능
# 하향식 - 메모이제이션 (탑다운)
#   - 한번 계산한 결과를 메모리 공간에 메모 (캐싱)
#   - 재귀 사용
# 상향식 - 보텀업
#   - 아래에서 해결하면서 올라옴
#   - 반복문 사용

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

# 탑다운
d = [0] * 100 # 캐싱용 배열

def fibo_topdown(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = n(x - 1) + fibo_topdown(x - 2)
    return d[x]

# 보텀업
d = [0] * 100
d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]
print(d[n])

print(fibo(10))