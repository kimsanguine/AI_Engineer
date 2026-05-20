# habix-series 발행 인계 문서

**작성일**: 2026-05-19
**대상**: 다음 로컬 세션 — habix.ai 사이트 레포 작업자
**범위**: 컨텐츠 제작은 완료. habix.ai 사이트 적용만 남음.

---

## 0. 한 줄 요약

`kimsanguine/AI_Engineer` 레포의 `main`에 17편 강의 시리즈와 모든 발행 자산이 완성·반영되어 있습니다. **habix.ai 사이트는 아직 라이브가 아닙니다** (`/playbook/harness-engineering/` 및 하위 챕터 모두 404). 사이트 레포에 메뉴·라우팅·컴포넌트 추가 작업이 필요합니다.

---

## 1. 현재 상태 한눈에

| 영역 | 상태 | 위치 |
|---|---|---|
| 강의 본문 17편 | 완성 | `habix-series/lectures/*.md` |
| 메타데이터 17개 | canonical_url + published_at 입력 완료 | `habix-series/metadata/*.json` |
| 다이어그램 SVG 7종 | 완성 | `habix-series/diagrams/*.svg` |
| OG 이미지 PNG 17종 (1200×630) | 완성 | `habix-series/og-images/*.png` |
| 루틴팩 5종 | 완성 | `habix-series/routine-pack/*` |
| 랜딩 카피·와이어프레임 | 완성 | `habix-series/landing/*.md` |
| 사이트 nav 데이터 | 완성 | `habix-series/metadata/nav-structure.json` |
| 사이트 허브 페이지 본문 | 완성 (마크다운) | `habix-series/site/playbook-harness-engineering.md` |
| **habix.ai 사이트** | **미배포 (404)** | habix.ai 사이트 레포 작업 필요 |

---

## 2. 레포 자산 위치 디렉토리 맵

```
habix-series/
├── HANDOFF.md                         # 이 문서
│
├── lectures/                          # 강의 본문 17편 (.md)
│   ├── ch00a-the-mindset-of-delegation.md
│   ├── ch00b-15-words-week-one.md
│   ├── ch00c-pick-your-tool-stack.md
│   ├── ch01-why-smart-ai-cant-finish.md
│   ├── ch02-set-up-the-workshop.md
│   ├── ch03-let-the-folder-remember.md
│   ├── ch04-claude-md-one-page.md
│   ├── ch05-leave-notes-for-tomorrow.md
│   ├── ch06-five-minute-briefing.md
│   ├── ch07-stop-ai-from-overreaching.md
│   ├── ch08-feature-list-changes-everything.md
│   ├── ch09-no-victory-without-evidence.md
│   ├── ch10-click-like-a-real-user.md
│   ├── ch11-window-into-ai.md
│   ├── ch12-clean-exit.md
│   ├── ch13-refactor-your-routine-files.md
│   └── capstone-30-day-routine-challenge.md
│
├── metadata/                          # 강의별 메타 + 사이트 nav 데이터
│   ├── index.json                     # 17편 목록 + base_url
│   ├── nav-structure.json             # 사이드바·prev/next·OG 메타 단일 공급원 (사이트 빌드가 읽음)
│   └── ch00a-...json ~ capstone-...json  # 강의별 메타 17개
│
├── diagrams/                          # 강의 본문 인라인 SVG 7종
│   ├── ch01-barehand-vs-harness.svg
│   ├── ch02-five-rooms-floorplan.svg
│   ├── ch04-claude-md-3layer.svg
│   ├── ch06-initialization-timeline.svg
│   ├── ch09-verification-ladder.svg
│   ├── ch11-four-windows.svg
│   └── capstone-30day-gantt.svg
│
├── og-images/                         # OG 카드 PNG 17종 (1200×630)
│   ├── _generate.py                   # 재생성 스크립트 (cairosvg + Pillow + Noto Sans CJK KR)
│   └── ch00a-...png ~ capstone-...png
│
├── routine-pack/                      # 루틴팩 v1 다운로드 자산 5종
│   ├── CLAUDE.md                      # 3변형 (PM / 1인빌더 / 마케터)
│   ├── feature_list.json
│   ├── progress.md
│   ├── intent_sheet.md
│   └── session-end-checklist.md
│
├── landing/                           # 랜딩 페이지 자산
│   ├── main-page-copy.md
│   └── wireframe.md
│
├── site/                              # 사이트 적용 자산
│   └── playbook-harness-engineering.md   # /playbook/harness-engineering/ 허브 페이지 본문
│
└── review-report-v1.md                # v1 발행 직전 자기 검토 보고서
```

