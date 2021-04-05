#进度条2
import time
start=time.perf_counter()
for i in range(1,101):
    a='*'*i
    b='.'*(100-i)
    c=i
    dur=time.perf_counter()-start
    print('\r{}{}当前进度：{}%，用时{:.2f}s'.format(a,b,c,dur),end='')
    time.sleep(0.3)