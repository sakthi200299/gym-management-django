from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_user_tenant_id'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.RemoveField(model_name='user', name='otp'),
                migrations.RemoveField(model_name='user', name='otp_expiry'),
            ]
        ),
    ]
