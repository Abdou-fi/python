string1 = "Hello, world! 你好，世界！"
b = string1.encode("utf-8")
print(b)
# Output: b'Hello, world! \\xe4\\xbd\\xa0\\xe5\\xa5\\xbd\\xef\\xbc\\x8c\\xe4\\xb8\\x96\\xe7\\x95\\x8c\\xef\\xbc\\x81'
s_decoded = b.decode("utf-8")
print(s_decoded)