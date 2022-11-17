# picture_service
Запуск
-----
    docker build . -t postgres-01
    docker run -e POSTGRES_PASSWORD=password -d -p 5432:5432 postgres-01:latest
    pip install -r requirements.txt
    python main.py


для эндпоинта /image пихаем байтики в поле image, а наименование картинки в поле image_name

p.s. Чет не 1,5 часа задача заняла. Ковырялся всю ночь. Сделал чтоб работало.