---

## 3. 작업 내역 (커밋·PR 히스토리)

| Squash SHA | PR | 내용 |
|---|---|---|
| `4c14194` | [#1](https://github.com/kimsanguine/AI_Engineer/pull/1) | v1 컨텐츠 + 다이어그램 7종 + OG 17종 + /playbook/ 적용 + 메뉴 라벨 통일 |
| `6bdd0e6` | [#2](https://github.com/kimsanguine/AI_Engineer/pull/2) | D0 발행일을 2026-05-19로 — ch00a/b/c + ch01/02/03 |
| `b08cd40` | [#3](https://github.com/kimsanguine/AI_Engineer/pull/3) | ch04~capstone 매일 발행 (2026-05-20 ~ 05-30) |

세부 커밋은 `git log --all --oneline` 또는 위 PR 페이지에서 확인.

---

## 4. 발행 일정 (현재 메타데이터에 박힌 값)

| 일자 | 요일 | 챕터 | slug |
|---|---|---|---|
| 2026-05-19 | 화 | ch00a — 위임의 사고방식 | `ch00a-the-mindset-of-delegation` |
| 2026-05-19 | 화 | ch00b — 1주차 15단어 | `ch00b-15-words-week-one` |
| 2026-05-19 | 화 | ch00c — 도구 스택 선택 | `ch00c-pick-your-tool-stack` |
| 2026-05-19 | 화 | ch01 — 똑똑한 AI가 끝까지 못 끝내는 이유 | `ch01-why-smart-ai-cant-finish` |
| 2026-05-19 | 화 | ch02 — 작업장 차리기 | `ch02-set-up-the-workshop` |
| 2026-05-19 | 화 | ch03 — 폴더가 기억하게 하라 | `ch03-let-the-folder-remember` |
| 2026-05-20 | 수 | ch04 — CLAUDE.md 한 장 | `ch04-claude-md-one-page` |
| 2026-05-21 | 목 | ch05 — 메모 남기기 (progress.md) | `ch05-leave-notes-for-tomorrow` |
| 2026-05-22 | 금 | ch06 — 5분 브리핑 | `ch06-five-minute-briefing` |
| 2026-05-23 | 토 | ch07 — AI 과욕 막기 | `ch07-stop-ai-from-overreaching` |
| 2026-05-24 | 일 | ch08 — feature_list 한 장 | `ch08-feature-list-changes-everything` |
| 2026-05-25 | 월 | ch09 — 증거 요구하기 | `ch09-no-victory-without-evidence` |
| 2026-05-26 | 화 | ch10 — 사용자처럼 클릭 | `ch10-click-like-a-real-user` |
| 2026-05-27 | 수 | ch11 — 관측 4개 창문 | `ch11-window-into-ai` |
| 2026-05-28 | 목 | ch12 — 클린 종료 | `ch12-clean-exit` |
| 2026-05-29 | 금 | ch13 — 루틴 파일 리팩토링 | `ch13-refactor-your-routine-files` |
| 2026-05-30 | 토 | capstone — 30일 챌린지 졸업 | `capstone-30-day-routine-challenge` |

총 17편 / 12일 연속 / 졸업: 2026-05-30 (토).

> **주의**: 사이트 배포가 늦어질 경우 ch00a~ch03의 published_at(2026-05-19)이 이미 지난 날짜가 됩니다. 사이트 측 적용 일정에 맞춰 *전체 일정을 후방으로 한꺼번에 밀어주는 패치*가 필요할 수 있습니다 — §7 참고.

---

## 5. 사이트 측 데이터 계약 (Data Contract)

habix.ai 사이트 빌드가 이 레포에서 *무엇을 어떻게* 읽어가야 하는지의 명세.

### 5.1 메뉴 항목

- **라벨**: `Harness Engineering Playbook`
- **URL**: `/playbook/harness-engineering`
- **위치**: 상단 Playbook 메뉴, 기존 5개(LLM Wiki / GEO / AI Agent Cheat Sheet / Claude Code Cheat Sheet / LangGraph Cheatsheet)와 동격

### 5.2 URL 패턴

```
/playbook/harness-engineering              ← 허브 (인덱스)
/playbook/harness-engineering/{slug}       ← 개별 강의 17개
```

각 강의의 정확한 slug는 `metadata/index.json`의 `chapters[].slug` 또는 `nav-structure.json`의 `chapters[].slug` 참조.

### 5.3 단일 공급 데이터 파일

`habix-series/metadata/nav-structure.json` — 사이드바·breadcrumb·prev/next·OG 메타를 모두 이 한 파일에서 읽음.

스키마 요약:

```json
{
  "series": {
    "slug", "title", "subtitle", "url", "menu_label",
    "total_chapters", "total_reading_time_min", "last_updated"
  },
  "parts": [{ "id", "label", "subtitle", "chapters": [slug...] }],
  "chapters": [{
    "slug", "chapter_number", "title", "url",
    "og_image", "reading_time_min", "published_at",
    "part_id", "position_in_part", "position_in_series",
    "prev_slug", "next_slug", "key_concept"
  }]
}
```

### 5.4 부 그룹화

- **서장 (prologue)**: ch00a, ch00b, ch00c (3편)
- **1부. 5개 방 (part-1)**: ch01~ch06 (6편)
- **2부. 공통 도구 (part-2)**: ch07~ch10 (4편)
- **3부. 매일의 루틴 (part-3)**: ch11, ch12, ch13 (3편)
- **졸업 (graduation)**: capstone (1편)

### 5.5 정적 자산 경로 (빌드 시 복사)

| 원본 | 사이트 정적 경로 (가정) |
|---|---|
| `habix-series/og-images/{slug}.png` | `/assets/harness-engineering/og/{slug}.png` |
| `habix-series/diagrams/{file}.svg` | `/assets/harness-engineering/diagrams/{file}.svg` |

강의 본문의 `![alt](../diagrams/...svg)` 상대 경로는 사이트 빌드 시 *절대 경로로 변환* 필요.

### 5.6 허브 페이지 본문

`habix-series/site/playbook-harness-engineering.md` — `/playbook/harness-engineering`의 본문으로 렌더. 프론트매터에 title·subtitle·last_updated 등 포함.

---

## 6. 남은 작업 (habix.ai 사이트 레포에서)

### P0 — 배포 차단 항목

1. **메뉴 항목 추가** — Playbook 메뉴에 "Harness Engineering Playbook" → `/playbook/harness-engineering`
2. **라우팅** — Nested URL 지원: `/playbook/harness-engineering` + `/playbook/harness-engineering/{slug}`
3. **데이터 소스 import** — `nav-structure.json` + 17개 메타데이터 JSON을 시리즈 페이지가 빌드 타임에 읽도록
4. **정적 자산 파이프** — `og-images/`, `diagrams/`를 사이트 정적 자산 디렉토리로 복사
5. **빌드 + 배포** — 트리거 후 라이브 200 OK 확인

### P1 — 시리즈 페이지 UX (신규 컴포넌트 3종)

6. **Series sidebar (sticky)** — 17편 + 부 그룹화, 현재 챕터 강조 (사이트맵 역할)
7. **Breadcrumb** — `Playbook › Harness Engineering › Chapter N`
8. **Prev/Next 챕터 nav** — 본문 하단

### P2 — 옵셔널, 발행 이후

- 다이어그램 `ch04-claude-md-3layer.svg`의 라벨 겹침 정리 (3-Layer 박스의 내부 라벨이 색 박스와 약간 겹침 — 원본 SVG 직접 수정 후 OG 재생성)
- Pretendard 폰트가 있는 환경에서 `og-images/_generate.py` 재실행해 PNG 일괄 교체 (현재는 Noto Sans CJK KR fallback)
- 시리즈 표지 `og-images/series-cover.png` 신규 생성 (허브 페이지 OG 카드용 — 현재 `series-cover.png` 경로만 메타에 박혀 있고 파일 부재)
- ch00a/00b/00c의 OG title 형식 일관화 (현재 P-01/02/03 표기 vs 본 강의의 Ch.NN 표기 혼재)

---

## 7. 다음 세션에서 시작할 때

### 7.1 권한 확보 절차

1. claude.ai/code 환경 설정에서 habix.ai 사이트 레포를 GitHub MCP 화이트리스트에 추가 (현재 `kimsanguine/ai_engineer` 만 허용됨)
2. 새 세션 시작 시 두 레포 모두 접근 가능한 상태로 시작

### 7.2 작업 첫 단계

1. **사이트 레포 스캔** — 스택 파악 (Next.js / Astro / SvelteKit / 자체 빌드 등)
2. **기존 playbook 등록 코드 찾기** — 메뉴/라우팅이 어디에 하드코딩되어 있는지 (e.g., `app/playbook/[slug]/page.tsx`, `src/data/playbooks.ts`, `content/playbook/*.md` 등)
3. **신규 추가 패턴 설계** — 기존 5개와 호환되면서 nested URL을 받아주도록
4. **한 챕터로 로컬 빌드 확인** — ch01부터 시작해 렌더 검증
5. **사이드바·breadcrumb·prev-next 컴포넌트 3종 신규 추가**
6. **사이트 레포 PR 생성** → 검토 → 머지 → 배포 트리거
7. **라이브 확인** — `/playbook/harness-engineering` 200 OK + 메뉴 노출 + ch01 페이지 정상 렌더

### 7.3 시리즈 일정 재조정 검토

오늘이 D0(2026-05-19)인데 사이트 작업에 N일 걸리면 ch00a~ch03의 published_at이 과거 날짜가 됩니다. 두 가지 옵션:

- **(A) 그대로 유지** — 백데이트로 발행, "이미 N편 공개됨" 형태로 라이브
- **(B) 일정 후방 시프트** — 사이트 라이브 날짜를 새 D0로 재설정. 메타데이터 17개를 한 패치로 일괄 이동 (이 레포에 PR 추가)

---

## 8. 참고 자료

### PR 링크 (이 레포)
- PR #1 — v1 + 다이어그램 + OG + /playbook/: https://github.com/kimsanguine/AI_Engineer/pull/1
- PR #2 — D0 발행: https://github.com/kimsanguine/AI_Engineer/pull/2
- PR #3 — 매일 발행: https://github.com/kimsanguine/AI_Engineer/pull/3

### 작업 컨벤션
- 루트 `CLAUDE.md` — habix-series 작업 톤·구조·문장 종결 컨벤션
- `habix-series/review-report-v1.md` — v1 발행 직전 자기 검토 보고서

### 강의 본문에 인용된 외부 자료
- Eugene Yan — "How to Work and Compound with AI"
- Andrej Karpathy — Behavioral guidelines / CLAUDE.md
- Anthropic — Claude Code best practices, Opus 4.5 system card
- Latent Space — "Is Harness Engineering Real?"
- Walking Labs — 원본 강의 시리즈

---

**이 문서를 다음 세션에서 가장 먼저 펴보세요. 모든 작업 컨텍스트의 시작점입니다.**
