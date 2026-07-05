# Track 01 — Claude Code System

Claude Code를 "질문하면 답하는 챗봇"이 아니라, 파일과 루틴을 기억하고
작업을 끝까지 밀고 가는 업무 시스템으로 만든다.

이 track은 `habix-series`의 Harness Engineering 강의 17편과
`routine-pack`을 공식 학습 경로로 재구성한다. 목표는 Claude Code를 잘
쓰는 팁을 배우는 것이 아니라, 매번 같은 설명을 반복하지 않아도 되는
작업 환경을 만드는 것이다.

## 대상 사용자

- Claude Code를 쓰지만 매 세션마다 맥락 설명을 반복하는 PM
- 기획서, 강의안, landing page, prototype을 혼자 운영하는 1인 빌더
- 비개발자에게 AI coding workflow를 가르치는 강사
- 팀 안에서 Claude Code 사용 규칙을 표준화하려는 운영자

## 이 Track이 해결하는 문제

Claude Code 실패는 모델 성능 부족보다 harness 부족에서 자주 발생한다.
작업 목표, 파일 구조, 금지 사항, 현재 진행 상태, 검증 기준이 없으면
모델은 매번 새로운 작업처럼 추측한다.

이 track은 아래 5개 파일을 통해 Claude Code의 작업 기억을 만든다.

| 파일 | 역할 | 질문 |
|---|---|---|
| `CLAUDE.md` | 프로젝트 운영 규칙 | 이 프로젝트에서 좋은 작업이란 무엇인가? |
| `feature_list.json` | 기능/업무 후보 관리 | 무엇을 할지, 말지, 보류할지 어떻게 나누는가? |
| `progress.md` | 세션 간 진행 기록 | 어제 어디까지 했고 오늘 무엇을 이어가나? |
| `intent_sheet.md` | 의도와 사용자 문제 | 왜 이 작업을 하는가? |
| `session-end-checklist.md` | 종료 루틴 | 다음 세션이 바로 이어받을 증거가 있는가? |

## 핵심 패턴

### 1. Prompt보다 Project Memory

좋은 프롬프트 한 줄보다 프로젝트 안에 남아 있는 `CLAUDE.md`가 오래 간다.
Claude Code가 매번 같은 기준을 읽게 만들면, 답변 품질보다 작업 일관성이
먼저 좋아진다.

### 2. 업무 후보를 JSON으로 관리

비개발자는 "뭘 만들지"와 "지금 만들면 안 되는 것"을 섞기 쉽다.
`feature_list.json`은 아이디어, 진행 중, 완료, 보류, 제외를 분리해
작업 범위를 좁힌다.

### 3. Progress는 회고가 아니라 재시작 장치

`progress.md`는 멋진 보고서가 아니다. 다음 세션의 첫 5분을 줄이기 위한
운영 로그다. 마지막 상태, 검증된 것, 다음 명령을 짧게 남긴다.

### 4. 검증은 명령, 화면, 파일로 남긴다

"잘 된 것 같다"는 검증이 아니다. 실행 명령, 생성 파일, 브라우저 화면,
배포 URL, 테스트 결과 중 하나 이상이 남아야 한다.

## 7일 학습 경로

| Day | 주제 | 읽을 자료 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|---|
| 1 | Setup and delegation mindset | `ch00a`, `ch00b`, `ch00c`, `ch01` | 실습 폴더를 만들고 오늘 맡길 업무 1개를 고른다 | 실습 폴더, 업무 설명 1개 | Claude Code가 폴더를 읽고 5줄 요약 |
| 2 | Project memory | `ch02`, `ch03`, `ch04` | 프로젝트 규칙, 대상 사용자, 금지 사항을 적는다 | `CLAUDE.md` 초안 | 새 세션에서 같은 설명 없이 작업 방향을 맞춘다 |
| 3 | Progress memory | `ch05`, `ch06` | 어제/오늘/다음 작업을 기록한다 | `progress.md` 첫 항목 | 다음 명령이 한 줄로 남아 있다 |
| 4 | Boundaries and scope | `ch07`, `ch08` | 할 일, 안 할 일, 보류할 일을 나눈다 | `feature_list.json` | scope 밖 요청을 거절하거나 보류한다 |
| 5 | Verification ladder | `ch09`, `ch10` | 수동 검증과 자동 검증을 분리한다 | `validation-log.md` | 명령, 화면, 파일 중 최소 1개 증거 기록 |
| 6 | Operating windows | `ch11`, `ch12` | 세션 종료 루틴을 만든다 | `session-end-checklist.md` | 종료 후에도 다음 사람이 이어갈 수 있다 |
| 7 | System refactor | `ch13`, `capstone` | 반복 요청을 파일/명령/체크리스트로 흡수한다 | 30일 루틴 계획 | 같은 설명을 반복하는 빈도가 줄어든다 |

