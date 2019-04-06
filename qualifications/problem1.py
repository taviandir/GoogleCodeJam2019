

# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231


def doTest(test_no, input_num, input_str):
    num_1 = 0
    num_2 = input_num
    for idx in range(0, len(input_str)):
        ch_num = int(input_str[idx])
        if ch_num == 4:
            idx_from_right = len(input_str) - idx - 1
            modifier = pow(10, idx_from_right)
            num_1 += modifier
            num_2 -= modifier
    print("Case #" + str(test_no) + ": " + str(num_1) + " " + str(num_2))
    
# ---- START OF TEST ----
row_1 = input()
num_of_tests = int(row_1)
for idx in range(1, num_of_tests + 1):
    test_row_input = input()
    test_number = int(test_row_input)
    doTest(idx, test_number, test_row_input)
