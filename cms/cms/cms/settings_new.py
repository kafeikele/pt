# coding: utf-8
"""
Django settings for cms project.

Generated by 'django-admin startproject' using Django 1.8.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import tempfile

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'd#)ds)3b)s2li@30d3la)s%fo1b&z=ohbgtrys@+uhy#yziid4'

LOGIN_URL = '/accounts/login/'

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
    ('pt', 'pt_admin@putao.cn'),
)

# 邮箱设置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'

EMAIL_HOST = 'smtp.exmail.qq.com'

EMAIL_PORT = 25

EMAIL_HOST_USER = SERVER_EMAIL = 'pt_admin@putao.cn'

EMAIL_HOST_PASSWORD = 'putao2015'

PTLOGSUBJECT = 'Debug'

EMAIL_SUBJECT_PREFIX = '[PutaoLife]'

MANAGERS = ADMINS

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.humanize',
    # 'cache',
    'main',
    'config',
    'pt_open',
    'activity',
    'tags',
    'tab',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.middleware.locale.LocaleMiddleware',
)

# ROOT_URLCONF = 'cms.urls'
URL_ENTRY = {"api": "cms.api_urls", "cms": "cms.urls"}
URL_FOR = ""
ROOT_URLCONF = URL_ENTRY.get(URL_FOR, "cms.urls")

WSGI_APPLICATION = 'cms.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

"""
    #本地
    C:\Program Files\MySQL\MySQL Server 5.6\bin>mysqldump.exe -h 192.168.1.247
    -u root -p123456 --database pt_cms_db > d:\cms.sql
    修改cms.sql文件，把pt_cms_db改为pt_cms_db2
    C:\Program Files\MySQL\MySQL Server 5.6\bin>mysql.exe -h 192.168.1.247 -u
    root -p123456 < d:\cms.sql
    测试
    mysqldump -h 10.117.51.209 -u root -pputao1234 --database
    pt_cms_db > cms.sql
    修改cms.sql文件，把pt_cms_db改为pt_cms_online
    mysql -h 10.117.51.209 -u root -pputao1234 < cms.sql
