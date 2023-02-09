# Generated by Django 3.2.16 on 2023-02-06 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import stdimage.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Atividade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('area', models.CharField(choices=[('Aerodinâmica', 'Aerodinâmica'), ('Direção e Suspenção', 'Direção e Suspenção'), ('Elétrica', 'Elétrica'), ('Estrutura', 'Estrutura'), ('Freio e Ergonomia', 'Freio e Ergonomia'), ('Powewtrain', 'Powewtrain'), ('Comercial', 'Comercial'), ('Financeiro', 'Financeiro'), ('Gestão de Pessoas', 'Gestão de Pessoas'), ('Marketing', 'Marketing'), ('NA', 'Nenhuma')], max_length=100)),
                ('situacao', models.CharField(choices=[('AF', 'A fazer'), ('FA', 'Fazendo'), ('FE', 'Feito')], max_length=100)),
                ('descricao', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Atividade',
                'verbose_name_plural': 'Atividades',
            },
        ),
        migrations.CreateModel(
            name='FluxodeCX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'verbose_name': 'Fluxo de Caixa',
                'verbose_name_plural': 'Fluxo de Caixa',
            },
        ),
        migrations.CreateModel(
            name='Lembrete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lemb', models.CharField(max_length=80, verbose_name='lembrete')),
            ],
        ),
        migrations.CreateModel(
            name='ObjetivosArea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=40)),
                ('descricao', models.CharField(max_length=200)),
                ('area', models.CharField(choices=[('Aerodinâmica', 'Aerodinâmica'), ('Direção e Suspenção', 'Direção e Suspenção'), ('Elétrica', 'Elétrica'), ('Estrutura', 'Estrutura'), ('Freio e Ergonomia', 'Freio e Ergonomia'), ('Powewtrain', 'Powewtrain'), ('Comercial', 'Comercial'), ('Financeiro', 'Financeiro'), ('Gestão de Pessoas', 'Gestão de Pessoas'), ('Marketing', 'Marketing'), ('NA', 'Nenhuma')], default='Nenhuma', max_length=50)),
            ],
            options={
                'verbose_name': 'Objetivo',
                'verbose_name_plural': 'Objetivos',
            },
        ),
        migrations.CreateModel(
            name='Integrantes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('funcao', models.CharField(choices=[('Cordenador', 'Cordenador'), ('Assesor', 'Assesor'), ('Conselheiro', 'Conselheiro'), ('Capitão', 'Capitão(ã)'), ('Vice Capitão', 'Vice Capitão(ã)'), ('Diretor de Projetos', 'Diretor(a) de Projetos'), ('Diretor Administrativo', 'Diretor(a) Administrativo')], max_length=50)),
                ('area', models.CharField(choices=[('Aerodinâmica', 'Aerodinâmica'), ('Direção e Suspenção', 'Direção e Suspenção'), ('Elétrica', 'Elétrica'), ('Estrutura', 'Estrutura'), ('Freio e Ergonomia', 'Freio e Ergonomia'), ('Powewtrain', 'Powewtrain'), ('Comercial', 'Comercial'), ('Financeiro', 'Financeiro'), ('Gestão de Pessoas', 'Gestão de Pessoas'), ('Marketing', 'Marketing'), ('NA', 'Nenhuma')], max_length=50)),
                ('foto', stdimage.models.StdImageField(blank=True, force_min_size=False, null=True, upload_to='integrantes', variations={}, verbose_name='foto')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Integrante',
                'verbose_name_plural': 'Integrantes',
            },
        ),
    ]
