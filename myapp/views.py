# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.views.generic.list_detail import object_list, object_detail
from django.views.generic.create_update import create_object, delete_object, \
    update_object
from google.appengine.ext import db
from mimetypes import guess_type
from myapp.forms import PersonForm
from myapp.models import Contract, File, Person
from ragendja.dbutils import get_object_or_404
from ragendja.template import render_to_response

def list_people(request):
    return object_list(request, Person.all(), paginate_by=10)

def show_person(request, key):
    return object_detail(request, Person.all(), key)

def add_person(request):
    return create_object(request, form_class=PersonForm,
        post_save_redirect=reverse('myapp.views.show_person',
                                   kwargs=dict(key='%(key)s')))

def edit_person(request, key):
    return update_object(request, object_id=key, form_class=PersonForm,
        post_save_redirect=reverse('myapp.views.show_person',
                                   kwargs=dict(key='%(key)s')))

def delete_person(request, key):
    return delete_object(request, Person, object_id=key,
        post_delete_redirect=reverse('myapp.views.list_people'))

def download_file(request, key, name):
    file = get_object_or_404(File, key)
    if file.name != name:
        raise Http404('Could not find file with this name!')
    return HttpResponse(file.file,
        content_type=guess_type(file.name)[0] or 'application/octet-stream')

def create_admin_user(request):
    user = User.get_by_key_name('admin')
    if not user or user.username != 'admin' or not (user.is_active and
            user.is_staff and user.is_superuser and
            user.check_password('admin')):
        user = User(key_name='admin', username='admin',
            email='admin@localhost', first_name='Boss', last_name='Admin',
            is_active=True, is_staff=True, is_superuser=True)
        user.set_password('admin')
        user.put()
    return render_to_response(request, 'myapp/admin_created.html')

def ah_warmup(request):
    """
    This handler is hit by GAE every time a new instance is brought up.
    This ensures a real user request doesn't see a delay while the imports are
    resolved, caches are loaded, etc.
    """
    return HttpResponse("ah_warmup complete.")

def ah_start(request):
    """
    This handler is hit by GAE every time a new backend instance is brought up.
    """
    return HttpResponse("ah_start complete.")

def ah_stop(request):
    """
    This handler is hit by GAE every time an instance is to be terminated.
    """
    return HttpResponse("ah_stop complete.")

def ah_queue_deferred(request):
    """
    We use this to get around the app engine patch interfering with the
    deferred library.  Using the default deferred causes all sorts of sporadic
    errors to occur from the sequence of unzipping the django libraries.
    """

    from google.appengine.ext import deferred
    try:
        deferred.run(request.raw_post_data)
    except PermanentTaskFailure, e:
        logging.error("Permanent task failure; task will never finish.")
        raise e
    return HttpResponse("ah_queue_deferred replacement complete.")

