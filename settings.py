import os


import djcelery

djcelery.setup_loader()

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
SITE_ID = 2
SITE_BUIDS = []



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ph9g4%rc7&@v^elr34!6hf89dyll_*#h3ij%6x_su77x8b_rm2'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1',]


LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/redirect/'
LOGIN_ERROR_URL    = '/login-error/'
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/redirect/'
SOCIAL_AUTH_NEW_USER_REDIRECT_URL = '/registrations/change_github_pass'
SOCIAL_AUTH_COMPLETE_URL_NAME  = 'socialauth_complete'
SOCIAL_AUTH_ASSOCIATE_URL_NAME = 'socialauth_associate_complete'


AUTHENTICATION_BACKENDS = (
    'social.backends.github.GithubOAuth2',
    'social.backends.linkedin.LinkedinOAuth',
    'backends.CaseInsensitiveAuthBackend',
    'django.contrib.auth.backends.ModelBackend',  # default
    'django.contrib.auth.backends.RemoteUserBackend',  # http
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = 'webtechno49@gmail.com'
SERVER_EMAIL = 'webtechno49@gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'webtechno49@gmail.com'
EMAIL_HOST_PASSWORD = 'Quest@123'

# Application definition


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.sitemaps',
    'django.contrib.flatpages',
    'django.contrib.redirects',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    'django_extensions',
    'usermodel',
    'myprofile',
    'registration',
    'eregistration',
    'company',
    'postajob',
    'password_reset',
    'suggestiondata',
    'savesearch',
    'dashboard',
    'questomessages',
    'filetransfers',
    'bootstrap_pagination',
    'newsletter',
    'edashboard',
    'chartjs',
    'djcelery',
    'kombu.transport.django',
    'social.apps.django_app.default',
    'multiselectfield',
)



#Broker settings

BROKER_URL = "django://"
BROKER_PORT = 5672
BROKER_USER = "guest"
BROKER_VHOST = "/"

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'questo.middleware.PasswordChangeRedirectMiddleware',
)

FILE_UPLOAD_HANDLERS = (
    "django.core.files.uploadhandler.MemoryFileUploadHandler",
    "django.core.files.uploadhandler.TemporaryFileUploadHandler",
)

ROOT_URLCONF = 'questo.urls'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:8000',
    }
}

TEMPLATE_DIRS = [
    os.path.join(BASE_DIR,"templates"),
    ]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        #'DIRS': (os.path.join(BASE_DIR, 'templates'),),
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.contrib.auth.context_processors.auth',
                # 'django.core.context_processors.i18n',
                'django.core.context_processors.media',
                'django.template.context_processors.request',
                'django.core.context_processors.request',

                'django.contrib.messages.context_processors.messages',
                'social.apps.django_app.context_processors.backends',
                'social.apps.django_app.context_processors.login_redirect',
            ],
        },
    },
]

WSGI_APPLICATION = 'questo.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'questoio',
        'USER': 'root',
        'PASSWORD': '123',
        'HOST': 'localhost',
        'PORT': '',
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = False

USE_L10N = False

USE_TZ = True

AUTH_USER_MODEL = 'usermodel.User'
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static","static_root")


MEDIA_URL = '/media/'
STATIC_ROOT = os.path.join(BASE_DIR, "static","static_root")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static","static_dirs"),
    )



# email types
ACTIVATION = 1
CREATE_CONTACT_RECORD = 3
FORGOTTEN_PASSWORD = 4
GENERIC = 5
INACTIVITY = 6
INVITATION = 7
INVOICE = 8
PARTNER_SAVED_SEARCH_RECIPIENT_OPTED_OUT = 10
POSTING_REQUEST_CREATED = 11
SAVED_SEARCH = 12
SAVED_SEARCH_DIGEST = 13
SAVED_SEARCH_DISABLED = 14
SAVED_SEARCH_INITIAL = 15
SAVED_SEARCH_UPDATED = 16


FORM_DATE_FORMAT = '%d %B, %Y'

DATE_INPUT_FORMATS = (
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y', '%b %d %Y', '%b %d, %Y',
    '%d %b %Y', '%d %b, %Y', '%B %d %Y', '%B %d, %Y', '%d %B %Y',
    '%d %B, %Y',
)



DATE_INPUT_FORMATS += (FORM_DATE_FORMAT,)

PROFILE_COMPLETION_MODULES = (
    'basicinfo',
    'experience',
    'skill',
    'education',
    # 'social',
    'resume',
)

import mimetypes
mimetypes.add_type("image/svg+xml", ".svg", True)
mimetypes.add_type("image/svg+xml", ".svgz", True)

SOCIAL_AUTH_GITHUB_KEY = '4d1ca71b8ff2f8d1d053'
SOCIAL_AUTH_GITHUB_SECRET = '01273aa1947ef690a18f411db13047b07164f067'
SOCIAL_AUTH_GITHUB_SCOPE = ['user','public_repo','notifications']
SOCIAL_AUTH_GITHUB_EXTRA_DATA = ['public_repo']

SOCIAL_AUTH_LINKEDIN_KEY = '75pzdo5bjf6u6v' # The LinkedIn application "API Key"
SOCIAL_AUTH_LINKEDIN_SECRET = 'HzcOXWvT5jKe7Xkz' # The LinkedIn application "Secret Key"
SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile','r_emailaddress','rw_company_admin','w_share']
SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
    'first-name',
    'last-name',
    'email-address',
    'headline', # The job title
    'positions', # Used to retrieve the company
]
SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
                       ('first-name', 'first_name'),
                       ('last-name', 'last_name'),] + [(field, field.replace('-', '_'), True) for field in SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS],
# SOCIAL_AUTH_LINKEDIN_KEY
# LINKEDIN_CONSUMER_KEY = '754lrk46s6znch'
# SOCIAL_AUTH_LINKEDIN_SECRET = 'FjzEjUMJFAt6L2ep'
# SOCIAL_AUTH_LINKEDIN_SCOPE = ['r_basicprofile', 'r_emailaddress',]
# SOCIAL_AUTH_LINKEDIN_FIELD_SELECTORS = [
#     'first-name',
#     'last-name',
#     'email-address',
#     'headline', # The job title
#     'positions', # Used to retrieve the company
# ]
# SOCIAL_AUTH_LINKEDIN_OAUTH2_EXTRA_DATA = [('id', 'id'),
#                        ('first-name', 'first_name'),
#                        ('last-name', 'last_name'),]



FIELDS_STORED_IN_SESSION = ['key']
USERNAME_IS_FULL_EMAIL = True
# GITHUB_EXTENDED_PERMISSIONS = ['user','public_repo']
# GITHUB_EXTRA_DATA = ['user','public_repo']
# GITHUB_OAUTH_SCOPES = ['user','public_repo']
# SOCIAL_AUTH_USERNAME_IS_FULL_EMAIL = True
# SOCIAL_AUTH_URL_NAMESPACE = 'social'
# end of email check
SOCIAL_AUTH_PIPELINE = (
    # http://psa.matiasaguirre.net/docs/pipeline.html
    # http://python-social-auth.readthedocs.org/en/latest/use_cases.html
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.user.get_username',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.create_user',
    'registration.views.load_user',
    'social.pipeline.social_auth.associate_user',
    # 'social.pipeline.user.user_details',
    'registration.models.create_user_profile',
    'social.pipeline.debug.debug',
)
SOCIAL_AUTH_USER_MODEL = AUTH_USER_MODEL


# github accesstoken : 526aa286e9a98f68b8a338deb1ae14fc3dcb1bb5