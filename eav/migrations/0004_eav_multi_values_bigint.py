from django.db import migrations
from django.db import connection

MYSQL = 'mysql'

def alter_id_column(apps, schema_editor):
    # workaround for test db
    if connection.vendor == MYSQL:
        schema_editor.execute(
            """
            ALTER TABLE eav_value_value_enum_multi MODIFY COLUMN id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            ALGORITHM=COPY,
            LOCK=SHARED;
            """
        )


class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0003_add_values_unique_constraint'),
    ]

    operations = [
        migrations.RunPython(alter_id_column),
    ]
