# ROADMAP.md — AI Engineer 개편 로드맵

## 목표

AI_Engineer를 `100 Agents` 선언형 레포에서 Agent Engineering Lab으로
개편한다. 좋은 오픈소스와 fork 레퍼런스를 생근님 관점으로 재정의하고,
한국어 실습, 실행 가능한 starter kit, 검증 로그, 제품 판단까지 이어지는
구조를 만든다.

## 성공 기준

- 처음 방문한 사람이 이 레포의 역할을 3분 안에 이해한다.
- `Track 01`을 따라 하면 Claude Code 프로젝트 루틴 파일 3개 이상을 만들 수 있다.
- 각 외부 레퍼런스는 출처, 라이선스, 선택 이유, 재정의 방향이 남아 있다.
- starter kit은 실행 명령, 샘플 데이터, 테스트 또는 검증 체크리스트를 가진다.
- 공개 데이터 경계가 문서와 템플릿에 반복적으로 박혀 있다.

## Phase 0 — 기준선 정리

상태: 완료 초안

산출물:

- README 재정의
- `SOURCE_MAP.md`
- `CURATION_POLICY.md`
- `validation/*` 기본 체크리스트
- `case-studies/_template/`
- `starter-kits/_template/`

검증:

- 루트에서 핵심 문서 링크가 깨지지 않는다.
- 기존 `habix-series` 자산을 삭제하지 않는다.

## Phase 1 — Claude Code System Track 완성

목표: 이미 존재하는 `habix-series`를 첫 번째 공식 track으로 승격한다.

작업:

1. `tracks/01-claude-code-system/README.md` 완성
2. 7일 학습 경로를 강의 17편과 routine pack에 연결
3. `routine-pack`을 실제 프로젝트에 복사해 쓰는 실습 가이드 작성
4. `validation-log.md` 샘플 추가

완료 기준:

- Day 1~7 각각 입력 파일, 활동, 산출물, 검증 기준이 있다.
- `habix-series/lectures/*` 중 어떤 파일을 읽어야 하는지 연결되어 있다.

## Phase 2 — Source Map 기반 Case Study 5개 작성

목표: fork 레퍼런스를 단순 목록이 아니라 생근님 관점의 해설/실습으로 바꾼다.

우선순위:

1. `mcp-for-beginners` — MCP 기본과 도구 연결
2. `fastapi-langgraph-agent-production-ready-template` — production backend
3. `oh-my-claudecode` 또는 `gstack` — Claude Code 운영 체계
4. `geo-seo-claude` 또는 `ai-marketing-skills` — workflow automation
5. `urstory-rag` 또는 `graphrag-tools-retriever` — RAG/memory

완료 기준:

- 각 case study가 원본 출처, 잘하는 점, 재정의, 실습, 검증, 제품 판단을 포함한다.
- 원본 코드 복사는 최소화하고, 필요한 경우 라이선스와 변경 범위를 명시한다.

## Phase 3 — Starter Kit 3개 완성

목표: 레포가 읽을거리에서 실행 가능한 Lab으로 전환된다.

우선순위:

1. `faq-agent-lite` — 합성 FAQ 기반 검색/응답
2. `document-brief-agent` — 문서 요약/브리핑/액션아이템
3. `mcp-tool-agent` — 도구 연결 구조를 보여주는 최소 예제

완료 기준:

- 각 starter kit은 `README.md`, 샘플 데이터, 실행 명령, 검증 로그를 가진다.
- API key 없이 실행 가능한 경로를 우선 제공한다.
- API가 필요한 확장은 별도 optional 단계로 분리한다.

## Phase 4 — 100 Agents 확장 체계 복원

목표: 기존 `agents/` 폴더를 장기 확장 목표로 되살린다.

작업:

1. `agents/README.md` 추가
2. 카테고리를 track과 연결
3. 각 Agent 항목을 `problem -> pattern -> implementation -> validation -> product judgment`로 표준화
4. `starter-kits`에서 검증된 예제만 `agents/`로 승격

완료 기준:

- `0/100`처럼 비어 보이는 표기 대신 검증 상태별 pipeline을 보여준다.
- 최소 3개 Agent가 runnable 또는 documented prototype 상태다.

## 운영 cadence

- 매주 1개 case study 또는 1개 starter kit을 완성한다.
- 모든 변경은 `SOURCE_MAP.md`와 validation checklist를 함께 업데이트한다.
- 공개 전 `validation/public-safety-checklist.md`를 확인한다.
