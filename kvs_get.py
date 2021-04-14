import consul

c = consul.Consul()

# poll a key for updates
# index = None
# while True:
#     index, data = c.kv.get('key1', index=index)
#     print(data['Value'])

data = c.kv.get('key1')
print(data[1]['Value'])