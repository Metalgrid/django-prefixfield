from django.db import models


class PrefixField(models.CharField):
    "Implements a prefix field"

    description = "Implements a prefix field"

    def db_type(self, connection):
        """ Returns the database column type for table creation"""

        if connection.settings_dict['ENGINE'] == 'django.db.backends.postgresql':
            # Check for PostgreSQL and for the prefix plugin
            c = connection.cursor()
            c.execute("SELECT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'prefix_range')")
            if c.fetchone()[0]:
                return 'prefix_range'
        return 'char({})'.format(self.max_length)