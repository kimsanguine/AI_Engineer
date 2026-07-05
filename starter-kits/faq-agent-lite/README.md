# FAQ Agent Lite

합성 FAQ 데이터에서 근거가 있는 답변을 찾아주는 가장 작은 retrieval-style
agent 예제다. API key 없이 Python 표준 라이브러리만으로 실행된다.

## 대상 사용자

- 비개발자 PM
- 보험/서비스 운영자
- Agent 수업 입문자
- eval과 handoff를 처음 배우는 교육생

## Public-first safety

이 예제는 fictional company `ACME Life`와 합성 FAQ만 사용한다. 실제 고객
정보, 계약번호, 약관 원문, 상담 로그, API key를 사용하지 않는다.

## 빠른 시작

```bash
cd starter-kits/faq-agent-lite
python3 agent.py "Can I change my billing date?"
python3 -m unittest discover -s tests
```

## 파일 구조

```text
faq-agent-lite/
├── README.md
├── agent.py
├── sample_data/
│   └── faqs.json
├── tests/
│   └── test_agent.py
└── validation-log.md
```

## 작동 방식

1. 질문을 소문자 토큰으로 나눈다.
2. FAQ의 question, answer, tags를 같은 방식으로 토큰화한다.
3. 겹치는 토큰 수와 tag 일치 수를 점수화한다.
4. 기준 점수 미만이면 모른다고 답한다.
5. 답변에는 항상 source id와 category를 붙인다.

이 방식은 production 검색 품질을 위한 것이 아니다. 입문자가 retrieval,
grounding, fallback, eval의 기본 구조를 한 화면에서 이해하기 위한 예제다.

## 예시

```text
Q: Can I change my billing date?
A: Yes. In this fictional ACME Life sample, customers can request one billing-date change per month before the next invoice is issued.
Source: FAQ-001 | Category: billing | Confidence: 0.71
```

## 검증

```bash
python3 -m unittest discover -s tests
```

수동 검증:

- [ ] 답변에 source가 붙는다.
- [ ] 모르는 질문에는 모른다고 답한다.
- [ ] 실제 고객 데이터가 필요하지 않다.
- [ ] 답변이 `sample_data/faqs.json` 밖의 사실을 주장하지 않는다.

## 제품 판단

| 항목 | 판단 |
|---|---|
| 실제 사용자 문제 | 반복 FAQ 대응, 운영자 온보딩, 내부 정책 검색 |
| 반복 빈도 | 높음. 고객센터/운영/교육에서 매일 발생 |
| 자동화 가능 범위 | public/synthetic FAQ에서는 안전. 실제 업무 적용 전 권한/로그/정책 최신성 필요 |
| 사람 승인선 | 고객-facing 답변 전 상담원 또는 운영자 확인 필요 |
| production 전 필요한 것 | vector search, access control, freshness check, hallucination eval, audit log |

## 다음 확장

- CSV/Markdown FAQ loader 추가
- golden set을 20문항으로 확대
- answer abstention 기준을 별도 config로 분리
- UI 또는 MCP tool wrapper 추가
