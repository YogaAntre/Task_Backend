# Generated by Django 2.2.2 on 2022-08-03 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('marketplace', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='file')),
            ],
        ),
        migrations.CreateModel(
            name='Texts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instruction', models.CharField(max_length=30)),
                ('ref_no', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='carimage',
            name='car',
        ),
        migrations.DeleteModel(
            name='Car',
        ),
        migrations.DeleteModel(
            name='CarImage',
        ),
        migrations.AddField(
            model_name='image',
            name='img',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='marketplace.Texts'),
        ),
    ]
