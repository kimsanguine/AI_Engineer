#!/bin/bash
# run_daily.sh — LaunchAgent에서 호출되는 래퍼 스크립트
# collect_cases.py 가 있는 위치를 동적으로 찾아서 실행

set -euo pipefail

SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
COLLECT_PY="$SCRIPT_DIR/collect_cases.py"
LOG_DIR="$HOME/Library/Logs"
LOG_FILE="$LOG_DIR/llmwiki-collect.log"

mkdir -p "$LOG_DIR"

echo "[$(date '+%Y-%m-%d %H:%M:%S')] 시작" >> "$LOG_FILE"

# pyenv / conda 등 사용자 shell 환경 로드
if [ -f "$HOME/.zshrc" ]; then
    # 비인터랙티브 환경에서 PATH 보정
    export PATH="/usr/local/bin:/opt/homebrew/bin:/usr/bin:$PATH"
fi

# python3 실행 (없으면 python 시도)
PYTHON_BIN=$(command -v python3 || command -v python || echo "")

if [ -z "$PYTHON_BIN" ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] ERROR: python3 를 찾을 수 없습니다." >> "$LOG_FILE"
    exit 1
fi

"$PYTHON_BIN" "$COLLECT_PY" >> "$LOG_FILE" 2>&1
EXIT_CODE=$?

if [ $EXIT_CODE -eq 0 ]; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 완료 (exit 0)" >> "$LOG_FILE"
else
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 오류 (exit $EXIT_CODE)" >> "$LOG_FILE"
fi

exit $EXIT_CODE