"""

# 安装类型，
# 1是本地，
# 2是测试环境，
# 3是正式环境
# 4是联想
INSTALL_TYPE = 1

# 更改mysql支持事务
# ALTER TABLE  tableName TYPE = INNODB;
# 如果mysql是高版本时建议使用： ALTER TABLE  tableName ENGINE=INNODB;



if INSTALL_TYPE == 1:
    # 本地
    DEBUG = True
    CMS_CHECK_ON = True
    CMS_URL_ROOT = ""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_cms_db',
            'USER': 'root',
            'PASSWORD': 'putao123',
            'HOST': '192.168.1.240',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
        'auth_db': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_auth_admin',
            'USER': 'root',
            'PASSWORD': 'putao123',
            'HOST': '192.168.1.240',
            'PORT': '',
        },
        # 'online': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'pt_cms_db2',
        #     'USER': 'root',
        #     'PASSWORD': 'putao123',
        #     'HOST': '192.168.1.240',
        #     'PORT': '',
        #     'ATOMIC_REQUESTS': True
        # },
        'open': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_open',
            'USER': 'root',
            'PASSWORD': 'putao123',
            'HOST': '192.168.1.240',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
        'activity': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_activity_coupon',
            'USER': 'root',
            'PASSWORD': 'putao1234',
            'HOST': '120.26.214.19',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
        # 'user': {
        #     'ENGINE': 'django.db.backends.mysql',
        #     'NAME': 'pt_db',
        #     'USER': 'root',
        #     'PASSWORD': 'putao123',
        #     'HOST': '192.168.1.240',
        #     'PORT': '',
        #     'ATOMIC_REQUESTS': True
        # },
    }
    STATIC_ROOT = ''
    STATIC_URL = '/static/'
elif INSTALL_TYPE == 2:
    # 测试环境
    DEBUG = True
    CMS_CHECK_ON = True
    CMS_URL_ROOT = ""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_cms_db_backup',
            'USER': 'root',
            'PASSWORD': 'putao1234',
            # 'HOST': '10.117.51.209',
            'HOST': '120.26.214.19',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
        'online': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_cms_db',
            'USER': 'root',
            'PASSWORD': 'putao1234',
            # 'HOST': '10.117.51.209',
            'HOST': '120.26.214.19',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
    }
    STATIC_ROOT = '/root/cms/cms/static/'
    STATIC_URL = '/static/'
elif INSTALL_TYPE == 3:
    # 正式环境
    DEBUG = False
    CMS_CHECK_ON = False
    CMS_URL_ROOT = ""
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_cms_db',
            'USER': 'pt_cms',
            'PASSWORD': 'cms2015',
            'HOST': 'rds2seb3yiymjlg8gumzv.mysql.rds.aliyuncs.com',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
    }
    STATIC_ROOT = '/usr/local/new-cms/cms/static/'
    STATIC_URL = '/static/'
elif INSTALL_TYPE == 4:
    # 联想环境
    DEBUG = False
    CMS_CHECK_ON = True
    CMS_URL_ROOT = "v2/cms_test/"
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_cms_db',
            'USER': 'root',
            'PASSWORD': 'putao123',
            'HOST': '192.168.1.240',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
        'online': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': 'pt_cms_db2',
            'USER': 'root',
            'PASSWORD': 'putao123',
            'HOST': '192.168.1.240',
            'PORT': '',
            'ATOMIC_REQUESTS': True
        },
    }
    STATIC_ROOT = '/mnt/hgfs/cms/static/'
    STATIC_URL = '/%sstatic/' % CMS_URL_ROOT
    # 联想的稍有不同，css和js需要把static替换为/v2/cms_root/static/,
    # 请运行下lenovo.py脚本进行替换

    # 联想nginx配置
    # upstream pt_cms_test{
    #     server 192.168.1.234:8000;
    # }
    # location /v2/cms_test/ {
    #     proxy_pass http://pt_cms_test;
    #     proxy_redirect off;
    #     proxy_set_header Host $host;
    #     proxy_set_header X-Real-IP $remote_addr;
    #     proxy_set_header X-Forwarded-For $remote_addr;
    #     client_max_body_size 20m;
    #     client_body_buffer_size 256k;
    #     proxy_connect_timeout 90;
    #     proxy_send_timeout 90;
    #     proxy_read_timeout 90;
    #     proxy_buffer_size 128k;
    #     proxy_buffers 4 64k;
    #     proxy_busy_buffers_size 128k;
    #     proxy_temp_file_write_size 128k;
    # }


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

AUTHENTICATION_BACKENDS = (
    'common.myuserbackend.MyRemoteUserBackend',
    'django.contrib.auth.backends.ModelBackend',
)


LANGUAGE_CODE = 'zh-hans'

DATABASE_ROUTERS = ['cms.dbsettings.AuthRouter']

TIME_ZONE = 'Asia/Shanghai'
# TIME_ZONE = 'UTC'
USE_I18N = True

USE_L10N = True

USE_TZ = False

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.join(os.path.dirname(
        BASE_DIR), "frontend"), "static"),
)

STATIC_PATH = os.path.join(os.path.join(os.path.dirname(
    BASE_DIR), "frontend"), "static")

TEMPLATES_PATH = os.path.join(os.path.join(os.path.dirname(
    BASE_DIR), "frontend"), "templates")

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(os.path.join(os.path.dirname(BASE_DIR),
                                           "frontend"), "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# log config
LOG_DIR = tempfile.gettempdir() + '/cms/logs/'
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s [%(threadName)s:%(thread)d] [%(name)s:%(lineno)d] [%(levelname)s]- %(message)s'
        },
    },
    'filters': {
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler',
            'include_html': True,
        },
        'default': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            # 或者直接写路径：'c:\logs\all.log',
            'filename': os.path.join(LOG_DIR, 'console.log'),
            'maxBytes': 1024 * 1024 * 1024,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'standard'
        },
        'request_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            # 或者直接写路径：'filename':'c:\logs\request.log''
            'filename': os.path.join(LOG_DIR, 'except.log'),
            'maxBytes': 1024 * 1024 * 1024,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'scprits_handler': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            # 或者直接写路径：'filename':'c:\logs\script.log'
            'filename': os.path.join(LOG_DIR, 'script.log'),
            'maxBytes': 1024 * 1024 * 1024,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['default', 'console'],
            'level': 'INFO',
            'propagate': False
        },
        'main.app': {
            'handlers': ['default', 'console'],
            'level': 'ERROR',
            'propagate': True
        },
        'config.app': {
            'handlers': ['default', 'console'],
            'level': 'ERROR',
            'propagate': True
        },
        'django.request': {
            'handlers': ['request_handler'],
            'level': 'INFO',
            'propagate': False
        },
        'scripts': {  # 脚本专用日志
            'handlers': ['scprits_handler'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}

# IP限制
PT_IPLIMIT = {"default": [],
              "test": ["192.168.1.165"]
              }