# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Recipe.ingredient_total_cost'
        db.add_column('mystore_recipe', 'ingredient_total_cost', self.gf('django.db.models.fields.CharField')(default=0, max_length=30), keep_default=False)

        # Adding field 'Recipe.servings'
        db.add_column('mystore_recipe', 'servings', self.gf('django.db.models.fields.CharField')(default=0, max_length=30), keep_default=False)

        # Adding field 'Recipe.cost_per_serving'
        db.add_column('mystore_recipe', 'cost_per_serving', self.gf('django.db.models.fields.CharField')(default=0, max_length=30), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Recipe.ingredient_total_cost'
        db.delete_column('mystore_recipe', 'ingredient_total_cost')

        # Deleting field 'Recipe.servings'
        db.delete_column('mystore_recipe', 'servings')

        # Deleting field 'Recipe.cost_per_serving'
        db.delete_column('mystore_recipe', 'cost_per_serving')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
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
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'})
        },
        'mystore.purchase': {
            'Meta': {'object_name': 'Purchase'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'purchased_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'purchaser': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mystore.Recipe']"}),
            'token': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'mystore.recipe': {
            'Meta': {'object_name': 'Recipe'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'categories'", 'to': "orm['mystore.Category']"}),
            'cost_per_serving': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient_total_cost': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'price': ('django.db.models.fields.DecimalField', [], {'max_digits': '6', 'decimal_places': '2'}),
            'prodID': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime(2011, 11, 25, 17, 41, 55, 504419)'}),
            'servings': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '255', 'db_index': 'True'}),
            'thumbnail': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'video': ('django.db.models.fields.files.FileField', [], {'max_length': '100'})
        },
        'mystore.recipedetail': {
            'Meta': {'object_name': 'RecipeDetail'},
            'amount': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'cost': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingredient': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'recipe': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['mystore.Recipe']"})
        }
    }

    complete_apps = ['mystore']
