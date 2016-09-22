# encoding:utf8
"""
Django settings for Project Name project.

For more information on this file, see
https://docs.djangoproject.com/en/dev/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/dev/ref/settings/
"""

import os
import environ

ROOT_DIR = environ.Path(__file__) - 3  # (project_name/src/config/common.py - 3 = project_name/)
APPS_DIR = ROOT_DIR.path('{{cookiecutter.app_name}}')

env = environ.Env()
environ.Env.read_env(ROOT_DIR('.env'))

# APP CONFIGURATION
# ------------------------------------------------------------------------------
DJANGO_APPS = (
    # Default Django apps:
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    # 'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Useful template tags:
    # 'django.contrib.humanize',

    # Admin
    'django.contrib.admin',
)

THIRD_PARTY_APPS = (
    # 'crispy_forms',  # Form layouts
    # 'allauth',  # registration
    # 'allauth.account',  # registration
    # 'allauth.socialaccount',  # registration
    'rest_framework',  # utilities for rest apis
    'rest_framework.authtoken',  # token authentication
    'crispy_forms',
    'django_rq',  # asynchronous queuing
    'versatileimagefield',  # image manipulation
    'rest_framework_swagger',
    'import_export'
)

# Apps specific for this project go here.
LOCAL_APPS = (
    # custom users app
    # 'project_name.users.apps.UsersConfig',
    # Your stuff: custom apps go here
    'authentication',
    'users',
    '{{cookiecutter.app_name}}',
)

# See: https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS

# https://docs.djangoproject.com/en/1.8/topics/http/middleware/
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware'
)

ROOT_URLCONF = 'urls'

# SECRET CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#secret-key
# Note: This key only used for development and testing.
SECRET_KEY = env("DJANGO_SECRET_KEY", default='NotASFDSKAFDJsecret')
# WSGI_APPLICATION = 'wsgi.application'

# Email
# https://docs.djangoproject.com/en/1.10/topics/email/
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
# EMAIL_BACKEND = env('DJANGO_EMAIL_BACKEND', default='django.core.mail.backends.console.EmailBackend')
EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = ROOT_DIR('logs')  # change this to a proper location

EMAIL_HOST = 'smtp.qq.com'
EMAIL_PORT = 465
# 在pycharm中运行时, 注意配置好运行时的环境变量
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER', default='{{cookiecutter.email}}')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD', default='xxxx')
# EMAIL_USE_SSL = True
EMAIL_TIMEOUT = 30

# MANAGER CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#admins
# See: https://docs.djangoproject.com/en/dev/ref/settings/#managers
MANAGERS = (
    ('Author', '{{cookiecutter.email}}'),
)
ADMINS = MANAGERS

# DATABASE CONFIGURATION
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#databases
DATABASES = {
    # Raises ImproperlyConfigured exception if DATABASE_URL not in os.environ
    'default': env.db('DATABASE_URL', default='postgres://localhost/{{cookiecutter.app_name}}_dev'),
}
DATABASES['default']['ATOMIC_REQUESTS'] = True

# General
APPEND_SLASH = True
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'
# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOGIN_REDIRECT_URL = '/'

# Static Files
STATIC_ROOT = ROOT_DIR('staticfiles')
# STATIC_ROOT = 'staticfiles'
# STATICFILES_DIRS = [ROOT_DIR.path('static'), ]
STATICFILES_DIRS = [ROOT_DIR('static'), ]
STATIC_URL = '/static/'
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Media files
MEDIA_ROOT = ROOT_DIR('media')
MEDIA_URL = '/media/'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [STATICFILES_DIRS],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages'
            ],
            # 'loaders':[
            #     ('django.template.loaders.cached.Loader', [
            #         'django.template.loaders.filesystem.Loader',
            #         'django.template.loaders.app_directories.Loader',
            #     ]),
            # ],
        },
    },
]

# DEBUG
# ------------------------------------------------------------------------------
# See: https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool('DJANGO_DEBUG', False)

