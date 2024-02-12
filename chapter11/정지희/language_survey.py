from survey import AnonymousSurvey

# 설문의 정의하고 설문조사를 만듭니다
question = "What language did you first learn to speak?"
langugae_survey = AnonymousSurvey(question)

# 설문을 표시하고 응답을 저장합니다
langugae_survey.show_question()
print("Entet 'q' at any time to quit")
while True:
    response = input("Language: ")
    if response == 'q':
        break
    langugae_survey.store_resposne(response)

# 설문조사 결과를 표시합니다
print("\nThank you to everyone who participated in the survey!")
langugae_survey.show_results()