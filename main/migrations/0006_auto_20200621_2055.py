# Generated by Django 3.0.2 on 2020-06-21 13:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0005_auto_20200618_2111'),
    ]

    operations = [
        migrations.RenameField(
            model_name='listtweet',
            old_name='date',
            new_name='updated_date',
        ),
        migrations.RenameField(
            model_name='listtweet',
            old_name='author',
            new_name='user',
        ),
        migrations.AddField(
            model_name='listtweet',
            name='create_date',
            field=models.DateTimeField(null=True),
        ),
        migrations.AddField(
            model_name='listtweet',
            name='status',
            field=models.BooleanField(default=True),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(max_length=255)),
                ('create_time', models.DateTimeField(auto_now=True)),
                ('post', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main.ListTweet')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
