## Quiz API service

Quiz API service made with Django Framework.


### Setup

- To access admin page create a superuser: `make superuser`
- To enable sending emails rename `.env.example` to `.env` and set correct values for:
```
    EMAIL_HOST=smtp.gmail.com
    EMAIL_HOST_USER=YourEmail@address
    EMAIL_HOST_PASSWORD=YourAppPassword
```

- Ways to serve this api:
1. `docker-compose up`
2. `make install && make run`
3. `pip install -r requirements.txt && python manage.py runserver`


### Documentation

- Once you run the API, Swagger docs are provided at `/docs` (PS: don't forget to authenticate once inside docs)
