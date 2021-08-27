# 그리디 알고리즘 (탐욕법)
# 현재 상황에서 지금 당장 좋은것만 고르는 방법
# 문제를 풀기 위한 최소한의 아이디어를 떠올릴 수 있는 능력을 요구
# 그리디 해법은 정당성 분석이 중요하다.
#   - 단순히 좋아 보이는 것을 반복적으로 선택해도 최적의 해를 구할 수 있는지 검토

# 거스름 돈 문제
n = 1260
count = 0
array = [500, 100, 50, 10]

for coin in array:
    count += n // coin
    n %= coin

print(count)