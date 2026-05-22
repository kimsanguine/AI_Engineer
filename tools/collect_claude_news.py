#!/usr/bin/env python3
"""Claude AI 일일 뉴스 클리핑 수집기.

Google News RSS에서 Claude/Anthropic 관련 뉴스를 수집해
마크다운 파일로 저장합니다. 매일 아침 6시 LaunchAgent가 실행합니다.
"""

import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
import os
import re

OUTPUT_DIR = "/Users/sanguinekim/Documents/3_Code/Vibe/Project/260516_llm_brain/raw/clippings"
MAX_ITEMS = 10

FEEDS = [
    (
        "Global",
        "https://news.google.com/rss/search?q=claude+anthropic+AI&hl=en-US&gl=US&ceid=US:en",
    ),
    (
        "Korea",
        "https://news.google.com/rss/search?q=%ED%81%B4%EB%A1%9C%EB%93%9C+AI+Anthropic&hl=ko&gl=KR&ceid=KR:ko",
    ),
]


def fetch_feed(url: str) -> bytes:
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=15) as resp:
        return resp.read()


def parse_items(xml_data: bytes, label: str) -> list[dict]:
    root = ET.fromstring(xml_data)
    items = []
    for item in root.findall(".//item"):
        title = item.findtext("title", "").strip()
        link = item.findtext("link", "").strip()
        pub_date = item.findtext("pubDate", "").strip()
        source_el = item.find("source")
        source = source_el.text.strip() if source_el is not None else ""
        desc = re.sub(r"<[^>]+>", "", item.findtext("description", ""))[:200].strip()
        if title:
            items.append(
                {
                    "title": title,
                    "link": link,
                    "pub_date": pub_date,
                    "source": source,
                    "desc": desc,
                    "feed": label,
                }
            )
    return items


def main() -> None:
    os.makedirs(OUTPUT_DIR, exist_ok=True)

    all_items: list[dict] = []
    for label, url in FEEDS:
        try:
            xml_data = fetch_feed(url)
            all_items.extend(parse_items(xml_data, label))
        except Exception as e:
            print(f"[WARN] {label} 피드 오류: {e}")

    # 제목 기준 중복 제거 후 MAX_ITEMS 개 선택
    seen: set[str] = set()
    unique: list[dict] = []
    for item in all_items:
        key = item["title"][:60]
        if key not in seen:
            seen.add(key)
            unique.append(item)
        if len(unique) >= MAX_ITEMS:
            break

    today = datetime.now().strftime("%Y-%m-%d")
    now_str = datetime.now().strftime("%Y-%m-%d %H:%M")
    out_path = os.path.join(OUTPUT_DIR, f"claude-news-{today}.md")

    with open(out_path, "w", encoding="utf-8") as f:
        f.write(f"# Claude AI 뉴스 클리핑 — {today}\n\n")
        f.write(f"수집 시각: {now_str}  |  항목 수: {len(unique)}/{MAX_ITEMS}\n\n")
        f.write("---\n\n")
        for i, item in enumerate(unique, 1):
            f.write(f"## {i}. {item['title']}\n\n")
            meta_parts = []
            if item["source"]:
                meta_parts.append(f"**출처**: {item['source']}")
            if item["pub_date"]:
                meta_parts.append(f"**날짜**: {item['pub_date']}")
            meta_parts.append(f"**분류**: {item['feed']}")
            f.write("  ".join(meta_parts) + "\n\n")
            if item["desc"]:
                f.write(f"{item['desc']}…\n\n")
            f.write(f"[원문 보기]({item['link']})\n\n")
            f.write("---\n\n")

    print(f"[OK] {len(unique)}개 저장 → {out_path}")


if __name__ == "__main__":
    main()
