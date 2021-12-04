
from collections import Counter
from typing import List

TEST = """
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010"""


def input_parser(s:str) -> List:
    s = s.strip().split("\n")
    s = [list(i) for i in s]
    s = [list(map(int,j)) for j in s]
    s = list(zip(*s))
    return s

def binary_decrypter(l:List) -> float:
    max_list = [Counter(i).most_common(1)[0][0] for i in l]
    max_list = [str(i) for i in max_list]
    max_list = "".join(max_list)

    min_list = [Counter(i).most_common(2)[1][0] for i in l]
    min_list = [str(i) for i in min_list]
    min_list = "".join(min_list)

    return int(max_list,2),int(min_list,2)

binary_decrypter(input_parser(TEST)) == 22,9


if __name__ == "__main__":
    INPUT = open("day3_BinaryDiagnostic_input.txt").read()

    gamma, epsilon = binary_decrypter(input_parser(INPUT))

    print(gamma * epsilon)

    