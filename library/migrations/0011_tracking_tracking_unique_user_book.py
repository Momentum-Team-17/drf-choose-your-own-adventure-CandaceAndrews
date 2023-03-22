# Generated by Django 4.1.7 on 2023-03-22 21:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0010_author_unique_author_name_genre_unique_genre_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('want to read', 'Want To Read'), ('reading', 'Reading'), ('read/done', 'Read/Done')], max_length=50)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='library.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddConstraint(
            model_name='tracking',
            constraint=models.UniqueConstraint(fields=('user', 'book'), name='unique_user_book'),
        ),
    ]
