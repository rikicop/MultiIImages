# Generated by Django 2.2 on 2021-03-30 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.FileField(blank=True, upload_to='here/2021/03/30'),
        ),
        migrations.AlterField(
            model_name='postimage',
            name='images',
            field=models.FileField(upload_to='here/images2021/03/30'),
        ),
    ]
