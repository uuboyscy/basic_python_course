# 自訂例外
class CustomException(Exception):
    pass

class LengthError(Exception):
    def __init__(self, value):
        self.value = value
    def __repr__(self):
        return self.value

def rectangleArea(length, width):
    print('length =', length, 'width =', width)
    if length < 0 or width < 0:
        raise CustomException('Custom Exception.')
    elif length < width:
        raise LengthError('Length should be greater than or equal to width.')
    else:
        return length * width

if __name__ == '__main__':
    try:
        rectangleArea(1, -1)
    except CustomException as e:
        print(e)

    try:
        rectangleArea(1, 3)
    except LengthError as e:
        print(e)
