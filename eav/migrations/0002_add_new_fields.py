# Generated by Django 3.0.2 on 2020-07-27 07:30

from django.db import migrations, models
import django.db.models.deletion
import eav.fields


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('eav', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='attribute',
            name='entity_ct',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='attribute_entities', to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='attribute',
            name='entity_id',
            field=models.UUIDField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='enumvalue',
            name='legacy_value',
            field=models.CharField(blank=True, db_index=True, max_length=100, null=True, verbose_name='Legacy Value'),
        ),
        migrations.AddField(
            model_name='value',
            name='value_decimal',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=14, null=True),
        ),
        migrations.AddField(
            model_name='value',
            name='value_enum_multi',
            field=models.ManyToManyField(related_name='eav_multi_values', to='eav.EnumValue'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='datatype',
            field=eav.fields.EavDatatypeField(
                choices=[('text', 'Text'), ('date', 'Date'), ('float', 'Float'), ('decimal', 'Decimal'),
                         ('int', 'Integer'), ('bool', 'True / False'), ('object', 'Django Object'), ('enum', 'Choice'),
                         ('enum_multi', 'Multiple Choice')], max_length=10, verbose_name='Data Type'),
        ),
        migrations.AlterField(
            model_name='attribute',
            name='slug',
            field=eav.fields.EavSlugField(help_text='Short attribute label', verbose_name='Slug'),
        ),
        migrations.AlterField(
            model_name='enumgroup',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='enumvalue',
            name='value',
            field=models.CharField(db_index=True, max_length=100, verbose_name='Value'),
        ),
    ]