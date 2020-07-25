# Generated by Django 2.2.12 on 2020-07-25 12:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0002_load_initial_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='Test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('r1', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_r1', to='home.CustomText')),
                ('r2', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_r2', to=settings.AUTH_USER_MODEL)),
                ('r3', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_r3', to='home.HomePage')),
            ],
        ),
    ]