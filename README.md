[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Version](https://img.shields.io/badge/version-0.1.0-green.svg)](https://github.com/watanabe3tipapa/notion-ollama-pe)

Notion + Ollama 連携ツールです。Notionページの要約をOllamaで自動生成します。

## 特徴

- Notionページの要約をOllamaで生成
- 結果はMarkdownファイル（Summary.md）として保存
- uvで簡単なセットアップ
- 他のマシンへ легко移植

## クイックスタート

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

## 詳細ドキュメント

- [USAGE.md](https://watanabe3tipapa.github.io/notion-ollama-pe/docs/USAGE.html) - 詳しい使い方
- [GitHub Pages](https://watanabe3tipapa.github.io/notion-ollama-pe/docs/USAGE.html) - スタイリング済みドキュメント

## 必要な環境

- Python 3.13+
- [uv](https://github.com/astral-sh/uv)
- [Ollama](https://ollama.com/)（ローカルで起動中）
- Notion APIキー

## ファイル構成

```
notion-ollama-pe/
├── main.py          # メインスクリプト
├── USAGE.md        # 使用方法（Markdown版）
├── docs/           # GitHub Pages用
│   ├── USAGE.html  # スタイリング済みドキュメント
│   ├── style.css   # スタイル
│   └── bg-main.jpg # 背景画像
├── .env.example    # 環境変数テンプレート
└── pyproject.toml  # uv設定
```

## ライセンス

このプロジェクトは [MIT License](LICENSE) の下でライセンスされています。
