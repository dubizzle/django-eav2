from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('eav', '0003_add_values_unique_constraint'),
    ]

    operations = [
        migrations.RunSQL(
            """
            ALTER TABLE eav_value_value_enum_multi
            MODIFY COLUMN id BIGINT UNSIGNED NOT NULL AUTO_INCREMENT,
            ALGORITHM=COPY,
            LOCK=SHARED;
            """
        )
    ]
