# Generated by Django 4.0.2 on 2022-04-05 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_alter_user_first_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.AlterField(
            model_name='auctionlisting',
            name='imageUrl',
            field=models.ImageField(upload_to='images/'),
        ),
    ]