#!/bin/bash
# install_agent.sh — LaunchAgent 설치 (최초 1회 실행)
# 사용법: bash llm-wiki/scripts/install_agent.sh

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PLIST_TEMPLATE="$SCRIPT_DIR/com.llmwiki.daily.plist"
PLIST_LABEL="com.llmwiki.daily"
PLIST_DST="$HOME/Library/LaunchAgents/${PLIST_LABEL}.plist"
LOG_DIR="$HOME/Library/Logs"
RUN_SCRIPT="$SCRIPT_DIR/run_daily.sh"

echo "=== llm-wiki LaunchAgent 설치 ==="
echo "스크립트 위치: $RUN_SCRIPT"
echo "설치 위치: $PLIST_DST"
echo "실행 시간: 매일 06:30"
echo ""

# 이미 로드된 에이전트가 있으면 언로드 먼저
if launchctl list | grep -q "$PLIST_LABEL" 2>/dev/null; then
    echo "[1/4] 기존 LaunchAgent 언로드 중..."
    launchctl unload "$PLIST_DST" 2>/dev/null || true
fi

# plist 복사 + 경로 치환
echo "[2/4] plist 생성 중..."
mkdir -p "$(dirname "$PLIST_DST")"
sed \
    -e "s|__SCRIPT_PATH__|$RUN_SCRIPT|g" \
    -e "s|__LOG_DIR__|$LOG_DIR|g" \
    "$PLIST_TEMPLATE" > "$PLIST_DST"

# 실행 권한 부여
chmod +x "$RUN_SCRIPT"

# LaunchAgent 로드
echo "[3/4] LaunchAgent 로드 중..."
launchctl load "$PLIST_DST"

# 확인
echo "[4/4] 상태 확인..."
if launchctl list | grep -q "$PLIST_LABEL"; then
    echo ""
    echo "[ok] 설치 완료."
    echo "     매일 오전 06:30에 collect_cases.py 가 자동 실행됩니다."
    echo "     로그: $LOG_DIR/llmwiki-collect.log"
    echo ""
    echo "     즉시 테스트 실행:"
    echo "     bash $RUN_SCRIPT"
    echo ""
    echo "     제거:"
    echo "     bash $SCRIPT_DIR/uninstall_agent.sh"
else
    echo "[error] LaunchAgent 로드에 실패했습니다. 아래 명령으로 확인하세요:"
    echo "  launchctl list | grep llmwiki"
    exit 1
fi
