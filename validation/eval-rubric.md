# Agent Example Eval Rubric

이 문서는 AI_Engineer의 starter kit과 case study 품질을 평가하는 기준이다.

## 5점 척도

| 점수 | 의미 |
|---|---|
| 5 | 실행 가능하고, 검증 로그와 제품 판단까지 있다. |
| 4 | 실행 가능하고, 최소 테스트 또는 수동 검증이 있다. |
| 3 | 실습은 가능하지만 자동 검증이나 실패 사례가 부족하다. |
| 2 | 설명은 좋지만 실행 경로가 약하다. |
| 1 | 링크 모음 또는 아이디어 수준이다. |

## 평가 항목

| 항목 | 질문 |
|---|---|
| Problem clarity | 어떤 사용자 문제가 반복적으로 발생하는가? |
| Input contract | 입력 데이터와 금지 데이터가 분리되어 있는가? |
| Execution | 한 줄 또는 짧은 절차로 실행할 수 있는가? |
| Output usefulness | 출력물이 실제 다음 업무에 쓰이는가? |
| Grounding | 답변/결과에 source, 근거, trace가 있는가? |
| Failure behavior | 모르는 것, 부족한 데이터, 오류를 어떻게 처리하는가? |
| Evaluation | golden set, unit test, checklist 중 하나 이상이 있는가? |
| Safety | secret, PII, private URL, proprietary data를 배제하는가? |
| Product judgment | build/buy/hold, 비용, 운영 리스크 판단이 있는가? |

## 최소 통과 기준

공개 starter kit은 아래를 모두 충족해야 한다.

- score 3 이상
- public-first checklist 통과
- 실행 또는 수동 검증 절차 존재
- 원본 출처가 있는 경우 `SOURCE_MAP.md`에 등록
