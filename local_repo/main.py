import os
import time
for i in range(10):
  print(f'CHECK_{i}_out.txt')
  if os.path.exists('out.txt'):
    print('FLAG_FILE_FOUND')
    with open('out.txt', 'r') as f: print(f.read())
    break
  else:
    print('NOT_FOUND')
    os.system('ls -la')
  time.sleep(2)