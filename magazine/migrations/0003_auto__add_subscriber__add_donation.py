# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Subscriber'
        db.create_table(u'magazine_subscriber', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('streetAddress1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('streetAddress2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zipCode', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('customerID', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('renew', self.gf('django.db.models.fields.BooleanField')()),
            ('subscriptionType', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'magazine', ['Subscriber'])

        # Adding model 'Donation'
        db.create_table(u'magazine_donation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('amount', self.gf('django.db.models.fields.IntegerField')()),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('email', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('streetAddress1', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('streetAddress2', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zipCode', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('customerID', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('time', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'magazine', ['Donation'])


    def backwards(self, orm):
        # Deleting model 'Subscriber'
        db.delete_table(u'magazine_subscriber')

        # Deleting model 'Donation'
        db.delete_table(u'magazine_donation')


    models = {
        u'magazine.article': {
            'Meta': {'object_name': 'Article', '_ormbases': [u'magazine.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['magazine.Content']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'magazine.content': {
            'Meta': {'object_name': 'Content'},
            'body': ('tinymce.models.HTMLField', [], {}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['magazine.Contributor']", 'symmetrical': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Issue']"}),
            'medium': ('tinymce.models.HTMLField', [], {}),
            'section': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['magazine.Section']"}),
            'size': ('tinymce.models.HTMLField', [], {}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'}),
            'statement': ('tinymce.models.HTMLField', [], {}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tags': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['magazine.Tag']", 'symmetrical': 'False'}),
            'teaser': ('django.db.models.fields.TextField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magazine.contributor': {
            'Meta': {'object_name': 'Contributor'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'})
        },
        u'magazine.donation': {
            'Meta': {'object_name': 'Donation'},
            'amount': ('django.db.models.fields.IntegerField', [], {}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'customerID': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'streetAddress1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'streetAddress2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magazine.image': {
            'Meta': {'object_name': 'Image', '_ormbases': [u'magazine.Content']},
            u'content_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['magazine.Content']", 'unique': 'True', 'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'})
        },
        u'magazine.issue': {
            'Meta': {'object_name': 'Issue'},
            'cover_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'issue': ('django.db.models.fields.CharField', [], {'default': "'Fall'", 'max_length': '255'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'}),
            'pub_date': ('django.db.models.fields.DateField', [], {}),
            'theme': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'year': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        u'magazine.section': {
            'Meta': {'object_name': 'Section'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '255'})
        },
        u'magazine.subscriber': {
            'Meta': {'object_name': 'Subscriber'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'customerID': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'email': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'renew': ('django.db.models.fields.BooleanField', [], {}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'streetAddress1': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'streetAddress2': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'subscriptionType': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'time': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'zipCode': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'magazine.tag': {
            'Meta': {'object_name': 'Tag'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['magazine']