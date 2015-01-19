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
