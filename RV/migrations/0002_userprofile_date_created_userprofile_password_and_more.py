# Generated by Django 4.2 on 2023-06-20 05:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RV', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
