# Behavior Contract Template

Agent 또는 workflow를 만들기 전에 "무엇을 해야 하는가"와 "무엇을 하면
안 되는가"를 먼저 정의한다. 이 파일은 prompt보다 먼저 작성하는 제품 계약서다.

## 1. 목적

| 항목 | 내용 |
|---|---|
| Agent/workflow 이름 |  |
| 대상 사용자 |  |
| 반복 문제 |  |
| 기대 산출물 |  |
| 사용하면 안 되는 데이터 |  |

## 2. 해야 할 일

| ID | Required behavior | 기준 |
|---|---|---|
| B-001 |  |  |
| B-002 |  |  |
| B-003 |  |  |

## 3. 하지 말아야 할 일

| ID | Forbidden behavior | 이유 | 대응 |
|---|---|---|---|
| F-001 | 추측으로 답변하지 않는다 | 신뢰 하락 | 근거 없음/모름 처리 |
| F-002 | private data를 요구하지 않는다 | 공개/보안 경계 | public/synthetic data만 사용 |
| F-003 | 승인 없이 write/send/delete/deploy하지 않는다 | 비가역 작업 위험 | draft 또는 approval 필요 |

## 4. 모르면 어떻게 할 것인가

| 상황 | 응답 방식 | 다음 행동 |
|---|---|---|
| source 없음 |  |  |
| tool 실패 |  |  |
| 입력 부족 |  |  |
| 권한 없음 |  |  |

## 5. Human Approval Line

| 작업 | 자동 가능 | 승인 필요 | 메모 |
|---|---:|---:|---|
| 읽기/검색 | yes | no |  |
| 요약/분류 | yes | no |  |
| 초안 작성 | yes | no | draft-only |
| 외부 발송 | no | yes |  |
| DB/schema/write action | no | yes |  |
| 삭제/배포/결제/credential 변경 | no | yes |  |

## 6. Eval Cases

| ID | Input | Expected behavior | Forbidden behavior | Evidence |
|---|---|---|---|---|
| E-001 |  |  |  |  |
| E-002 |  |  |  |  |
| E-003 |  |  |  |  |

## 7. Release Gate

- [ ] required behavior가 3개 이상 정의되어 있다.
- [ ] forbidden behavior가 3개 이상 정의되어 있다.
- [ ] 모름/실패/권한 없음 대응이 있다.
- [ ] human approval line이 있다.
- [ ] eval case가 최소 5개 있다.
- [ ] public-first safety checklist를 통과했다.

## Official References

- OpenAI Agents SDK guide: https://developers.openai.com/api/docs/guides/agents
- OpenAI Agents SDK guardrails: https://openai.github.io/openai-agents-python/guardrails/
- LangChain human-in-the-loop middleware: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- Claude Code hooks guide: https://docs.anthropic.com/en/docs/claude-code/hooks-guide
