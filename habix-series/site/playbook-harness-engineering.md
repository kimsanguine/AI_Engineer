---
title: Harness Engineering Playbook
subtitle: Claude Code가 일을 끝까지 못 끝낸다면, 모델이 아니라 하네스가 문제입니다
slug: harness-engineering
canonical_url: https://habix.ai/playbook/harness-engineering
last_updated: 2026-05-25
total_chapters: 17
total_reading_time_min: 259
og_image: /assets/harness-engineering/og/series-cover.png
---

# Harness Engineering Playbook

> Claude Code가 일을 끝까지 못 끝낸다면, 모델이 아니라 하네스가 문제입니다.

**최신 점검**: 2026-05-25 · **총 17편** · **예상 학습 시간 259분** (≈ 하루 20분 × 13일)

## 시리즈 한 줄로

모델은 이미 충분히 똑똑합니다. 그런데도 Claude Code, Cursor, Lovable이 70% 지점에서 무너지는 이유는 모델이 아니라 *작업장*이 비어 있기 때문입니다. 이 시리즈는 비개발자·1인 빌더·PM이 매일 30분으로 에이전트에게 일을 시키는 *루틴*을 직접 만들도록 17편으로 안내합니다. 도구 사용법이 아니라, 폴더가 기억하게 만들고, 의도를 한 장에 적고, 증거로 완료를 확인하는 *습관*을 다룹니다. 읽고 끝나지 않습니다. 각 챕터마다 5분 액션이 붙어 있어 그 자리에서 손이 한 번 움직이게 설계했습니다.

## 누구를 위한 시리즈인가

- **PM 출신 빌더** — 기획은 되는데 손이 모자랍니다. 백로그는 쌓이는데 마감해 줄 사람이 없습니다. 의도를 `feature_list.json` 한 장으로 적으면 에이전트가 마감까지 끌고 갑니다.
- **1인 SaaS 창업자** — 바이브 코딩으로 v1은 만들었는데 v2가 안 됩니다. 매번 처음부터 설명하느라 어제 한 일을 오늘 또 잃어버립니다. 폴더가 기억하게 만들면 어제 끝낸 자리에서 오늘 이어갑니다.
- **마케터·디자이너 출신 빌더** — 도구는 많이 봤지만, 매일 굴러가는 루틴으로 묶이지 않습니다. 5분 액션 13개로 *내가 안 봐도 도는 작업장*이 만들어집니다.

## 어떻게 읽으면 좋은가

세 가지 시나리오 중 하나를 고르시면 됩니다.

1. **순서대로 17편 완주** (권장 · 약 13일). 서장 3편으로 사고방식과 용어를 깔고, 1부에서 작업장 5개 방을 짓고, 2부에서 매일 쓰는 자산을 채우고, 3부에서 멈춤·관측·정리 루틴을 굳히는 흐름입니다. 마지막은 30일 챌린지로 봉합합니다.
2. **막힌 자리 먼저 펴기** (1시간 코스). 지금 막힌 증상이 분명하다면 그 챕터부터 펼치셔도 됩니다. *"AI가 일을 키운다"*면 Ch.07, *"매번 처음부터 설명한다"*면 Ch.03 + Ch.05, *"됐다고 했는데 깨졌다"*면 Ch.09 + Ch.10.
3. **페르소나 핵심 3편만** (45분 코스). 코드를 한 줄도 모르신다면 Ch.03(폴더가 기억하게), Ch.04(CLAUDE.md 한 장), Ch.08(feature_list)만 따라 하셔도 작업장이 섭니다. 나머지는 필요할 때 돌아오시면 됩니다.

읽고 끝내지 마시고, 챕터 마지막의 *5분 액션*을 그 자리에서 한 번 손으로 옮겨 주십시오. 17편 모두에 5분 액션이 붙어 있습니다.

## 17편 인덱스

### 서장 (Prologue) — 마인드셋과 도구

- **Ch 00a · AI에게 일 시킨다는 것** — 위임 사고방식: 에이전트는 마법사가 아니라 주니어 인턴입니다. 의도·결과·제약·검증 4단계. · 약 12분 · [읽기](/playbook/harness-engineering/ch00a-the-mindset-of-delegation)
- **Ch 00b · 1주차에 꼭 아는 15개 단어** — AI 필수 용어 15개: 토큰·컨텍스트 윈도우·에이전트… 에러 메시지의 그 단어들을 비유 한 줄로 정리합니다. · 약 13분 · [읽기](/playbook/harness-engineering/ch00b-15-words-week-one)
- **Ch 00c · 내 도구 스택 정하기** — 도구 스택 선택: Cursor·Claude Code·Lovable·Replit… 다섯 개 다 깔고 아무것도 못 끝낸 1년을 끝낼 시간. · 약 13분 · [읽기](/playbook/harness-engineering/ch00c-pick-your-tool-stack)

