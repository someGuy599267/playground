import requests

session = requests.Session()

session.get('https://gamejolt.com/')


# deltarune
for i in range(1, 20):
    response = session.get(
        f'https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_aFilters[Generic_Category]=18736&_nPage={i}')
    for m in response.json()['_aRecords']:
        print(m['_sName'])
        print(m)
print('*'*10)
for i in range(1, 20):
    response = session.get(
        f'https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_aFilters[Generic_Category]=4443&_nPage={i}')
    for m in response.json()['_aRecords']:
        print(m['_sName'])
        print(m)

print('*'*10)
# kristal
for i in range(1, 20):
    response = session.get(
        f'https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_aFilters%5BGeneric_Category%5D=16803&_nPage={i}')
    print(response.status_code)
    for m in response.json()['_aRecords']:
        print(m['_sName'])
        print(m)