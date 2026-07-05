# Agent Lab Templates

이 폴더는 7개 track에서 반복해서 사용하는 공통 artifact 양식이다. 각
템플릿은 prompt보다 먼저 쓰는 운영 계약서 역할을 한다.

## Template Map

| Template | Primary Track | Use When |
|---|---|---|
| [behavior-contract.md](behavior-contract.md) | Track 01, 05, 07 | agent/workflow의 required behavior, forbidden behavior, approval line을 정할 때 |
| [tool-spec.md](tool-spec.md) | Track 02, 03 | MCP tool, API tool, read/write tool contract를 정의할 때 |
| [eval-cases.jsonl](eval-cases.jsonl) | Track 05 | 정상, 모름, private data, tool failure, approval case를 최소 세트로 만들 때 |
| [product-judgment.md](product-judgment.md) | Track 07 | agent idea를 product/pilot/build-buy-hold 관점으로 판단할 때 |
| [skill-spec.md](skill-spec.md) | Track 06 | 반복 업무를 Claude Code/Codex skill 또는 command로 바꿀 때 |
| [corpus-map.md](corpus-map.md) | Track 04 | RAG, memory, second brain corpus와 golden questions를 설계할 때 |
| [request-lifecycle.md](request-lifecycle.md) | Track 03 | agent backend의 request state, tool calls, persistence, failure mode를 정리할 때 |
| [agent-template.md](agent-template.md) | Phase 4 | 장기적으로 100 Agents 항목을 표준화할 때 |

## Public Rule

템플릿은 공개 repo에서 바로 볼 수 있는 실행 양식이다. 내부 기획 문서,
private URL, 실제 고객/수강생 데이터, API key, 계정 정보는 이 폴더에 넣지
않는다.
