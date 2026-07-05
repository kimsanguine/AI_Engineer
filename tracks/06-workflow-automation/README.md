# Track 06 — Workflow Automation

반복 업무를 prompt, skill, command, automation으로 전환하는 방법을 다룬다.

이 track은 "좋은 프롬프트 모음"을 만드는 과정이 아니다. 사람이 반복해서
설명하던 업무를 입력, 처리, 출력, 승인선, 실패 처리, 기록으로 분해해
재사용 가능한 workflow로 바꾸는 과정이다.

## 대상 사용자

- 매주 반복되는 리서치, 문서, 마케팅, 강의 운영 업무를 줄이고 싶은 PM
- Claude Code/Codex skill 또는 slash command를 만들고 싶은 1인 빌더
- 팀의 반복 업무를 표준 운영 절차로 만들고 싶은 리더
- 자동화가 사람 승인선을 넘지 않게 설계해야 하는 운영자

## 이 Track이 해결하는 문제

프롬프트는 한 번의 요청을 해결한다. workflow automation은 반복 업무를
운영 가능한 루틴으로 바꾼다. 차이는 입력 계약과 실패 처리다.

| 단계 | 질문 | 예시 |
|---|---|---|
| Trigger | 언제 시작되는가? | 매주 월요일, 파일 업로드 후, 사용자가 요청할 때 |
| Input | 무엇을 받는가? | URL, CSV, 회의록, issue list |
| Process | 어떤 순서로 처리하는가? | 검색, 분류, 초안, 검증 |
| Output | 무엇을 남기는가? | markdown report, draft email, PR comment |
| Approval | 어디서 사람이 결정하는가? | send, publish, delete, deploy |
| Failure | 실패하면 어떻게 멈추는가? | fallback, retry, manual handoff |
| Retention | 무엇을 기록하고 버리는가? | validation log, source list, no PII |

## 핵심 패턴

### 1. Prompt에서 Skill로

같은 요청을 세 번 이상 반복하면 skill 후보가 된다. skill은 prompt보다
입력/출력/검증/금지 사항이 더 명확해야 한다.

### 2. Draft-only를 기본값으로

자동화는 초안 생성, 분류, 요약, 검증까지는 넓게 허용할 수 있다. send,
publish, delete, deploy, billing change는 명시 승인 후 실행한다.

### 3. 자동화 결과는 artifact로 남긴다

좋은 automation은 "답변"으로 끝나지 않는다. 파일, 체크리스트, report,
draft, validation log처럼 다음 사람이 볼 수 있는 산출물을 남긴다.

### 4. 실패를 숨기지 않는다

도구 연결 실패, source 부족, 권한 없음, 검증 미완료는 output에 남긴다.
"완료" 대신 "초안", "부분 검증", "보류" 상태를 분리한다.

## 우선 Case Study

| Source | 이 track에서 볼 관점 | Reuse level |
|---|---|---|
| `geo-seo-claude` | SEO/GEO 업무를 skill로 포장하는 방식 | L1/L2 |
| `ai-marketing-skills` | 마케팅 반복 업무의 입력/출력 구조 | L1/L2 |
| `ai-prompts-playbook` | prompt library를 workflow로 바꾸는 기준 | L1 |
| `oh-my-claudecode` | Claude Code skill/orchestration 운영 패턴 | L1/L2 |

라이선스 확인 전에는 원본 skill 파일을 복사하지 않는다. 업무 패턴과
검증 구조를 새 실습으로 재작성한다.

## 6단계 학습 경로

| Step | 주제 | 활동 | 산출물 | 검증 |
|---|---|---|---|---|
| 1 | Repetition audit | 반복 업무 5개를 적고 빈도/시간을 추정한다 | automation backlog | 3회 이상 반복 업무 식별 |
| 2 | Workflow contract | trigger/input/output/approval을 정의한다 | workflow spec | 승인선이 분리됨 |
| 3 | Prompt to procedure | 프롬프트를 단계별 절차로 바꾼다 | SOP 초안 | 누락 단계가 줄어듦 |
| 4 | Artifact design | 결과물을 파일/초안/report로 정한다 | output template | 재사용 가능 |
| 5 | Validation | source, lint, review, browser check 등을 정한다 | validation checklist | 완료/미검증 분리 |
| 6 | Skill packaging | 재사용 가능한 skill/command로 묶는다 | skill spec | 다른 세션에서 재실행 가능 |

## 실습 — 반복 업무 하나를 Skill Spec으로 바꾸기

### 입력

- 최근 2주 동안 반복한 업무 1개
- 실제 데이터 대신 합성 또는 공개 샘플
- 기대 산출물 예시 1개

### Skill Spec Template

```text
Name:
Purpose:
Trigger:
Inputs:
Forbidden inputs:
Steps:
Outputs:
Approval line:
Failure handling:
Validation:
Retention:
```

### 예시

```text
Name: weekly-learning-digest
Purpose: 공개 학습 자료와 수업 공지에서 주간 요약 초안 생성
Trigger: 매주 금요일 또는 강사 요청
Inputs: public links, synthetic schedule
Forbidden inputs: 실제 수강생 점수, private Padlet URL, 이메일
Outputs: markdown digest draft
Approval line: 발송은 사람이 직접 수행
Validation: source link count, private data scan
```

## 자동화 승인선

| 작업 | 기본 상태 | 이유 |
|---|---|---|
| 요약 | 자동 가능 | 되돌리기 쉬움 |
| 분류/라벨 추천 | 자동 가능 | 사람이 검토 가능 |
| draft 작성 | 자동 가능 | 전송 전 승인 가능 |
| 파일 생성 | 대체로 가능 | git diff로 검토 가능 |
| email/slack send | 승인 필요 | 외부 커뮤니케이션 |
| production deploy | 승인 필요 | 운영 영향 |
| delete/archive | 승인 필요 | 데이터 손실 가능 |
| billing/schema/credential 변경 | 승인 필요 | 되돌리기 어려움 |

## 제품화 관점의 판단

| 항목 | 판단 |
|---|---|
| 사용자 문제 | 반복 업무가 사람의 기억과 수동 복붙에 의존함 |
| 반복 빈도 | 주간/일간 운영, 콘텐츠, 마케팅, 리서치에서 높음 |
| 비용 리스크 | tool call, source search, review time |
| 품질 리스크 | source 누락, 오래된 정보, 잘못된 tone |
| 안전 리스크 | private data 포함, 승인 없이 외부 발송 |
| build/buy/hold | 개인/팀 특화 workflow는 build, 범용 SaaS는 buy/use, 승인선 불명확하면 hold |

## 완료 기준

- automation backlog 5개
- skill spec 1개
- output template 1개
- validation checklist 1개
- 승인선과 failure handling이 포함된 운영 메모

## 다음 확장

- tool 연결이 필요하면 Track 02로 이동한다.
- 공개 전 안전 검토는 Track 05로 이동한다.
- 제품 운영 루틴으로 바꾸려면 Track 07로 이동한다.
