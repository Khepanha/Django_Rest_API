# Generated by Django 3.1.4 on 2020-12-23 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='scene',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(max_length=20)),
                ('scene_image', models.CharField(max_length=20)),
                ('level', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='bookmark',
            name='word',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='users',
            name='user_password',
            field=models.CharField(max_length=20),
        ),
        migrations.CreateModel(
            name='word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('pic', models.CharField(max_length=20)),
                ('audio', models.CharField(max_length=20)),
                ('synonym', models.CharField(max_length=20)),
                ('definition', models.TextField()),
                ('example', models.TextField()),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.scene')),
            ],
        ),
        migrations.CreateModel(
            name='understood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='scene_percentage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_name', models.CharField(max_length=20)),
                ('percentage', models.IntegerField()),
                ('total_vocab', models.IntegerField()),
                ('complete', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
        migrations.CreateModel(
            name='recommendation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene_image', models.CharField(max_length=20)),
                ('scene', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.scene')),
            ],
        ),
        migrations.CreateModel(
            name='not_understood',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.users')),
            ],
        ),
    ]
