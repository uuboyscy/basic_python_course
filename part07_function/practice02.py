"""
Assume there exists a series 1, 1, 1, 2, 3, 4, 6, 9, 13, 19, 28, 41, 60, 88, 129
Define a one-row-function func(n) that denote the series
Where:
    n: int >= 0
    func(0)  -> 1
    func(1)  -> 1
    func(2)  -> 1
    func(3)  -> 2
    func(4)  -> 3
    func(5)  -> 4
    func(6)  -> 6
    func(7)  -> 9
    func(8)  -> 13
    func(9)  -> 19
    func(10) -> 28
    func(11) -> 41
    func(12) -> 60
    func(13) -> 88
    func(14) -> 129
"""

def func(n):
    return 1 if n < 3 else Func(n-1) + Func(n-3)

if __name__ == '__main__':
    for i in range(0, 16):
        print(Func(i))
