#!/bin/bash
# uninstall_agent.sh — LaunchAgent 제거
# 사용법: bash llm-wiki/scripts/uninstall_agent.sh

PLIST_LABEL="com.llmwiki.daily"
PLIST_DST="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"

echo "=== llm-wiki LaunchAgent 제거 ==="

if [ ! -f "$PLIST_DST" ]; then
    echo "[skip] plist 파일이 없습니다: $PLIST_DST"
    exit 0
fi

launchctl unload "$PLIST_DST" 2>/dev/null && echo "[ok] 언로드 완료" || true
rm -f "$PLIST_DST" && echo "[ok] plist 삭제 완료"
echo "LaunchAgent 제거 완료."
