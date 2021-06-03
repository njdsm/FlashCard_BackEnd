# Generated by Django 3.1.8 on 2021-06-03 14:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Flashcard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('front_text', models.CharField(blank=True, max_length=250, null=True)),
                ('back_text', models.CharField(blank=True, max_length=250, null=True)),
                ('collection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='collection.collection')),
            ],
        ),
    ]
