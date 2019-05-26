import time

def dynamic(sum_of_money, index_of_coin): 
    if index_of_coin < 0:
        return 0
    if index_of_coin == 0 or sum_of_money == 0:
        return 1
    if mat_list[sum_of_money][index_of_coin] > 0:
        return mat_list[sum_of_money][index_of_coin]
    if coin_list[index_of_coin] > sum_of_money:
        return dynamic(sum_of_money, index_of_coin - 1)
    mat_list[sum_of_money][index_of_coin] = dynamic(sum_of_money, index_of_coin-1)+ \
                                     dynamic(sum_of_money-coin_list[index_of_coin],index_of_coin)
    return mat_list[sum_of_money][index_of_coin]


start = time.clock()
coin_list = [1,2,5,10,20,50,100,200]
mat_list=[[0,0,0,0,0,0,0,0] for i in range(201)]
print(dynamic(200,7)) 
time_ = time.clock()-start
print(f"Result found in {time_} seconds")