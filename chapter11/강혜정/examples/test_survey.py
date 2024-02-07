# from survey import AnonymousSurvey

# def test_store_single_response():
#     """단일 응답이 제대로 저장되는지 테스트"""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     language_survey.store_response("English")
#     assert "English" in language_survey.responses

# def test_store_three_responses():
#     """세 가지 개별 응답이 제대로 저장되는지 테스트"""
#     question = "What language did you first learn to speak?"
#     language_survey = AnonymousSurvey(question)
#     responses = ["English", "Spanish", "Mandarin"]
#     for response in responses:
#         language_survey.store_response(response)

#     for response in responses:
#         assert response in language_survey.responses


import pytest
from survey import AnonymousSurvey

@pytest.fixture
def language_survey():
    """모든 테스트에서 사용할 수 있는 설문조사 인스턴스"""
    question = "What language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey

def test_store_single_response(language_survey):
    """단일 응답이 제대로 저장되는지 테스트"""
    language_survey.store_response("English")
    assert "English" in language_survey.responses

def test_store_three_responses(language_survey):
    """세 가지 개별 응답이 제대로 저장되는지 테스트"""
    responses = ["English", "Spanish", "Mandarin"]
    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses