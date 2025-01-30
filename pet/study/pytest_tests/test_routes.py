from http import HTTPStatus

import pytest
from pytest_django.asserts import assertRedirects

from study.pytest_tests import constant

ANONYMOUS_CLIENT = pytest.lazy_fixture('client')
ADMIN_CLIENT = pytest.lazy_fixture('admin_user_client')
READER_CLIENT = pytest.lazy_fixture('reader_client')

STUDY_DETAIL_URL = pytest.lazy_fixture('study_detail_url')
STUDY_UPDATE_URL = pytest.lazy_fixture('study_update_url')
STUDY_REDIRECT_UPDATE_URL = pytest.lazy_fixture('study_redirect_update_url')
STUDY_DELETE_URL = pytest.lazy_fixture('study_delete_url')
STUDY_REDIRECT_DELETE_URL = pytest.lazy_fixture('study_redirect_delete_url')

CATEGORY_REDIRECT_LIST_URL = pytest.lazy_fixture('category_redirect_list_url')
CATEGORY_DETAIL_URL = pytest.lazy_fixture('category_detail_url')
CATEGORY_REDIRECT_DETAIL_URL = pytest.lazy_fixture(
    'category_redirect_detail_url'
)
CATEGORY_UPDATE_URL = pytest.lazy_fixture('category_update_url')
CATEGORY_REDIRECT_UPDATE_URL = pytest.lazy_fixture(
    'category_redirect_update_url'
)
CATEGORY_DELETE_URL = pytest.lazy_fixture('category_delete_url')
CATEGORY_REDIRECT_DELETE_URL = pytest.lazy_fixture(
    'category_redirect_delete_url'
)


@pytest.mark.parametrize(
    'url, user_client, status',
    (
        (constant.STUDY_LIST_URL, ANONYMOUS_CLIENT, HTTPStatus.OK),
        (constant.LOGIN_URL, ANONYMOUS_CLIENT, HTTPStatus.OK),
        (constant.LOGOUT_URL, ANONYMOUS_CLIENT, HTTPStatus.OK),
        (constant.REGISTRATION_URL, ANONYMOUS_CLIENT, HTTPStatus.OK),
        (STUDY_DETAIL_URL, ANONYMOUS_CLIENT, HTTPStatus.OK),
        (STUDY_UPDATE_URL, ANONYMOUS_CLIENT, HTTPStatus.FOUND),
        (STUDY_UPDATE_URL, ADMIN_CLIENT, HTTPStatus.OK),
        (STUDY_UPDATE_URL, READER_CLIENT, HTTPStatus.FORBIDDEN),
        (STUDY_DELETE_URL, ANONYMOUS_CLIENT, HTTPStatus.FOUND),
        (STUDY_DELETE_URL, ADMIN_CLIENT, HTTPStatus.OK),
        (STUDY_DELETE_URL, READER_CLIENT, HTTPStatus.FORBIDDEN),
    )
)
def test_pages_availability(url, user_client, status, study):
    assert user_client.get(url).status_code == status


@pytest.mark.parametrize(
    'url, expected_url',
    (
        (STUDY_UPDATE_URL, STUDY_REDIRECT_UPDATE_URL),
        (STUDY_DELETE_URL, STUDY_REDIRECT_DELETE_URL),
        (constant.CATEGORY_LIST_URL, CATEGORY_REDIRECT_LIST_URL),
        (CATEGORY_DETAIL_URL, CATEGORY_REDIRECT_DETAIL_URL),
        (CATEGORY_UPDATE_URL, CATEGORY_REDIRECT_UPDATE_URL),
        (CATEGORY_DELETE_URL, CATEGORY_REDIRECT_DELETE_URL),
    )
)
def test_pages_redirects_for_anon_user(url, expected_url, client):
    assertRedirects(client.get(url), expected_url)
