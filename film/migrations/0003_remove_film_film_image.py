
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0002_auto_20201109_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='film',
            name='film_image',
        ),
    ]
