# Generated by Django 3.0.2 on 2021-02-11 22:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='название')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, default='default/event_pic.jpg', upload_to='photos/events/%Y/%m/%d', verbose_name='фото')),
                ('short_description', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('rating', models.CharField(default='0+', max_length=3)),
            ],
            options={
                'verbose_name': 'событие-родитель',
                'verbose_name_plural': 'события-родители',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='название')),
                ('slug', models.SlugField(blank=True, max_length=100)),
                ('photo', models.ImageField(blank=True, default='default/place_pic.jpg', upload_to='photos/place/%Y/%m/%d', verbose_name='фото')),
                ('short_description', models.CharField(max_length=70)),
                ('description', models.TextField()),
                ('address', models.CharField(max_length=100)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='places', to='account.City')),
            ],
            options={
                'verbose_name': 'место-родитель',
                'verbose_name_plural': 'места-родители',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='CinemaTheatre',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Place')),
                ('work_time', models.CharField(max_length=30)),
                ('room_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'кинотеатр',
                'verbose_name_plural': 'кинотеатры',
            },
            bases=('events.place',),
        ),
        migrations.CreateModel(
            name='ExhibitionEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('artists', models.TextField()),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'выставка',
                'verbose_name_plural': 'выставки',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='FilmEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('author', models.CharField(max_length=50)),
                ('artists', models.TextField()),
                ('director', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=15)),
                ('premier_date', models.DateField()),
                ('country', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'фильм',
                'verbose_name_plural': 'фильмы',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='NontypeEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
            ],
            options={
                'verbose_name': 'событие',
                'verbose_name_plural': 'события',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='NontypePlace',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Place')),
            ],
            options={
                'verbose_name': 'место',
                'verbose_name_plural': 'места',
            },
            bases=('events.place',),
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Place')),
                ('work_time', models.CharField(max_length=30)),
                ('table_count', models.IntegerField()),
                ('cousine', models.CharField(max_length=30)),
                ('average_bill', models.IntegerField()),
                ('category', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'ресторан',
                'verbose_name_plural': 'рестораны',
            },
            bases=('events.place',),
        ),
        migrations.CreateModel(
            name='Showroom',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Place')),
                ('work_time', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'выставочный зал',
                'verbose_name_plural': 'выставочные залы',
            },
            bases=('events.place',),
        ),
        migrations.CreateModel(
            name='SportEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('category', models.CharField(max_length=30)),
            ],
            options={
                'verbose_name': 'спортивное событие',
                'verbose_name_plural': 'спортивные события',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='Theatre',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Place')),
                ('work_time', models.CharField(max_length=30)),
                ('seat_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'театр',
                'verbose_name_plural': 'театры',
            },
            bases=('events.place',),
        ),
        migrations.CreateModel(
            name='TheatreEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('author', models.CharField(max_length=50)),
                ('artists', models.TextField()),
                ('director', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'театральный спектакль',
                'verbose_name_plural': 'театральные спектакли',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='СoncertEvent',
            fields=[
                ('event_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Event')),
                ('artist', models.CharField(max_length=50)),
                ('time', models.CharField(max_length=15)),
            ],
            options={
                'verbose_name': 'концерт',
                'verbose_name_plural': 'концерты',
            },
            bases=('events.event',),
        ),
        migrations.CreateModel(
            name='СoncertHall',
            fields=[
                ('place_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='events.Place')),
                ('work_time', models.CharField(max_length=30)),
                ('seat_count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'концертный зал',
                'verbose_name_plural': 'концертные залы',
            },
            bases=('events.place',),
        ),
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='start_at', to='events.Event')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Place')),
            ],
            options={
                'verbose_name': 'расписание',
                'verbose_name_plural': 'расписания',
                'ordering': ['date'],
            },
        ),
        migrations.CreateModel(
            name='PlaceComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Place')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='comments',
            field=models.ManyToManyField(through='events.PlaceComments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='place',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='liked_places', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='place',
            name='owner',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='places', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='EventComments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='events.Event')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='comments',
            field=models.ManyToManyField(through='events.EventComments', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='followers',
            field=models.ManyToManyField(blank=True, related_name='followed_events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='organizer',
            field=models.ForeignKey(blank=True, default=1, on_delete=django.db.models.deletion.CASCADE, related_name='events', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='event',
            name='schedule',
            field=models.ManyToManyField(through='events.Schedule', to='events.Place'),
        ),
    ]
