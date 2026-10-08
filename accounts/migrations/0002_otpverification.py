from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtpVerification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('otp', models.CharField(max_length=6)),
                ('otp_expiry', models.DateTimeField()),
                ('purpose', models.CharField(max_length=20)),
            ],
            options={
                'app_label': 'accounts',
            },
        ),
    ]
