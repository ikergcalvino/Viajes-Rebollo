# Generated by Django 4.2.4 on 2023-11-28 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viajes', '0003_alter_activity_loc'),
    ]

    operations = [
        migrations.AddField(
            model_name='package',
            name='activities',
            field=models.ManyToManyField(blank=True, to='viajes.activity'),
        ),
        migrations.AddField(
            model_name='tripplan',
            name='customized_activities',
            field=models.ManyToManyField(blank=True, to='viajes.activity'),
        ),
        migrations.AddField(
            model_name='tripplan',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tripplan',
            name='name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ActivityPackage',
        ),
    ]