
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/000000000008830b

alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# ref : https://stackoverflow.com/questions/1801391/what-is-the-best-algorithm-for-checking-if-a-number-is-prime
def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False
        i += w
        w = 6 - w

    return True


# def createAlphabetPrimeList(prime_high):
#     current_num = prime_high
#     alphabet_primes = [0 for x in range(0, len(alphabet))]
#     next_index = len(alphabet) - 1
#     while (next_index >= 0 and current_num > 1):
#         if isprime(current_num): # and current_num % 2 == 1
#             alphabet_primes[next_index] = current_num
#             next_index -= 1
#         current_num -= 1
#     return alphabet_primes

def getAllPossiblePrimes(prime_high):
    result = []
    current_num = prime_high
    while (current_num > 1):
        if isprime(current_num):
            result.append(current_num)
        current_num -= 1
    return result
    

def getCharIndex(char):
    return alphabet.index(char)


def doTest(test_no, prime_high, input_num_arr):
    possible_prime_list = getAllPossiblePrimes(prime_high)
    primes_found = []
    for num_a in possible_prime_list:
        for num_b in possible_prime_list:
            val = num_a * num_b
            if val in input_num_arr:
                # match found, add to found primes
                if num_a not in primes_found:
                    # print("adding " + str(num_a) + " to prime list")
                    primes_found.append(num_a)
                if num_b not in primes_found:
                    # print("adding " + str(num_b) + " to prime list")
                    primes_found.append(num_b)
    # print(len(primes_found))
    sorted_primes = sorted(primes_found, key=int, reverse=False)
    answer = ""
    last_prime = 0
    first_val = False
    for idx_a in range(0, len(sorted_primes)):
        num_a = sorted_primes[idx_a]
        for idx_b in range(0, len(sorted_primes)):
            num_b = sorted_primes[idx_b]
            if num_a * num_b == input_num_arr[0]:
                answer += alphabet[idx_a]
                answer += alphabet[idx_b]
                last_prime = num_b
                first_val = True
                break
        if first_val:
            break 
    # decrypt the rest of the input
    for input_idx in range(1, len(input_num_arr)):
        input_num = input_num_arr[input_idx]
        for idx_b in range(0, len(sorted_primes)):
            num_b = sorted_primes[idx_b]
            if last_prime * num_b == input_num:
                answer += alphabet[idx_b]
                last_prime = num_b
                break
    print("Case #" + str(test_no) + ": " + answer)

# ---- START OF TEST ----
# row_1 = "103 31"
# row_2 = "217 1891 4819 2291 2987 3811 1739 2491 4717 445 65 1079 8383 5353 901 187 649 1003 697 3239 7663 291 123 779 1007 3551 1943 2117 1679 989 3053"
# row_1 = "10000 25"
# row_2 = "3292937 175597 18779 50429 375469 1651121 2102 3722 2376497 611683 489059 2328901 3150061 829981 421301 76409 38477 291931 730241 959821 1664197 3057407 4267589 4729181 5335543"
# row_1_parts = row_1.split(' ')
# row_2_parts = row_2.split(' ')
# prime_high = int(row_1_parts[0])
# input_num_arr = [int(x) for x in row_2_parts]
# doTest(1, prime_high, input_num_arr)
row_1 = input()
num_of_tests = int(row_1)
for test_no in range(1, num_of_tests + 1):
    test_row_1 = input()
    test_row_2 = input()
    row_1_parts = test_row_1.split(' ')
    row_2_parts = test_row_2.split(' ')
    prime_high = int(row_1_parts[0])
    input_num_arr = [int(x) for x in row_2_parts]
    doTest(test_no, prime_high, input_num_arr)