import os, ldap
from django_auth_ldap.config import LDAPSearch
#from django_auth_ldap.config import LDAPSearch, GroupOfNamesType

# Django settings for voipdb project.

DEBUG = False
#TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

#DATABASES = {
#    'default': {
#        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
#        #'OPTIONS': { 'options': '-c search_path=public'},   # use defined schema in postgresql
#        'NAME': 'ff_voip',                                  # Or path to database file if using sqlite3.
#        'USER': 'theuser',                                  # Not used with sqlite3.
#        'PASSWORD': 'thepass',                              # Not used with sqlite3.
#        'HOST': 'localhost',                                # Set to empty string for localhost. Not used with sqlite3.
#        'PORT': '',                                         # Set to empty string for default. Not used with sqlite3.
#     }
#}
# these settings live in databases.py which is on .gitignore list for security reasons
from databases import *

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/{{ docs_version }}/ref/settings/#allowed-hosts
ALLOWED_HOSTS = ['voip.funkfeuer.at', 'www.voip.funkfeuer.at',]

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# On Unix systems, a value of None will cause Django to use the same
# timezone as the operating system.
# If running in a Windows environment this must be set to the same as your
# system time zone.
#TIME_ZONE = 'America/Chicago'
TIME_ZONE = 'Europe/Vienna'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'de-at'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale
USE_L10N = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = ''

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = ''

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = ''

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

# URL prefix for admin static files -- CSS, JavaScript and images.
# Make sure to use a trailing slash.
# Examples: "http://foo.com/static/admin/", "/static/admin/".
ADMIN_MEDIA_PREFIX = '/static/admin/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'nptnc)(crw*xl^mmqcf&@@60w)6-2+45o2b3_k@66#d#=-t1%5'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

ROOT_URLCONF = 'voipdb.urls'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join('/home/christoph/voipdb', 'templates')
)

LOGIN_URL='/login/'
LOGIN_REDIRECT_URL='/'

CACERTS = '/etc/ssl/certs/cacert.pem'
# Baseline configuration.
AUTH_LDAP_SERVER_URI = "ldaps://ldap.funkfeuer.at"

#AUTH_LDAP_USER_SEARCH = LDAPSearch("ou=users,dc=funkfeuer,dc=at",
#    ldap.SCOPE_SUBTREE, "(uid=%(user)s)")
AUTH_LDAP_GLOBAL_OPTIONS = {
    ldap.OPT_X_TLS_REQUIRE_CERT: True, # (TLS equivalent: TLS_REQCERT)
    ldap.OPT_REFERRALS: True,
} 
AUTH_LDAP_USER_DN_TEMPLATE = 'uid=%(user)s,ou=Users,dc=funkfeuer,dc=at'
AUTH_LDAP_BIND_AS_AUTHENTICATING_USER = True
#AUTH_LDAP_ALWAYS_UPDATE_USER = True
# setting the following two options are needed so LDAPBackend().populate_user() doesnt generate an error in django-ldap-debug.log
#AUTH_LDAP_BIND_DN = "vchrizz"
#AUTH_LDAP_BIND_PASSWORD = "changeme"
AUTH_LDAP_USER_ATTR_MAP = {
#    "id": "uidNumber",
    "username": "uid",
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail",
    "password": "userPassword",
}
AUTH_LDAP_PROFILE_ATTR_MAP = {
    "uid": "uid",
    "cn": "cn",
    "sn": "sn",
    "givenName": "givenName",
    "userPassword": "userPassword",
    "shadowLastChange": "shadowLastChange",
    "shadowMax": "shadowMax",
    "shadowWarning": "shadowWarning",
    "loginShell": "loginShell",
    "uidNumber": "uidNumber",
    "gidNumber": "gidNumber",
    "homeDirectory": "homeDirectory",
    "gecos": "gecos",
    "mail": "mail",
    "l": "l",
    "telephoneNumber": "telephoneNumber",
}
#AUTH_LDAP_BIND_PASSWORD = '%(password)s'
#AUTH_LDAP_GROUP_TYPE = GroupOfNamesType(name_attr="cn")

AUTH_PROFILE_MODULE = 'voip.UserProfile'

# Keep ModelBackend around for per-user permissions and maybe a local
# superuser.
AUTHENTICATION_BACKENDS = (
    'django_auth_ldap.backend.LDAPBackend',
#    'django.contrib.auth.backends.ModelBackend',
#    'voip.backends.RedeemerAuth',
)
#AUTHENTICATION_BACKENDS = ('voip.backends.RedeemerAuth',)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    #'django.contrib.admindocs',
    'voip',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format' : "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt' : "%d/%b/%Y %H:%M:%S",
        },
        'simple': {
            'format': '%(levelname)s %(message)s',
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
        },
        'file': {
            'level': 'DEBUG',
            'class': 'logging.FileHandler',
            'filename': '/tmp/django-debug.log',
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            #'handlers': ['mail_admins'],
            'handlers': ['file'],
            'level': 'DEBUG',
            'propagate': True,
        },
        'voipdb': {
            'handlers': ['file'],
            'level': 'DEBUG',
        },
    }
}
