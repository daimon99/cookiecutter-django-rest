# -*- coding: utf-8 -*-
"""
Local settings

- Run in Debug mode

- Use console backend for emails

- Add Django Debug Toolbar
- Add django-extensions as app
"""

import os
from .common import *  # noqa

DEBUG = env.bool('DJANGO_DEBUG', default=True)

for config in TEMPLATES:
    config['OPTIONS']['debug'] = DEBUG

# Testing
INSTALLED_APPS += ('django_nose',)
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
# NOSE_ARGS = [
#     ROOT_DIR(),
#     '--nologcapture',
#     '--with-coverage',
#     '--with-progressive',
#     '--cover-package={}'.format(ROOT_DIR())
# ]

# Vesitle Image Field settings
VERSATILEIMAGEFIELD_SETTINGS['create_images_on_demand'] = True

# Django RQ local settings
RQ_QUEUES = {
    'default': {
        'URL': os.getenv('REDISTOGO_URL', 'redis://localhost:6379'),
        'DB': 0,
        'DEFAULT_TIMEOUT': 500,
    },
}

# If unittest, 不创建数据库, 使用当前的数据库。
import sys

if 'test' in sys.argv:
    # pass
    sys.argv.append('--keepdb')
    DATABASES['default']['TEST'] = {
        'MIRROR': 'default'
    }

# mediafile将自动上传
DEFAULT_FILE_STORAGE = 'aliyun_oss2_storage.backends.AliyunMediaStorage'
BUCKET_NAME = "hxt-{{cookiecutter.app_name}}-tst"
# staticfile将自动上传
# STATICFILES_STORAGE = 'aliyun_oss2_storage.backends.AliyunStaticStorage'


CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',
        'LOCATION': ROOT_DIR('caches'),
    }
}

MIDDLEWARE_CLASSES = ('django.middleware.cache.UpdateCacheMiddleware',) + MIDDLEWARE_CLASSES + (
    'django.middleware.cache.FetchFromCacheMiddleware',)
CACHE_MIDDLEWARE_SECONDS = 60 * 0  # 缓存有效期0分钟
