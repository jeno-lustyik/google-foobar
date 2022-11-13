import base64
import getpass

message = """
F1IAARoKDl0ZQk5VTFIUBhwIHwlGRUkMAxkfERgOHktNRVRPSxAAABwMBksOQkJPSxAVEhYbH11N
RVRPSxwdFwsMD0cICQtIQFVUFRoBAkscAAMKAgFUVENJTFsECQEMBxAXU1VJTFwLBwwGGAZUVENJ
TF0LAwtIQFVUEhYGTA5QRUkYBRtSUwQ=
"""

key = 'lustyik.jeno'
result = []
for i, c in enumerate(base64.b64decode(message)):
    result.append(chr(ord(c) ^ ord(key[i % len(key)])))

print ''.join(result)