for config in TEMPLATES:
    config['OPTIONS']['debug'] = DEBUG

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
        'rq_console': {
            'format': '%(asctime)s %(message)s',
            'datefmt': '%H:%M:%S',
        },
    },
    'filters': {
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'handlers': {
        'console': {
            'level': 'INFO',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'rq_console': {
            'level': 'DEBUG',
            'class': 'rq.utils.ColorizingStreamHandler',
            'formatter': 'rq_console',
            'exclude': ['%(asctime)s'],
        },
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'db_file': {
            'level': 'DEBUG',
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': ROOT_DIR('logs/db.log'),
            'formatter': 'simple',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'propagate': True,
        },
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': False,
        },
        'rq.worker': {
            'handlers': ['rq_console'],
            'level': 'DEBUG'
        },
        'django.db': {
            'handlers': ['db_file'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# Custom user app
AUTH_USER_MODEL = 'users.User'

# Django Rest Framework
REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'config.VuetablePagination',
    'PAGE_SIZE': int(os.getenv('DJANGO_PAGINATION_LIMIT', 10)),
    'DATETIME_FORMAT': '%Y-%m-%dT%H:%M:%S%z',
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
        # 'rest_framework.permissions.IsAdminUser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    'DEFAULT_FILTER_BACKENDS': ('rest_framework.filters.DjangoFilterBackend',),
}

# Versatile Image Field
VERSATILEIMAGEFIELD_SETTINGS = {
    # The amount of time, in seconds, that references to created images
    # should be stored in the cache. Defaults to `2592000` (30 days)
    'cache_length': 2592000,
    'cache_name': 'versatileimagefield_cache',
    'jpeg_resize_quality': 70,
    'sized_directory_name': '__sized__',
    'filtered_directory_name': '__filtered__',
    'placeholder_directory_name': '__placeholder__',
    'create_images_on_demand': False
}

# django-rq
# Adds dashboard link for queues in /admin, This will override the default
# admin template so it may interfere with other apps that modify the
# default admin template. If you're using such an app, simply remove this.
RQ_SHOW_ADMIN_LINK = True

# 艺美短信帐号
YIMEI_KEY = env('YIMEI_KEY', default='INPUT_YIMEI_KEY')
YIMEI_SECRET = env('YIMEI_SECRET', default='INPUT_YIMEI_SECRET')

# 阿里帐号
# OSS开通Region和Endpoint对照表
# Region中文名称	Region英文表示	外网Endpoint	ECS访问的内网Endpoint
# 华北 2 (北京)	oss-cn-beijing	oss-cn-beijing.aliyuncs.com	oss-cn-beijing-internal.aliyuncs.com
# tst环境: hxt-{{cookiecutter.app_name}}-tst
# prd环境: hxt-{{cookiecutter.app_name}}-prd
# qa 环境: hxt-{{cookiecutter.app_name}}-qa
ACCESS_KEY_ID = env('ALI_KEY', default='INPUT_ALI_KEY')
ACCESS_KEY_SECRET = env('ALI_SECRET', default='INPUT_ALI_SECRET')
END_POINT = "oss-cn-beijing.aliyuncs.com"
BUCKET_NAME = "hxt-{{cookiecutter.app_name}}-tst"
BUCKET_ACL_TYPE = "public-read"  # private, public-read, public-read-write

# mediafile将自动上传
# DEFAULT_FILE_STORAGE = 'aliyun_oss2_storage.backends.AliyunMediaStorage'
# staticfile将自动上传
# STATICFILES_STORAGE = 'aliyun_oss2_storage.backends.AliyunStaticStorage'

# J800账号
J800_KEY = env('J800_KEY', default='J800_KEY')
J800_SECRET = env('J800_SECRET', default='J800_SECRET')
J800_IP = env('J800_IP', default='192.168.0.1')  # J800要求必须在参数中附上请求机器的IP地址。只有允许的IP地址才能访问服务。
J800_REAL_CHARGE = env.bool('J800_REAL_CHARGE', default=True)  # J800 是真充还是假充。假充的话, 会模拟真充返回结果, 但实际

# Swagger(API DOC)设置
SWAGGER_SETTINGS = {
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'USE_SESSION_AUTH': True,
    'DOC_EXPANSION': 'list',
    'APIS_SORTER': 'alpha'
}

# 微信设置
WECHAT_KEY = env('WECHAT_KEY', default='')
WECHAT_SECRET = env('WECHAT_SECRET', default='')
WECHAT_TOKEN = env('WECHAT_TOKEN', default='')
WECHAT_AESKEY = env('WECHAT_AESKEY', default='')
