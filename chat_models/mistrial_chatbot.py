from dotenv import load_dotenv
from langchain_mistralai import ChatMistralAI
from langchain_core.messages import HumanMessage,SystemMessage,AIMessage
load_dotenv()

model = ChatMistralAI(model ='mistral-small-2506')

print("choose you AI Mode")
print(" press-1 for Happy Mode")
print("press-2 for Angry Mode")
print("press-3 for Sad Mode")

choice =int(input('confirm your AI-Mode :-'))

if choice == 1 :
    mode = "your a happy AI Agent so you always will proivde the responses in happy and cheerfull"
elif choice ==2 :
    mode="you are angry ai agent so you always will provide the respones in angry way and always discourages with your responses"
elif choice ==3:
    mode = 'your a sad ai agent so you alway will provdie the response in sad manner '
    
print("Please text your prompt/Message............")

messages = [SystemMessage(content=mode)]

print('Welcome to Application')
print('press 0 to exit the Application')

while True:
    prompt = input('You : ')
    messages.append(HumanMessage(content=prompt))
    if prompt == 0 :
        print('Bye')
        break
    response = model.invoke(messages).content
    messages.append(AIMessage(content=response))
    print('Bot :',response)
    