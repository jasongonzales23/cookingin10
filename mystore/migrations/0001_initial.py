# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Catalog'
        db.create_table('mystore_catalog', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('mystore', ['Catalog'])

        # Adding model 'Category'
        db.create_table('mystore_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('catalog', self.gf('django.db.models.fields.related.ForeignKey')(related_name='categories', to=orm['mystore.Catalog'])),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='children', null=True, to=orm['mystore.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('mystore', ['Category'])

        # Adding model 'Recipe'
        db.create_table('mystore_recipe', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(related_name='products', to=orm['mystore.Category'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('slug', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('thumbnail', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('video', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('price', self.gf('django.db.models.fields.DecimalField')(max_digits=6, decimal_places=2)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime(2011, 11, 10, 18, 25, 49, 726834))),
        ))
        db.send_create_signal('mystore', ['Recipe'])


    def backwards(self, orm):
        
        # Deleting model 'Catalog'
        db.delete_table('mystore_catalog')

        # Deleting model 'Category'
        db.delete_table('mystore_category')

        # Deleting model 'Recipe'
        db.delete_table('mystore_recipe')


    models = {
        'mystore.catalog': {
            'Meta': {'object_name': 'Catalog'},
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mystore.category': {
            'Meta': {'object_name': 'Category'},
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': "orm['mystore.Catalog']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['mystore.Category']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mystore.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'products'", 'to': "orm['mystore.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 11, 10, 18, 25, 49, 726834)'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['mystore']
