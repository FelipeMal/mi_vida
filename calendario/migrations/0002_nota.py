from django.db import models
from django.db.models import CASCADE
from django.db import migrations

class Migration(migrations.Migration):
    dependencies = [
        ('calendario', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('contenido', models.TextField()),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('mes', models.ForeignKey(on_delete=CASCADE, related_name='notas', to='calendario.mes')),
            ],
            options={
                'verbose_name_plural': 'Notas',
                'ordering': ['fecha_creacion'],
            },
        ),
    ]