# Harness Engineering Playbook

> Claude Code가 일을 끝까지 못 끝낸다면, 모델이 아니라 하네스가 문제입니다.

`habix-series`는 비개발자, 1인 빌더, PM이 Claude Code를 단발성 챗봇이
아니라 반복 가능한 업무 시스템으로 쓰도록 만든 17편 강의 시리즈입니다.

이 폴더는 강의 본문만이 아니라 metadata, diagram, OG image, routine pack,
사이트 적용용 허브 문서까지 포함한 발행 패키지입니다.

## 빠른 시작

| 목적 | 바로가기 |
|---|---|
| 전체 강의 흐름을 본다 | [17편 인덱스](#17편-인덱스) |
| 프로젝트에 바로 적용한다 | [routine-pack/](routine-pack/) |
| 웹사이트 허브 문안을 본다 | [site/playbook-harness-engineering.md](site/playbook-harness-engineering.md) |
| 발행 자산 상태를 확인한다 | [HANDOFF.md](HANDOFF.md) |
| v1 품질 리뷰를 확인한다 | [review-report-v1.md](review-report-v1.md) |

## 학습 경로

| 경로 | 추천 대상 | 읽을 순서 |
|---|---|---|
| 17편 완주 | Claude Code 작업 방식을 처음부터 다시 잡고 싶은 사람 | 서장 -> 1부 -> 2부 -> 3부 -> 캡스톤 |
| 7일 압축 실습 | 파일을 만들며 바로 적용하고 싶은 사람 | [Track 01](../tracks/01-claude-code-system/) |
| 45분 핵심 코스 | 지금 당장 프로젝트 기억을 만들고 싶은 사람 | Ch03 -> Ch04 -> Ch08 |
| 검증 중심 코스 | "됐어요"를 믿지 않고 증거를 남기고 싶은 사람 | Ch09 -> Ch10 -> Ch11 -> Ch12 |

## 17편 인덱스

### 서장 — 마인드셋과 도구

| Chapter | 주제 | 파일 |
|---|---|---|
| Ch 00a | 위임 사고방식 | [AI에게 일 시킨다는 것](lectures/ch00a-the-mindset-of-delegation.md) |
| Ch 00b | 1주차 필수 용어 15개 | [1주차에 꼭 아는 15개 단어](lectures/ch00b-15-words-week-one.md) |
| Ch 00c | 도구 스택 선택 | [내 도구 스택 정하기](lectures/ch00c-pick-your-tool-stack.md) |

### 1부. 5개 방 — 작업장 차리기

| Chapter | 주제 | 파일 |
|---|---|---|
| Ch 01 | 하네스 개념 | [똑똑한 AI가 끝까지 못 끝내는 이유](lectures/ch01-why-smart-ai-cant-finish.md) |
| Ch 02 | 하네스 5개 방 구조 | [AI에게 일 시키는 작업장 차리기](lectures/ch02-set-up-the-workshop.md) |
| Ch 03 | 시스템 오브 레코드 | [채팅창 말고 폴더가 기억하게 하라](lectures/ch03-let-the-folder-remember.md) |
| Ch 04 | `CLAUDE.md` 작성법 | [CLAUDE.md 한 장으로 프로젝트 가르치기](lectures/ch04-claude-md-one-page.md) |
| Ch 05 | `progress.md` 세션 메모 | [AI는 어제 한 일을 잊는다](lectures/ch05-leave-notes-for-tomorrow.md) |
| Ch 06 | 세션 초기화 브리핑 | [시작 전에 5분 브리핑](lectures/ch06-five-minute-briefing.md) |

### 2부. 공통 도구 — 매일 쓰는 자산

| Chapter | 주제 | 파일 |
|---|---|---|
| Ch 07 | 과욕 방지와 정지 규칙 | [AI가 일 키우는 걸 막는 법](lectures/ch07-stop-ai-from-overreaching.md) |
| Ch 08 | `feature_list.json` 작업 관리 | [할 일 한 장이 모든 것을 바꾼다](lectures/ch08-feature-list-changes-everything.md) |
| Ch 09 | 검증 사다리 | ['됐어요'를 믿지 마라](lectures/ch09-no-victory-without-evidence.md) |
| Ch 10 | E2E 자동 테스트 | [실제 사용자처럼 클릭해보는 자동 테스트](lectures/ch10-click-like-a-real-user.md) |

### 3부. 매일의 루틴 — 멈춤, 관측, 정리

| Chapter | 주제 | 파일 |
|---|---|---|
| Ch 11 | 관측 가능성 | [AI가 뭘 했는지 들여다보는 창문](lectures/ch11-window-into-ai.md) |
| Ch 12 | 클린 세션 종료 | [내일의 나를 위해 책상 정리하고 나가기](lectures/ch12-clean-exit.md) |
| Ch 13 | 루틴 파일 리팩토링 | [한 달 후, 내 루틴 파일을 리팩토링하는 법](lectures/ch13-refactor-your-routine-files.md) |

### 졸업 — 30일 챌린지

| Chapter | 주제 | 파일 |
|---|---|---|
| Capstone | 30일 루틴 자동화 챌린지 | [내 첫 30일 루틴 챌린지](lectures/capstone-30-day-routine-challenge.md) |

## Routine Pack

강의를 읽으면서 아래 5개 파일을 실제 프로젝트에 복사해 씁니다.

| 파일 | 역할 |
|---|---|
| [CLAUDE.md](routine-pack/CLAUDE.md) | 프로젝트 운영 규칙과 금지 사항 |
| [feature_list.json](routine-pack/feature_list.json) | 할 일, 진행 중, 완료, 실패, 보류 상태 관리 |
| [progress.md](routine-pack/progress.md) | 세션 간 이어받기 메모 |
| [intent_sheet.md](routine-pack/intent_sheet.md) | 의도, 결과, 제약, 평가 기준 |
| [session-end-checklist.md](routine-pack/session-end-checklist.md) | 다음 세션을 위한 종료 체크리스트 |

## 발행 자산

| 자산 | 위치 |
|---|---|
| 강의 본문 | [lectures/](lectures/) |
| 강의별 메타데이터와 navigation source | [metadata/](metadata/) |
| 본문 다이어그램 SVG | [diagrams/](diagrams/) |
| OG 이미지 PNG | [og-images/](og-images/) |
| 랜딩 카피와 와이어프레임 | [landing/](landing/) |
| 사이트 허브 본문 | [site/](site/) |

## 공식 출처와 참고 자료

- Anthropic Claude Code overview: https://code.claude.com/docs/en/overview
- Anthropic Claude Code memory / `CLAUDE.md`: https://code.claude.com/docs/en/memory
- Anthropic Claude Opus 4.5 system card: https://www.anthropic.com/claude-opus-4-5-system-card
- Eugene Yan, How to Work and Compound with AI: https://eugeneyan.com/writing/working-with-ai/

Karpathy-inspired `CLAUDE.md` rule set은 공식 1차 문서가 아니라 커뮤니티
레퍼런스입니다. 코드나 문구를 복사하지 않고 행동 원칙 수준에서만 참고합니다.
