import pytest

from langworld_db_pyramid.models.doculect import Doculect
from langworld_db_pyramid.views.doculects_list import view_all_doculects
from langworld_db_pyramid.views.doculect_profile import view_doculect_profile
from langworld_db_pyramid.views.json_api import get_doculects_by_substring, get_doculects_for_map
from langworld_db_pyramid.views.notfound import notfound_view

NUMBER_OF_TEST_DOCULECTS_WITH_FEATURE_PROFILES = 338  # only those (out of 429) that have has_feature_profile set to '1'


@pytest.mark.parametrize(
    'query, locale, expected_ids',
    [
        ('dut', 'en', ('afrikaans', 'dutch')),  # 'dut' is in aliases for Afrikaans and in main name for Dutch
        # the request is in Russian but IDs received are English:
        ('немец', 'ru', ('dutch', 'german', 'luxembourgian', 'swiss_german', 'yiddish')),
        # this query produces 7 doculects without 'has_feature_profile' restriction but only 3 with it:
        ('пар', 'ru', ('parachi', 'parthian', 'middle_persian'))
    ]

)
def test_json_api_get_doculects_by_substring(
        dummy_request, setup_models_for_views_testing,
        query, locale, expected_ids,
):

    dummy_request.matchdict['locale'] = locale
    dummy_request.matchdict['query'] = query

    doculects = get_doculects_by_substring(dummy_request)

    assert len(doculects) == len(expected_ids)

    for doculect in doculects:
        for key in ('id', 'name', 'aliases', 'iso639p3Codes', 'glottocodes'):
            assert key in doculect.keys()

    for doculect_id in expected_ids:
        ids = [doculect['id'] for doculect in doculects]
        assert doculect_id in ids


@pytest.mark.parametrize(
    'locale, expected_first_doculect, expected_last_doculect',
    [
        (
            'ru',
            {'id': 'abaza', 'name': 'абазинский', 'latitude': '44.1556', 'longitude': '41.9368'},
            {'id': 'yaoure', 'name': 'яурэ', 'latitude': '6.85', 'longitude': '-5.3'},
        ),
        (
            'en',
            {'id': 'abaza', 'name': 'Abaza', 'latitude': '44.1556', 'longitude': '41.9368'},
            {'id': 'zefrei', 'name': 'Zefrei', 'latitude': '32.80592', 'longitude': '52.11667'},
        ),
    ]
)
def test_json_api_get_doculects_for_map(
        dummy_request, setup_models_for_views_testing, locale, expected_first_doculect, expected_last_doculect
):

    dummy_request.matchdict['locale'] = locale
    doculects = get_doculects_for_map(dummy_request)

    assert len(doculects) == NUMBER_OF_TEST_DOCULECTS_WITH_FEATURE_PROFILES
    assert doculects[0] == expected_first_doculect
    assert doculects[-1] == expected_last_doculect


def test_view_all_doculects(dummy_request, setup_models_for_views_testing):

    info = view_all_doculects(dummy_request)
    assert dummy_request.response.status_int == 200
    assert len(info['doculects']) == NUMBER_OF_TEST_DOCULECTS_WITH_FEATURE_PROFILES


def test_view_doculect_profile(dummy_request, setup_models_for_views_testing):
    dummy_request.matchdict['doculect_man_id'] = 'aragonese'

    info = view_doculect_profile(dummy_request)
    doculect = info['doculect']
    assert isinstance(doculect, Doculect)
    assert doculect.name_en == 'Aragonese'


def test_notfound_view(dummy_request):
    info = notfound_view(dummy_request)
    assert dummy_request.response.status_int == 404
    assert info == {}
