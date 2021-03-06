# Generated by Django 3.0.7 on 2021-01-03 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('private_chats', '0011_delete_groupchatroom'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='groupmessages',
            name='members',
        ),
        migrations.AlterField(
            model_name='groupmessages',
            name='content',
            field=models.TextField(max_length=2000),
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=50)),
                ('admin', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='grouproom', to='accounts.Profile')),
                ('members', models.ManyToManyField(related_name='group_members', to='accounts.Profile')),
            ],
        ),
        migrations.AddField(
            model_name='groupmessages',
            name='grouproom',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_message', to='private_chats.Group'),
        ),
    ]
