# llm-wiki — Claude Code B2B 활용사례 일일 적재

## 목적
Claude Code의 B2B 엔터프라이즈 활용사례를 매일 자동 수집하여
`/Users/sanguinekim/Documents/3_Code/Vibe/Project/260516_llm_brain/raw/` 에 적재합니다.

## 폴더 구조
```
llm-wiki/
  scripts/
    collect_cases.py    ← 일일 수집 스크립트 (직접 실행 가능)
  README.md
```

## 실행 방법

### 수동 실행
```bash
python3 llm-wiki/scripts/collect_cases.py
```

### 적재 경로 변경 (선택)
```bash
export LLM_RAW_DIR="/원하는/경로/raw"
python3 llm-wiki/scripts/collect_cases.py
```

## SessionStart 훅 자동화
`.claude/settings.json`에 SessionStart 훅이 등록되어 있습니다.
Claude Code 세션 시작 시 오늘 파일이 없으면 자동으로 생성됩니다.

## 파일 포맷
- 파일명: `YYYY-MM-DD.md`
- 하루 5건, 날짜 시드 기반으로 재현 가능
- 카테고리: 소프트웨어개발 / 고객서비스 / 법무컴플라이언스 / 재무회계 / HR / 영업마케팅 / 운영데이터 / 교육연구

## 사례 DB 확장
`collect_cases.py` 내 `CASE_POOL` 리스트에 항목을 추가하면 됩니다.
필드: `id`, `category`, `company_type`, `title`, `problem`, `solution`, `harness`, `result`, `tags`
