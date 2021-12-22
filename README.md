# Обрезка ссылок при помощи битли

### Описание

Программа принимает обязятаельный арунмент в виде url адреса и возвращает сокращенную ссылку используя сервис [Битли](https://app.bitly.com/Blc58Dqv93o/bitlinks/33kiQfx).
Если передать уже сокращенную ссылку, то вернется число переходов по ней.

### Как установить

Python должен быть установлен.
Затем используйте `pip` (или `pip3` если есть конфликт с Python2) для установки зависимостей.
```
pip install -r requirements.txt
```

Рекомендутся использовать вирутальное окружение [vurtualenv/venv]('https://virtualenv.pypa.io/en/stable/') для изоляции проекта.

### Перменные окружения

Для доступа к серису Битли необходим токен авторизации, который можно получить в своем аккаунте по [ссылке]('https://app.bitly.com/settings/api/'). В программе токен используется в переменной auth_token.
После получения токена, создайте в корневой директории файл с перменными окружения .env и добавьте ваш токен в формате:
```
AUTH_TOKEN=<ващ_токен>
```

### Цель проекта

Код написан в образовательных целях для проекта [devman]('https://dvmn.org/').