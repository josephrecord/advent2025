import re


def invalid(num) -> bool:
    st = str(num)
    l = len(st)
    if l % 2 != 0:
        return False
    mp = l // 2
    if st[:mp] == st[mp:]:
        return True
    return False


def sum_invalid(start, stop) -> int:
    total = 0
    for num in range(start, stop + 1):
        if invalid(num):
            total += num
    return total


s = 0

with open(r"/workspaces/codespaces-jupyter/data/input.txt") as f:
    line = f.readline().strip().split(",")


ex = [
    "11-22",
    "95-115",
    "998-1012",
    "1188511880-1188511890",
    "222220-222224",
    "1698522-1698528",
    "446443-446449",
    "38593856-38593862",
    "565653-565659",
    "824824821-824824827",
    "2121212118-2121212124",
]


for elem in line:
    mo = re.search(r"(\d+)-(\d+)", elem)
    start, stop = int(mo.group(1)), int(mo.group(2))
    s += sum_invalid(start, stop)

print(s)
