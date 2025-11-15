## Проект по django "Запись на тестдрайв"

### РУКОВОДСТВО ПОЛЬЗОВАТЕЛЯ
Проект представляет собой сайт из 3 страниц с функцией записи на тестдрайв.
На главной странице отображаются активные записи клиентов.

<img width="343" height="231" alt="image" src="https://github.com/user-attachments/assets/c578a4d8-dc54-455d-ac71-f45558fc110c" />

Страница "О компании" содержит описание деятельности компании

<img width="617" height="302" alt="image" src="https://github.com/user-attachments/assets/57f6df73-fd36-4db5-aa66-b5de6980a990" />

Для записи на тестдрайв нужно перейти на страницу "Тестдрайв" с формой записи

<img width="395" height="294" alt="image" src="https://github.com/user-attachments/assets/2fc87781-7fda-44a4-bbbc-06d531557fc0" />

После заполнения формы и её отправки новая запись появитя на главной страницы

### РУКОВОДСТВО ПРОГРАММИСТА
>Django — бесплатный высокоуровневый фреймворк для веб-приложений на языке Python с открытым исходным кодом. Цель — помочь разработчикам быстро и безопасно создавать серверную часть сайтов.
Начало работы со средой:
```
# создаём виртуальную среду
python -m venv .venv
# активируем виртуальную среду
.venv\Scripts\activate
# устанавливаю библиотеку
pip install django==5
# создаю проект
django-admin startproject testdrive
# перехожу в папку проекта
cd testdrive
# создаю приложение
python manage.py startapp app
# перейдите в файл settings.py и в разделе INSTALLED_APPS впишите "app"
# папускаю проект
python manage.py runserver
```
