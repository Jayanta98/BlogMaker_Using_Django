#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
#this is the manage file ----to run---> python manage.py runserver
#for help---- python manage.py
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'JGproject.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
