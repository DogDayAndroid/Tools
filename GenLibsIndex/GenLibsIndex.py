import sys
import os

# 读取参数
prefix=sys.argv[1]
filePath=sys.argv[2]

print(prefix)

for filename in os.listdir(filePath):
    print(os.path.join(prefix,filename),"\\")