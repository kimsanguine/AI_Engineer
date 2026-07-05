# Track 03 — Agent Backend

Agent를 데모에서 서비스 구조로 옮길 때 필요한 backend 패턴을 다룬다.

이 track은 FastAPI, LangGraph, queue, database, observability를 한꺼번에
멋있게 붙이는 과정이 아니다. "데모가 왜 운영에서 깨지는가"를 먼저 보고,
필요한 backend 부품을 최소 단위로 선택하는 과정이다.

## 대상 사용자

- agent demo를 내부 서비스나 고객-facing workflow로 바꾸려는 PM
- LangGraph, FastAPI, worker, queue 구조를 제품 관점에서 이해하려는 비개발자
- prototype과 production claim 사이의 차이를 설명해야 하는 팀 리더
- starter kit을 backend 서비스로 확장하려는 1인 빌더

## 이 Track이 해결하는 문제

노트북이나 로컬 스크립트는 한 번의 성공을 보여준다. 서비스 backend는
반복 실행, 실패 복구, 기록, 권한, 비용 관리를 책임진다.

| 데모에서는 보이지 않는 문제 | backend에서 필요한 질문 |
|---|---|
| 요청이 오래 걸림 | sync response인가, job queue인가? |
| 중간에 실패함 | retry, timeout, partial result를 어떻게 처리하나? |
| 답변 근거가 사라짐 | trace, log, source snapshot을 어디에 남기나? |
| 비용이 커짐 | model call, tool call, cache를 어떻게 측정하나? |
| 사용자가 늘어남 | rate limit, auth, tenancy가 필요한가? |

## 핵심 아키텍처

```text
User / UI
  -> API endpoint
  -> Orchestrator / graph
  -> Tools / retrieval / model
  -> Store / log / trace
  -> Result / review / retry
```

각 박스는 "있으면 좋아 보이는 기술"이 아니라 실패 모드를 막기 위해 존재한다.

| 구성요소 | 필요한 순간 | 없을 때의 증상 |
|---|---|---|
| API server | 여러 사용자가 같은 entrypoint를 써야 할 때 | 실행 방법이 사람마다 다름 |
| Orchestrator | 단계, 분기, tool call이 2개 이상일 때 | prompt 안에 상태 관리가 섞임 |
| Queue/worker | 작업이 느리거나 재시도가 필요할 때 | request timeout, 중복 실행 |
| Database | 결과, 상태, audit log를 보존해야 할 때 | 재현 불가, 운영 판단 불가 |
| Observability | 실패 원인을 추적해야 할 때 | "가끔 안 됨"만 남음 |
| Eval harness | 변경 전후 품질을 비교해야 할 때 | 개선인지 회귀인지 모름 |

## 우선 Case Study

| Source | 이 track에서 볼 관점 | Reuse level |
|---|---|---|
| `fastapi-langgraph-agent-production-ready-template` | API, graph, queue, observability의 역할 분리 | L1/L2 |
| API server + worker + eval harness 구조 | production-ready라는 표현을 검증 기준으로 분해 | L2 |

라이선스 확인 전에는 코드를 복사하지 않는다. 구조를 diagram, checklist,
starter-kit 축소판으로 재구성한다.

## 6단계 학습 경로

| Step | 주제 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Request lifecycle | agent 요청 1건의 흐름을 그린다 | sequence diagram | 입력/출력/실패 지점이 보임 |
| 2 | State model | running/succeeded/failed/retry 상태를 정의한다 | state table | 중간 실패가 기록됨 |
| 3 | Tool boundary | backend가 호출할 tool을 분리한다 | tool list | 권한과 timeout이 분리됨 |
| 4 | Logging | 무엇을 저장하고 무엇을 저장하지 않을지 정한다 | log policy | secret/PII 미저장 |
| 5 | Eval hook | 최소 golden set을 붙인다 | eval cases | 변경 전후 비교 가능 |
| 6 | Release gate | public demo와 production claim을 분리한다 | release checklist | 과장 표현 제거 |

## 실습 — Agent Backend Blueprint 작성

### 입력

- starter kit 또는 agent idea 1개
- 사용자 요청 예시 3개
- 실패 시나리오 3개

### 산출물

```text
backend-blueprint.md
├── request lifecycle
├── state table
├── tool boundary
├── logging policy
├── eval hook
└── release gate
```

### 예시 State Table

| State | Meaning | User visible? | Retry? |
|---|---|---|---|
| queued | 요청 접수 | 예 | 아니오 |
| running | tool/model 실행 중 | 예 | 아니오 |
| needs_review | 사람 확인 필요 | 예 | 아니오 |
| succeeded | 결과 생성 | 예 | 아니오 |
| failed_retryable | 일시 오류 | 예 | 예 |
| failed_final | 복구 불가 | 예 | 아니오 |

## 운영 리스크

| 리스크 | 질문 | 최소 대응 |
|---|---|---|
| Timeout | 사용자가 기다릴 수 있는 시간은 몇 초인가? | long job은 queue로 분리 |
| Cost spike | 요청 1건당 model/tool call 비용은 얼마인가? | per-run cost log |
| Data leakage | prompt/log에 private data가 남는가? | redaction, allowlist |
| Silent failure | 실패했는데 성공처럼 보이는가? | explicit status, validation |
| Drift | prompt/model/tool 변경 후 품질이 변하는가? | golden set regression |

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | 로컬 agent demo를 반복 가능한 서비스로 운영해야 함 |
| 반복 빈도 | 팀 내부 workflow나 고객-facing 기능이면 높음 |
| 비용 리스크 | model call, queue, DB, observability 비용 |
| 품질 리스크 | partial failure, stale state, retry 중복 |
| 안전 리스크 | 로그에 private data 저장, write action 오남용 |
| build/buy/hold | 핵심 업무 흐름이면 build, 일반 workflow면 플랫폼 사용, 실패 모드 불명확하면 hold |

## 완료 기준

- agent request lifecycle diagram 1개
- state table 1개
- logging policy 1개
- 실패 시나리오 3개
- release checklist에서 public demo와 production claim 분리

## 연결 템플릿

| 템플릿 | 쓰는 시점 |
|---|---|
| [Request Lifecycle](../../templates/request-lifecycle.md) | 사용자 요청 1건의 상태, 저장, 실패 흐름을 그릴 때 |
| [Tool Spec](../../templates/tool-spec.md) | backend가 호출할 tool contract를 분리할 때 |
| [Eval Cases JSONL](../../templates/eval-cases.jsonl) | request lifecycle의 happy path와 failure path를 검증할 때 |
| [Release Checklist](../../validation/release-checklist.md) | public demo와 production claim을 분리할 때 |

## 다음 확장

- retrieval이 필요하면 Track 04로 이동한다.
- eval과 safety gate를 강화하려면 Track 05로 이동한다.
- 실제 runnable backend는 `starter-kits/`에 별도 kit으로 만든다.
