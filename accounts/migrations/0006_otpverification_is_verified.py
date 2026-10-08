from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_fix_userrolepermission_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='otpverification',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
    ]
