# как поднять и сбилдить проект 
</br>
sudo docker-compose up --build 
</br>
http://0.0.0.0:8000/auth/users/ (post) регистрация, key: username, password, email
</br>
http://0.0.0.0:8000/auth/jwt/create/ (post) key: username, password. Получить токен
</br>
http://0.0.0.0:8000/api/todo/all-tasks (get) по токену вывести все задачи
</br>
http://0.0.0.0:8000/api/todo/task/id (put) по токену изменить задачи
</br>
http://0.0.0.0:8000/api/todo/profile/id (put) по токену изменить профиль
