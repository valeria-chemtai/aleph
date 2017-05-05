from os import environ as env

DEBUG = False
ASSETS_DEBUG = False
CACHE = True
SECRET_KEY = env.get('ALEPH_SECRET_KEY')

APP_TITLE = env.get('ALEPH_APP_TITLE', 'Aleph')
APP_NAME = env.get('ALEPH_APP_NAME', 'aleph')
APP_BASEURL = env.get('ALEPH_APP_URL')
APP_LOGO = env.get('ALEPH_LOGO')
APP_FAVICON = env.get('ALEPH_FAVICON')
OPENGAZETTES_URL = env.get('OPENGAZETTES_URL',
                           'http://opengazettes.or.ke')
# Name given to a citizen of the country you are deploying Aleph to
# e.g Afghan, Indian, Maltese
# More here: https://en.wikipedia.org/wiki/Lists_of_people_by_nationality
NATIONALITY = env.get('NATIONALITY', 'Kenyan')

SAMPLE_SEARCHES = ['SASSA', '"call for comment"', 'sheriff auction']

ELASTICSEARCH_URL = env.get('ALEPH_ELASTICSEARCH_URI')

SQLALCHEMY_DATABASE_URI = env.get('ALEPH_DATABASE_URI')

PREFERRED_URL_SCHEME = env.get('ALEPH_URL_SCHEME')

REGEX_ENTITIES = False
# don't try to classify languages
LANGUAGES = []

MAIL_FROM = env.get('MAIL_FROM')
MAIL_SERVER = env.get('MAIL_HOST')
MAIL_ADMINS = [env.get('MAIL_ADMIN')]
MAIL_USERNAME = env.get('MAIL_USERNAME')
MAIL_PASSWORD = env.get('MAIL_PASSWORD')

# this is GMail-specific, factor it out?
MAIL_USE_TLS = True
MAIL_PORT = 587

CELERY_BROKER_URL = env.get('ALEPH_BROKER_URI')
BROKER_TRANSPORT_OPTIONS = {
    'region': 'eu-west-1',
    'queue_name_prefix': '%s.' % env.get('ALEPH_APP_NAME', 'aleph')
}

NEO4J_URI = env.get('ALEPH_NEO4J_URI')

ARCHIVE_TYPE = env.get('ALEPH_ARCHIVE_TYPE', 's3')
ARCHIVE_AWS_KEY_ID = env.get('AWS_ACCESS_KEY_ID')
ARCHIVE_AWS_SECRET = env.get('AWS_SECRET_ACCESS_KEY')
ARCHIVE_BUCKET = env.get('ALEPH_ARCHIVE_BUCKET')
ARCHIVE_PATH = env.get('ALEPH_ARCHIVE_PATH')

OAUTH = [{
    'name': 'facebook',
    'base_url': 'https://graph.facebook.com/',
    'request_token_url': None,
    'access_token_url': 'oauth/access_token',
    'authorize_url': 'https://www.facebook.com/dialog/oauth',
    'consumer_key': env.get('FACEBOOK_OAUTH_KEY'),
    'consumer_secret': env.get('FACEBOOK_OAUTH_SECRET'),
    'request_token_params': {'scope': 'email'}
}, {
    'name': 'google',
    'consumer_key': env.get('GOOGLE_OAUTH_KEY'),
    'consumer_secret': env.get('GOOGLE_OAUTH_SECRET'),
    'request_token_params': {
        'scope': 'https://www.googleapis.com/auth/userinfo.email'
    },
    'base_url': 'https://www.googleapis.com/oauth2/v1/',
    'request_token_url': None,
    'access_token_method': 'POST',
    'access_token_url': 'https://accounts.google.com/o/oauth2/token',
    'authorize_url': 'https://accounts.google.com/o/oauth2/auth',
}]

OCR_PDF_PAGES = env.get('ALEPH_PDF_OCR_IMAGE_PAGES', 'true')
OCR_PDF_PAGES = OCR_PDF_PAGES.strip().lower() == "true"

MAX_CONTENT_LENGTH = int(env.get('ALEPH_MAX_CONTENT_LENGTH',
                                 500 * 1024 * 1024))

# GA_TRACKING_ID = 'UA-48399585-47'

# Tell users to email the admins if their search has results in collections
# that are hidden from them?
ALLOW_PEEKING = False
