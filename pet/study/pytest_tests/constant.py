from django.urls import reverse

IS_PUBLISHED = True
IS_ON_MAIN = True
DESCRIPTION = 'description'
TITLE = 'title'
NAME = 'name'
SLUG = 'slug'
MARK = 1
TEXT = 'text'

AUTHOR_USERNAME = 'author'
READER_USERNAME = 'reader'
ADMIN_USERNAME = 'admin'
READER_ADMIN_USERNAME = 'another_admin'

STUDY_LIST_URL = reverse('study:list')
STUDY_CREATE_URL = reverse('study:create')

CATEGORY_LIST_URL = reverse('study:category_list')
CATEGORY_CREATE_URL = reverse('study:category_create')

LOGIN_URL = reverse('login')
LOGOUT_URL = reverse('logout')
REGISTRATION_URL = reverse('registration')
