from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_user_options_user_tenant_id'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.AddField(
                    model_name='user',
                    name='otp',
                    field=models.CharField(blank=True, max_length=6, null=True),
                ),
                migrations.AddField(
                    model_name='user',
                    name='otp_expiry',
                    field=models.DateTimeField(blank=True, null=True),
                ),
            ]
        ),
        migrations.CreateModel(
            name='UserTenant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tenant_id', models.CharField(max_length=50, unique=True)),
                ('tfa_email', models.BooleanField(default=False)),
                ('tfa_phone', models.BooleanField(default=False)),
            ],
            options={
                'db_table': 'users_usertenant',
                'app_label': 'users',
            },
        ),
    ]
