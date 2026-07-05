# Product Judgment Template

Agent demo를 제품 기능이나 운영 루틴으로 바꾸기 전에 build/buy/hold를 판단한다.
이 문서는 "만들 수 있는가"가 아니라 "만들어야 하는가"를 검토한다.

## 1. Problem

| 항목 | 내용 |
|---|---|
| 대상 사용자 |  |
| 반복 상황 |  |
| 현재 대안 |  |
| 현재 대안의 불편 |  |
| 문제 빈도 | daily / weekly / monthly / rare |
| 실패 비용 | low / medium / high |

## 2. Agent Promise

| 항목 | 내용 |
|---|---|
| Agent가 대신할 일 |  |
| Agent가 보조할 일 |  |
| Agent가 절대 하지 않을 일 |  |
| 최종 산출물 |  |
| 사람 승인선 |  |

## 3. Pilot Scope

| Stage | Data | User | Claim | Exit criteria |
|---|---|---|---|---|
| public demo | synthetic/public | learner/reviewer | pattern demo |  |
| internal pilot | limited internal | operator/team | workflow support |  |
| beta | approved data | selected users | limited outcome |  |
| production | governed data | real users | operational promise |  |

## 4. Metrics

| Metric | Definition | Baseline | Target | Stop condition |
|---|---|---:|---:|---|
| Task success rate |  |  |  |  |
| Human review rate |  |  |  |  |
| Abstention quality |  |  |  |  |
| Cost per task |  |  |  |  |
| Latency |  |  |  |  |
| Incident count |  |  |  |  |

## 5. Risk Table

| Risk | Likelihood | Impact | Mitigation | Owner |
|---|---|---|---|---|
| Wrong answer |  |  |  |  |
| Tool misuse |  |  |  |  |
| Private data exposure |  |  |  |  |
| Cost spike |  |  |  |  |
| User overtrust |  |  |  |  |

## 6. Build / Buy / Hold Decision

| Decision | 기준 | 선택 |
|---|---|---|
| Build | 핵심 차별화이고 기존 도구로 해결 안 됨 |  |
| Buy/use | 범용 workflow이고 좋은 SaaS/connector가 있음 |  |
| Hold | 문제 빈도, 데이터 경계, 실패 비용이 불명확함 |  |

## 7. Next Validation

1. 
2. 
3. 

## Official References

- OpenAI practical guide to building agents: https://openai.com/business/guides-and-resources/a-practical-guide-to-building-ai-agents/
- OpenAI Agents SDK guide: https://developers.openai.com/api/docs/guides/agents
- OpenAI Agents SDK tracing/HITL overview: https://openai.github.io/openai-agents-python/
- LangChain human-in-the-loop middleware: https://docs.langchain.com/oss/python/langchain/human-in-the-loop
