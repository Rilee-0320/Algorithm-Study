# 제한사항
# numbers는 길이 1 이상 7 이하인 문자열입니다.
# numbers는 0~9까지 숫자만으로 이루어져 있습니다.
# "013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.

from itertools import permutations
# https://docs.python.org/3/library/itertools.html#itertools.permutations

def solution(numbers): # O((n! + (n-1)! + ... + 1!)*(x^(1/2)))
    arr = {False}
    # 가능한 모든 순열을 생성한다.
    for i in range(1, len(numbers)+1): # O(n! + (n-1)! + ... + 1!),  n = len(numbers)
        # 각 순열을 생성하고, 소수인지 판별한다.
        arr.update(isPrime(''.join(x)) for x in permutations(numbers, i))
    
    # 집합의 크기를 return 한다.(False를 제외하므로 -1)
    return len(arr) - 1

# isPrime(x) : 소수판별기 O(x^(1/2))
# 주어진 숫자(x)가 소수인 경우 x를 return 하고, 소수가 아닌 경우 False을 return 한다.
def isPrime(x): # O(x^(1/2))
    x = int(x)
    # 10 이하의 수는 바로 소수 여부를 판별한다.
    if x in [0, 1, 4, 6, 8, 9]:
        return False
    if x in [2, 3, 5, 7]:
        return x
    
    # 주어진 숫자(x)를 2부터 제곱근까지의 모든 정수로 나누어 본다.
    for i in range(2, int(x**(1/2))+1):
        if not x%i:
            return False
    return x

# permutations(string, n) : 순열생성기
# 주어진 문자열(string) 에서 크기 n의 순열을 생성한다.