## 실습 1 — 빈 프로젝트에 Routine Pack 적용

### 입력

- 빈 폴더 1개
- 오늘 처리할 작은 업무 1개
- `habix-series/routine-pack/`의 5개 파일

### 절차

1. 새 실습 폴더를 만든다.
2. `habix-series/routine-pack/`의 5개 파일을 복사한다.
3. `CLAUDE.md`에서 프로젝트명, 대상 사용자, 금지 사항을 채운다.
4. `feature_list.json`에 첫 업무 후보 3개를 적는다.
5. Claude Code에게 "이 폴더를 읽고 오늘 시작할 가장 작은 작업을 골라줘"라고 요청한다.
6. 작업 후 `progress.md`와 `session-end-checklist.md`를 갱신한다.

### 기대 산출물

```text
my-practice-project/
├── CLAUDE.md
├── feature_list.json
├── progress.md
├── intent_sheet.md
└── session-end-checklist.md
```

## 실습 2 — 기존 프로젝트에 Harness 추가

기존 프로젝트에는 이미 코드와 문서가 있으므로, 파일을 무작정 덮어쓰지 않는다.
먼저 현재 구조를 읽고, 운영 기억이 비어 있는 부분만 추가한다.

| 확인 항목 | 질문 | 추가 파일 |
|---|---|---|
| 프로젝트 목적 | 이 프로젝트는 누구의 어떤 문제를 해결하는가? | `intent_sheet.md` |
| 작업 규칙 | 어떤 파일을 먼저 읽고 어떤 변경을 피해야 하는가? | `CLAUDE.md` |
| 현재 상태 | 무엇이 완료, 미완료, 검증됨인가? | `progress.md` |
| 범위 관리 | 지금 하면 안 되는 기능은 무엇인가? | `feature_list.json` |
| 종료 루틴 | 다음 세션이 무엇부터 해야 하는가? | `session-end-checklist.md` |

## 검증 루프

이 track의 검증은 "파일이 있다"가 아니라 "다음 세션이 이어받는다"이다.

| 검증 | 방법 | 통과 기준 |
|---|---|---|
| Memory check | 새 세션에서 `CLAUDE.md`만 읽고 요약 요청 | 대상 사용자, 금지 사항, 작업 방식이 맞다 |
| Progress check | `progress.md`만 읽고 다음 작업 요청 | 다음 명령이 구체적으로 나온다 |
| Scope check | feature 후보 5개를 주고 우선순위 요청 | 제외/보류가 분리된다 |
| Evidence check | 완료 보고 요청 | 실행 명령 또는 파일 증거가 포함된다 |

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | AI tool을 쓰지만 매번 맥락이 끊기고 결과가 재사용되지 않음 |
| 반복 빈도 | 높음. 모든 Claude Code 세션에서 발생 |
| 자동화 가능 범위 | 파일 템플릿, 종료 체크리스트, progress update는 자동화 가능 |
| 사람 승인선 | 배포, 삭제, 고객-facing 변경은 사람이 승인해야 함 |
| production 전 필요한 것 | 팀별 템플릿, onboarding guide, validation log 샘플 |

## 완료 기준

이 track을 완료했다는 말은 다음 4개가 모두 있다는 뜻이다.

- 프로젝트별 `CLAUDE.md`
- 최신 `progress.md` 항목
- 최소 3개 항목이 들어간 `feature_list.json`
- 실행 또는 수동 확인 결과가 담긴 `validation-log.md`

## 연결 템플릿

| 템플릿 | 쓰는 시점 |
|---|---|
| [Behavior Contract](../../templates/behavior-contract.md) | 프로젝트별 해야 할 일, 금지 사항, 승인선을 정할 때 |
| [Skill Spec](../../templates/skill-spec.md) | 반복 지시를 재사용 가능한 skill/command로 분리할 때 |

## 다음 확장

- 반복 지시를 Track 06의 skill/command 패턴으로 분리한다.
- 외부 도구 연결이 필요하면 Track 02 MCP Tools로 이동한다.
- runnable agent가 필요하면 `starter-kits/` 템플릿을 사용한다.
