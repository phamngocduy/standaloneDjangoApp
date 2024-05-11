import inspect, os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
from django.db import connection
# Ensure settings are read
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
# Your application specific imports
from database.models import Test

# Delete all data
def clean_data():
    Test.objects.all().delete()

# Test Django Model Setup
def test_setup():
    try:
        clean_data()
        test = Test(name='DUY')
        test.save()
        # Check test table is not empty
        assert Test.objects.count() > 0
        print('Django Model Setup completed.')
    except AssertionError as exception:
        print('Django Model setup failed with error:')
        raise(exception)
    except Exception as error:
        print('Unexpected error', error)

test_setup()
