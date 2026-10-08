from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_otpverification'),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=[],
            state_operations=[
                migrations.AlterUniqueTogether(
                    name='userrolepermission',
                    unique_together=set(),
                ),
                migrations.RemoveField(model_name='userrolepermission', name='user'),
                migrations.AddField(
                    model_name='userrolepermission',
                    name='user_id',
                    field=models.IntegerField(default=0),
                ),
                migrations.AlterField(
                    model_name='userrolepermission',
                    name='role',
                    field=models.CharField(max_length=50),
                ),
                migrations.AlterField(
                    model_name='userrolepermission',
                    name='permission',
                    field=models.CharField(max_length=100),
                ),
            ]
        ),
        migrations.AlterField(
            model_name='otpverification',
            name='otp',
            field=models.CharField(max_length=6, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='otpverification',
            name='otp_expiry',
            field=models.DateTimeField(null=True, blank=True),
        ),
    ]
