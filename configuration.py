# URL_SERVICE хранит базовый URL веб-сервиса, который используется для доступа к API или другим ресурсам.
# Значение должно быть скопировано из настроек или документации сервиса, к которому предоставляется доступ.
# Пример значения: "https://api.example.com"
URL_SERVICE = "https://dc9c1e40-1dcb-4931-afa4-dc51c14e31bd.serverhub.praktikum-services.ru"

# DOC_PATH содержит путь к документации веб-сервиса.
# Этот путь используется для формирования полного URL пути к документации, добавляя его к базовому URL сервиса.
# В результате получится что-то вроде "https://api.example.com/docs/"
DOC_PATH = "/docs/"

# CREATE_USER_PATH хранит путь к API-методу для создания нового пользователя.
# Этот путь будет использоваться для формирования полного URL-адреса в сочетании с базовым URL сервиса,
# когда необходимо выполнить запрос на создание пользователя.
CREATE_USER_PATH = "/api/v1/users/"

PRODUCTS_KITS_PATH = "/api/v1/products/kits/"