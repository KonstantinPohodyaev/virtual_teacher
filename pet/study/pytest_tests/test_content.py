import pytest
from django.conf import settings

from study.pytest_tests import constant

ANONYMOUS_CLIENT = pytest.lazy_fixture('client')
READER_CLIENT = pytest.lazy_fixture('reader_client')

LIST_OF_STUDIES = pytest.lazy_fixture('list_of_studies')
LIST_OF_CATEGORIES = pytest.lazy_fixture('list_of_categories')


@pytest.mark.parametrize(
    'user_client, url, content, expected_count',
    ((ANONYMOUS_CLIENT, constant.STUDY_LIST_URL, LIST_OF_STUDIES,
      settings.STUDY_COUNT_ON_LIST_PAGE),
     (READER_CLIENT, constant.CATEGORY_LIST_URL, LIST_OF_CATEGORIES,
      settings.CATEGORY_COUNT_ON_LIST_PAGE))
)
def test_study_count(user_client, url, content, expected_count):
    assert len(user_client.get(url).context['page_obj']) == expected_count


@pytest.mark.parametrize(
    'user_client, url, content',
    ((ANONYMOUS_CLIENT, constant.STUDY_LIST_URL, LIST_OF_STUDIES),
     (READER_CLIENT, constant.CATEGORY_LIST_URL, LIST_OF_CATEGORIES))
)
def test_order(user_client, url, content):
    all_dates = [
        obj.created for obj in user_client.get(url).context['page_obj']
    ]
    assert all_dates == sorted(all_dates)


def test_reviews_order(client, list_of_reviews, study_detail_url):
    response = client.get(study_detail_url)
    assert 'reviews' in response.context
    all_dates = [review.created for review in response.context['reviews']]
    assert all_dates == sorted(all_dates, reverse=True)


@pytest.mark.skip(reason='Пока не написал тест')
def test_mark_in_page_of_ListView(client, list_of_studies):
    study = client.get(constant.STUDY_LIST_URL).context['page_obj'][0]
    assert 'mark' in [field.name for field in study._meta.fields]
