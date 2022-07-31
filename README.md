# Test app for Oracle Digital

## Настройка

Первое, что нужно сделать, это клонировать репозиторий:

```sh
$ git clone https://github.com/timur737/test_oracle.git
$ cd test_oracle
```
После этого зайти в ```school/school/```
и создать файл ```.env```. Пример файла ```.example_env```

## Запуск
На Docker с docker-compose: 
```sh
$ docker-compose up
```
Если в процессе создания контейнера при запуске ```python manage.py migrate``` пишет ```Connectin refused```
Еще раз запустите 
```sh
$ docker-compose up
```
И перейдите к `http://127.0.0.1:8000`.

## Алгоритм первых действий в Школьной системе
Вы как учитель регистрируетесь, авторизуетесь
и в начале нужно создать ```School```
потом ```Class```
и потом можно уже создавать ```Student```
Все кнопки для создания расположены в Navbar'e

