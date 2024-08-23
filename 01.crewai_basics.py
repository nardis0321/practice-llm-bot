from crewai import Crew, Agent, Task 
from langchain_ollama import ChatOllama

user_question = input('편하게 질문해주세요 :)')

llm = ChatOllama(
	model ='llama3.1',
	base_url='http://127.0.0.1:11434' # 컨트롤 누르고 링크 눌러보면 Ollama is running이라고 알려줌
)

recommand_book_agent = Agent(
	role='책 구매 어시스턴트',
	goal='고객이 상황을 설명하면 해당 상황에 맞는 우리 서점에 있는 책을 소개합니다',
	backstory='당신은 우리 서점의 모든 책 정보를 알고 있으며, 사람들의 상황에 맞는 책을 소개하는 데 전문가입니다.'
	llm=llm
)

recommand_book_task = Task(
	description='고객의 상황에 맞는 최고의 추천 도서 제안하기',
	expected_output='고객의 상황에 맞는 5개의 도서를 추천하고 추천 이유를 간단히 알려줘'
	agent=book_agent
)

review_agent = Agent(
	role='책 리뷰 어시스턴트',
	goal='추천 받은 도서에 대한 리뷰를 제공하고, 해당 도서에 대한 심도 있는 평가를 제공합니다',
	backstory='당신은 우리 서점의 모든 책 정보를 알고 있으며, 추천 받은 책에 대한 전문가 수준의 리뷰를 제공합니다.'
	llm=llm
)

review_task = Task(
	description='고객의 선택한 책에 대한 리뷰를 제공합니다',
	expected_output='고객이 선택한 책에 대한 리뷰를 제공합니다.'
	agent=review_agent
)
crew = Crew(
	agents=[recommand_book_agent, review_agent],
	task=[recommand_book_task, review_task],
	verbose=True
)

result = crew.kickoff() # 언어모델에 핑을 날리기
print(result)
