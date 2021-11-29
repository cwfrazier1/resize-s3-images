#!/usr/local/bin/python

import sys
import boto3

s3 = boto3.resource('s3')
s3bucket = s3.Bucket(sys.argv[1])
size = 0
totalCount = 0

for key in s3bucket.objects.filter(Prefix="2021/11/28-timelapse-1"):
    totalCount += 1
    size += key.size
    print(key.key)

print('total size:')
print("%.3f GB" % (size*1.0/1024/1024/1024))
print('total count:')
print(totalCount)
