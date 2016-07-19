from django.db.models import Lookup


class PrefixLookup(Lookup):
    lookup_name = "prefix"

    def as_sql(self, compiler, connection):
        lhs, lhs_params = self.process_lhs(compiler, connection)
        rhs, rhs_params = self.process_rhs(compiler, connection)
        params = lhs_params + rhs_params

        if connection.settings_dict['ENGINE'] == 'django.db.backends.postgresql':
            # Check for PostgreSQL and for the prefix plugin
            c = connection.cursor()
            c.execute(
                "SELECT EXISTS (SELECT 1 FROM pg_type WHERE typname = 'prefix_range')")
            if c.fetchone()[0]:
                return '%s @> %s' % (lhs, rhs), params
        if connection.settings_dict['ENGINE'] in ('django.db.backends.oracle', 'django.db.backends.sqlite3'):
            substr_fn = "SUBSTR"
        else:
            substr_fn = "SUBSTRING"
        return "{column} = {substr_fn}({data}, 1, LENGTH({column}))".format(
                column=lhs, data=rhs, substr_fn=substr_fn), params
