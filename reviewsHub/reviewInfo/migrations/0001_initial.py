# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ReviewInfo'
        db.create_table(u'reviewInfo_reviewinfo', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('sku', self.gf('django.db.models.fields.IntegerField')()),
            ('rating', self.gf('django.db.models.fields.FloatField')()),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('comment', self.gf('django.db.models.fields.TextField')()),
            ('submissionTime', self.gf('django.db.models.fields.DateTimeField')()),
            ('reviewer', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'reviewInfo', ['ReviewInfo'])


    def backwards(self, orm):
        # Deleting model 'ReviewInfo'
        db.delete_table(u'reviewInfo_reviewinfo')


    models = {
        u'reviewInfo.reviewinfo': {
            'Meta': {'object_name': 'ReviewInfo'},
            'comment': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'rating': ('django.db.models.fields.FloatField', [], {}),
            'reviewer': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'sku': ('django.db.models.fields.IntegerField', [], {}),
            'submissionTime': ('django.db.models.fields.DateTimeField', [], {}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'})
        }
    }

    complete_apps = ['reviewInfo']