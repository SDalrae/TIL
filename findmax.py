# 주어진 숫자 n개 중 가장 큰 숫자 찾기.
def max_num(num_list):
    big_num = num_list[0]
    for i in range(1, len(num_list)):
        if big_num < num_list[i]:
            big_num = num_list[i]
        else:
            big_num = big_num
    return big_num


# 리스트에 숫자가 n개 있을 떄, 가장 큰 값이 있는 인덱스를 돌려주기.
def max_num_index(num_list):
    big_num = num_list[0]
    big_num_index = 0
    for i in range(1, len(num_list)):
        if big_num < num_list[i]:
            big_num = num_list[i]
            big_num_index = i
        else:
            big_num = big_num
    return big_num_index


# 주어진 숫자 n개 중 가장 작은 숫자 찾기.
def min_num(num_list):
    small_num = num_list[0]
    for i in range(1, len(num_list)):
        if small_num > num_list[i]:
            small_num = num_list[i]
        else:
            small_num = small_num
    return small_num
