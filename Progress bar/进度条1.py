#进度条1
import time
for i in range(1,101):
    print('\r'+'▋'*i+'当前进度：{}%'.format(i),end='')
    time.sleep(0.3)