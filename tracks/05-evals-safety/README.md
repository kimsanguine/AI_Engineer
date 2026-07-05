# Track 05 — Evals Safety

Agent 예제를 공개하거나 실습에 쓰기 전에 필요한 검증과 안전 기준을 다룬다.

이 track은 "AI 답변이 좋은지 느낌으로 보는 단계"를 끝내기 위한 과정이다.
좋은 답변, 안전한 동작, 공개 가능한 데이터, 실패 처리 기준을 파일로 남긴다.

## 대상 사용자

- starter kit을 공개하기 전에 최소 검증 기준이 필요한 운영자
- 강의용 agent 예제가 private data를 포함하지 않는지 확인해야 하는 강사
- PM 관점에서 "이 agent가 좋아졌다"를 판단해야 하는 사람
- eval, validation log, release checklist를 처음 만드는 교육생

## 이 Track이 해결하는 문제

Agent는 성공 사례 하나만 보여주기 쉽다. 하지만 공개 repo와 수업에서는
실패 사례, 모름 처리, secret/PII 경계, 재현 가능한 검증이 더 중요하다.

| 위험 | 예시 | 필요한 검증 |
|---|---|---|
| 품질 착시 | 좋은 답변 1개만 보고 공개 | golden set, regression check |
| 정보 유출 | 실제 고객명/이메일/sample log 포함 | public safety checklist |
| 과장된 claim | "production-ready"라고 쓰지만 운영 로그 없음 | release checklist |
| 침묵 실패 | tool이 실패했는데 성공처럼 답함 | failure case |
| 평가 불가 | 변경 후 좋아졌는지 모름 | score rubric |

## 시작점

| 파일 | 역할 |
|---|---|
| `validation/eval-rubric.md` | agent example 품질 5점 척도 |
| `validation/public-safety-checklist.md` | 공개 전 데이터/보안 점검 |
| `validation/release-checklist.md` | starter kit/case study 공개 기준 |
| `starter-kits/faq-agent-lite/validation-log.md` | 검증 로그 예시 |

## 핵심 패턴

### 1. Eval은 모델 시험이 아니라 제품 계약 검증이다

Agent가 해야 하는 일, 하지 말아야 하는 일, 모르면 멈춰야 하는 일을
작은 테스트 케이스로 바꾼다.

### 2. 자동 검증과 수동 검증을 섞는다

unit test는 deterministic behavior를 잡고, 수동 검증은 화면, 문서, 출처,
사용자 경험을 본다. 둘 중 하나만으로는 부족하다.

### 3. 실패 사례를 먼저 쓴다

좋은 답변만 모으면 agent가 위험해진다. 모르는 질문, private data 요청,
도구 실패, 애매한 입력을 반드시 포함한다.

### 4. Public-first가 기본값이다

공개 repo에서는 실제 고객 데이터, 수강생 정보, private URL, API key를
사용하지 않는다. 예제는 합성 데이터로도 충분히 패턴을 가르칠 수 있어야 한다.

## 5단계 학습 경로

| Step | 주제 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Behavior contract | agent가 해야 할 일/하지 말 일 작성 | behavior table | forbidden behavior가 있음 |
| 2 | Golden set | 정상/실패 질문을 만든다 | eval cases | 실패 케이스 1개 이상 |
| 3 | Safety scan | public checklist를 적용한다 | safety note | secret/PII 없음 |
| 4 | Validation log | 실행 명령과 관찰 결과를 남긴다 | `validation-log.md` | 명령과 결과 분리 |
| 5 | Release gate | 공개 가능 여부를 판단한다 | release memo | 과장 표현 제거 |

## 실습 — Starter Kit Release Review

### 입력

- starter kit 하나
- README
- sample data
- test 또는 수동 검증 절차

### 절차

1. `validation/eval-rubric.md`로 1~5점을 매긴다.
2. `public-safety-checklist.md`를 항목별로 확인한다.
3. 정상 질문 3개, 실패 질문 2개를 만든다.
4. 실행 명령과 결과를 `validation-log.md`에 남긴다.
5. release checklist에서 남은 항목을 공개/보류로 분리한다.

### 산출물

```text
validation-log.md
release-review.md
eval-cases.json 또는 eval-cases.md
```

## Eval Case Template

| id | input | expected_behavior | forbidden_behavior | source |
|---|---|---|---|---|
| E001 | 알려진 FAQ 질문 | source 포함 답변 | source 없는 단정 | FAQ-001 |
| E002 | 모르는 질문 | 모른다고 답함 | 추측 답변 | NONE |
| E003 | 개인정보 요청 | 거절 또는 범위 안내 | 실제 개인정보 요구 | safety |

## Validation Log 기준

좋은 validation log는 실행 명령과 해석을 섞지 않는다.

```text
Command:
python3 -m unittest discover -s tests

Observed:
Ran 3 tests in 0.002s
OK

Interpretation:
baseline deterministic tests passed.

Remaining risk:
manual UI flow not tested.
```

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | agent 품질과 안전을 설명 가능한 기준으로 바꿔야 함 |
| 반복 빈도 | 모든 starter kit, 수업 예제, public release에서 발생 |
| 비용 리스크 | eval set 유지보수, model regression 확인 비용 |
| 품질 리스크 | eval이 쉬운 케이스만 커버하는 착시 |
| 안전 리스크 | secret/PII 노출, private workflow 공개 |
| build/buy/hold | 핵심 제품 agent는 build, 일반 benchmark는 buy/use, 데이터 경계 없으면 hold |

## 완료 기준

- eval case 5개 이상
- 실패/거절 케이스 1개 이상
- `validation-log.md`
- public safety checklist 통과 기록
- release checklist의 보류 항목 명시

## 연결 템플릿

| 템플릿 | 쓰는 시점 |
|---|---|
| [Behavior Contract](../../templates/behavior-contract.md) | 평가해야 할 required/forbidden behavior를 먼저 고정할 때 |
| [Eval Cases JSONL](../../templates/eval-cases.jsonl) | 최소 5개 baseline eval case를 만들 때 |
| [Eval Rubric](../../validation/eval-rubric.md) | agent example 품질을 5점 척도로 판단할 때 |
| [Public Safety Checklist](../../validation/public-safety-checklist.md) | 공개 데이터/secret/PII 경계를 점검할 때 |
| [Release Checklist](../../validation/release-checklist.md) | starter kit 공개 여부를 판단할 때 |

## 다음 확장

- RAG 품질 평가는 Track 04의 golden set과 연결한다.
- backend 운영 평가는 Track 03의 logs/state table과 연결한다.
- 제품화 판단은 Track 07의 build/buy/hold memo로 연결한다.
