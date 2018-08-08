from django.db import models


class PrefixField(models.CharField):
    "Implements a prefix field"

    db_index = True
    description = "Implements a prefix field"

    def db_type(self, connection):
        """ Returns the database column type for table creation"""

        if connection.settings_dict['ENGINE'] == 'django.db.backends.postgresql':
            # Check for PostgreSQL and for the prefix plugin
            c = connection.cursor()
            c.execute("SELECT 1 FROM pg_type WHERE typname = 'prefix_range'")
            if c.fetchone() is not None:
                return 'prefix_range'
        return 'varchar({})'.format(self.max_length)
