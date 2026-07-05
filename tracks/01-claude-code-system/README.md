# Track 01 — Claude Code System

## 목표

Claude Code를 "질문하면 답하는 챗봇"이 아니라, 파일과 루틴을 기억하고
작업을 끝까지 밀고 가는 업무 시스템으로 만든다.

이 track은 `habix-series`의 Harness Engineering 강의 17편과
`routine-pack`을 공식 학습 경로로 재구성한다.

## 7일 학습 경로

| Day | 주제 | 읽을 자료 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Setup and delegation mindset | `ch00a`, `ch00b`, `ch00c`, `ch01` | 실습 폴더 1개, 오늘의 업무 1개 | 폴더 안에서 Claude Code가 파일을 읽고 요약 |
| 2 | Project memory | `ch02`, `ch03`, `ch04` | `CLAUDE.md` 초안 | 다음 세션에서 같은 설명을 반복하지 않음 |
| 3 | Progress memory | `ch05`, `ch06` | `progress.md` 첫 항목 | 어제/오늘/내일이 5줄 안에 이어짐 |
| 4 | Boundaries and scope | `ch07`, `ch08` | `feature_list.json` | 할 일, 안 할 일, 보류가 분리됨 |
| 5 | Verification ladder | `ch09`, `ch10` | `validation-log.md` | 명령, 화면, 파일 중 최소 1개 증거 기록 |
| 6 | Operating windows | `ch11`, `ch12` | 종료 체크리스트 | 세션 종료 시 현재 상태와 다음 명령이 남음 |
| 7 | System refactor | `ch13`, `capstone` | 30일 루틴 계획 | 반복 작업이 파일/명령/체크리스트로 흡수됨 |

## 핵심 파일

| File | Source | Purpose |
|---|---|---|
| `CLAUDE.md` | `habix-series/routine-pack/CLAUDE.md` | 프로젝트의 작업 기억과 행동 규칙 |
| `feature_list.json` | `habix-series/routine-pack/feature_list.json` | 기능/업무 후보의 상태 관리 |
| `progress.md` | `habix-series/routine-pack/progress.md` | 세션 간 단기 기억 |
| `intent_sheet.md` | `habix-series/routine-pack/intent_sheet.md` | 만들려는 이유와 사용자 의도 정리 |
| `session-end-checklist.md` | `habix-series/routine-pack/session-end-checklist.md` | 종료 전 검증과 다음 세션 준비 |

## 실습: 빈 프로젝트에 루틴팩 적용

1. 새 실습 폴더를 만든다.
2. `habix-series/routine-pack/`의 5개 파일을 복사한다.
3. `CLAUDE.md`에서 프로젝트명, 대상 사용자, 금지 사항을 채운다.
4. `feature_list.json`에 첫 업무 후보 3개를 적는다.
5. Claude Code에게 "이 폴더를 읽고 오늘 시작할 가장 작은 작업을 골라줘"라고 요청한다.
6. 작업 후 `progress.md`와 `session-end-checklist.md`를 갱신한다.

## 완료 기준

이 track을 완료했다는 말은 다음 4개가 모두 있다는 뜻이다.

- 프로젝트별 `CLAUDE.md`
- 최신 `progress.md` 항목
- 최소 3개 항목이 들어간 `feature_list.json`
- 실행 또는 수동 확인 결과가 담긴 `validation-log.md`

## 다음 확장

- 반복 지시를 `case-studies`의 skill 패턴으로 분리한다.
- 외부 도구 연결이 필요하면 Track 02 MCP Tools로 이동한다.
- runnable agent가 필요하면 `starter-kits/` 템플릿을 사용한다.
