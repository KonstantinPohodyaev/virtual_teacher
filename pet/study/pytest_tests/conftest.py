import pytest
from django.conf import settings
from django.test.client import Client
from django.urls import reverse

from study.models import Category, Review, Study
from study.pytest_tests import constant


@pytest.fixture(autouse=True)
def enable_access_db_for_all_test(db):
    pass


@pytest.fixture
def author(django_user_model):
    return django_user_model.objects.create(username=constant.AUTHOR_USERNAME)


@pytest.fixture
def author_client(author):
    client = Client()
    client.force_login(author)
    return client


@pytest.fixture
def reader(django_user_model):
    return django_user_model.objects.create(username=constant.READER_USERNAME)


@pytest.fixture
def reader_client(reader):
    client = Client()
    client.force_login(reader)
    return client


@pytest.fixture
def admin_user(django_user_model):
    return django_user_model.objects.create(
        username=constant.ADMIN_USERNAME, is_staff=True)


@pytest.fixture
def admin_user_client(admin_user):
    client = Client()
    client.force_login(admin_user)
    return client


@pytest.fixture
def reader_admin_user(django_user_model):
    return django_user_model.objects.create(
        username=constant.READER_ADMIN_USERNAME, is_staff=True)


@pytest.fixture
def reader_admin_user_client(reader_admin_user):
    client = Client()
    client.force_login(reader_admin_user)
    return client


@pytest.fixture
def study(admin_user):
    return Study.objects.create(
        is_published=constant.IS_PUBLISHED,
        is_on_main=constant.IS_ON_MAIN,
        title=constant.TITLE,
        slug=constant.SLUG,
        description=constant.DESCRIPTION,
        author=admin_user
    )


@pytest.fixture
def study_detail_url(study):
    return reverse('study:detail', args=(study.id,))


@pytest.fixture
def study_update_url(study):
    return reverse('study:update', args=(study.id,))


@pytest.fixture
def study_redirect_update_url(study_update_url):
    return f'{constant.LOGIN_URL}?next={study_update_url}'


@pytest.fixture
def study_delete_url(study):
    return reverse('study:delete', args=(study.id,))


@pytest.fixture
def study_redirect_delete_url(study_delete_url):
    return f'{constant.LOGIN_URL}?next={study_delete_url}'


@pytest.fixture
def category(admin_user):
    return Category.objects.create(
        is_published=constant.IS_PUBLISHED,
        is_on_main=constant.IS_ON_MAIN,
        name=constant.NAME,
        slug=constant.SLUG,
        description=constant.DESCRIPTION,
        author=admin_user
    )


@pytest.fixture
def category_redirect_list_url():
    return f'{constant.LOGIN_URL}?next={constant.CATEGORY_LIST_URL}'


@pytest.fixture
def category_detail_url(category):
    return reverse('study:category_detail', args=(category.slug,))


@pytest.fixture
def category_redirect_detail_url(category_detail_url):
    return f'{constant.LOGIN_URL}?next={category_detail_url}'


@pytest.fixture
def category_update_url(category):
    return reverse('study:category_update', args=(category.slug,))


@pytest.fixture
def category_redirect_update_url(category_update_url):
    return f'{constant.LOGIN_URL}?next={category_update_url}'


@pytest.fixture
def category_delete_url(category):
    return reverse('study:category_delete', args=(category.slug,))


@pytest.fixture
def category_redirect_delete_url(category_delete_url):
    return f'{constant.LOGIN_URL}?next={category_delete_url}'


@pytest.fixture
def review_redirect_create_url(study_detail_url):
    return f'{study_detail_url}#reviews'


@pytest.fixture
def list_of_studies(author):
    Study.objects.bulk_create(
        (
            Study(
                is_published=constant.IS_PUBLISHED,
                is_on_main=constant.IS_ON_MAIN,
                title=constant.TITLE,
                slug=f'{constant.SLUG}_{index}',
                author=author
            )
            for index in range(settings.STUDY_COUNT_ON_LIST_PAGE + 1)
        )
    )


@pytest.fixture
def list_of_categories(author):
    Category.objects.bulk_create(
        (
            Category(
                is_published=constant.IS_PUBLISHED,
                is_on_main=constant.IS_ON_MAIN,
                name=constant.NAME,
                slug=f'{constant.SLUG}_{index}',
                author=author
            )
            for index in range(settings.CATEGORY_COUNT_ON_LIST_PAGE + 1)
        )
    )


@pytest.fixture
def list_of_reviews(author, study):
    Review.objects.bulk_create(
        Review(
            text=constant.TEXT,
            mark=(constant.MARK + index),
            author=author,
            study=study
        )
        for index in range(4)
    )
