import time
import math

filepath="euler99.txt"
list_=[]
expoList=[]


def extract_data_from_file():
    fline=open(filepath).readlines()
    for x in range(len(fline)):
        val_list=(fline[x].split("\n")[0]).split(",")
        list_.append(list(map(lambda x: int(x),val_list)))
    return (list_)

def calculate_power(base, power):
    '''
        2**3=3*log10(2)

    '''    

    # result = 1
    # while power > 0:

    #     if power % 2 == 1:
    #         power=power-1
    #         result = (result * base)
    #     else:
    #         power=power//2
    #         base=base*base

    #     power = power // 2
    #     base = (base * base) 

    return power*math.log10(base)


def main():
    max_res=0
    final_data=extract_data_from_file()
    for x in range(len(final_data)):
        res_=calculate_power(final_data[x][0],final_data[x][1])
        expoList.append(res_)
    print(expoList.index(max(expoList))+1)


if __name__ == '__main__':
    start=time.process_time()
    main()
    end=time.process_time()
    print(f"Time taken: {end-start} ms")
