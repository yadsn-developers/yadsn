# YADSN ARCHITECTURE

### Architecture Layers

YADSN architecture layers:

- Views
    - HTTP input / output only.
- Forms
    - Data validation only (all fields defined, all fields are valid types).
- Models
    - Bussiness logic layer.
- Database models
    - Dry Django ORM (models definition only).
- Services
    - Third party integration modules (Codecha, Facebook, Gmail, GitHub, StackOverflow clients...)

How YADSN architecture layers can talk to each other?

- Views
    - Can talk to:
        - Forms (for pre-validating / filtering HTTP input data).
        - Models (for providing some functionality).
- Forms:
    - Can talk to:
        - Nobody.
- Models:
    - Can talk to:
        - Database models of current application (for data persistance).
        - Other models (for creating some kind of aggregates).
        - Services (for interacting with third party services).
- Database models:
    - Can talk to:
        - Other database models.
- Services:
    - Can talk to:
        - Nobody.
