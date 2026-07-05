# Track 04 — RAG Memory

RAG, graph retrieval, second brain, agent memory를 제품 관점으로 다룬다.

이 track의 핵심은 "벡터 DB를 붙이는 법"이 아니다. 어떤 질문에는 검색이
필요하고, 어떤 질문에는 단순 문서 링크가 충분하며, 어떤 경우에는 memory를
제품 기능으로 약속하면 안 되는지 판단하는 것이다.

## 대상 사용자

- 사내 문서, 강의 자료, FAQ, 개인 지식을 agent가 읽게 만들고 싶은 PM
- RAG demo를 만들었지만 답변 품질을 설명하기 어려운 1인 빌더
- GraphRAG, rerank, memory를 언제 써야 하는지 판단하려는 교육생
- public/private knowledge boundary를 설계해야 하는 운영자

## 이 Track이 해결하는 문제

RAG는 "모델이 모르는 정보를 넣어주는 장치"처럼 설명되지만, 실제 제품에서는
검색 품질, 권한, 최신성, citation, 모름 처리까지 포함한다.

| 흔한 착각 | 실제 질문 |
|---|---|
| 벡터 DB를 붙이면 hallucination이 줄어든다 | 검색 결과가 틀리면 더 그럴듯하게 틀릴 수 있다 |
| memory는 많을수록 좋다 | 오래된 memory와 private memory를 어떻게 구분하나? |
| GraphRAG가 항상 더 좋다 | 관계 구조가 실제 사용자 질문에 필요한가? |
| citation이 있으면 안전하다 | citation이 답변 문장을 실제로 뒷받침하는가? |

## 핵심 패턴

### 1. Retrieval before Generation

먼저 어떤 문서를 찾았는지 보여주고, 그 다음 답변을 만든다. 답변 품질을
논하려면 검색 결과 품질부터 봐야 한다.

### 2. Golden Set으로 검색 품질을 본다

RAG 품질은 느낌으로 평가하지 않는다. 대표 질문 10~20개와 기대 source를
작게 만든 뒤, 변경 전후를 비교한다.

### 3. Memory는 제품 약속이다

"기억합니다"라고 말하는 순간 사용자는 정확성과 지속성을 기대한다. 개인
메모리, 세션 메모리, 프로젝트 메모리, 공개 문서를 분리해야 한다.

### 4. 없는 정보는 없다고 말한다

검색 결과가 부족할 때 답을 지어내지 않는 것이 RAG 제품의 핵심 UX다.
abstention은 실패가 아니라 신뢰 장치다.

## 우선 Case Study

| Source | 이 track에서 볼 관점 | Reuse level |
|---|---|---|
| `llm-brain` | 개인 지식과 memory를 second brain으로 구조화하는 관점 | 내부 자산/L1 |
| `urstory-rag` | 한국어 RAG, rerank, guardrail, monitoring 요소 | L1/L2 |
| `graphrag-tools-retriever` | graph retrieval이 필요한 질문 유형 | L1/L2 |

라이선스 확인 전에는 원본 코드를 복사하지 않는다. 검색 품질 평가표와
제품 판단 프레임으로 재구성한다.

## 6단계 학습 경로

| Step | 주제 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Knowledge boundary | public/private/session/project 지식을 나눈다 | scope table | private data 제외 |
| 2 | Corpus design | 문서 단위와 metadata를 정한다 | corpus map | source 추적 가능 |
| 3 | Query set | 대표 질문 10개를 만든다 | golden set | 기대 source가 있음 |
| 4 | Retrieval check | top-k 결과를 수동 평가한다 | retrieval log | 관련 없는 문서 탐지 |
| 5 | Answer policy | citation, abstention, uncertainty 문구를 정한다 | answer policy | 없는 정보에 모름 |
| 6 | Product judgment | search, RAG, GraphRAG, memory 중 선택한다 | decision memo | 과한 기술 선택 방지 |

## 실습 — 작은 Golden Set 만들기

### 입력

- 공개 문서 또는 합성 FAQ 10~30개
- 사용자 질문 10개
- 각 질문의 기대 source id

### 산출물

```text
golden-set.csv
retrieval-log.md
answer-policy.md
```

### Golden Set 예시

| question_id | question | expected_source | must_not_claim |
|---|---|---|---|
| Q001 | 환불 가능 기간은? | FAQ-003 | 실제 약관 조항 번호 |
| Q002 | 상담원 연결은 언제 가능한가? | FAQ-006 | 24시간 운영 |
| Q003 | 없는 상품 가격을 물으면? | NONE | 가격 추정 |

## RAG 품질 체크리스트

- [ ] 답변 전에 source 후보를 확인했다.
- [ ] 질문별 기대 source가 있다.
- [ ] 검색 실패와 답변 실패를 분리했다.
- [ ] citation이 답변 문장을 실제로 지지한다.
- [ ] private 문서가 public demo에 섞이지 않는다.
- [ ] stale document 처리 기준이 있다.
- [ ] 없는 정보는 없다고 말한다.

## Search vs RAG vs GraphRAG vs Memory

| 선택 | 적합한 경우 | 피해야 할 경우 |
|---|---|---|
| Search | 사용자가 문서 위치를 찾으면 충분함 | 자연어 요약과 비교가 필요함 |
| RAG | 여러 문서를 근거로 답변해야 함 | corpus가 작고 정적이면 과함 |
| GraphRAG | 관계, 계층, 연결이 질문의 핵심임 | 단순 FAQ 검색 |
| Memory | 사용자/프로젝트별 지속 맥락이 가치임 | 최신성/삭제/권한을 보장할 수 없음 |

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | 필요한 지식이 흩어져 있어 찾고 답하는 시간이 반복됨 |
| 반복 빈도 | 교육, CS, 사내 지식, PM research에서 높음 |
| 비용 리스크 | embedding, vector DB, rerank, long context 비용 |
| 품질 리스크 | 잘못된 검색, stale source, citation mismatch |
| 안전 리스크 | private data leakage, 삭제 요청 미반영 |
| build/buy/hold | corpus와 권한이 단순하면 buy/use, domain-specific memory면 build, 데이터 경계 불명확하면 hold |

## 완료 기준

- corpus map 1개
- golden set 10문항 이상
- retrieval log 1개
- answer policy 1개
- public/private scope table 1개

## 다음 확장

- retrieval 결과를 자동 평가하려면 Track 05로 이동한다.
- backend service로 운영하려면 Track 03으로 이동한다.
- starter kit은 `faq-agent-lite`에서 시작해 `document-brief-agent`로 확장한다.
