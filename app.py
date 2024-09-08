import discord
import requests
import os
from dotenv import load_dotenv

# .envファイルから環境変数を読み込む
load_dotenv()

# 環境変数からトークンとAPIキーを取得
DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DIFY_API_URL = os.getenv('DIFY_API_URL')  
DIFY_API_KEY = os.getenv('DIFY_API_KEY')

# Discordクライアントのインスタンス作成
intents = discord.Intents.default()
intents.message_content = True  # メッセージコンテンツのアクセス権を有効化
client = discord.Client(intents=intents)

# メッセージをDify APIに送信する関数
def send_to_dify(message):
    headers = {
        'Authorization': f'Bearer {DIFY_API_KEY}',  # API-Key認証
        'Content-Type': 'application/json'
    }
    
    # 正しいリクエストボディ
    data = {
        "query": message,  # DiscordメッセージをAPIに渡す
        "response_mode": "blocking",  # レスポンスモードを "blocking" に設定
        "user": "discord_user",  # 固定ユーザーID、任意に変更可能
        "inputs": {},  # 必要な場合は入力パラメータを追加
        "conversation_id": ""  # セッション追跡に必要であれば適宜設定
    }

    try:
        # POSTリクエストを送信
        response = requests.post(DIFY_API_URL, json=data, headers=headers)
        response.raise_for_status()  # ステータスコードが200番台でなければ例外を発生
        return response.json().get('answer', 'APIから応答がありませんでした。')
    except requests.exceptions.RequestException as e:
        return f'APIリクエストエラー: {e}'

# Discordでメッセージを受信した際のイベントハンドラー
@client.event
async def on_ready():
    print(f'ログインしました: {client.user}')

@client.event
async def on_message(message):
    # ボット自身のメッセージには応答しない
    if message.author == client.user:
        return

    # ユーザーのメッセージをDify APIに転送して応答を取得
    response = send_to_dify(message.content)

    # 応答をDiscordに送信
    await message.channel.send(response)

# Discordボットの起動
client.run(DISCORD_TOKEN)
