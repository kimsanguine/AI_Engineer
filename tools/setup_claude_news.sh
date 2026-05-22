#!/bin/bash
# Claude AI 뉴스 수집 루틴 설치 스크립트 (macOS)
# 실행: bash tools/setup_claude_news.sh

set -e

SCRIPT_DIR="$HOME/.claude/scripts"
PLIST_NAME="com.kimsanguine.claude-news"
LAUNCH_AGENTS_DIR="$HOME/Library/LaunchAgents"
OUTPUT_DIR="/Users/sanguinekim/Documents/3_Code/Vibe/Project/260516_llm_brain/raw/clippings"

echo "=== Claude 뉴스 수집 루틴 설치 ==="

# 1. 스크립트 디렉토리 생성
mkdir -p "$SCRIPT_DIR"
mkdir -p "$OUTPUT_DIR"
mkdir -p "$LAUNCH_AGENTS_DIR"

# 2. Python 스크립트 복사
cp "$(dirname "$0")/collect_claude_news.py" "$SCRIPT_DIR/collect_claude_news.py"
chmod +x "$SCRIPT_DIR/collect_claude_news.py"
echo "[1/4] 스크립트 복사 완료: $SCRIPT_DIR/collect_claude_news.py"

# 3. plist 복사
cp "$(dirname "$0")/com.kimsanguine.claude-news.plist" "$LAUNCH_AGENTS_DIR/$PLIST_NAME.plist"
echo "[2/4] LaunchAgent plist 복사 완료"

# 4. 기존 LaunchAgent 언로드 (있을 경우)
launchctl unload "$LAUNCH_AGENTS_DIR/$PLIST_NAME.plist" 2>/dev/null || true

# 5. LaunchAgent 등록
launchctl load "$LAUNCH_AGENTS_DIR/$PLIST_NAME.plist"
echo "[3/4] LaunchAgent 등록 완료 (매일 오전 6시 자동 실행)"

# 6. 즉시 테스트 실행
echo "[4/4] 즉시 테스트 실행 중..."
python3 "$SCRIPT_DIR/collect_claude_news.py"

echo ""
echo "설치 완료! 매일 오전 6:00에 뉴스가 아래 경로에 저장됩니다:"
echo "  $OUTPUT_DIR/claude-news-YYYY-MM-DD.md"
echo ""
echo "로그 확인:"
echo "  cat $SCRIPT_DIR/claude_news.log"
echo "  cat $SCRIPT_DIR/claude_news_error.log"
echo ""
echo "제거하려면:"
echo "  launchctl unload $LAUNCH_AGENTS_DIR/$PLIST_NAME.plist"
echo "  rm $LAUNCH_AGENTS_DIR/$PLIST_NAME.plist"
