[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/watanabe3tipapa/notion-ollama-pe)

# Notion + Ollama 連携（要約作成ツール）

Notionページの要約をOllamaで自動生成するためのツールです。リポジトリ内のスクリプトでNotionのページを取得し、要約結果をMarkdownファイル（Summary.md）として保存する構成が提供されています。

## 主な特徴

- Notionページの要約をOllamaで生成する機能（README内の説明に基づく）
- 要約結果をMarkdown（Summary.md）として保存する記述あり
- uvを使ったセットアップ手順が用意されている
- .env.example を用いた環境変数の管理

## 必要な環境（確認済み情報）

- Python 3.13+
- uv（プロジェクトで使用されていることを示すファイルあり）
- Ollama（READMEにローカルで起動中であることが必要と明記されています）
- Notion APIキー（.env で設定することが想定されています）
- 依存パッケージ（pyproject.toml に記載）: requests, ollama, python-dotenv

## クイックスタート（READMEに記載されている手順）

以下はリポジトリ内のREADMEに記載されている手順です。実行前に各ファイルや環境を確認してください。

```bash
# 1. リポジトリをクローン
git clone https://github.com/watanabe3tipapa/notion-ollama-pe.git
cd notion-ollama-pe

# 2. 依存関係をインストール
uv sync

# 3. 環境変数を設定
cp .env.example .env
# .envファイルを編集（NOTION_API_KEYとPAGE_IDを入力）

# 4. 実行
uv run python main.py
```

注: 上記はリポジトリ内の説明に基づく手順です。実行の際は環境（Ollamaの稼働状態やNotion APIの認証情報など）を事前に確認してください。

## ドキュメント

- スタイリング済みドキュメント（GitHub Pages）: https://watanabe3tipapa.github.io/notion-ollama-pe/USAGE.html

## ファイル構成（主要ファイル、README での記載に基づく）

```
notion-ollama-pe/
├── main.py          # メインスクリプト（READMEに記載あり）
├── USAGE.md        # 使用方法（Markdown版）
├── docs/           # GitHub Pages用ドキュメント等
│   ├── USAGE.html
│   ├── style.css
│   └── bg-main.jpg
├── .env.example    # 環境変数テンプレート
└── pyproject.toml  # uv設定、依存関係記載
```

## 開発・保守状態

- リポジトリはアーカイブされていません（最終更新: 2026-03-04 に関するメタデータあり）。

## ライセンス

- このプロジェクトは MIT License の下でライセンスされています（README内の記載およびLICENSEファイルに基づく）。

---

補足: 実行や設定の詳細（例えば main.py の引数や出力の正確な場所、Ollama側のモデル設定など）はリポジトリ内のスクリプトや USAGE.md/USAGE.html を参照してください。READMEでは、リポジトリ内に存在するドキュメントとファイルに基づく情報のみを記載しています。
