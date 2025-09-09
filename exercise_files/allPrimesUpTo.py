def allPrimesUpTo(num):
    primes = [2]

# this code fails for num of 3 - the for loop is never entered
# fixed by adding +1 to the for; otherwise the in range will go up to, but not include the num
    print(f'number: {num}')
    for number in range(3,num+1):
        print(f'in for loop: {number}')
        sqrtNum = number ** 0.5
        print(f'{sqrtNum} is the square root of {number}')
        for factor in primes:
            if number % factor == 0:
                print(f'{number} is not prime, break')
                # not prime
                break
            if factor > sqrtNum:
                print(f'{number} is prime, add to primes, break')
                # it is prime!
                primes.append(number)
                break
        print(f'out of ifs for number: {number}')
    return primes
        # for factor in range(2, int(number ** 0.5) + 1):
        #     if number % factor == 0:
        #         break
        # else:
        #     print(f'{number} is prime!')


print(allPrimesUpTo(2))
print(allPrimesUpTo(3))
print(allPrimesUpTo(10))
print(allPrimesUpTo(100))
