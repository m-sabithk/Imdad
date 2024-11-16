# Generated by Django 4.2.4 on 2024-10-13 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app', '0004_remove_expence_user_expence_last_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='GivenExpence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cost', models.IntegerField()),
                ('discription', models.TextField(blank=True, null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('expence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.expence')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]