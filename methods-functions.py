##1.LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, but returns the greater if one or both numbers are odd

def less(a,b):
    if a%2 == 0 and b%2 ==0 :
        return min(a,b)
    else:
        return max(a,b)
print(less(2,4))
print(less(2,5))

##2. Write a function takes a two-word string and returns True if both words begin with same letter

def animals(text):
    wordlist = text.split()
    return wordlist[0][0] == wordlist[1][0]
print(animals('Levelheaded Llama'))
print(animals('Crazy Kangaroo'))

##3. Given two integers, return True if the sum of the integers is 20 or if one of the integers is 20. If not, return False

def makes_twenty(a,b):
    #if a==20 or b==20 or (a+b)==20:
    #    return True
    #else:
    #    return False
    return a==20 or b==20 or (a+b)==20
print(makes_twenty(5,5))
print(makes_twenty(20,5))
print(makes_twenty(15,5))

##Level 1

###1. Write a function that capitalizes the first and fourth letters of a name

def cap(name):
    if len(name) > 3:
        return name[:3].capitalize() + name[3:].capitalize()
    else:
        print('Name is too short')

print(cap('hacktoberfest'))

###2. Given a sentence, return a sentence with the words reversed

def master_yoda(text):
    return ' '.join(text.split()[::-1])

print(master_yoda("I am home"))

###3. Given an integer n, return True if n is within 10 of either 100 or 200

def almost(n):
    return ((abs(100-n) <= 10) or (abs(200-n) <= 10))

print(almost(150))
print(almost(104))
print(almost(100))

###Level 2

###1. Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

def has_33(nums):
    for i in range(0,len(nums)-1):
        if nums[i:i+2] == [3,3]:
            return True
    return False
print(has_33([1,2,3,3]))
print(has_33([1,2,3,1]))

###2. Given a string, return a string where for every character in the original there are three characters

def three(text):
    result = ''
    for char in text:
        result += char * 3
    return result
print(three("hacktoberfest"))

###3. Given three integers between 1 and 11, if their sum is less than or equal to 21, return their sum.
# If their sum exceeds 21 and there's an eleven, reduce the total sum by 10.
# Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'

def blackjack(a,b,c):
    if sum((a,b,c)) <= 21:
        return sum((a,b,c))
    elif sum((a,b,c)) <= 31 and 11 in ((a,b,c)):
        return a+b+c-10
    else:
        return 'BUST'
print(blackjack(5,6,7))
print(blackjack(9,9,11))
print(blackjack(9,9,9))

###4. SUMMER OF '69: Return the sum of the numbers in the array,
# except ignore sections of numbers starting with a 6 and extending to the next 9
# (every 6 will be followed by at least one 9). Return 0 for no numbers.

def summer_69(arr):
    total = 0
    add = True
    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break
    return total

print(summer_69([1,3,5]))
print(summer_69([1,3,5,6,7,8,9]))
print(summer_69([1,3,5,6,9,2,7]))

####CHALLENGING PROBLEMS¶

###1. Write a function that returns the number of prime numbers that exist up to and including a given number
def count_primes(num):
    prime = [2]
    x = 3
    if x < 2:
        return 0
    while x <= num:
        for y in prime:
            if x%y == 0:
                x += 2
                break
        else:
            prime.append(x)
            x += 2
    print(prime)
    return print(len(prime))
count_primes(100)

###2. Write a function that takes in a list of integers and returns True if it contains 007 in order
def spy_game(nums):
    code = [0,0,7,'x']
    for num in nums:
        if num == code[0]:
            code.pop(0)
    return  len(code) == 1

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,1,0,7,5]))
print(spy_game([1,2,4,0,7,5]))

### Write a function that takes in a single letter, and returns a 5x5 representation of that letter¶
def print_big(letter):
    pattern = {1:'  *  ',2:' * * ',3:'*   *',4:'*****',5:'**** ',6:'   * ',7:' *   ',8:'*   * ',9:'*    '}
    alpha = {'A':[1,2,4,3,3],'B':[5,3,5,3,5],'C':[4,9,9,9,4],'D':[5,3,3,3,5],'E':[4,9,4,9,4]}
    for patterns in alpha[letter.upper()]:
        print(pattern[patterns])
print_big('b')







