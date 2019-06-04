import time

def main():
    cubes={}
    i=0
    while True:
        cube=sorted(list(str(i**3)))
        if i not in cubes.keys():
            try:
                cubes[i]=cube
            except:
                print("Exception Occured!")

        if list(cubes.values()).count(cube)==5:
            result=(list(cubes.keys())[list(cubes.values()).index(cube)])
            break
        i+=1
    print(result**3)
    #print(cubes)

if __name__ == '__main__':
    start=time.perf_counter()
    main()
    print(f"Time Elapsed:{time.perf_counter()-start}")
