def solution(n):
    numbers = []

    i = 9
    while i > 1:
        if (n/i).is_integer():
            numbers.append(i) 
            n //= i
        else:
            i -= 1
            
    if n != 1:
        print("The desired number q does not exist!")
        return -1
    
    multiple = 1
    result = 0
    for num in numbers:
        result += num * multiple
        multiple *= 10

    return result
    

            

print(solution(81))
