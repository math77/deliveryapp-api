# Generated by Django 2.1.7 on 2019-03-24 23:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(max_length=30, verbose_name='username')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('phone', models.CharField(max_length=13)),
                ('about', models.CharField(max_length=150)),
                ('criminal_background_check_pic', models.ImageField(upload_to='pic_folder/')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('profile_pic', models.ImageField(upload_to='pic_profile_folder/')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initial_latitude', models.FloatField()),
                ('initial_longitude', models.FloatField()),
                ('final_latitude', models.FloatField()),
                ('final_longitude', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delivered', models.BooleanField(default=False)),
                ('id_delivery', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Delivery')),
                ('id_user_sender', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=80)),
                ('confirmed', models.BooleanField(default=False)),
                ('confirmation_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.IntegerField()),
                ('comment', models.TextField()),
                ('id_user_appraiser', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_appraiser', to=settings.AUTH_USER_MODEL)),
                ('id_user_evaluated', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_evaluated', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('completed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('start_time', models.DateTimeField()),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='TypeLocomotion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='trip',
            name='id_type_locomotion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.TypeLocomotion'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='id_payment',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='api.Payment'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='id_trip',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.Trip'),
        ),
    ]
