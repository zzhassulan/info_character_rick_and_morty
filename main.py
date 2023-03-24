#    Работа с ошибками try  и except
# 12

# try:
#     with open('image/a.txt' , 'r') as f:
#         f.read()
        
# except FileNotFoundError:
#     os.mkdir('image')
#     os.system('touch image/a.txt')
#     with open('image/a.txt', 'r') as f:
#         f.read
# else:
#     print('все было окей')

# def my_function(name, age = 10):




import requests



def get_url(id):
    url = f'https://rickandmortyapi.com/api/character/{id}'

    responce = requests.get(url = url)
    data = responce.json()

    return data
# pprint(get_url(25))

def get_location(id):
    character = get_url(id)
    for i in character.keys():
        if i == 'location':
            name_lacation = character['location']['name']
            url_location = character['location']['url']
            if url_location not in '':
                location_responce = requests.get(url_location)
                data = location_responce.json()
                
                info = f"""названия локаций: {name_lacation}
тип локаций: {data['type']}
измерение локаций: {data['dimension']}
дата создания локаций: {data['created']}
"""
                return info
            else:
                info = f"""
названия локаций: {name_lacation}
тип локаций: Unknown
измерение локаций: Unknown
дата создания локаций: Unknown
"""
                return info
#     return data        
# print(get_location(19))

def get_character(id):
    if id <= 826:
        character = get_url(id)
        info = f"""
номер персонажа: {character['id']}
имя персонажа: {character['name']}
пол персонажа: {character['gender']}
раса персонажа: {character['species']}
жизненная линия: {character['status']}
личность: {character['type']}
дата создание: {character['created']}

{get_location(id)}"""
        
        return info
    else:
        return 'не правильный id персонажа'
    

id_charaters = int(input('номер персонажа: '))

print(get_character(id_charaters))