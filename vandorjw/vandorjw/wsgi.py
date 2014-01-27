import os
from projectcore.settings.deployment_variables import PROJECT_STATUS

if PROJECT_STATUS == 0:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.production")
elif PROJECT_STATUS == 1:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.stadgine")
elif PROJECT_STATUS == 2:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.local")
elif PROJECT_STATUS == 3:
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.developement")
else:
   pass # PROJECT_STATUS undefined

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
