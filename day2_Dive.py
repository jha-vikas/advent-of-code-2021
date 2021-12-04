from typing import List

TEST = """forward 5
down 5
forward 8
up 3
down 8
forward 2"""

TEST = TEST.strip().split("\n")

def final_position(l: list) -> List[int]:
    h = 0
    d = 0
    for i in l:
        dir, val = i.split()
        val = int(val)
        if dir == "down":
            d += val
        elif dir == "up":
            d -= val
        elif dir == "forward":
            h += val
    
    return h, d


def final_position2(l: list) -> List[int]:
    h = 0
    d = 0
    aim = 0
    for i in l:
        dir, val = i.split()
        val = int(val)
        if dir == "down":
            aim += val
        elif dir == "up":
            aim -= val
        elif dir == "forward":
            h += val
            d += aim*val
    
    return h, d


if __name__ == "__main__":
    h,d = final_position(TEST)
    print(h*d)

    h2,d2 = final_position2(TEST)
    print(h2*d2)


    with open("day2_Dive_input.txt") as f:
        INPUT = f.read().strip()
    
    INPUT = INPUT.split("\n")

    h,d = final_position(INPUT)
    print(h*d)

    h2,d2 = final_position2(INPUT)
    print(h2*d2)