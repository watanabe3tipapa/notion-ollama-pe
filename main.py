"""Notion + Ollama でページの要約を取得"""
import os
import requests
from ollama import chat
from dotenv import load_dotenv

load_dotenv()

NOTION_KEY = os.getenv("NOTION_API_KEY")
PAGE_ID = os.getenv("PAGE_ID")

def get_page_content(page_id: str) -> dict:
    """Notion APIでページを取得"""
    url = f"https://api.notion.com/v1/pages/{page_id}"
    headers = {
        "Authorization": f"Bearer {NOTION_KEY}",
        "Notion-Version": "2022-06-28",
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers)
    return response.json()

def extract_text(page_data: dict) -> str:
    """ページからテキストを抽出（簡易版）"""
    # プロパティからタイトルを取得
    props = page_data.get("properties", {})
    title = ""
    for key, prop in props.items():
        if prop.get("type") == "title":
            title_list = prop.get("title", [])
            title = "".join([t.get("plain_text", "") for t in title_list])
            break
    
    return title

def summarize_with_ollama(text: str) -> str:
    """Ollamaで要約"""
    response = chat('llama3.2', messages=[
        {"role": "user", "content": f"このテキストを3文で要約して:\n\n{text}"}
    ])
    return response['message']['content']

def save_summary(summary: str, filename: str = "Summary.md"):
    """要約をMarkdownファイルに保存"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write("# 要約\n\n")
        f.write(summary)
        f.write("\n")
    print(f"💾 {filename} に保存しました")

def main():
    if not NOTION_KEY or NOTION_KEY == "secret_xxxxx":
        print("❌ .envにNOTION_API_KEYを設定してください")
        return
    
    if not PAGE_ID:
        print("❌ .envにPAGE_IDを設定してください")
        return
    
    print(f"📄 ページ取得中: {PAGE_ID}")
    page_data = get_page_content(PAGE_ID)
    
    if "error" in page_data:
        print(f"❌ エラー: {page_data['error']}")
        return
    
    text = extract_text(page_data)
    if not text:
        print("❌ テキストが取得できませんでした")
        return
    
    print(f"📝 抽出テキスト: {text[:100]}...")
    print("🤖 Ollamaで要約中...")
    
    summary = summarize_with_ollama(text)
    print(f"\n📌 要約:\n{summary}")
    
    save_summary(summary)

if __name__ == "__main__":
    main()
