import os
import time
for i in range(10):
  if os.path.exists('env.txt'): print(open('env.txt').read()); break
  time.sleep(2)