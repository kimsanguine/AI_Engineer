# Track 02 — MCP Tools

Agent가 실제 업무 도구를 읽고 쓰게 만드는 연결 계층을 다룬다.

MCP는 "모델에게 플러그인을 붙이는 기술"이 아니라, Agent에게 어떤 도구를
어떤 권한으로 열어줄지 정하는 운영 계약이다. 이 track은 MCP를 프로토콜
설명에서 출발하지 않고, 비개발자와 PM이 이해할 수 있는 업무 연결 문제로
다시 설명한다.

## 대상 사용자

- Claude Code, ChatGPT, Cursor, Codex에서 외부 도구를 연결하고 싶은 PM
- Google Drive, Slack, Notion, GitHub, DB 같은 업무 surface를 Agent에게 열어주려는 운영자
- MCP 서버를 처음 만들거나 도입하려는 교육생
- tool 권한, read/write 경계, 승인선을 문서화해야 하는 팀 리더

## 이 Track이 해결하는 문제

채팅 입력만으로는 실제 업무가 끝나지 않는다. Agent가 문서를 찾고, 이슈를
읽고, 데이터를 조회하고, 초안을 만들고, 필요한 경우 상태를 바꿔야 한다.
문제는 연결 자체보다 권한과 실패 처리다.

| 흔한 실패 | 원인 | 필요한 장치 |
|---|---|---|
| Agent가 엉뚱한 파일을 읽음 | resource discovery 기준 없음 | 읽기 범위, 파일 선택 규칙 |
| 쓰기 작업이 너무 쉽게 일어남 | approval line 없음 | draft-only, dry-run, explicit approval |
| 도구 오류를 숨김 | fallback path 없음 | 실패 메시지, 수동 경로 |
| private data가 노출됨 | public/private boundary 없음 | dummy data, PII 금지, secret scan |

## 핵심 개념

### 1. Tool은 기능이 아니라 계약이다

도구 이름, 입력 schema, 출력 형태, 실패 메시지는 Agent와 사람 사이의
계약이다. 좋은 tool은 "무엇을 할 수 있는가"보다 "무엇을 하지 않는가"가
명확하다.

### 2. Read와 Write를 분리한다

읽기 도구는 비교적 넓게 열 수 있지만, 쓰기 도구는 승인선이 필요하다.
초안 생성, preview, dry-run은 안전하지만 send, delete, deploy, schema
write는 별도 승인 단계로 둔다.

### 3. MCP는 UI가 아니라 운영 surface다

MCP 서버를 붙였다고 일이 자동으로 끝나지 않는다. 어떤 도구를 언제 쓰고,
결과를 어디에 기록하고, 실패하면 어떻게 멈출지까지 설계해야 한다.

## 우선 Case Study

| Source | 이 track에서 볼 관점 | Reuse level |
|---|---|---|
| `mcp-for-beginners` | MCP 개념, client/server/tool/resource 구조 | L1/L2 |
| `real-estate-mcp` | 공개 데이터 기반 단일 업무 tool 예시 | L1/L2 |
| 공개 API 단일 도구 예제 | API key 없이 tool contract를 설명하는 최소 예제 | L2 |

`SOURCE_MAP.md`의 license status가 "확인 필요"인 동안에는 원본 코드를
복사하지 않는다. 구조와 아이디어를 내 언어로 재구성한다.

## 5단계 학습 경로

| Step | 주제 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Tool boundary | read/write/draft/delete 작업을 분류한다 | tool risk table | 비가역 작업이 분리됨 |
| 2 | Input schema | tool 하나의 입력과 출력 contract를 쓴다 | tool spec 초안 | 잘못된 입력의 오류가 명확함 |
| 3 | Dummy data | public/synthetic 데이터로 실습한다 | sample payload | private data 없음 |
| 4 | Fallback path | tool 실패 시 사람이 할 수 있는 경로를 적는다 | failure table | 실패를 숨기지 않음 |
| 5 | MCP handoff | Agent가 언제 tool을 써야 하는지 지침화한다 | `CLAUDE.md` tool section | 같은 요청에 같은 tool 선택 |

## 실습 — "읽기 전용 업무 도구" 설계

### 입력

- 공개 JSON 또는 합성 CSV 1개
- 조회하고 싶은 질문 5개
- tool 이름 1개

### 예시 업무

```text
업무: 교육 과정 FAQ 검색
Tool name: search_course_faq
Allowed data: sample_data/faqs.json
Forbidden data: 실제 수강생 이름, 점수, 연락처, 내부 링크
Write access: 없음
Fallback: 검색 결과가 없으면 "자료에 없음" 반환
```

### 산출물

```text
tool-spec.md
sample_data/
validation-log.md
```

## Tool 설계 체크리스트

- [ ] tool 이름이 업무 동사를 포함한다.
- [ ] 입력 schema에 필수/선택 필드가 분리되어 있다.
- [ ] 출력에 source 또는 trace가 있다.
- [ ] 실패 시 빈 답변이 아니라 이유를 반환한다.
- [ ] read-only와 write action이 같은 tool에 섞여 있지 않다.
- [ ] private data를 요구하지 않는다.
- [ ] 쓰기 작업은 draft, preview, explicit approval로 분리되어 있다.

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | Agent가 업무 도구를 직접 읽지 못해 사람이 복사/붙여넣기를 반복함 |
| 반복 빈도 | 높음. 문서 검색, issue triage, CRM/CS 조회에서 자주 발생 |
| 비용 리스크 | tool 호출 수, API rate limit, 권한 관리 비용 |
| 품질 리스크 | 잘못된 파일 조회, stale data, schema 변경 |
| 안전 리스크 | private data, write action, irreversible state change |
| build/buy/hold | 기존 connector가 있으면 buy/use, 내부 업무 특화는 build, 권한 불명확하면 hold |

## 완료 기준

이 track을 완료했다는 말은 다음을 갖췄다는 뜻이다.

- read-only tool spec 1개
- write action approval table 1개
- public/synthetic sample data 1개
- 실패 시나리오가 포함된 validation log
- `SOURCE_MAP.md`에 참조 source와 reuse level 기록

## 연결 템플릿

| 템플릿 | 쓰는 시점 |
|---|---|
| [Tool Spec](../../templates/tool-spec.md) | tool 이름, input schema, output contract, failure mode를 정의할 때 |
| [Behavior Contract](../../templates/behavior-contract.md) | read/write/approval boundary를 사람과 agent의 계약으로 고정할 때 |
| [Eval Cases JSONL](../../templates/eval-cases.jsonl) | tool 실패, 모름, 승인 필요 case를 검증 세트로 만들 때 |

## 다음 확장

- 실행 가능한 `mcp-tool-agent` starter kit으로 이동한다.
- 도구 호출 결과를 eval하려면 Track 05로 이동한다.
- tool이 backend queue나 database를 필요로 하면 Track 03으로 이동한다.
