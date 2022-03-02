
def dig_pow(num, p):
    sum_num = 0
    for i in str(num):
        sum_num = sum_num + pow(int(i), p)
        p += 1
 
    return int(sum_num/num) if (sum_num % num) == 0 else -1

        