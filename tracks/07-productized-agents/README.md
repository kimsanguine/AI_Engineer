# Track 07 — Productized Agents

Agent 데모를 실제 제품 또는 운영 루틴으로 바꾸는 판단을 다룬다.

이 track은 agent를 더 많이 만드는 과정이 아니다. 데모가 실제 사용자
문제를 반복적으로 해결하는지, 비용과 품질과 안전을 견딜 수 있는지,
build/buy/hold 중 무엇이 맞는지 판단하는 과정이다.

## 대상 사용자

- agent demo를 제품 기능, 내부 운영 루틴, 유료 서비스로 바꾸려는 PM
- model cost, latency, reliability를 제품 언어로 설명해야 하는 리더
- 금융/데이터/업무 자동화 agent의 위험 경계를 정해야 하는 1인 빌더
- `hplan`식 build gate와 agent prototype을 연결하고 싶은 사용자

## 이 Track이 해결하는 문제

Agent demo는 쉽게 인상적이다. 제품화는 어렵다. 사용자는 반복 문제 해결,
예측 가능한 품질, 비용, 책임 소재, 중단 기준을 요구한다.

| 데모 질문 | 제품 질문 |
|---|---|
| 한 번 잘 답했나? | 매일 100번 실행해도 품질이 유지되나? |
| 멋진 tool을 쓰나? | 사용자가 그 결과로 다음 행동을 할 수 있나? |
| 자동화가 되나? | 사람 승인선과 책임 경계가 명확한가? |
| 모델이 똑똑한가? | 비용, latency, 실패율이 허용 가능한가? |
| 시장성이 있나? | build/buy/hold 중 build할 이유가 충분한가? |

## 핵심 패턴

### 1. Agent는 기능이 아니라 운영 약속이다

사용자는 "agent"를 사지 않는다. 반복 문제 해결, 시간 절감, 품질 안정,
의사결정 지원을 산다.

### 2. Production claim을 늦게 한다

public demo, internal pilot, beta, production은 다르다. 각 단계마다
데이터, 권한, 로그, SLA, 사람 승인선이 달라진다.

### 3. Build Gate를 통과해야 한다

문제가 충분히 반복되는가, 기존 도구로 해결되지 않는가, agent가 명확히
나은가, 실패 비용을 감당할 수 있는가를 먼저 본다.

### 4. 중단 기준도 제품 요구사항이다

실패율, 비용, latency, 사용자 불신, safety incident가 기준을 넘으면
agent를 멈추거나 사람 검토 단계로 되돌려야 한다.

## 우선 Case Study

| Source | 이 track에서 볼 관점 | Reuse level |
|---|---|---|
| `vibe-investing` | finance/data agent의 검증과 위험 경계 | L1/L2 |
| `kronos` | 금융 예측 모델을 제품 claim으로 과장하지 않는 법 | L1 |
| finance/data agent 예제 | backtest, simulation, approval line | L1/L2 |
| `hplan` build gate | 만들기 전 build/no-build 판단 | 내부 자산 |

금융/투자 예제는 public demo로만 다룬다. 실제 투자 조언, 계좌, 주문,
고객 데이터, 수익률 보장은 포함하지 않는다.

## 6단계 학습 경로

| Step | 주제 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Problem framing | 반복 문제와 사용자 JTBD를 쓴다 | problem memo | 사용자/빈도/대안이 있음 |
| 2 | Agent value | agent가 기존 방식보다 나은 이유를 적는다 | value hypothesis | 시간/품질/비용 기준 |
| 3 | Risk model | 비용, latency, reliability, safety를 추정한다 | risk table | failure mode 포함 |
| 4 | Pilot design | public demo와 internal pilot을 분리한다 | pilot plan | 데이터 경계 명확 |
| 5 | Metrics | 운영 지표와 중단 기준을 정한다 | metrics table | stop condition 있음 |
| 6 | Build decision | build/buy/hold를 결정한다 | product judgment memo | 다음 행동이 명확 |

## 실습 — Agent Product Judgment Memo

### 입력

- agent idea 1개
- 대상 사용자 1명 또는 1개 역할
- 현재 대안 2개
- 실패 시나리오 3개

### 산출물

```text
product-judgment.md
├── user problem
├── current workaround
├── agent promise
├── pilot scope
├── metrics
├── risk table
├── build/buy/hold decision
└── next validation
```

### Product Judgment Template

| 항목 | 질문 |
|---|---|
| 사용자 | 누가 반복적으로 겪는 문제인가? |
| 상황 | 언제, 얼마나 자주 발생하는가? |
| 현재 대안 | 지금은 어떻게 해결하고 무엇이 불편한가? |
| Agent 약속 | agent가 대신하거나 보강하는 일은 무엇인가? |
| Output | 사용자가 실제로 쓰는 산출물은 무엇인가? |
| Human approval | 어디서 사람이 결정해야 하는가? |
| Metrics | 성공/실패를 어떻게 측정하는가? |
| Stop condition | 어떤 경우 중단하거나 축소하는가? |

## 운영 지표

| Metric | 의미 | 예시 기준 |
|---|---|---|
| Task success rate | 사용자가 기대 output을 얻은 비율 | 80% 이상 |
| Abstention quality | 모르는 경우 멈추는 품질 | 추측 답변 0건 |
| Human review rate | 사람 검토가 필요한 비율 | 초기에는 높아도 허용 |
| Cost per task | 업무 1건당 model/tool 비용 | 사람이 하던 비용보다 낮아야 함 |
| Latency | 사용자가 기다리는 시간 | 업무 맥락별 기준 필요 |
| Incident count | 데이터/권한/품질 사고 | 공개 전 0건 |

## Build / Buy / Hold 기준

| 결정 | 선택 기준 | 다음 행동 |
|---|---|---|
| Build | 업무가 핵심 차별화이고 기존 도구로 해결 안 됨 | starter kit, eval, pilot |
| Buy/Use | 범용 workflow이고 좋은 SaaS/connector가 있음 | integration, 운영 규칙 |
| Hold | 문제 빈도/데이터 경계/실패 비용이 불명확함 | discovery, manual process |

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | agent demo를 실제 반복 문제 해결로 바꿔야 함 |
| 반복 빈도 | 내부 운영, CS, research, finance/data workflow에서 중간~높음 |
| 비용 리스크 | model call, tool call, monitoring, human review |
| 품질 리스크 | false confidence, silent failure, stale data |
| 안전 리스크 | 투자/법률/의료/고객 데이터 등 high-stakes 영역 |
| build/buy/hold | product judgment memo로 결정 |

## 완료 기준

- problem memo 1개
- risk table 1개
- metrics table 1개
- stop condition 3개 이상
- build/buy/hold decision 1개

## 다음 확장

- build로 결정한 항목은 `starter-kits/`로 이동한다.
- validation이 부족하면 Track 05로 돌아간다.
- backend 운영이 필요하면 Track 03으로 이동한다.
- external tool 연결이 핵심이면 Track 02로 이동한다.
