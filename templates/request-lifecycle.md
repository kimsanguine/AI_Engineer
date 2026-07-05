# Agent Request Lifecycle Template

Agent backend를 설계할 때 요청 1건이 어디서 시작해 어디에 기록되고 어떻게
끝나는지 먼저 그린다. 이 파일은 backend 구현 전 blueprint다.

## 1. Use Case

| 항목 | 내용 |
|---|---|
| Agent/workflow name |  |
| User action |  |
| Expected output |  |
| Max acceptable latency |  |
| Human review needed? | yes/no |

## 2. Lifecycle

```text
User/UI
  -> API endpoint
  -> Auth/permission check
  -> State created
  -> Orchestrator/graph
  -> Tool/retrieval/model calls
  -> Guardrails/HITL
  -> Result stored
  -> User response
  -> Trace/eval log
```

## 3. State Table

| State | Meaning | User visible? | Retry? | Owner |
|---|---|---:|---:|---|
| queued | Request accepted | yes | no | system |
| running | Agent/tool/model running | yes | no | system |
| needs_review | Human decision required | yes | no | human |
| succeeded | Result created | yes | no | system |
| failed_retryable | Temporary failure | yes | yes | system |
| failed_final | Cannot complete | yes | no | human/system |

## 4. Tool Calls

| Tool | Purpose | Timeout | Retry | Approval | Trace fields |
|---|---|---:|---:|---:|---|
|  |  |  |  | yes/no |  |

## 5. Persistence

| Data | Store? | Retention | Reason |
|---|---:|---|---|
| User input |  |  |  |
| Retrieved source IDs |  |  |  |
| Tool args/results |  |  |  |
| Final output |  |  |  |
| Trace events |  |  |  |
| Secrets/credentials | no | none | never store |

## 6. Guardrails and HITL

| Gate | Trigger | Action |
|---|---|---|
| Input guardrail |  | allow/block/rewrite |
| Tool approval |  | approve/edit/reject |
| Output guardrail |  | return/revise/escalate |

## 7. Failure Modes

| Failure | Detection | User message | Recovery |
|---|---|---|---|
| Timeout |  |  |  |
| Tool unavailable |  |  |  |
| Permission denied |  |  |  |
| Unsafe output |  |  |  |
| Missing source |  |  |  |

## 8. Validation

- [ ] State transitions are explicit.
- [ ] Risky tool calls have approval policy.
- [ ] Trace includes tool name, args summary, result status, latency.
- [ ] No secret or private data is stored by default.
- [ ] Failure message does not claim success.

## Official References

- LangGraph overview: https://docs.langchain.com/oss/python/langgraph/overview
- LangChain human-in-the-loop middleware: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
- OpenAI Agents SDK docs: https://openai.github.io/openai-agents-python/
- OpenAI Agents SDK guide: https://developers.openai.com/api/docs/guides/agents
