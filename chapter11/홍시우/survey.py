class AnonymousSurvery:
    # 설문조사의 익명 응답 수집

    def __init__(self, question):
        # 질문을 저장하고 응답 저장을 준비합니다.
        self.question   = question
        self.responses  = []

    def show_question(self):
        # 설문을 표시합니다.
        print(self.question)

    def store_response(self, new_response):
        # 응답을 저장합니다.
        self.responses.append(new_response)

    def show_results(self):
        # 수집된 응답을 표시합니다.
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}") 