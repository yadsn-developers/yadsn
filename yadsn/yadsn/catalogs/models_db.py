"""
Database models catalog.
"""

from pybinder import Catalog


class DatabaseModelsCatalog(Catalog):

    namespace = 'db_models'


catalog = DatabaseModelsCatalog()
