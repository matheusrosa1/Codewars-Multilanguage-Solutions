import operator

def basic_op(op, value1, value2):
    ops = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv
    }
    return ops[op](value1, value2)