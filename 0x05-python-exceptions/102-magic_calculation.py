#!/usr/bin/python3
import dis
def magic_calculation(a, b):
    result = 0
    for i in range(1, 3):
        try:
            if a > i:
                raise Exception("Too far")
            else:
                result += a ** b / i
        except:
            result = a + b
            break
    return result


print(magic_calculation(1, 20))
# dis.dis(magic_calculation)
