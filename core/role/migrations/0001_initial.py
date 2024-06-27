# Generated by Django 4.2.7 on 2024-06-21 08:36

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employee', '0001_initial'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('PublicId', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('DateLeft', models.DateTimeField(default=None, null=True)),
                ('Employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='employee.employee')),
                ('Job', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='job.job')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
