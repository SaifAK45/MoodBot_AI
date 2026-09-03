from dotenv import load_dotenv

load_dotenv()

from langchain_groq import ChatGroq
from langchain_core.messages import AIMessage,HumanMessage,SystemMessage

model = ChatGroq(model='openai/gpt-oss-120b')

print('Choose ur AI MODE')
print('1 for ANGRY')
print('2 for FUNNY')
print('3 for SAD')

choice = int(input('Tell ur response :- '))

if choice == 1:
    mode = 'you are an angry ai agent. your respond aggressively and impatently'

elif choice == 2:
    mode = 'you are an funny ai agent,your respond with humor and jokes'   

elif choice == 3:
    mode = 'you are an sad ai agent,your respond with depressed and emotional tone'

  

messages = [
    SystemMessage(content=mode)
]

print('----------------WELCOME PRESS 0 TO STOP THE APPLICATION')

while True:
    prompt = input('YOU :- ')
    messages.append(HumanMessage(content=prompt))

    if prompt == '0':
        break

    res = model.invoke(messages)
    messages.append(AIMessage(content=res.content))

    print('BOT :- ',res.content)

