# CLAUDE.md — AI_Engineer Project

## Project Context
This repository is being reorganized as **AI Engineer — Agent Engineering Lab**.
It curates strong AI agent / Claude Code / MCP / RAG references, then reframes
them through Korean-language practice, PM judgment, runnable starter kits, and
validation logs.

The existing `habix-series` remains the first major content asset: a
Korean-language lecture series on Harness Engineering for non-developers,
1-person builders, and PMs. Main message:
"Claude Code가 일을 끝까지 못 끝낸다면, 모델이 아니라 하네스가 문제입니다."

## Voice and Style
- Korean-language content targeting 비개발자/1인 빌더/PM
- No emojis in lecture files (except CLAUDE.md template which uses 💡 intentionally)
- 9-section structure per lecture: 후킹 → 문제 → 인사이트 → 사례 3개 → 표 → 5분 액션 → 자가 점검(5문항) → 마무리/예고
- 1인칭: "저는" / 운영자 자기소개: "20년 PM 출신 운영자"
- Sentence endings: "~합니다" 평서체 (not ~하세요 in main body; ~하세요 only in 5분 액션)

## Karpathy Behavioral Guidelines
(Derived from Andrej Karpathy's CLAUDE.md)

### 1. Think Before Coding
- State assumptions explicitly. If uncertain, ask.
- Present multiple interpretations — don't pick silently.
- If simpler approach exists, say so.

### 2. Simplicity First
- No features beyond what was asked.
- No abstractions for single-use code.
- If you write 200 lines and it could be 50, rewrite it.

### 3. Surgical Changes
- Touch only what you must. Match existing style.
- Don't refactor adjacent code unless asked.
- Every changed line should trace to the user's request.

### 4. Goal-Driven Execution
- Define verifiable success criteria before starting.
- Multi-step tasks: state plan with verify steps.
- Loop until verified; don't declare done without checking.

## File Map
- `README.md` — public positioning for Agent Engineering Lab
- `ROADMAP.md` — phased rework plan
- `SOURCE_MAP.md` — source/fork inventory and reframe direction
- `CURATION_POLICY.md` — reuse, license, and public-first policy
- `tracks/` — 7 learning tracks
- `case-studies/` — source reference reinterpretations
- `starter-kits/` — runnable agent examples
- `validation/` — eval, public safety, and release checklists
- `agents/` — long-term 100-agent expansion space
- `habix-series/lectures/` — 17 lecture files (ch00a through ch13 + capstone)
- `habix-series/routine-pack/` — 5 harness assets (CLAUDE.md, feature_list.json, progress.md, intent_sheet.md, session-end-checklist.md)
- `habix-series/landing/` — Landing page copy + wireframe
- `habix-series/metadata/` — Per-lecture publishing metadata
