# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import DataMigration
from django.db import models
from django.contrib.auth.models import User
from django.db import IntegrityError, transaction

class Migration(DataMigration):

	def forwards(self, orm):
		
		with transaction.atomic():
			User.objects.get_or_create(username='joe@example.com',email='joe@example.com')
			User.objects.get_or_create(username='tim@example.com',email='tim@example.com')
			User.objects.get_or_create(username='sam@example.com',email='sam@example.com')

	def backwards(self, orm):
		"Write your backwards methods here."

	models = {
		
	}

	complete_apps = ['accounts']
	symmetrical = True
