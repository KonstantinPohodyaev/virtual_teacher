import pytest
from django.urls import reverse
from pytest_django.asserts import assertRedirects

from study.models import Category, Review, Study
from study.pytest_tests import constant

STUDY_FORM_DATA = {
    'is_published': constant.IS_PUBLISHED,
    'is_on_main': constant.IS_ON_MAIN,
    'title': constant.TITLE,
    'description': constant.DESCRIPTION,
    'slug': constant.SLUG,
}
CATEGORY_FORM_DATA = {
    'is_published': constant.IS_PUBLISHED,
    'is_on_main': constant.IS_ON_MAIN,
    'description': constant.DESCRIPTION,
    'name': constant.NAME,
    'slug': constant.SLUG,
}
REVIEW_FORM_DATA = {
    'text': constant.TEXT,
    'mark': constant.MARK,
}


def test_auth_user_cant_create_study(reader_client):
    reader_client.post(constant.STUDY_CREATE_URL, STUDY_FORM_DATA)
    assert Study.objects.count() == 0


def test_admin_user_can_create_study(admin_user_client, admin_user, author):
    response = admin_user_client.post(
        constant.STUDY_CREATE_URL, STUDY_FORM_DATA)
    assert Study.objects.count() == 1
    study = Study.objects.get()
    assertRedirects(
        response,
        reverse('study:detail', args=(study.id,))
    )
    assert study.is_published == STUDY_FORM_DATA['is_published']
    assert study.is_on_main == STUDY_FORM_DATA['is_on_main']
    assert study.title == STUDY_FORM_DATA['title']
    assert study.slug == STUDY_FORM_DATA['slug']
    assert study.description == STUDY_FORM_DATA['description']
    assert study.author == admin_user


def test_auth_user_cant_create_category(author_client):
    author_client.post(constant.CATEGORY_CREATE_URL, CATEGORY_FORM_DATA)
    assert Category.objects.count() == 0


def test_admin_user_can_create_category(admin_user_client, admin_user):
    response = admin_user_client.post(
        constant.CATEGORY_CREATE_URL, CATEGORY_FORM_DATA)
    assert Category.objects.count() == 1
    assertRedirects(response, constant.CATEGORY_LIST_URL)
    category = Category.objects.get()
    assert category.is_published == STUDY_FORM_DATA['is_published']
    assert category.is_on_main == STUDY_FORM_DATA['is_on_main']
    assert category.name == CATEGORY_FORM_DATA['name']
    assert category.slug == CATEGORY_FORM_DATA['slug']
    assert category.description == CATEGORY_FORM_DATA['description']
    assert category.author == admin_user


def test_anonymous_user_cant_create_review(client, study):
    client.post(
        reverse('study:review_create', args=(study.id,)),
        REVIEW_FORM_DATA)
    assert Review.objects.count() == 0


def test_auth_user_can_create_review(
    author, author_client, study, study_detail_url
):
    response = author_client.post(
        reverse('study:review_create', args=(study.id,)), REVIEW_FORM_DATA)
    assert Review.objects.count() == 1
    assertRedirects(response, f'{study_detail_url}#reviews')
    review = Review.objects.get()
    assert review.text == REVIEW_FORM_DATA['text']
    assert review.mark == REVIEW_FORM_DATA['mark']
    assert review.author == author
    assert review.study == study


def test_auth_user_cant_delete_study(
    reader_client, admin_user, study_delete_url
):
    reader_client.post(study_delete_url)
    assert Study.objects.count() == 1
    study = Study.objects.get()
    assert study.is_published == STUDY_FORM_DATA['is_published']
    assert study.is_on_main == STUDY_FORM_DATA['is_on_main']
    assert study.title == STUDY_FORM_DATA['title']
    assert study.slug == STUDY_FORM_DATA['slug']
    assert study.description == STUDY_FORM_DATA['description']
    assert study.author == admin_user


def test_admin_user_can_delete_own_study(admin_user_client, study_delete_url):
    assertRedirects(
        admin_user_client.post(study_delete_url), constant.STUDY_LIST_URL)
    assert Study.objects.count() == 0


def test_reader_admin_user_cant_delete_another_study(
    reader_admin_user_client, study_delete_url, admin_user
):
    reader_admin_user_client.post(study_delete_url)
    assert Study.objects.count() == 1
    study = Study.objects.get()
    assert study.is_published == STUDY_FORM_DATA['is_published']
    assert study.is_on_main == STUDY_FORM_DATA['is_on_main']
    assert study.title == STUDY_FORM_DATA['title']
    assert study.slug == STUDY_FORM_DATA['slug']
    assert study.description == STUDY_FORM_DATA['description']
    assert study.author == admin_user
