# AI Engineer — 100 Agents

![License](https://img.shields.io/badge/license-MIT-green)
![Last Commit](https://img.shields.io/github/last-commit/kimsanguine/AI_Engineer)
![Agents](https://img.shields.io/badge/agents-100-blue)

> **"Agent를 설명하지 말고, 실행해서 보여줘라."**

100개의 AI Agent를 직접 만들고 실행합니다.
링크 모음이 아닙니다. 각 Agent는 **문제 정의 → 설계 → 코드 → 실행 결과**를 포함합니다.

20년 프로덕트 매니저가 "이 Agent가 어떤 문제를 해결하는지, 실제 제품에서 어떻게 쓸 수 있는지" PM 관점을 함께 담았습니다.

---

## 학습 경로

이 레포는 아래 시리즈의 두 번째 단계입니다.

```
[AI_Human]          →      [AI_Engineer]        →      [AI_PM]
 초급 · 100일 과정          중급 · 100 Agents           실전 · 워크플로우 재설계
 Python~RAG 기초            직접 만들고 실행              PM의 일하는 방식을 바꾸다
```

---

## 카테고리

| # | 카테고리 | 설명 | Agent 수 |
|---|---------|------|---------|
| 01 | 업무 자동화 | 이메일, 슬랙, 일정, 문서 자동화 | 15 |
| 02 | 데이터 & 리서치 | 웹 크롤링, 시장조사, 경쟁사 분석 자동화 | 15 |
| 03 | 콘텐츠 생성 | 블로그, SNS, 뉴스레터, 영상 스크립트 | 12 |
| 04 | 코드 & 개발 | 코드 리뷰, 테스트, 문서화, 디버깅 | 12 |
| 05 | 고객 서비스 | FAQ 봇, 티켓 분류, 감성 분석 | 10 |
| 06 | 세일즈 & 마케팅 | 리드 생성, CRM 연동, 캠페인 자동화 | 10 |
| 07 | 교육 & 코칭 | 맞춤 학습, 퀴즈 생성, 피드백 Agent | 8 |
| 08 | 멀티 에이전트 | 에이전트 협업, 오케스트레이션, 의사결정 | 10 |
| 09 | MCP & 도구 연동 | 외부 API, DB, 파일시스템 연결 | 8 |
| | | **합계** | **100** |

---

## 프로젝트 구조

```
AI_Engineer/
├── README.md
├── agents/
│   ├── 01-automation/
│   │   ├── 001-email-summarizer/
│   │   │   ├── README.md          # 문제 정의 + PM 인사이트
│   │   │   ├── agent.py           # 실행 코드
│   │   │   ├── config.yaml        # 설정
│   │   │   └── result.md          # 실행 결과 + 스크린샷
│   │   ├── 002-slack-standup-bot/
│   │   └── ...
│   ├── 02-data-research/
│   ├── 03-content/
│   ├── 04-code-dev/
│   ├── 05-customer-service/
│   ├── 06-sales-marketing/
│   ├── 07-education/
│   ├── 08-multi-agent/
│   └── 09-mcp-tools/
├── templates/
│   └── agent-template.md          # Agent 작성 템플릿
└── docs/
    ├── getting-started.md
    └── tech-stack.md
```

---

## 각 Agent 문서 구성

모든 Agent는 동일한 포맷을 따릅니다:

```markdown
# Agent 001: Email Summarizer

## 문제 정의
> 하루 50통의 이메일을 읽는 PM은 30분을 소비한다.

## PM 인사이트
이 Agent가 제품에서 쓰일 수 있는 시나리오:
- B2B SaaS의 inbox zero 기능
- 사내 커뮤니케이션 도구의 AI 요약

## 설계
- Input: Gmail API → 최근 24시간 이메일
- Process: LLM 요약 + 우선순위 분류
- Output: Slack 채널에 브리핑 전송

## 기술 스택
Claude API, Gmail MCP, Python

## 실행 결과
[스크린샷 / 실행 로그]

## 배운 점
- 긴 스레드의 요약 정확도는 chunk 전략에 따라 달라진다
- 우선순위 분류에는 few-shot이 rule-based보다 유효
```

---

## 기술 스택

| 영역 | 도구 |
|------|------|
| LLM | Claude API, OpenAI API, Gemini |
| Agent Framework | Claude Code, LangChain, CrewAI |
| MCP | Slack, Gmail, Notion, GitHub, Linear |
| 자동화 | n8n, Python scripts, Cron |
| 데이터 | SQLite, Supabase, Vector DB |
| 배포 | Docker, GitHub Actions |

---

## 시작하기

```bash
# 1. 레포 클론
git clone https://github.com/kimsanguine/AI_Engineer.git

# 2. 환경 설정
cp .env.example .env  # API 키 설정

# 3. 첫 번째 Agent 실행
cd agents/01-automation/001-email-summarizer
python agent.py
```

---

## 진행 현황

> 🟢 완료 | 🟡 진행 중 | ⚪ 예정

| 카테고리 | 진행률 | 상태 |
|---------|--------|------|
| 01 업무 자동화 | 0/15 | ⚪ |
| 02 데이터 & 리서치 | 0/15 | ⚪ |
| 03 콘텐츠 생성 | 0/12 | ⚪ |
| 04 코드 & 개발 | 0/12 | ⚪ |
| 05 고객 서비스 | 0/10 | ⚪ |
| 06 세일즈 & 마케팅 | 0/10 | ⚪ |
| 07 교육 & 코칭 | 0/8 | ⚪ |
| 08 멀티 에이전트 | 0/10 | ⚪ |
| 09 MCP & 도구 연동 | 0/8 | ⚪ |

---

## 기여하기

Agent 아이디어나 개선 사항을 Issue로 남겨주세요.
PR도 환영합니다 — `templates/agent-template.md`를 참고하여 새 Agent를 추가할 수 있습니다.

---

## 저작권

MIT License

---

**김생근** · [GitHub](https://github.com/kimsanguine) · [LinkedIn](https://linkedin.com/in/sanguinekim)

AI B2B/B2C SaaS CPO, 20년 프로덕트 매니저.
Agentic AI로 PM의 일하는 방식을 재설계하고 있습니다.
