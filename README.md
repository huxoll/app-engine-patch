##app-engine-patch

app-engine-patch is a set of patches to Django and to App Engine to allow Django to run on Google App Engine, using the full Google Datastore.  Without this patch, App Engine supports Django templates, but not the Django admin tools, middleware, and other Django features.

This repository was imported from the original [app-engine-patch](http://code.google.com/p/app-engine-patch) on bitbucket, which has been abandoned.  

There is also a native Django port, Django-nonrel, which uses a custom backend to provide Django-style database queries on top of the App Engine datastore.  That project does not currently support to full range of datastore operations available on the App Engine; ancestor queries and the NDB are not currently supported.  See 
[Django-nonrel] (http://www.allbuttonspressed.com/projects/django-nonrel)
for more information.

