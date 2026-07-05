# SOURCE_MAP.md — 외부 레퍼런스와 재정의 지도

이 파일은 AI_Engineer가 참고하거나 fork로 가져온 좋은 콘텐츠를 추적한다.
목적은 원본을 그대로 복제하는 것이 아니라, 출처와 라이선스를 존중하면서
생근님 관점의 한국어 실습, 제품 판단, 검증 루프로 재구성하는 것이다.

## 사용 규칙

- 원본 URL과 라이선스는 확인된 범위에서 기록한다.
- 라이선스가 불명확하면 코드 복사 없이 개념 해설과 링크만 사용한다.
- 원본의 강점과 이 레포에서의 재정의 방향을 분리한다.
- 실제 코드나 문서 조각을 가져오면 변경 범위와 고지 위치를 남긴다.

## 우선순위 레퍼런스

| Source | Type | Why selected | Reframe in AI_Engineer | License status | Target |
|---|---|---|---|---|---|
| `mcp-for-beginners` | Fork/reference | MCP 개념과 다중 언어 예제가 풍부함 | "프로토콜"보다 "내 업무 도구를 Agent에게 안전하게 연결하는 법"으로 재정의 | 확인 필요 | `tracks/02-mcp-tools`, `case-studies/mcp-for-beginners` |
| `fastapi-langgraph-agent-production-ready-template` | Fork/reference | Agent backend의 production 구조를 빠르게 보여줌 | 비개발자에게 backend 구성요소를 업무 운영 관점으로 설명 | 확인 필요 | `tracks/03-agent-backend` |
| `oh-my-claudecode` | Fork/reference | Claude Code multi-agent, skill, orchestration 아이디어가 많음 | "파워유저 도구"가 아니라 반복 업무를 팀처럼 나누는 운영 패턴으로 재정의 | 확인 필요 | `tracks/01-claude-code-system`, `tracks/06-workflow-automation` |
| `gstack` | Fork/reference | CEO/Designer/Eng Manager 등 역할 기반 Claude Code setup | 역할 기반 agent team을 PM/1인 빌더의 의사결정 구조로 번역 | 확인 필요 | `case-studies/gstack` |
| `geo-seo-claude` | Fork/reference | GEO/SEO 업무형 skill의 실전성이 높음 | 마케팅 자동화 예제가 아니라 "업무 skill 제품화" 사례로 재구성 | 확인 필요 | `tracks/06-workflow-automation` |
| `ai-marketing-skills` | Fork/reference | 성장/마케팅 업무 skill이 풍부함 | PM/마케터가 반복 업무를 skill로 포장하는 실습으로 전환 | 확인 필요 | `tracks/06-workflow-automation` |
| `urstory-rag` | Fork/reference | 한국어 RAG, rerank, guardrail, monitoring 요소가 풍부함 | production RAG를 "검색 품질 + 안전 + 운영" 관점으로 분해 | 확인 필요 | `tracks/04-rag-memory`, `tracks/05-evals-safety` |
| `graphrag-tools-retriever` | Fork/reference | GraphRAG와 tool retriever 구조 이해에 도움 | "GraphRAG를 언제 쓸 가치가 있는가" 제품 판단으로 재정의 | 확인 필요 | `tracks/04-rag-memory` |
| `vibe-investing` | Fork/reference | 금융 데이터, multi-agent, backtesting 소재가 있음 | finance/data agent의 위험 경계와 검증 중심으로 재구성 | 확인 필요 | `tracks/07-productized-agents` |
| `kronos` | Fork/reference | 금융 시장 foundation model 소재 | 모델 데모보다 데이터/예측/리스크 설명 사례로 제한 사용 | 확인 필요 | `tracks/07-productized-agents` |

## 내부 자산

| Asset | Role | Reframe |
|---|---|---|
| `habix-series/lectures/` | Harness Engineering 강의 17편 | Track 01의 원천 커리큘럼 |
| `habix-series/routine-pack/` | Claude Code 루틴 파일 5종 | Day 2~7 실습 산출물 |
| `habix-series/review-report-v1.md` | 발행 전 자체 검토 | 공개 전 validation 예시 |
| `templates/agent-template.md` | 기존 Agent 문서 템플릿 | Phase 4에서 새 표준으로 대체 예정 |

## 다음 업데이트

- 각 source의 실제 GitHub URL과 라이선스 파일을 확인한다.
- 우선순위 5개 case study부터 `case-studies/`에 작성한다.
- 코드 복사 여부를 결정하기 전 `CURATION_POLICY.md`의 reuse level을 적용한다.
