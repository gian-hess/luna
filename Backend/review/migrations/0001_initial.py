# Generated by Django 3.2 on 2021-07-02 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('text', models.CharField(max_length=300)),
                ('rating', models.IntegerField(choices=[(1, 'very bad'), (2, 'bad'), (3, 'average'), (4, 'good'), (5, 'very good')], default=3)),
            ],
        ),
    ]
