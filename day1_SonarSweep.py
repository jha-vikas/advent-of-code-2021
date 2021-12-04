import os

TEST = """199
200
208
210
200
207
240
269
260
263
"""

def incr_counter(l:list) -> int:
    count = 0
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            count += 1
    return count


def incr_counter2(l:list) -> int:
    count = 0
    for i in range(len(l)-3):
        if l[i] < l[i+3]:
            count += 1
    return count



TEST_LIST = str.split(TEST.strip(), "\n")
TEST_LIST = [int(i) for i in TEST_LIST]

assert(incr_counter(TEST_LIST)) == 7

assert(incr_counter2(TEST_LIST)) == 5

if __name__ == "__main__":
    with open("day1_SonarSweep_input.txt") as f:
        INPUT = f.read()
    
    INPUT = str.split(INPUT.strip(), "\n")
    INPUT = [int(i) for i in INPUT]
    print(incr_counter(INPUT))
    print(incr_counter2(INPUT))