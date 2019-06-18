# Generated by Django 2.2.2 on 2019-06-18 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_veiculo_proprietario'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='endereco',
            field=models.CharField(default='Sem bairro', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pessoa',
            name='telefone',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
    ]
