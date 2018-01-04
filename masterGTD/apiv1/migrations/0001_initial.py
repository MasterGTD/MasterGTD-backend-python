# Generated by Django 2.0.1 on 2018-01-04 09:40

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
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('pro_count', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='CheckList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='HabitDay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True)),
                ('done', models.BooleanField(default=False)),
                ('done_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=200, unique=True)),
                ('slug', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('is_finished', models.BooleanField(default=False)),
                ('of_list', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tasks', related_query_name='list', to='apiv1.CheckList')),
            ],
        ),
        migrations.CreateModel(
            name='Todo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.CharField(max_length=200, unique=True)),
                ('desc', models.TextField()),
                ('is_public', models.BooleanField()),
                ('start_day', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Habit',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apiv1.Todo')),
                ('done_today', models.BooleanField(default=False)),
                ('finished_days', models.IntegerField()),
                ('current_strike_days', models.IntegerField()),
                ('longet_strike_days', models.IntegerField()),
            ],
            bases=('apiv1.todo',),
        ),
        migrations.CreateModel(
            name='PercentTodo',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apiv1.Todo')),
                ('percent', models.IntegerField()),
                ('total_count', models.IntegerField()),
                ('current_count', models.IntegerField()),
            ],
            bases=('apiv1.todo',),
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('todo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='apiv1.Todo')),
                ('expect_finish_date', models.DateField(null=True)),
            ],
            bases=('apiv1.todo',),
        ),
        migrations.AddField(
            model_name='todo',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Todos', related_query_name='category', to='apiv1.Category'),
        ),
        migrations.AddField(
            model_name='todo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Todos', related_query_name='user', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='habitday',
            name='habit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apiv1.Habit'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='of_Project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lists', related_query_name='Todo', to='apiv1.Project'),
        ),
    ]