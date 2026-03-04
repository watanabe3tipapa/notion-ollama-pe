# Notion + Ollama 使用方法

## 準備

### 1. Notion APIキー取得
1. [notion.so/developers](https://www.notion.so/developers) にアクセス
2. 「New integration」をクリック
3. 名前を入力（例: `notion-ollama`）
4. 「Capabilities」で Full Access を選択
5. 保存後、Secretキーをコピー

### 2. ページID取得
- NotionページのURLから取得
- 例: `https://notion.so/page-name-abc123def456` → `abc123def456`

### 3. 環境変数設定
```bash
cp .env.example .env
```

`.env`ファイルを編集：
```
NOTION_API_KEY=secret_xxxxx（取得したAPIキー）
PAGE_ID=abc123def456（ページID）
```

## 実行

```bash
uv run python main.py
```

## 出力例
```
📄 ページ取得中: abc123def456
📝 抽出テキスト: プロジェクトAの仕様...
🤖 Ollamaで要約中...

📌 要約:
このドキュメントはプロジェクトAの仕様書です...
```

## カスタマイズ

### モデル変更
`main.py`の`llama3.2`を他のモデルに置換：
```python
response = chat('他のモデル名', messages=[...])
```

### プロンプト変更
要約のプロンプトを編集：
```python
{"role": "user", "content": f"このテキストを3文で要約して:\n\n{text}"}
```

## 他のマシンへ移植する場合

### 準備（現在のパソコンで）
テスト成功後、以下のコマンドで依存関係を固定：
```bash
uv sync
```
これにより `uv.lock` が更新され、相手の環境で同じバージョンが使われる

### 移植手順（相手のマシンで）
1. プロジェクトフォルダを丸ごとコピー
2. ターミナルでフォルダに移動
3. 以下を実行：
```bash
uv sync
```
4. `.env` ファイルを作成し、APIキーを設定

### 必要な環境
- Python 3.13+
- uv
- Ollama（ローカルで起動中）
- Notion APIキー

## Ollamaのセットアップ

### 1. Ollamaをインストール
Mac/Linux:
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Ollamaを起動
```bash
ollama serve
```
（別ターミナルで実行、またはバックグラウンド起動）

### 3. モデルをダウンロード
```bash
ollama pull llama3.2
```
他のモデル一覧は https://ollama.com/library

### 4. 確認
```bash
ollama list
```
ダウンロード済みモデルが表示される

## トラブルシューティング

### Ollamaが起動しない
```bash
# ポート11434が使用中か確認
lsof -i :11434

# 停止
ollama stop llama3.2
```

### モデルを変更したい
`main.py` のこの部分：
```python
response = chat('llama3.2', messages=[...])
```
`'llama3.2'` を他のモデル名に替换（例: `llama3`, `mixtral`, `phi3`）
