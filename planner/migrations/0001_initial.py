# Generated by Django 4.2.4 on 2023-08-17 10:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField(choices=[(3, 'High'), (2, 'Normal'), (1, 'Low')], default=2, verbose_name='Priority')),
                ('category', models.ManyToManyField(to='planner.category')),
            ],
            options={
                'verbose_name_plural': 'Activities',
            },
        ),
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('date', models.DateField()),
                ('status', models.CharField(choices=[('c', 'Complete'), ('o', 'Ongoing'), ('i', 'Incomplete')], default='i', max_length=1)),
                ('action', models.ForeignKey(null=True, on_delete=django.db.models.deletion.RESTRICT, to='planner.activity')),
            ],
            options={
                'ordering': ['start_time'],
            },
        ),
    ]
