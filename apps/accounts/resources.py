from django import http
from django.db import IntegrityError, transaction
from django.contrib.auth import authenticate, login, logout
from django.conf.urls import url
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from tastypie import fields
from tastypie.authorization import DjangoAuthorization
from tastypie.resources import ModelResource, ALL, ALL_WITH_RELATIONS
from tastypie.utils import trailing_slash
from tastypie.authentication import SessionAuthentication
from tastypie.authorization import Authorization


class UserResource(ModelResource):
		
	class Meta:
		queryset = User.objects.all()
		resource_name = 'user'
		allowed_methods = ('get', 'post', 'put','delete', 'patch')
		filtering = { "id" : ALL }
		
	# def prepend_urls(self):
	# 	return [
	# 		url(r"^(?P<resource_name>%s)/login%s$" %
	# 			(self._meta.resource_name, trailing_slash()),
	# 			self.wrap_view('handle_login'), name="api_login"),
	# 	]
	#
	# def handle_login(self, request, **kwargs):
	# 	username = request.REQUEST.get("username")
	# 	password = request.REQUEST.get("password")
	# 	user = authenticate(username=username, password=password)
	#
	# 	msg = ""
	# 	success = True
	# 	next_url = ""
	# 	if user:
	# 		login(request, user)
	# 		next_url = reverse('events:add')
	# 	else:
	# 		msg = "Invalid Username or Password"
	# 		success = False
	#
	# 	return self.create_response(request, { 'msg' : msg, 'success' : success, 'next_url' : next_url })
