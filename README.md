# Doc_filler
## Description
Doc filler is a simple web-application that allows to fill prepared .docx templates with values defined in .xlsx table.  
It allows to create a lot of similar documents without copy-pasting different fields (e.g. name field).  
[If you'd like to look at deployed app without deploying it by yourself, please contact me.](https://t.me/isbushcar)
## Local deployment (requires Docker and Docker-compose)
1. Clone repository: `git clone https://github.com/isbushcar/doc_filler.git`
2. Go to directory python-project-lvl4 `cd doc_filler`
3. Create .env file and define there a few variables (example below, DEBUG is optional):
```
POSTGRES_DB=example 
POSTGRES_USER=example
POSTGRES_PASSWORD=example
STATIC_ROOT=root
DJANGO_SECRET_KEY=example
DEBUG=True
```
4. Start the containers with `docker-compose up`
### Notes
This guide doesn't affect some important aspects of development and deployment
such as using Django secret key and other environment variables, setting up databases and so on.
In case you are going to use this app in production, please read the [official docs.](https://docs.djangoproject.com/)

Sorry, the only available language in project is Russian for now. I'm planning to add English soon.

Small roadmap:
1. Прикрутить API
2. Бот для телеги, который ходит по апи?
3. Добавить проверку на владельца документа
4. Сделать перевод
5. Сделать кастомные ошибки у формы