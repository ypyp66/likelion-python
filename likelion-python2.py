# is_prime 함수는 특정 숫자(n)이 들어왔을 때 
# 그 숫자가 소수면 True를 반환하고 아니면 False를 반환하는 함수입니다.
def is_prime(n):
    c=0
    for i in range(1, n+1):
        if n % i == 0:
            c+=1
    if c==2:
        return True
    else:
        return False

# prime_number_list 함수는 길이(length)가 들어왔을 때
# 그 길이만큼의 소수를 가지고 있는 리스트를 반환하는 함수입니다.
def prime_number_list(length):
    result = []
    i=2
    while (len(result) <= length-1):
        check = is_prime(i)
        if check==True:
            result.append(i)
        i+=1
    return result

length = int(input('Length? '))
print(prime_number_list(length))
