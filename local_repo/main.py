import os
import time
for i in range(10):
  if os.path.exists('out.txt'):
    print('FLAG_FILE_FOUND')
    with open('out.txt', 'r') as f: print(f.read())
    break
  time.sleep(1)