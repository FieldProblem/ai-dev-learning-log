from openai import OpenAI
from dotenv import load_dotenv
import os

def main():
    load_dotenv()
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("DEEPSEEK_API_KEY 未设置。请在 .env 中配置。")

    client = OpenAI(
        api_key=api_key,
        base_url="https://api.deepseek.com"
    )

    resp = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": "你是一名严谨、简洁的 AI 助手。"},
            {"role": "user", "content": "用三句话解释什么是 Prompt Engineering，并给出一个小例子。"}
        ],
        temperature=0.2
    )

    print(resp.choices[0].message.content)

if __name__ == "__main__":
    main()
