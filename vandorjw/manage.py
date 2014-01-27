#!/usr/bin/env python
import os
import sys
from vandorjw.settings.deployment_variables import PROJECT_STATUS

if __name__ == "__main__":
    if PROJECT_STATUS == 0:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vandorjw.settings.production")
    elif PROJECT_STATUS == 1:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vandorjw.settings.stading")
    elif PROJECT_STATUS == 2:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vandorjw.settings.local")
    elif PROJECT_STATUS == 3:
        os.environ.setdefault("DJANGO_SETTINGS_MODULE", "vandorjw.settings.developement")
    else:
       pass # PROJECT_STATUS undefined

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
