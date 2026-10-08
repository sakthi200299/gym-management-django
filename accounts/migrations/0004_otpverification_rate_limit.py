from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_fix_accounts'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpverification',
            name='failed_attempts',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='otpverification',
            name='locked_until',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