### 1부. 5개 방 — 작업장 차리기

- **Ch 01 · 똑똑한 AI가 끝까지 못 끝내는 이유** — 하네스(Harness) 개념: 같은 Opus 4.5, 20분 실패 vs 6시간 성공의 차이를 분해합니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch01-why-smart-ai-cant-finish)
- **Ch 02 · AI에게 일 시키는 작업장 차리기** — 하네스 5개 방 구조: 의도·메모리·실행·검증·세션을 처음으로 공개합니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch02-set-up-the-workshop)
- **Ch 03 · 채팅창 말고 폴더가 기억하게 하라** — 시스템 오브 레코드(System of Record): 채팅창은 휘발성, 폴더는 자산입니다. · 약 14분 · [읽기](/playbook/harness-engineering/ch03-let-the-folder-remember)
- **Ch 04 · CLAUDE.md 한 장으로 AI에게 프로젝트 가르치기** — CLAUDE.md 작성법: 8개 칸 템플릿 전문과 Karpathy 4원칙을 공개합니다. · 약 18분 · [읽기](/playbook/harness-engineering/ch04-claude-md-one-page)
- **Ch 05 · AI는 어제 한 일을 잊는다 — 메모를 남겨라** — progress.md 세션 메모: 5분 메모가 다음 세션 첫 명령을 한 줄로 줄입니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch05-leave-notes-for-tomorrow)
- **Ch 06 · 시작 전 5분, AI에게 프로젝트 브리핑하기** — 세션 초기화 브리핑: 매 세션 첫 5분이 그날의 품질을 결정합니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch06-five-minute-briefing)

### 2부. 공통 도구 — 매일 쓰는 자산

- **Ch 07 · AI가 일 키우는 걸 막는 법** — 제약·정지 규칙·작업 분해: 버튼 색 하나 바꿨는데 변경 파일 17개를 방지하는 3가지 무기. · 약 15분 · [읽기](/playbook/harness-engineering/ch07-stop-ai-from-overreaching)
- **Ch 08 · 할 일 한 장이 모든 것을 바꾼다** — feature_list.json 작업 관리: 의도를 데이터로 적는 순간 마감이 가능해집니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch08-feature-list-changes-everything)
- **Ch 09 · '됐어요'를 믿지 마라, 증거를 요구하라** — 검증 사다리 / 조기 완료 선언 방지: 완료 보고가 아니라 증거를 받는 4단계 사다리. · 약 16분 · [읽기](/playbook/harness-engineering/ch09-no-victory-without-evidence)
- **Ch 10 · 실제 사용자처럼 클릭하는 자동 테스트** — E2E 자동 테스트 / Playwright MCP: 단위 테스트는 부품을, E2E는 흐름을 봅니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch10-click-like-a-real-user)

### 3부. 매일의 루틴 — 멈춤·관측·정리

- **Ch 11 · AI가 뭘 했는지 들여다보는 창문** — 관측 가능성(Observability): 토큰·도구 호출·파일 변경·트랜스크립트 4개의 창문. · 약 16분 · [읽기](/playbook/harness-engineering/ch11-window-into-ai)
- **Ch 12 · 내일의 나를 위해 책상 정리하고 나가기** — 클린 세션 종료: 마지막 5분의 정리가 빠지면 다음 세션 첫 30분이 망가집니다. · 약 15분 · [읽기](/playbook/harness-engineering/ch12-clean-exit)
- **Ch 13 · 한 달 후, 내 루틴 파일을 리팩토링하는 법** — 트랜스크립트 마이닝 / 루틴 파일 리팩토링: 매월 1일, 책상이 아니라 *규칙 자체*를 정돈하는 의식. · 약 17분 · [읽기](/playbook/harness-engineering/ch13-refactor-your-routine-files)

### 졸업 — 30일 챌린지

- **Capstone · 내 첫 30일 루틴 챌린지** — 30일 루틴 자동화 챌린지: 13편을 30일 로드맵으로 굳힙니다. 마지막 날, 작업장은 혼자서도 굴러갑니다. · 약 20분 · [읽기](/playbook/harness-engineering/capstone-30-day-routine-challenge)

## 운영자

**김생근** — 20년 프로덕트 매니저, AI SaaS CPO.

