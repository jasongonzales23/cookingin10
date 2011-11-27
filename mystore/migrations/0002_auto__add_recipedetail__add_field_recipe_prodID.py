# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'RecipeDetail'
        db.create_table('mystore_recipedetail', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('recipe', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['mystore.Recipe'])),
        ))
        db.send_create_signal('mystore', ['RecipeDetail'])

        # Adding field 'Recipe.prodID'
        db.add_column('mystore_recipe', 'prodID', self.gf('django.db.models.fields.CharField')(default=0, max_length=30), keep_default=False)


    def backwards(self, orm):
        
        # Deleting model 'RecipeDetail'
        db.delete_table('mystore_recipedetail')

        # Deleting field 'Recipe.prodID'
        db.delete_column('mystore_recipe', 'prodID')


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
            'catalog': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mystore.Catalog']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'children'", 'null': 'True', 'to': "orm['mystore.Category']"}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'mystore.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': "orm['mystore.Category']"}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'prodID': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 11, 14, 12, 19, 0, 419081)'}),
            'slug': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'mystore.recipedetail': {
            'Meta': {'object_name': 'RecipeDetail'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mystore.Recipe']"})
        }
    }

    complete_apps = ['mystore']
