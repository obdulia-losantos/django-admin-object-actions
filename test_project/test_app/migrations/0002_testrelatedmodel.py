# Generated by Django 3.0.5 on 2020-04-27 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestRelatedModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(blank=True, default='')),
                ('reviewed', models.DateTimeField(default=None, editable=False, null=True)),
                ('test_model', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='related_models', to='test_app.TestModel')),
            ],
        ),
    ]