# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-17 10:25
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
#


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0023_alter_page_revision_on_delete_behaviour'),
        ('wagtaildocs', '0004_capitalizeverbose'),
        ('rtei', '0004_load_fixtures'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('document_file', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ResourceIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('title_en', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_fr', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_es', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('title_ar', models.CharField(help_text="The page title as you'd like it to be seen by the public", max_length=255, null=True, verbose_name='title')),
                ('slug_en', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_fr', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_es', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('slug_ar', models.SlugField(help_text='The name of the page as it will appear in URLs e.g http://domain.com/blog/[my-slug]/', max_length=255, null=True, verbose_name='slug')),
                ('url_path_en', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_fr', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_es', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('url_path_ar', models.TextField(blank=True, editable=False, null=True, verbose_name='URL path')),
                ('seo_title_en', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_fr', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_es', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('seo_title_ar', models.CharField(blank=True, help_text="Optional. 'Search Engine Friendly' title. This will appear at the top of the browser window.", max_length=255, null=True, verbose_name='page title')),
                ('search_description_en', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_fr', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_es', models.TextField(blank=True, null=True, verbose_name='search description')),
                ('search_description_ar', models.TextField(blank=True, null=True, verbose_name='search description')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', ),

        ),
        migrations.AddField(
            model_name='resourcedocument',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='rtei.ResourceIndexPage'),
        ),
    ]
