# Generated by Django 3.0.7 on 2021-01-02 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('private_chats', '0008_groupchatroom_groupmessages_personalchatroom_personalmessages'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalmessages',
            name='chatroom',
        ),
        migrations.AddField(
            model_name='personalmessages',
            name='msg_receiver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_receiver', to='accounts.Profile'),
        ),
        migrations.AddField(
            model_name='personalmessages',
            name='msg_sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='msg_sender', to='accounts.Profile'),
        ),
        migrations.DeleteModel(
            name='PersonalChatroom',
        ),
    ]
