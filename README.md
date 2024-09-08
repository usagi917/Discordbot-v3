# Discordbot

Pythonで構築されたDiscordボットで、Dify APIを使ったbotです

## 機能

- メッセージの自動応答
- APIとの連携機能
- Discordで発信した方の名前を呼んでくれます

## 必要条件

- Python 3.8以上
- [Discord.py](https://github.com/Rapptz/discord.py) ライブラリ
- その他の依存関係は`requirements.txt`をご確認ください。

## インストール

1. このリポジトリをクローンします。

    ```bash
    git clone https://github.com/usagi917/Discordbot-v3.git
    cd Discordbot-v3
    ```

2. 仮想環境を作成し、依存関係をインストールします。

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Windowsの場合は `venv\Scripts\activate`
    pip install -r requirements.txt
    ```


## 使用方法

1. ボットを起動するには、以下のコマンドを実行します。

    ```bash
    python app.py
    ```

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は`LICENSE`ファイルをご確認ください。
