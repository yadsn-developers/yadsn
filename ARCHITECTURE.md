# YADSN ARCHITECTURE

### Architecture layers

- Views
    - HTTP input / output only.
- Forms
    - Data validation only (all fields are defined, all fields are valid types).
- Models
    - Business logic layer.
- Database models
    - Dry Django ORM (models definition only).
- Services
    - Third party integration modules (Codecha, Facebook, Gmail, GitHub, StackOverflow clients...)

### Architecture layers interaction

- Views
    - Can talk to:
        - Forms (for pre-validating / filtering HTTP input data).
        - Models (for providing some functionality).
- Forms:
    - Can talk to:
        - Nobody.
- Models:
    - Can talk to:
        - Database models of current application (for data persistence).
        - Other models (for creating some kind of aggregates).
        - Services (for interacting with third party services).
- Database models:
    - Can talk to:
        - Other database models of current application.
- Services:
    - Can talk to:
        - Nobody.
        
### Application packages

YADSN has two application packages: backend and frontend.

```
- yadsn/
    - backend/         # Backend applications package
        - __init__.py
    - frontend/        # Frontend applications package
        - __init__.py
```

Backend packages provides:
- Models
- Database models
- Forms

Frontend packages provides:
- Views
- Templates

This is because of models and forms can be nicely reused, views and templates are not.

Examples of backend applications:
- Users
- Blogs
- Messages
- NewsFeed

Example of frontend applications:
- Website
- Api
- Mobile

### Applications interaction

YADSN applications are low coupled. 

The only layer, where backend applications can interact is `models`.

Interaction between database models of different applications is forbidden.

### Dependency management

YADSN uses PyBinder (https://pypi.python.org/pypi/PyBinder) for dependency management.

PyBinder catalogs are placed in `yadsn/catalogs` package:

```
- yadsn/
    - catalogs/
        - __init__.py   # PyBinder container definition.
        - forms.py      # Forms definition.
        - models.py     # Models definition.
        - services.py   # Services definition.
```

Views are not defined using PyBinder catalogs. Being on the top level of architecture, views use PyBinder `@inject` decorator for dependency injections.

Example:

```python
from django.views.generic import View
from yadsn.catalogs import models, forms


@models.inject('user_model')
@forms.inject('registration_form')
class Registration(View):

    user_model = None
    """:type: someapp.models.UserModel"""
    
    registration_form = None
    """:type: someapp.forms.RegistrationForm"""

    def get(request):
        form = self.registration_form(request.POST)
        
        if form.is_valid():
            user = self.user_model.create(**form.cleaned_data)
        # Etc...
```
