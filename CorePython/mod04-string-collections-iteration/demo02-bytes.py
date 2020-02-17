print(b'data')
d = b'some bytes'
print(d)
print(d[0])
print(d.split())

my_string = "Hello world from test"
my_bytes = my_string.encode('utf8')
print(my_string)
print(my_bytes)
my_new_string = my_bytes.decode('utf8')
print(my_new_string)
