import os, requests, time
from md5checker import make_hash

os.system('cls')
print("██████████████████████████████████████████")
print(" delta Driver Code MD5 Validation Service")
print("██████████████████████████████████████████")
time.sleep(1)

print(make_hash('bleading_edge.py', algo='md5'))