# YADSN ARCHITECTURE


### Tools

- Web framework
    - Flask
- ORM
    - SQLAlchemy
- Database
    - PostgreSQL


### Architecture layers

- Views
    - HTTP input / output only.
- Models
    - Business logic layer.
- Database models
    - Dry SQLAlchemy ORM (models definition only).
- Services
    - Third party integration modules (Codecha, Facebook, Gmail, GitHub, StackOverflow clients...)
    - Tech layer clients (Redis, Solr, Cassandra client...)
