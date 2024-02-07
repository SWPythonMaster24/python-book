import pytest
from survey import AnonymousSurvery

@pytest.fixture
def language_survey():
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    return language_survey

def test_store_single_response(language_survey):
    # 단일 응답이 제대로 저장되는지 테스트
    language_survey.store_response('English')
    assert 'English' in language_survey.responses

def test_store_single_response():
    # 단일 응답이 제대로 저장되는지 테스트
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvery(question)
    language_survey.store_response('English')
    assert 'English' in language_survey.responses


