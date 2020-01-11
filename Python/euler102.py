import urllib3
import numpy,time

start = time.perf_counter()

filepath= "https://projecteuler.net/project/resources/p102_triangles.txt"

urllib3.disable_warnings()
http = urllib3.PoolManager()
r = http.request('GET', filepath)

matrix=list()
counter_var=0
for line in (r.data.split()):
    _curr= line.decode("utf-8")
    
    _list = [int(x) for x in _curr.split(',')]
    matrix.append(_list)
r.release_conn()
    
for each_cord_list in matrix:
    A1=numpy.array(each_cord_list[:2])
    B1=numpy.array(each_cord_list[2:4])
    C1=numpy.array(each_cord_list[4:])
    
    if numpy.cross(A1,B1)>0 and numpy.cross(A1,C1)<0 or numpy.cross(A1,B1)<0 and numpy.cross(A1,C1)>0:
        if numpy.cross(B1,A1)>0 and numpy.cross(B1,C1)<0 or numpy.cross(B1,A1)<0 and numpy.cross(B1,C1)>0:
            if numpy.cross(C1,A1)>0 and numpy.cross(C1,B1)<0 or numpy.cross(C1,A1)<0 and numpy.cross(C1,B1)>0:
                counter_var+=1
                
print(counter_var)

stop = time.perf_counter()

print(f"Time Elapsed: {stop-start}")