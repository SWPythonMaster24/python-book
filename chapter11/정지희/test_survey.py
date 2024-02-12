import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """모든 설문조사에서 사용할 수 있는 인스턴스"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """단일 응답이 제대로 저장되는지 테스트"""
    language_survey.store_resposne('English')
    assert 'English' in language_survey.response

def test_store_three_response(language_survey):
    """세 가지 개별 응답이 제대로 저장되는지 테스트"""
    responses = ['English', "Korean", "Spanish"]
    for response in responses:
        language_survey.store_resposne(response)

    for response in responses:
        assert response in language_survey.response