# Generated by Django 4.2.11 on 2024-06-21 12:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_alter_review_title_delete_customer'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='equipment',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='reviews.equipment'),
        ),
    ]