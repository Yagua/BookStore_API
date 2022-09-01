## Bookstore REST API

Bookstore RESTFull API built with Django

#### Main Dependencies

- Django
- Django Rest Framework
- Elasticsearch
- Djoser
- JWT
- Mariadb

#### Run Project

The project can be easily run using project's Docker files (docker must be
installed)

```bash
# in the root project directory
$ docker-compose up --rebuild
```

- Once the containers are running, the django app will be available on
  `[::]:8000` - `(http://0.0.0.0:8000)`
- Elasticsearch service will be available on port `9200`
- Mariadb service will be available on port `5200`

### TODOS

- Write tests for all components in the apps
- Consider implementing signals to create profile and shoopping carts in user
  objects
