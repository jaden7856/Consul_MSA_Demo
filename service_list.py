import requests
import consul

client = consul.Consul(host='localhost', port=8500)

serviceName = "tax-ms"
service_address = client.catalog.service(serviceName)[1][0]['ServiceAddress']
service_port = client.catalog.service(serviceName)[1][0]['ServicePort']

print(service_address)
print(service_port)

# request url
# response = requests.get("http://{}:{}".format(service_address, service_port))
# res = response.content.decode('utf-8')

# print(res)


