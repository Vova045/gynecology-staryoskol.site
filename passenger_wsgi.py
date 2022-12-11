# -*- coding: utf-8 -*-
import os, sys
sys.path.insert(0, '/var/www/u1815677/data/www/gynecology-staryoskol.site/gynecology_staryoskol')
sys.path.insert(1, '/var/www/u1815677/data/env/lib/python3.7/site-packages')
os.environ['DJANGO_SETTINGS_MODULE'] = 'gynecology_staryoskol.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()