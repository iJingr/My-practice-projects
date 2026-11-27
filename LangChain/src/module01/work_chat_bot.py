import os
from dotenv import load_dotenv
from langchain.chat_models import init_chat_model
from langchain_core.messages import AIMessage, BaseMessage, HumanMessage, SystemMessage


load_dotenv()

class SimpleChatBot:

    MAX_HISTORY = 10

    def __init__(
            self,
            model_name: str = 'deepseek-chat',
            api_key: str = None,
            base_url: str = None,
            model_provider = 'openai'
    ):
        self._api_key = api_key or os.getenv('DEEPSEEK_API_KEY')
        self._base_url = base_url or os.getenv('DEEPSEEK_BASE_URL')

        self.model = init_chat_model(
            model=model_name,
            model_provider=model_provider,
            api_key=self._api_key,
            base_url=self._base_url,
            temperature=0.7
        )

        self.messages = [SystemMessage(content='你是一个简洁的助手，回答不超过三句话')]

    def _trim_history(self):
        dialog_count = len(self.messages) - 1
        limit = self.MAX_HISTORY * 2

        if dialog_count > limit:
            self.messages = [self.messages[0]] + self.messages[-limit:]

    def chat(self, user_input: str) -> str:
        self.messages.append(HumanMessage(content=user_input))
        response = self.model.invoke(self.messages)
        self.messages.append(response)
        self._trim_history()
        return response.content

    def chat_stream(self, user_input: str):
        self.messages.append(HumanMessage(content=user_input))
        count = ''
        for chunk in self.model.stream(self.messages):
            if chunk.content:
                count += chunk.content
                yield chunk.content
        self.messages.append(AIMessage(content=count))
        self._trim_history()

    def clear_history(self):
        """清除对话历史，保留系统消息"""
        self.messages = self.messages[:1]


if __name__ == '__main__':
    bot = SimpleChatBot()
    state = True

    while state:
        chat_ = input('请输入你想说的话：\n').strip()

        if chat_ == 'quit':
            state = False
        elif chat_ == 'clear':
            bot.clear_history()
            print('\n对话历史已清空。')
        elif chat_ == '':
            continue
        else:
            print('对话：', chat_)
            print('回复：', end='')
            for chunk in bot.chat_stream(chat_):
                print(chunk, end='', flush=True)
            print()

    print('再见')

