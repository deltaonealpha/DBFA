import time
time.sleep(2)
import pyAesCrypt
bufferSize = 64 * 1024
password = "root"
# encrypt
pyAesCrypt.encryptFile("hms1.py", "hms1.py.aes", password, bufferSize)
time.sleep(0.5)
print("encrypted s")
time.sleep(0.5)
exit()