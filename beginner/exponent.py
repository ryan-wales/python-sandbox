def raise_to_power(base_num,pow_num):
    result = 1
    if pow_num > 0:
        for index in range(pow_num):
            result = result * base_num
        return result
    elif pow_num == 0:
        return result
    else:
        pow_num = pow_num * -1
        for index in range(pow_num):
            result = result / base_num
        return result        

print(raise_to_power(2,0))