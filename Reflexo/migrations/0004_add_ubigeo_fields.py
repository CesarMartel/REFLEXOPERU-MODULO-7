# Generated manually to add ubigeo fields

from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('Reflexo', '0003_auto_20250808_1128'),
    ]

    operations = [
        # Agregar campos de ubigeo a Region
        migrations.AddField(
            model_name='region',
            name='ubigeo_code',
            field=models.CharField(
                max_length=2, 
                unique=True, 
                null=True, 
                blank=True, 
                help_text="Código de ubigeo de 2 dígitos"
            ),
        ),
        migrations.AddField(
            model_name='region',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='region',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, blank=True),
        ),
        
        # Agregar campos de ubigeo a Province
        migrations.AddField(
            model_name='province',
            name='ubigeo_code',
            field=models.CharField(
                max_length=4, 
                unique=True, 
                null=True, 
                blank=True, 
                help_text="Código de ubigeo de 4 dígitos"
            ),
        ),
        migrations.AddField(
            model_name='province',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='province',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, blank=True),
        ),
        
        # Agregar campos de ubigeo a District
        migrations.AddField(
            model_name='district',
            name='ubigeo_code',
            field=models.CharField(
                max_length=6, 
                unique=True, 
                null=True, 
                blank=True, 
                help_text="Código de ubigeo de 6 dígitos"
            ),
        ),
        migrations.AddField(
            model_name='district',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='district',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, blank=True),
        ),
        
        # Agregar campos de timestamps a Country
        migrations.AddField(
            model_name='country',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='country',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True, blank=True),
        ),
    ]
