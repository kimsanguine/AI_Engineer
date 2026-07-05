# Corpus Map Template

RAG 또는 memory agent를 만들기 전에 문서 집합의 범위, 출처, 최신성, 권한을
정리한다. 좋은 RAG는 embedding 이전에 corpus map이 있다.

## 1. Corpus Summary

| 항목 | 내용 |
|---|---|
| Corpus name |  |
| Use case |  |
| Target users |  |
| Public/private scope | public / synthetic / internal / private |
| Update frequency | static / weekly / monthly / event-driven |
| Owner |  |

## 2. Source Inventory

| Source ID | Title | Location | Data class | Owner | Freshness | Include? |
|---|---|---|---|---|---|---:|
| SRC-001 |  |  | public/synthetic/internal/private |  |  | yes/no |
| SRC-002 |  |  | public/synthetic/internal/private |  |  | yes/no |

## 3. Metadata Contract

| Field | Required | Example | Purpose |
|---|---:|---|---|
| `source_id` | yes | SRC-001 | citation and eval |
| `title` | yes |  | user-readable citation |
| `section` | no |  | local grounding |
| `updated_at` | yes | 2026-07-05 | freshness check |
| `data_class` | yes | public | safety boundary |
| `owner` | no |  | escalation |

## 4. Chunking Policy

| 항목 | 결정 |
|---|---|
| Chunk unit | paragraph / section / page / record |
| Max chunk size |  |
| Overlap |  |
| Keep tables? | yes/no |
| Keep code blocks? | yes/no |
| Citation granularity | document / section / chunk |

## 5. Golden Questions

| Question ID | Question | Expected source | Must not claim |
|---|---|---|---|
| Q-001 |  |  |  |
| Q-002 |  |  |  |
| Q-003 |  | NONE |  |

## 6. Retrieval Validation

- [ ] Top-k results include expected source for known questions.
- [ ] Unknown questions return no unsupported claim.
- [ ] Private/internal sources do not appear in public demo.
- [ ] Stale sources are flagged or excluded.
- [ ] Citation supports the answer sentence.

## 7. Memory Policy

| Memory type | Allowed? | Retention | Delete/edit path |
|---|---:|---|---|
| Session memory |  |  |  |
| Project memory |  |  |  |
| User memory |  |  |  |
| Long-term semantic memory |  |  |  |

## Official References

- RAGAS metrics: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/
- RAGAS faithfulness: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/faithfulness/
- RAGAS context precision: https://docs.ragas.io/en/stable/concepts/metrics/available_metrics/context_precision/
- LangSmith RAG evaluation: https://docs.langchain.com/langsmith/evaluate-rag-tutorial
