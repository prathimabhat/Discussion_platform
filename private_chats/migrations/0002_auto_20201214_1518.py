# Generated by Django 3.0.7 on 2020-12-14 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('private_chats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GroupChatroom',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=25)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'verbose_name_plural': 'Group chatroom',
            },
        ),
        migrations.CreateModel(
            name='GroupMessages',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('msg_sent_time', models.DateTimeField(auto_now_add=True)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='groupchat', to='private_chats.GroupChatroom')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='groupchatuser', to='accounts.Profile')),
            ],
            options={
                'verbose_name_plural': 'Group messages',
            },
        ),
        migrations.DeleteModel(
            name='PersonalMessages',
        ),
    ]