지금 100개의 AI Agent를 직접 만들고 실행 중입니다. 링크 모음이 아니라, 문제 정의부터 코드와 실행 결과까지 매일 한 개씩 쌓고 있습니다. 이 시리즈는 그 작업장에서 매일 쓰는 도구를 PM 1인칭으로 정리한 것입니다.

> "Agent를 설명하지 말고, 실행해서 보여줘라."

## Routine Pack v1 — 5종 무료 자산

운영자가 매일 쓰는 템플릿 5종을 한 묶음으로 보내드립니다. 강의를 읽으면서 그대로 폴더에 떨궈 쓰시면 됩니다.

- `CLAUDE.md` — 우리 프로젝트 1장 브리핑 템플릿 (PM·1인 빌더·마케터 3종 변형)
- `feature_list.json` — 할 일 한 장 데이터 포맷
- `progress.md` — 세션 간 기억을 이어주는 메모
- `intent_sheet.md` — 의도를 적는 1페이지 시트
- `session-end-checklist.md` — 내일의 나를 위한 마무리 10줄

> 한 줄 이메일이면 받습니다. [루틴팩 v1 신청하기](https://tally.so/r/habix-routine-pack-v1)

## FAQ

**Q1. 코드를 한 줄도 모르는데 따라갈 수 있나요?**
네. 17편 전체가 *코드를 쓰는 법*이 아니라 *에이전트에게 일을 시키는 법*입니다. Ch.03 · Ch.04 · Ch.08만 따라 해도 작업장이 섭니다.

**Q2. Cursor와 Lovable, Claude Code 다 필요한가요?**
아니요. 서장 Ch.00c에서 페르소나에 맞는 도구 하나를 고르도록 안내합니다. 본문 예시는 Claude Code 기준이지만, 다른 도구로도 그대로 옮길 수 있게 적었습니다.

**Q3. 챕터당 소요 시간은 얼마인가요?**
읽기 12~20분 + 5분 액션 = 챕터당 평균 20분이 기본입니다. 전 17편 누적 약 259분, 하루 20분씩 약 13일이면 완주합니다. 캡스톤(30일 챌린지)은 하루 30분 × 30일 구조입니다.

**Q4. Claude Code 말고 다른 도구를 써도 되나요?**
됩니다. 본 시리즈는 *하네스*를 가르치는 것이지 특정 도구를 가르치는 것이 아닙니다. Cursor·Windsurf·Aider 사용자를 위한 대체 명령도 챕터 하단에 함께 적어둡니다.

**Q5. 30일 챌린지가 안 맞으면 환불되나요?**
유료 챌린지 참여 후 7일 이내, 1주차 액션을 마쳤다면 100% 환불해 드립니다. 시도 자체를 막지 않기 위함입니다.

## Sources

이 시리즈가 17편에 걸쳐 인용한 외부 자료입니다. 더 깊이 파고 싶으신 챕터의 *참고* 섹션에서 다시 만나실 수 있습니다.

- **Eugene Yan**, [*How to Work and Compound with AI*](https://eugeneyan.com/writing/working-with-ai/) — 검증, 관측, 트랜스크립트 마이닝 사고의 참고 자료.
- **Anthropic**, [Claude Code overview](https://code.claude.com/docs/en/overview) — Claude Code를 terminal, IDE, desktop, browser에서 쓰는 공식 제품 개요.
- **Anthropic**, [Claude Code memory / `CLAUDE.md`](https://code.claude.com/docs/en/memory) — `CLAUDE.md`와 project memory를 다루는 공식 문서.
- **Anthropic**, [Claude Opus 4.5 system card](https://www.anthropic.com/claude-opus-4-5-system-card) — Ch.01의 모델/하네스 논의를 뒷받침하는 Anthropic 공식 시스템 카드.
- **Karpathy-inspired community reference**, [andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills) — Ch.04의 행동 원칙 참고. 공식 1차 문서가 아니므로 코드나 문구를 복사하지 않고 원칙 수준에서만 참고.
- **Walking Labs**, [Learn Harness Engineering (한국어)](https://walkinglabs.github.io/learn-harness-engineering/ko/) — 본 시리즈가 비개발자용으로 다시 쓴 원본 강의 시퀀스.

## Next Playbooks

- [Claude Code Cheat Sheet →](/playbook/claude-code-cheatsheet)
- [AI Agent Cheat Sheet →](/playbook/ai-agent-cheatsheet)
- [LangGraph Cheatsheet →](/playbook/langgraph-cheatsheet)
