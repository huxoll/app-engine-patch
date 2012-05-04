#!/bin/sh
# Set up path to run command line python/django scripts
export GAE_HOME=/usr/local/google_appengine
export PATH=$PATH:$GAE_HOME
export PYTHONPATH=$GAE_HOME:./common/zip-packages/django-1.1.zip:$GAE_HOME/lib/simplejson:$GAE_HOME/lib/yaml/lib:$GAE_HOME/lib/antlr3:$GAE_HOME/lib/ipaddr:$GAE_HOME/lib/webob_1_1_1:$GAE_HOME/lib/fancy_urllib:./common/appenginepatch:.

export DJANGO_SETTINGS_MODULE=settings
