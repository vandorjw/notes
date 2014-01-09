# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Article.short_content'
        db.alter_column('blog_article', 'short_content', self.gf('tinymce.models.HTMLField')())

        # Changing field 'ArticleSection.article_section'
        db.alter_column('blog_articlesection', 'article_section', self.gf('tinymce.models.HTMLField')())

    def backwards(self, orm):

        # Changing field 'Article.short_content'
        db.alter_column('blog_article', 'short_content', self.gf('django.db.models.fields.TextField')())

        # Changing field 'ArticleSection.article_section'
        db.alter_column('blog_articlesection', 'article_section', self.gf('django.db.models.fields.TextField')())

    models = {
        'blog.article': {
            'Meta': {'object_name': 'Article', 'ordering': "['sort', 'name']"},
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'meta_description': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'meta_keywords': ('django.db.models.fields.CharField', [], {'blank': 'True', 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_content': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        'blog.articlesection': {
            'Meta': {'object_name': 'ArticleSection', 'ordering': "['sort']"},
            'article': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['blog.Article']"}),
            'article_section': ('tinymce.models.HTMLField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'blank': 'True', 'null': 'True', 'max_length': '100'}),
            'image_caption': ('django.db.models.fields.CharField', [], {'blank': 'True', 'null': 'True', 'max_length': '255'}),
            'section_header': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'sort': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        }
    }

    complete_apps = ['blog']