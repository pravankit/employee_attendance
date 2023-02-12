# Generated by Django 4.1.6 on 2023-02-09 19:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('E_id', models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MaxValueValidator(9999999999)])),
                ('Name', models.CharField(max_length=50)),
                ('January', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('February', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('March', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('April', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('May', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('June', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('July', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('August', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('September', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('October', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('November', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
                ('December', models.PositiveIntegerField(validators=[django.core.validators.MaxValueValidator(31)])),
            ],
        ),
    ]