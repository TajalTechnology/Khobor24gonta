# Generated by Django 2.2 on 2020-04-07 06:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='InternationalPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('international_title', models.CharField(max_length=200, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(upload_to='images/')),
                ('international_content', models.TextField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Publish')], default=0)),
                ('visit_international', models.PositiveIntegerField(default=0)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='international_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='InternationalComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.EmailField(blank=True, max_length=200)),
                ('body', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('active', models.BooleanField(default=True)),
                ('internationalpost', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='international_comments', to='international.InternationalPost')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies_international_comment', to='international.InternationalComment')),
            ],
            options={
                'ordering': ('created',),
            },
        ),
    ]
