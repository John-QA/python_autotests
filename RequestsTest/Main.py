import requests

base_url = 'https://api.pokemonbattle.ru/v2'##Основной URL.
token = 'trainer_token' ##Ввести свой токен.
base_header = {'Content-Type':'application/json', 'trainer_token':token} ##Базовые заголовки.

body_create_new_pock = {
    "name": "generate",
    "photo_id": 10
}##JSON-запроса на создание нового покемона со случайным именем и фотографией с id = 10.
response_create_new_pok = requests.post(url = f'{base_url}/pokemons', headers = base_header,json=body_create_new_pock).json()##отправка запроса на создание нового.
print(response_create_new_pok)##Выведение ответа.

##Далее идёт проверка факта создания покемона.
if response_create_new_pok["message"]=="Покемон создан": ##проверка, что в ответе с ключом massage пришло сообщение о создании покмона. 
    pokemon_id = response_create_new_pok["id"] ##присвоить перменной, над которой будут проводитя дальнейшие действия id созданного покемона.
    photo_id = 10 ##Если покемон был создан - дальнейшие действия производятся с ним.
else:##Иначе - действия выполняются над первым покемон вне покебола из списка тренера.
    response_my_info = requests.get(url = f'{base_url}/me', headers = base_header).json()##полуение информации о тренере с указанным токеном.
    ##Из полученной в ответе информации уже можно распарсить необходимые данные, однако формат их представления усложняет отсеивание покемонов в покеболе.
    ##Для получения экземпляра данного покемона воспользуемся инструментарием API.
    trainer_id=response_my_info["data"][0]["id"]##присвоение ID тренера переменной.
    res_list_pok_without_pokeball=requests.get(url = f'{base_url}/pokemons', params= {'trainer_id':trainer_id,'status':"1",'in_pokeball':"0"}).json()
    ##Запрос на выдачу списка живых покемонов вне покебола, принадлежащих тренеру.
    pokemon_id=res_list_pok_without_pokeball["data"][0]["id"]##Присвоение переменной id первого живого покемона вне покебола.
    photo_id=res_list_pok_without_pokeball["data"][0]["photo_id"]##Присвоение переменной id фото первого живого покемона вне покебола.

body_update_name = {
    "pokemon_id": pokemon_id,
    "name": "New Name",
    "photo_id": photo_id
}##JSON-запроса на обновление имени. С учетом того, что в задаче указано обновиться через метод PUT, а не PATCH, все поля - обязательные. 

response_update_name = requests.put(url = f'{base_url}/pokemons', headers = base_header,json=body_update_name) ##Отправка запроса на изменение имени.
print(response_update_name.text)##Выведение ответа.

responseAddPokeball = requests.post(url = f'{base_url}/trainers/add_pokeball', headers = base_header,json={"pokemon_id": pokemon_id})
##Отправка запроса на добавление в покебол.
print(responseAddPokeball.text)##Выведение ответа.

response_delete_pokeball = requests.put(url = f'{base_url}/trainers/delete_pokeball', headers = base_header,json={"pokemon_id": pokemon_id})
##Вспомогательный запрос на изъятие покемона из покебола (для исключения участия в битве).