# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Article'
        db.create_table('blog_article', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=255, unique=True)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
            ('short_content', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('is_active', self.gf('django.db.models.fields.BooleanField')(default=True)),
            ('meta_description', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
            ('meta_keywords', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255)),
        ))
        db.send_create_signal('blog', ['Article'])

        # Adding model 'ArticleSection'
        db.create_table('blog_articlesection', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('article', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['blog.Article'])),
            ('sort', self.gf('django.db.models.fields.IntegerField')(default=0)),
            ('image', self.gf('django.db.models.fields.files.ImageField')(blank=True, max_length=100, null=True)),
            ('image_caption', self.gf('django.db.models.fields.CharField')(blank=True, max_length=255, null=True)),
            ('section_header', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('article_section', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('blog', ['ArticleSection'])


    def backwards(self, orm):
        # Deleting model 'Article'
        db.delete_table('blog_article')

        # Deleting model 'ArticleSection'
        db.delete_table('blog_articlesection')


    models = {
        'blog.article': {
            'Meta': {'object_name': 'Article', 'ordering': "['sort', 'name']"},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'unique': 'True'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'blog.articlesection': {
            'Meta': {'object_name': 'ArticleSection', 'ordering': "['sort']"},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Article']"}),
            'article_section': ('django.db.models.fields.TextField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'max_length': '100', 'null': 'True'}),
            'image_caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255', 'null': 'True'}),
            'section_header': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['blog']