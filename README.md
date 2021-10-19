# поднять и сбилдить проект 
sudo docker-compose up --build 
http://0.0.0.0:8000/auth/users/ (post) регистрация, key: username, password, email
http://0.0.0.0:8000/auth/jwt/create/ (post) key: username, password
http://0.0.0.0:8000/api/todo/all-tasks (get) по токену вывести все задачи
http://0.0.0.0:8000/api/todo/task/id (put) по токену изменить задачи
http://0.0.0.0:8000/api/todo/profile/id (put) по токену изменить профиль
