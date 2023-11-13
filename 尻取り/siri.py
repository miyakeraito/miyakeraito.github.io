import openai

# OpenAI APIキーを設定
api_key = "あなたのAPIキーをここに入力"

# GPT-3を使用して単語リストを生成
def generate_word_list(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # 使用するエンジンを指定
        prompt=prompt,
        max_tokens=50
    )
    return response.choices[0].text

# 単語リスト生成のためのプロンプト
prompt = "以下はしりとりの単語リストです。\nりんご\nごりん\nんまち\n"

# GPT-3を呼び出して単語リストを生成
word_list = generate_word_list(prompt)

# 生成された単語リストを表示
print(word_list)

