class DivisionByZeroError(Exception):
    pass


try:
    1/0
except ArithmeticError:
    print('ArithmeticError')
except DivisionByZeroError:
    print('DivisionByZero')
except Exception:
    print('Exception')
