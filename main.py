list_str = []


def foo2(num_start=None, num=None, num_list=''):
    if num_start:
        num = num_start.pop(0)
        if num_list:
            foo2(num_start.copy(), num, f"{num_list}+{num}")
            foo2(num_start.copy(), num, f"{num_list}-{num}")
            foo2(num_start.copy(), num, f"{num_list}{num}")
        else:
            foo2(num_start.copy(), num, f"{num}")
    else:
        return list_str.append(num_list)


def foo3(list_sum_num, result_sum):
    for sum_num_str in list_sum_num:
        sum_num_int = 0
        for val in ("+"+sum_num_str).replace('+', ' +').replace('-', ' -').split():
            if val[0] == '+':
                sum_num_int += int(val[1:])
            else:
                sum_num_int -= int(val[1:])
        if sum_num_int == result_sum:
           print(f"{sum_num_str}={sum_num_int}")


if __name__ == "__main__":
    foo2([9, 8, 7, 6, 5, 4, 3, 2, 1, 0])
    foo3(list_str, 200)
