# Generated by Django 4.2.13 on 2024-07-02 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auther', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Category',
            new_name='Genre',
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('file', models.FileField(blank=True, null=True, upload_to='book/')),
                ('image', models.ImageField(blank=True, null=True, upload_to='book-image')),
                ('edition', models.PositiveIntegerField()),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5)),
                ('ISBN_number', models.CharField(blank=True, max_length=40, null=True)),
                ('page_number', models.IntegerField()),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('demo_text', models.TextField(blank=True, null=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('discount_percent', models.DecimalField(decimal_places=2, max_digits=4)),
                ('volume', models.IntegerField()),
                ('language', models.CharField(blank=True, max_length=10, null=True)),
                ('is_published', models.BooleanField()),
                ('reference', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to='auther.author')),
                ('genre', models.ManyToManyField(to='book.genre')),
                ('publication', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='book.publication')),
            ],
        ),
    ]
