import feedparser
from newspaper import Article
import json
import os
import time


def crawl_vnexpress_news(
    limit=200,
    output_file=r"D:\artical-ai-agent\data\news_data.json"
):
    rss_url = "https://baomoi.com/"

    # Load dữ liệu cũ nếu có
    old_data = []

    if os.path.exists(output_file):
        try:
            with open(output_file, "r", encoding="utf-8") as f:
                old_data = json.load(f)
        except:
            old_data = []

    # set để kiểm tra trùng
    existing_links = {
        item["link"]
        for item in old_data
        if "link" in item
    }

    print(f"Đã có {len(existing_links)} bài trong dataset")
    print(f"Đang quét RSS...")

    feed = feedparser.parse(rss_url)

    new_articles = []

    for i, entry in enumerate(feed.entries[:limit], 1):

        # bỏ qua nếu đã có
        if entry.link in existing_links:
            print(f"[SKIP] Trùng: {entry.title}")
            continue

        try:
            print(f"[{i}] Crawl mới: {entry.title}")

            article = Article(
                entry.link,
                language="vi"
            )

            article.download()
            article.parse()

            item = {
                "title": entry.title,
                "link": entry.link,
                "published": getattr(
                    entry,
                    "published",
                    ""
                ),
                "content": article.text.strip(),
                "topic": "News"
            }

            new_articles.append(item)

            print("✓ Đã thêm")
            time.sleep(1)

        except Exception as e:
            print(f"Lỗi {entry.link}: {e}")

    # gộp cũ + mới
    all_data = old_data + new_articles

    # lưu lại
    with open(
        output_file,
        "w",
        encoding="utf-8"
    ) as f:
        json.dump(
            all_data,
            f,
            ensure_ascii=False,
            indent=4
        )

    print("\n==== KẾT QUẢ ====")
    print(f"Tin mới thêm: {len(new_articles)}")
    print(f"Tổng dataset: {len(all_data)}")
    print(f"Lưu tại: {output_file}")


if __name__ == "__main__":
    crawl_vnexpress_news()