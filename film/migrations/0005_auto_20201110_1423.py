
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('film', '0004_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-comment_date']},
        ),
        migrations.AlterModelOptions(
            name='film',
            options={'ordering': ['-created_date']},
        ),
    ]
