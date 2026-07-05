# AI Engineer — Agent Engineering Lab

![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/kimsanguine/AI_Engineer)
![Lab](https://img.shields.io/badge/agent_engineering-lab-blue)

> **Agent를 설명하지 말고, 실행 가능한 업무 시스템으로 바꾼다.**

AI Engineer는 좋은 AI Agent 오픈소스와 Claude Code 워크플로우를
한국어 실습, PM 판단, 실행 코드, 검증 루프로 재구성하는 Agent
Engineering Lab입니다.

이 레포는 링크 모음이 아닙니다. 원본 레퍼런스를 그대로 복제하는 곳도
아닙니다. 좋은 자료를 선별한 뒤 다음 질문으로 다시 읽습니다.

- 이 패턴은 어떤 업무 문제를 해결하는가?
- 비개발자, PM, 1인 빌더가 무엇부터 따라 해야 하는가?
- 실제 파일, 코드, 데이터, 검증 로그로 어디까지 확인할 수 있는가?
- 제품화하면 어떤 비용, 운영, 안전 리스크가 생기는가?

## 시리즈 안에서의 위치

```text
[AI_Human]          ->      [AI_Engineer]        ->      [AI_PM]
 초급 100일 과정            Agent Engineering Lab       PM workflow redesign
 Python~RAG 기초            실행/검증/재구성             전략/운영/자동화
```

관련 레포:

| Repo | 역할 |
|---|---|
| [AI_Human](https://github.com/kimsanguine/AI_Human) | Python, LLM, RAG 기초 학습 |
| [AI_PM](https://github.com/kimsanguine/AI_PM) | Claude Code로 PM 업무 방식을 재설계하는 실전 가이드 |
| [llm-brain](https://github.com/kimsanguine/llm-brain) | 개인 지식과 메모리를 LLM 기반 wiki로 바꾸는 second brain |
| [hplan](https://github.com/kimsanguine/hplan) | 만들기 전에 build/no-build를 판단하는 Product Build Gate |
| [codex-agent-fieldkit](https://github.com/kimsanguine/codex-agent-fieldkit) | 비개발자용 runnable agent, eval, safety, handoff kit |

## 무엇이 달라졌나

기존 README는 `100 Agents`를 직접 구현한다는 약속이 중심이었습니다.
새 방향은 더 운영 가능합니다.

| 기존 | 개편 후 |
|---|---|
| 100개 Agent 목록 선언 | 7개 track 기반 Agent Engineering Lab |
| 비어 있는 `agents/*` 폴더 중심 | 강의, case study, starter kit, validation 중심 |
| 코드 유무 중심 | 문제 정의 -> 패턴 -> 실습 -> 검증 -> 제품 판단 |
| fork 레포가 흩어짐 | `SOURCE_MAP.md`로 출처, 라이선스, 재정의 방향 관리 |

`100 Agents`는 장기 확장 목표로 유지합니다. 다만 첫 공개 약속은
"100개가 이미 있다"가 아니라 "100개 업무형 agent 패턴으로 확장하는
검증 가능한 Lab"입니다.

## 7개 Track

| Track | 질문 | 현재 상태 |
|---|---|---|
| [01 Claude Code System](tracks/01-claude-code-system/) | Claude Code를 챗봇이 아니라 업무 시스템으로 쓰려면? | `habix-series` 자산 연결 완료 |
| [02 MCP Tools](tracks/02-mcp-tools/) | Agent가 실제 도구와 데이터를 안전하게 읽고 쓰게 하려면? | source map 준비 |
| [03 Agent Backend](tracks/03-agent-backend/) | FastAPI, LangGraph, queue, observability를 어떻게 엮나? | source map 준비 |
| [04 RAG Memory](tracks/04-rag-memory/) | 검색, graph, second brain, memory를 어떻게 제품화하나? | source map 준비 |
| [05 Evals Safety](tracks/05-evals-safety/) | Agent를 어떻게 테스트하고 공개 가능한 상태로 검증하나? | validation 기준 초안 |
| [06 Workflow Automation](tracks/06-workflow-automation/) | 반복 업무를 skill, command, automation으로 어떻게 바꾸나? | source map 준비 |
| [07 Productized Agents](tracks/07-productized-agents/) | 데모를 실제 제품/운영 루틴으로 바꾸려면? | source map 준비 |

## 먼저 시작할 곳

Claude Code를 7일 안에 업무 시스템으로 바꾸는 경로부터 시작합니다.

1. [Track 01: Claude Code System](tracks/01-claude-code-system/)을 읽습니다.
2. `habix-series/routine-pack/`의 5개 파일을 빈 프로젝트에 복사합니다.
3. `CLAUDE.md`, `feature_list.json`, `progress.md`를 채웁니다.
4. 작은 업무 하나를 정해 실행하고, 결과를 `validation-log.md`로 남깁니다.

## 현재 포함된 주요 자산

| 자산 | 위치 | 용도 |
|---|---|---|
| Harness Engineering 강의 17편 | `habix-series/lectures/` | Claude Code를 시스템으로 쓰는 한국어 강의 원천 |
| Routine Pack | `habix-series/routine-pack/` | `CLAUDE.md`, `feature_list.json`, `progress.md` 등 실습 파일 |
| Landing/Wireframe | `habix-series/landing/` | 공개 강의/플레이북 페이지 설계 자산 |
| Publishing Metadata | `habix-series/metadata/` | 시리즈 발행용 chapter/nav 메타데이터 |
| Case Study Template | `case-studies/_template/` | fork 레퍼런스를 내 관점으로 재해석하는 양식 |
| Starter Kit Template | `starter-kits/_template/` | runnable agent kit을 추가하는 양식 |
| Agent Lab Templates | `templates/` | behavior contract, tool spec, eval case, product judgment 등 공통 실습 양식 |
| Validation 기준 | `validation/` | public-first, eval, release checklist |

## 운영 원칙

1. **Source-first**: 원본 레퍼런스, 라이선스, 선택 이유를 `SOURCE_MAP.md`에 남깁니다.
2. **Reframe, do not mirror**: fork한 좋은 콘텐츠는 생근님 관점의 문제 정의와 실습으로 재구성합니다.
3. **Public-first**: 공개, 합성, 더미 데이터만 사용합니다. API key, private URL, 고객 정보는 커밋하지 않습니다.
4. **Runnable before impressive**: 멋진 설명보다 `make test`, `python agent.py`, `validation-log.md`를 우선합니다.
5. **PM judgment included**: 모든 Agent 패턴은 제품화 판단, 비용, 실패 모드, 운영 리스크를 포함합니다.

## 문서 지도

| 문서 | 역할 |
|---|---|
| [ROADMAP.md](ROADMAP.md) | 4단계 개편 계획과 milestone |
| [SOURCE_MAP.md](SOURCE_MAP.md) | fork/original source inventory와 재정의 방향 |
| [CURATION_POLICY.md](CURATION_POLICY.md) | 어떤 레퍼런스를 어떻게 고르고 바꿀지의 기준 |
| [docs/track-content-plan.md](docs/track-content-plan.md) | 7개 track을 실제 콘텐츠, template, starter kit, case study로 채우는 실행 기획 |
| [validation/eval-rubric.md](validation/eval-rubric.md) | Agent 예제 품질 평가 기준 |
| [validation/public-safety-checklist.md](validation/public-safety-checklist.md) | 공개 전 데이터/보안 점검 |
| [validation/release-checklist.md](validation/release-checklist.md) | starter kit 공개 전 확인 사항 |

## 저작권과 출처

이 레포의 신규 작성 콘텐츠는 MIT License를 따릅니다. 외부 레퍼런스와
fork에서 온 아이디어, 구조, 코드 조각은 각 원본의 라이선스와 고지 조건을
따릅니다. 재사용 전 반드시 [SOURCE_MAP.md](SOURCE_MAP.md)와
[CURATION_POLICY.md](CURATION_POLICY.md)를 확인합니다.

---

**김생근** · [GitHub](https://github.com/kimsanguine) · [LinkedIn](https://linkedin.com/in/sanguinekim)

AI B2B/B2C SaaS CPO, 20년 프로덕트 매니저. Agentic AI로 PM과
비개발자의 일하는 방식을 재설계하고 있습니다.
