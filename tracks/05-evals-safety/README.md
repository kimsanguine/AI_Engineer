# Track 05 — Evals Safety

Agent 예제를 공개하거나 실습에 쓰기 전에 필요한 검증과 안전 기준을 다룬다.

## 핵심 질문

- 좋은 답변을 어떻게 테스트 가능한 기준으로 바꾸는가?
- public repo에 절대 들어가면 안 되는 데이터는 무엇인가?
- 수동 검증과 자동 eval을 어떻게 함께 쓰는가?

## 시작점

- `validation/eval-rubric.md`
- `validation/public-safety-checklist.md`
- `validation/release-checklist.md`

## 완료 기준

- starter kit마다 validation log가 있다.
- secret, PII, private URL 점검이 포함된다.
- 실패 사례가 최소 1개 이상 기록된다.
