import requests

session = requests.Session()

session.get('https://gamejolt.com/')

lst = []

# deltarune
for i in range(1, 20):
    response = session.get(
        f'https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_aFilters[Generic_Category]=18736&_nPage={i}')
    lst += [i['_sName'] for i in response.json()['_aRecords']]
# for i in range(1, 20):
#     response = session.get(
#         f'https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_aFilters[Generic_Category]=4443&_nPage={i}')
#     print(response.status_code)
#     lst += [i['_sName'] for i in response.json()['_aRecords']]

# kristal
# for i in range(1, 4):
#     response = session.get(
#         f'https://gamebanana.com/apiv11/Mod/Index?_nPerpage=15&_aFilters%5BGeneric_Category%5D=16803&_nPage={i}')
#     print(response.status_code)
#     lst += ["kristal " + i['_sName'] for i in response.json()['_aRecords']]

lst = list(set(lst))

for i in lst:
    print(i)
print(len(lst))

with open('out/gamebanana_mods.txt', 'w') as f:
    for i in lst:
        f.write("gamebanana mod " + i + '\n')
