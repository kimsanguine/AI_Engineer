# Track Content Plan - AI Engineer Agent Engineering Lab

## 목적

현재 7개 track README는 방향과 학습 골격을 갖췄지만, 아직 실제 교육/실습
콘텐츠로 바로 운영하기에는 각 track의 세부 모듈, case study, starter kit,
검증 산출물이 부족하다.

이 문서는 공식 문서와 원본 레퍼런스를 기준으로 각 track을 어떻게 채울지
정리한 실행 기획서다. 목표는 링크 모음이 아니라, 한국어 학습자와 PM/1인
빌더가 따라 할 수 있는 artifact 중심 Lab으로 만드는 것이다.

## 리서치 기준

우선순위는 아래 순서로 둔다.

1. 공식 문서
2. 원본 GitHub repo
3. 이미 이 repo 안에 있는 `habix-series`, `validation`, `starter-kits`
4. 라이선스가 불명확한 third-party 자료는 구조와 개념만 참고

## 핵심 참고 소스

| 영역 | Source | 확인한 핵심 |
|---|---|---|
| Claude Code | [Claude Code overview](https://docs.anthropic.com/en/docs/claude-code/overview) | Claude Code는 codebase를 읽고, 파일을 수정하고, 명령을 실행하는 agentic coding tool |
| Claude memory | [Claude Code memory](https://docs.anthropic.com/en/docs/claude-code/memory) | `CLAUDE.md`, `CLAUDE.local.md`, `/memory`, project memory 운영 방식 |
| Claude skills | [Claude Code skills](https://docs.anthropic.com/en/docs/claude-code/skills) | 반복 절차는 `SKILL.md`로 분리 가능, custom commands와 skills가 같은 invocation surface로 통합 |
| Claude hooks | [Claude Code hooks guide](https://docs.anthropic.com/en/docs/claude-code/hooks-guide) | hooks는 deterministic control에 적합, LLM 판단이 아니라 lifecycle event에 붙는 자동 실행 |
| Claude subagents | [Claude Code subagents](https://docs.anthropic.com/en/docs/claude-code/sub-agents) | 반복 worker, context isolation, code reviewer/debugger/data scientist 같은 역할 분리 |
| Claude MCP | [Claude Code MCP](https://docs.anthropic.com/en/docs/claude-code/mcp) | 복사/붙여넣기 대신 외부 tools/databases/APIs를 Claude Code에 연결 |
| MCP standard | [MCP intro](https://modelcontextprotocol.io/docs/getting-started/intro) | MCP는 AI app이 data source, tool, workflow에 연결되는 open standard |
| MCP tools | [MCP tools spec](https://modelcontextprotocol.io/specification/2025-06-18/server/tools) | tool은 name, description, input schema를 가진 model-invoked function |
| LangGraph | [LangGraph overview](https://docs.langchain.com/oss/python/langgraph/overview) | persistence, human-in-the-loop, memory, durable execution이 production agent 핵심 |
| HITL | [LangChain human-in-the-loop](https://docs.langchain.com/oss/python/langchain/human-in-the-loop) | 위험한 tool call 전 pause, approve/edit/reject 정책 구성 |
| OpenAI Agents | [OpenAI Agents SDK guide](https://developers.openai.com/api/docs/guides/agents) | agents는 planning, tools, state, specialist collaboration을 포함하는 application pattern |
| OpenAI Agents SDK | [Agents SDK docs](https://openai.github.io/openai-agents-python/) | sessions, HITL, tracing, guardrails를 agent loop 안에서 다룸 |
| OpenAI guardrails | [Agents SDK guardrails](https://openai.github.io/openai-agents-python/guardrails/) | input/output validation, 빠른 모델/저비용 guardrail로 위험 요청 차단 가능 |
| OpenAI eval datasets | [OpenAI datasets/evals](https://developers.openai.com/api/docs/guides/evaluation-getting-started) | dataset과 grader로 prompt/application behavior를 빠르게 평가 |
| RAGAS | [RAGAS metrics](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/) | RAG와 agentic workflow 평가 metric 제공 |
| RAGAS faithfulness | [RAGAS faithfulness](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/) | 답변 claim이 retrieved context로 지지되는지 평가 |
| RAGAS context precision | [RAGAS context precision](https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/) | retriever가 관련 chunk를 상위에 배치하는지 평가 |
| LangSmith RAG eval | [LangSmith RAG evaluation](https://docs.langchain.com/langsmith/evaluate-rag-tutorial) | test dataset 생성, app 실행, metric 측정 흐름 |
| Google ADK eval | [ADK eval codelab](https://codelabs.developers.google.com/adk-eval/instructions) | golden dataset과 automated evaluation으로 regression을 잡는 방식 |

## 전체 콘텐츠 설계 원칙

각 track은 같은 골격을 가진다.

```text
Problem
-> Mental model
-> Pattern library
-> Guided exercise
-> Artifact template
-> Validation
-> Product judgment
-> Next starter kit or case study
```

각 track마다 최소 4개 산출물이 있어야 한다.

1. `README.md` - 학습 경로
2. `case-studies/{source}/README.md` - 외부 레퍼런스 재정의
3. `templates/{artifact}.md` 또는 starter kit - 직접 쓸 수 있는 양식
4. `validation-log.md` 또는 eval/golden set - 검증 기록

## Track 01 - Claude Code System

### 채울 방향

Track 01은 이미 `habix-series`와 `routine-pack`이라는 강한 내부 자산이 있다.
여기서는 새 이론보다 "실습 루틴화"가 중요하다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. Project memory | `CLAUDE.md`, `CLAUDE.local.md`, `/memory` 차이 | `templates/project-claude.md` |
| 02. Progress memory | 세션 간 이어받기, status separation | `templates/progress-log.md` |
| 03. Skill extraction | 반복 지시를 `SKILL.md`로 분리 | `case-studies/claude-skill-extraction/` |
| 04. Hooks vs CLAUDE.md | deterministic rule은 hook, judgment는 instruction | `templates/hook-decision-table.md` |
| 05. Subagent delegation | reviewer/debugger/researcher 역할 분리 | `templates/subagent-brief.md` |
| 06. Cost/context hygiene | skill, hook, memory로 context 낭비 줄이기 | `validation/context-hygiene-checklist.md` |

### 우선 작성할 파일

- `templates/project-claude.md`
- `templates/progress-log.md`
- `case-studies/claude-code-memory/README.md`
- `case-studies/skill-vs-hook/README.md`

### 검증 기준

- 빈 프로젝트에 routine pack을 복사해 Claude Code가 다음 작업을 제안할 수 있어야 한다.
- 같은 요청을 새 세션에서 반복했을 때, `CLAUDE.md`와 `progress.md`만으로 맥락을 복원해야 한다.

## Track 02 - MCP Tools

### 채울 방향

MCP는 protocol 설명보다 "내 업무 도구를 안전하게 Agent에게 연결하는 법"으로
가르쳐야 한다. 공식 MCP 문서가 tool/resource/prompt 구조를 제공하므로,
이 track은 tool contract와 권한 경계를 먼저 잡는다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. MCP mental model | host/client/server/tool/resource/prompt | `templates/mcp-system-map.md` |
| 02. Tool contract | tool name, description, input schema, output trace | `templates/tool-spec.md` |
| 03. Read/write boundary | read-only, draft, write, destructive action 분류 | `templates/tool-risk-table.md` |
| 04. Dummy data MCP | public JSON/CSV를 읽는 최소 MCP 서버 설계 | `starter-kits/mcp-tool-agent/` |
| 05. MCP failure modes | unavailable server, stale schema, permission error | `validation/mcp-failure-log.md` |
| 06. Claude Code integration | `.mcp.json`, `/mcp`, project-level setting 운영 | `case-studies/claude-code-mcp/` |

### 우선 작성할 파일

- `templates/tool-spec.md`
- `templates/tool-risk-table.md`
- `starter-kits/mcp-tool-agent/README.md`
- `case-studies/mcp-for-beginners/README.md`

### 검증 기준

- API key 없이 synthetic JSON을 읽는 tool demo가 있어야 한다.
- write action은 항상 approval line이 있어야 한다.
- tool output에 source 또는 trace가 있어야 한다.

## Track 03 - Agent Backend

### 채울 방향

Track 03은 "FastAPI/LangGraph를 써보자"가 아니라, agent demo가 서비스로
갈 때 필요한 상태, queue, persistence, HITL, observability를 설명해야 한다.
LangGraph 공식 문서의 persistence/HITL/memory 축과 OpenAI Agents SDK의
tracing/session/guardrails 축을 함께 쓴다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. Request lifecycle | API -> graph -> tool -> trace -> result | `templates/request-lifecycle.md` |
| 02. State table | queued/running/needs_review/succeeded/failed | `templates/agent-state-table.md` |
| 03. HITL approval | risky tool call 전 pause/approve/edit/reject | `templates/hitl-policy.md` |
| 04. Persistence | thread/session/checkpoint/memory 구분 | `case-studies/langgraph-persistence/` |
| 05. Observability | traces, spans, tool calls, guardrail events | `templates/trace-review.md` |
| 06. Backend starter | FastAPI 없이 시작하는 local service blueprint | `starter-kits/agent-backend-blueprint/` |

### 우선 작성할 파일

- `templates/request-lifecycle.md`
- `templates/hitl-policy.md`
- `case-studies/fastapi-langgraph-agent-production-ready-template/README.md`
- `starter-kits/agent-backend-blueprint/README.md`

### 검증 기준

- "production-ready"라는 표현은 금지하고, 어떤 운영 조건을 충족했는지만 적는다.
- 최소 3개 failure mode와 retry/abort/review 기준이 있어야 한다.

## Track 04 - RAG Memory

### 채울 방향

RAG는 검색 품질 평가와 public/private data boundary가 핵심이다. RAGAS,
LangSmith, LlamaIndex/RAG 평가 문서에서 공통적으로 나타나는 핵심은
retrieval quality와 answer groundedness를 분리해서 보는 것이다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. Corpus map | source, freshness, owner, public/private 분류 | `templates/corpus-map.md` |
| 02. Chunk and metadata | chunk size보다 source trace와 metadata 설계 | `templates/document-metadata.md` |
| 03. Golden set | 질문, expected source, must-not-claim | `templates/rag-golden-set.csv` |
| 04. Retrieval eval | context precision, recall, irrelevant chunk 점검 | `validation/retrieval-log.md` |
| 05. Answer eval | faithfulness, citation support, abstention | `validation/rag-answer-eval.md` |
| 06. Memory policy | session/project/user memory와 삭제/수정 기준 | `templates/memory-policy.md` |

### 우선 작성할 파일

- `templates/corpus-map.md`
- `templates/rag-golden-set.csv`
- `case-studies/rag-eval-metrics/README.md`
- `starter-kits/document-brief-agent/README.md`

### 검증 기준

- 10문항 golden set이 있어야 한다.
- 없는 정보 질문에 추측하지 않는 abstention case가 있어야 한다.
- citation이 답변 문장을 실제로 지지하는지 수동 검증 항목이 있어야 한다.

## Track 05 - Evals Safety

### 채울 방향

Track 05는 모든 track의 release gate 역할을 한다. OpenAI datasets/evals,
ADK eval, RAGAS, LangSmith의 공통점은 "작은 golden dataset을 만들고,
변경 전후를 비교하며, failure case를 남긴다"는 점이다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. Behavior contract | 해야 할 일, 하지 말 일, 모르면 멈출 일 | `templates/behavior-contract.md` |
| 02. Eval cases | normal, edge, refusal, tool failure | `templates/eval-cases.jsonl` |
| 03. Public safety | secret, PII, private URL, real customer data scan | 기존 checklist 확장 |
| 04. Guardrails | input guardrail, output guardrail, tool guardrail | `templates/guardrail-policy.md` |
| 05. Trace to eval | production failure를 eval case로 바꾸기 | `templates/trace-to-eval.md` |
| 06. Release review | score, residual risk, next validation | `templates/release-review.md` |

### 우선 작성할 파일

- `templates/behavior-contract.md`
- `templates/eval-cases.jsonl`
- `templates/guardrail-policy.md`
- `case-studies/faq-agent-lite-eval/README.md`

### 검증 기준

- 각 starter kit은 최소 5개 eval case를 가져야 한다.
- 실패/거절 케이스가 최소 1개 있어야 한다.
- validation log에는 command, observed output, interpretation, remaining risk가 분리되어야 한다.

## Track 06 - Workflow Automation

### 채울 방향

Workflow Automation은 prompt library가 아니라 skill/command/hook/approval
system으로 가야 한다. Claude Code 공식 문서 기준으로 skills는 반복 절차,
hooks는 deterministic lifecycle enforcement, subagents는 context-isolated
worker에 적합하다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. Repetition audit | 반복 업무 후보를 빈도/시간/위험으로 평가 | `templates/automation-backlog.md` |
| 02. Skill spec | trigger, input, steps, output, validation | `templates/skill-spec.md` |
| 03. Command vs skill vs hook | 어디에 넣을지 결정 | `templates/automation-decision-table.md` |
| 04. Approval line | draft/send/delete/deploy/billing 경계 | `templates/approval-line.md` |
| 05. Output templates | digest, report, draft, PR note | `templates/output-contract.md` |
| 06. Marketing/research workflow | GEO/SEO, research, content workflow case | `case-studies/geo-seo-claude/README.md` |

### 우선 작성할 파일

- `templates/skill-spec.md`
- `templates/automation-decision-table.md`
- `case-studies/geo-seo-claude/README.md`
- `case-studies/ai-marketing-skills/README.md`

### 검증 기준

- 자동화마다 사람 승인선이 있어야 한다.
- 외부 발송/send/publish/deploy는 draft-only 기본값으로 둔다.
- output artifact가 파일로 남아야 한다.

## Track 07 - Productized Agents

### 채울 방향

Track 07은 agent idea를 제품 판단으로 바꾸는 track이다. OpenAI Agents guide는
tools/state/orchestration이 필요한 경우 Agents SDK로 확장하라고 설명하고,
LangChain/HITL/OpenAI guardrails 문서는 위험 action 전 사람 개입을 강조한다.
이 track은 그 기술 판단을 build/buy/hold memo로 번역해야 한다.

### 세부 모듈

| Module | 내용 | 산출물 |
|---|---|---|
| 01. Problem/JTBD | 반복 문제, 사용자, 현재 대안 | `templates/problem-memo.md` |
| 02. Agent promise | agent가 대신할 일과 하지 않을 일 | `templates/agent-promise.md` |
| 03. Pilot scope | public demo, internal pilot, beta, production 분리 | `templates/pilot-plan.md` |
| 04. Metrics | success rate, abstention, review rate, cost, latency | `templates/agent-metrics.md` |
| 05. Stop conditions | 언제 멈추고 사람 검토로 돌릴지 | `templates/stop-conditions.md` |
| 06. Build/buy/hold | 만들지, 살지, 보류할지 판단 | `templates/product-judgment.md` |

### 우선 작성할 파일

- `templates/product-judgment.md`
- `templates/agent-metrics.md`
- `case-studies/vibe-investing/README.md`
- `case-studies/kronos/README.md`

### 검증 기준

- high-stakes 영역은 public demo와 production claim을 분리한다.
- finance/data agent는 실제 투자 조언, 주문, 계좌 연결을 포함하지 않는다.
- build/buy/hold 결정과 다음 검증 행동이 있어야 한다.

## 우선순위 로드맵

### Sprint 1 - Templates first

목표: 모든 track에서 바로 쓸 수 있는 공통 artifact를 만든다.

Status: baseline completed on 2026-07-05.

1. `templates/tool-spec.md`
2. `templates/behavior-contract.md`
3. `templates/eval-cases.jsonl`
4. `templates/product-judgment.md`
5. `templates/skill-spec.md`
6. `templates/corpus-map.md`
7. `templates/request-lifecycle.md`

### Sprint 2 - Starter kits

목표: 읽을거리에서 runnable lab으로 전환한다.

1. `starter-kits/mcp-tool-agent`
2. `starter-kits/document-brief-agent`
3. `starter-kits/agent-backend-blueprint`

### Sprint 3 - Case studies

목표: SOURCE_MAP의 우선순위 레퍼런스를 생근님 관점으로 재정의한다.

1. `case-studies/mcp-for-beginners`
2. `case-studies/fastapi-langgraph-agent-production-ready-template`
3. `case-studies/geo-seo-claude`
4. `case-studies/rag-eval-metrics`
5. `case-studies/vibe-investing`

### Sprint 4 - Track README deepening

목표: 각 track README에서 위 artifact와 case study를 링크해 실제 학습
순서를 완성한다.

## 다음 작업 제안

Sprint 1 baseline은 완료했다. 바로 다음 세션에서는 Sprint 2로 넘어가
starter kit을 만드는 것이 맞다. 이유는 세부 lecture를 쓰기 전에 runnable
lab이 있어야 track별 콘텐츠가 같은 실행 기준으로 쌓인다.

가장 먼저 만들 starter kit은 아래 3개다.

1. `starter-kits/mcp-tool-agent`
2. `starter-kits/document-brief-agent`
3. `starter-kits/agent-backend-blueprint`

이 3개가 있으면 Track 02, 03, 05, 07의 실습 골격이 runnable 형태로 생기고,
이후 case study가 같은 format으로 연결된다.
