# agents/ — 100 Agents 확장 공간

이 폴더는 장기적으로 100개 업무형 Agent 패턴을 모으는 공간이다. 단, 앞으로는
검증되지 않은 아이디어를 바로 `agents/`에 넣지 않는다.

## 승격 기준

Agent 항목은 아래 중 하나를 통과한 뒤 이 폴더로 들어온다.

1. `starter-kits/`에서 실행과 검증이 끝났다.
2. `case-studies/`에서 원본 레퍼런스 재정의와 실습이 끝났다.
3. 수업/워크숍에서 public-first 데이터로 재현되었다.

## 표준 구조

```text
agents/{category}/{number}-{slug}/
├── README.md
├── agent.py 또는 implementation.md
├── sample_data/
├── tests/ 또는 evals/
├── validation-log.md
└── product-judgment.md
```

## 상태 체계

| Status | Meaning |
|---|---|
| idea | 문제와 가설만 있음 |
| case-study | 외부 레퍼런스 재정의 완료 |
| starter | 실행 가능한 최소 예제 있음 |
| validated | 테스트, eval, 또는 수동 검증 로그 있음 |
| product-candidate | 비용, 운영, 안전 판단까지 완료 |

## 현재 우선순위

1. `faq-agent-lite`를 validated 상태로 승격 후보화
2. `document-brief-agent` starter kit 작성
3. `mcp-tool-agent` starter kit 작성
