s = '你好,python'
#encode对字符串编码,转二
res = s.encode()
print(res)
ss = b'\xe4\xbd\xa0\xe5\xa5\xbd,python'
#decode解码,转字符串
print(ss.decode())