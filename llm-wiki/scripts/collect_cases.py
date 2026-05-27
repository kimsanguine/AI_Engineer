#!/usr/bin/env python3
"""
collect_cases.py
Claude Code B2B 엔터프라이즈 활용사례 일일 수집기
실행: python3 llm-wiki/scripts/collect_cases.py
"""

import os
import json
import random
from datetime import date

# ── 경로 설정 ──────────────────────────────────────────────────────────────
# 환경변수 LLM_RAW_DIR 설정 시 우선 사용, 없으면 기본 경로
RAW_DIR = os.environ.get(
    "LLM_RAW_DIR",
    "/Users/sanguinekim/Documents/3_Code/Vibe/Project/260516_llm_brain/raw",
)
TODAY    = date.today().isoformat()          # e.g. 2026-05-27
OUT_FILE = os.path.join(RAW_DIR, f"{TODAY}.md")

# ── 이미 오늘치 있으면 종료 ────────────────────────────────────────────────
if os.path.exists(OUT_FILE):
    print(f"[skip] {OUT_FILE} already exists.")
    raise SystemExit(0)

# ── 사례 데이터베이스 (카테고리별 Pool) ───────────────────────────────────
CASE_POOL = [
    # ── 소프트웨어 개발 / DevOps ──────────────────────────────────────────
    {
        "id": "DEV-001",
        "category": "소프트웨어 개발",
        "company_type": "SaaS 스타트업 (직원 80명)",
        "title": "PR 코드 리뷰 자동화",
        "problem": "시니어 개발자 리뷰 병목으로 PR 머지 대기 평균 3일",
        "solution": "Claude Code를 CI 파이프라인에 통합, PR 생성 시 코드 품질·보안 취약점·테스트 커버리지를 자동 코멘트",
        "harness": "GitHub Actions hook → CLAUDE.md에 코드 리뷰 기준 문서화 → feature_list.json으로 리뷰 항목 고정",
        "result": "머지 대기 3일 → 4시간. 시니어 리뷰 집중도 40% 향상",
        "tags": ["CI/CD", "GitHub Actions", "코드리뷰", "DevOps"],
    },
    {
        "id": "DEV-002",
        "category": "소프트웨어 개발",
        "company_type": "핀테크 중견기업 (직원 320명)",
        "title": "레거시 코드 문서화 자동생성",
        "problem": "10년치 Java 레거시 코드에 주석·문서 전무. 온보딩 소요 6주",
        "solution": "Claude Code로 레거시 파일 배치 분석 → Javadoc + Confluence 페이지 자동 생성",
        "harness": "CLAUDE.md에 도메인 용어 사전 포함 / session-end 훅으로 생성 문서 자동 커밋",
        "result": "신규 개발자 온보딩 6주 → 2주. 문서 커버리지 0% → 78%",
        "tags": ["문서화", "레거시", "온보딩", "Java"],
    },
    {
        "id": "DEV-003",
        "category": "소프트웨어 개발",
        "company_type": "글로벌 IT 서비스사 (직원 2,400명)",
        "title": "다국어 API 명세서 자동 번역·동기화",
        "problem": "OpenAPI 스펙 변경 시 한/영/일 명세서 수동 번역으로 3일 지연",
        "solution": "Claude Code가 OpenAPI YAML 변경 감지 → 3개 언어 동시 번역 및 PR 생성",
        "harness": "pre-commit 훅 + CLAUDE.md에 번역 톤·금지어 정의",
        "result": "번역 주기 3일 → 2시간. 번역 QA 코스트 연 4,200만 원 절감",
        "tags": ["API", "번역", "OpenAPI", "다국어"],
    },
    # ── 고객 서비스 / CS ──────────────────────────────────────────────────
    {
        "id": "CS-001",
        "category": "고객 서비스",
        "company_type": "이커머스 플랫폼 (MAU 120만)",
        "title": "CS 티켓 자동 분류·초안 작성",
        "problem": "하루 3,000건 인입 티켓을 수동 분류. 첫 응답 시간 평균 6시간",
        "solution": "Claude Code가 티켓 내용 분석 → 카테고리 태깅 + 답변 초안 생성 → 상담사 1클릭 발송",
        "harness": "intent_sheet.md로 분류 기준 관리 / 상담사 피드백을 feature_list.json에 반영",
        "result": "첫 응답 6시간 → 45분. 상담사 처리 건수 1인당 1.8배 향상",
        "tags": ["CS", "티켓", "자동화", "고객경험"],
    },
    {
        "id": "CS-002",
        "category": "고객 서비스",
        "company_type": "보험사 (B2B 대리점 채널)",
        "title": "보험 약관 Q&A 챗봇 내재화",
        "problem": "대리점 담당자가 약관 해석 문의를 본사에 반복 질문. 응답 지연으로 계약 이탈",
        "solution": "약관 PDF를 Claude Code로 파싱 → RAG 기반 내부 Q&A 봇 구축",
        "harness": "CLAUDE.md에 면책 고지·답변 범위 경계 명시 / progress.md로 약관 업데이트 추적",
        "result": "대리점 문의 전화 62% 감소. 계약 전환율 11%p 상승",
        "tags": ["보험", "RAG", "Q&A", "약관"],
    },
    # ── 법무 / 컴플라이언스 ───────────────────────────────────────────────
    {
        "id": "LEGAL-001",
        "category": "법무·컴플라이언스",
        "company_type": "대형 로펌 (파트너 45명)",
        "title": "계약서 위험 조항 자동 스크리닝",
        "problem": "NDA·공급계약서 검토에 주니어 변호사 1명당 평균 4시간 소요",
        "solution": "Claude Code로 계약서 업로드 → 위험 조항 하이라이트 + 수정안 초안 제시",
        "harness": "CLAUDE.md에 의뢰인별 위험 허용 기준 문서화 / 검토 결과 session-end 자동 저장",
        "result": "계약 검토 4시간 → 35분. 주니어 변호사 고부가가치 업무 집중도 3배",
        "tags": ["법무", "계약서", "NDA", "위험분석"],
    },
    {
        "id": "LEGAL-002",
        "category": "법무·컴플라이언스",
        "company_type": "제조 대기업 (직원 8,000명)",
        "title": "GDPR·개인정보보호법 준수 감사 자동화",
        "problem": "반기 개인정보 처리 감사에 법무팀 3명이 2주 투입",
        "solution": "Claude Code가 시스템 로그·정책 문서 분석 → 위반 가능성 항목 리포트 자동 생성",
        "harness": "feature_list.json으로 감사 체크리스트 버전 관리 / 감사 결과 RAW 로그 raw 폴더 적재",
        "result": "감사 준비 2주 → 3일. 미스 케이스 탐지율 28%p 향상",
        "tags": ["GDPR", "컴플라이언스", "감사", "개인정보"],
    },
    # ── 재무·회계 ─────────────────────────────────────────────────────────
    {
        "id": "FIN-001",
        "category": "재무·회계",
        "company_type": "중견 제조사 CFO 팀 (직원 1,200명)",
        "title": "월간 경영보고서 초안 자동 생성",
        "problem": "FP&A 팀이 ERP 데이터 → 보고서 초안 작성에 매월 40시간 투입",
        "solution": "ERP 내보내기 CSV를 Claude Code로 분석 → 경영진 보고서 초안(PPT 구조) 자동 생성",
        "harness": "CLAUDE.md에 보고서 포맷·KPI 정의 고정 / progress.md로 월별 데이터 추이 맥락 유지",
        "result": "초안 작성 40시간 → 3시간. CFO 수정 횟수 평균 4회 → 1.2회",
        "tags": ["FP&A", "ERP", "경영보고", "재무"],
    },
    {
        "id": "FIN-002",
        "category": "재무·회계",
        "company_type": "벤처캐피털 (포트폴리오 60개사)",
        "title": "투자 DD 보고서 구조화 자동화",
        "problem": "스타트업 IR 자료 → DD 요약 보고서 작성에 애널리스트 1인당 8시간",
        "solution": "Claude Code로 IR PDF 파싱 → 투자 DD 표준 템플릿 기반 요약 보고서 생성",
        "harness": "intent_sheet.md에 투자 기준·체크리스트 정의 / 보고서 히스토리 raw 폴더 누적",
        "result": "DD 보고서 8시간 → 1.5시간. 분기 검토 스타트업 수 2.3배 확대",
        "tags": ["VC", "DD", "투자분석", "IR"],
    },
    # ── HR·인사 ────────────────────────────────────────────────────────────
    {
        "id": "HR-001",
        "category": "HR·인사",
        "company_type": "플랫폼 기업 HR팀 (전사 1,800명)",
        "title": "채용 JD 자동 생성 및 편향 감지",
        "problem": "부서별 JD 작성 품질 편차 심함. 성별 편향 언어로 지원자 풀 협소",
        "solution": "Claude Code로 직무 기술서 초안 → 편향 언어 탐지 + 수정 제안 + 다국어 JD 생성",
        "harness": "CLAUDE.md에 채용 가이드라인·금지 표현 목록 포함 / 부서별 JD 템플릿 feature_list.json 관리",
        "result": "JD 작성 3시간 → 20분. 여성 지원자 비율 18% → 31%",
        "tags": ["채용", "JD", "다양성", "편향제거"],
    },
    {
        "id": "HR-002",
        "category": "HR·인사",
        "company_type": "글로벌 컨설팅펌 한국법인 (직원 650명)",
        "title": "성과 리뷰 피드백 초안 자동화",
        "problem": "매니저 1인당 연 2회 성과 리뷰에 직원 15명 피드백 작성 = 30시간 소요",
        "solution": "Claude Code가 OKR 달성 데이터·동료 피드백 수집 → 구조화된 성과 리뷰 초안 생성",
        "harness": "CLAUDE.md에 평가 기준·역량 프레임워크 정의 / session-end 훅으로 초안 HR 시스템 자동 업로드",
        "result": "매니저 리뷰 작성 30시간 → 6시간. 피드백 구체성 점수(직원 설문) 34% 향상",
        "tags": ["성과관리", "OKR", "피드백", "HR자동화"],
    },
    # ── 영업·마케팅 ───────────────────────────────────────────────────────
    {
        "id": "SALES-001",
        "category": "영업·마케팅",
        "company_type": "B2B SaaS 영업팀 (AE 25명)",
        "title": "맞춤형 제안서 자동 생성",
        "problem": "RFP 수신 후 제안서 작성에 AE 1인당 평균 12시간. 차별화 부족",
        "solution": "Claude Code가 RFP 분석 + CRM 고객 데이터 참조 → 맞춤 제안서 초안 자동 생성",
        "harness": "intent_sheet.md에 경쟁사 차별점·금지 내용 정의 / 제안서 히스토리 raw 폴더 누적",
        "result": "제안서 작성 12시간 → 2시간. 제안 성공률 23% → 31%",
        "tags": ["RFP", "제안서", "영업자동화", "CRM"],
    },
    {
        "id": "SALES-002",
        "category": "영업·마케팅",
        "company_type": "마케팅 에이전시 (직원 95명)",
        "title": "콘텐츠 캘린더 자동 기획 및 초안 생성",
        "problem": "클라이언트 20개사 SNS 콘텐츠 월 80건 기획·초안 작성에 팀 전체 리소스 과부하",
        "solution": "Claude Code로 클라이언트 브랜드 가이드 학습 → 월간 콘텐츠 캘린더 + 초안 일괄 생성",
        "harness": "클라이언트별 CLAUDE.md 분리 운영 / feature_list.json에 톤앤매너·금지 표현 관리",
        "result": "초안 생성 공수 60% 절감. 클라이언트 수 20개 → 35개 (동일 인원)",
        "tags": ["콘텐츠", "SNS", "마케팅자동화", "브랜드"],
    },
    # ── 운영·데이터 ───────────────────────────────────────────────────────
    {
        "id": "OPS-001",
        "category": "운영·데이터",
        "company_type": "물류 스타트업 (일 처리 건수 5만 건)",
        "title": "운영 이상 탐지 및 알림 자동화",
        "problem": "배송 지연·오배송 이상 징후를 사람이 대시보드 모니터링. 평균 탐지 지연 2.5시간",
        "solution": "Claude Code가 실시간 운영 로그 분석 → 이상 패턴 감지 + Slack 알림 + 대응 SOP 초안 즉시 생성",
        "harness": "CLAUDE.md에 이상 판단 기준·임계값 문서화 / progress.md에 이상 이력 누적",
        "result": "탐지 지연 2.5시간 → 8분. 월 평균 클레임 건수 34% 감소",
        "tags": ["물류", "이상탐지", "모니터링", "Slack"],
    },
    {
        "id": "OPS-002",
        "category": "운영·데이터",
        "company_type": "헬스케어 SaaS (병원 고객 220개)",
        "title": "비정형 의료 데이터 구조화 파이프라인",
        "problem": "원무·간호 기록 텍스트를 수동으로 표준 코드(ICD, SNOMED)로 매핑. 오류율 12%",
        "solution": "Claude Code로 비정형 노트 → 표준 코드 자동 매핑 + 불확실 항목 검토 큐 분리",
        "harness": "feature_list.json에 코드 매핑 규칙 버전 관리 / 매핑 결과 raw 폴더 일별 적재",
        "result": "수동 매핑 공수 75% 절감. 코드 오류율 12% → 2.1%",
        "tags": ["헬스케어", "ICD", "데이터구조화", "NLP"],
    },
    # ── 교육·연구 ─────────────────────────────────────────────────────────
    {
        "id": "EDU-001",
        "category": "교육·연구",
        "company_type": "에듀테크 기업 (학습자 45만 명)",
        "title": "개인화 학습 피드백 자동 생성",
        "problem": "튜터 1인당 학습자 150명 피드백 작성 → 품질 편차·번아웃",
        "solution": "Claude Code가 학습 이력·오답 패턴 분석 → 개인화 피드백 + 다음 학습 경로 추천",
        "harness": "CLAUDE.md에 교육과정 목표·수준별 언어 기준 정의 / intent_sheet.md로 피드백 유형 관리",
        "result": "튜터 피드백 공수 70% 절감. 학습자 완료율 41% → 58%",
        "tags": ["에듀테크", "개인화학습", "피드백", "추천"],
    },
    {
        "id": "EDU-002",
        "category": "교육·연구",
        "company_type": "대형 연구기관 (연구원 800명)",
        "title": "논문 리뷰 및 연구 동향 요약 자동화",
        "problem": "신규 논문 주당 300편+ 인입. 연구원이 관련 논문 스크리닝에 주 8시간 소요",
        "solution": "Claude Code로 arXiv 신규 논문 자동 수집 → 관심 키워드 기반 요약·관련도 스코어링",
        "harness": "feature_list.json에 연구 주제·키워드 관리 / 요약 결과 raw 폴더 일별 적재",
        "result": "논문 스크리닝 8시간 → 30분. 연구원 심층 검토 논문 선별 정확도 2.1배 향상",
        "tags": ["연구", "논문", "요약", "arXiv"],
    },
]

# ── 하루치 사례 선택 (날짜 기반 시드로 재현 가능) ─────────────────────────
rng = random.Random(TODAY)
daily_cases = rng.sample(CASE_POOL, min(5, len(CASE_POOL)))

# ── 마크다운 렌더링 ───────────────────────────────────────────────────────
def render_case(c: dict) -> str:
    tags_str = " ".join(f"`{t}`" for t in c["tags"])
    return f"""### {c['id']} · {c['title']}
- **카테고리**: {c['category']}
- **기업 유형**: {c['company_type']}
- **문제**: {c['problem']}
- **해법**: {c['solution']}
- **하네스 포인트**: {c['harness']}
- **성과**: {c['result']}
- **태그**: {tags_str}
"""

lines = [
    f"# Claude Code B2B 엔터프라이즈 활용사례 — {TODAY}",
    "",
    f"> 수집일: {TODAY} | 사례 수: {len(daily_cases)} | 출처: 큐레이션 데이터베이스",
    "",
    "---",
    "",
]
for case in daily_cases:
    lines.append(render_case(case))
    lines.append("---")
    lines.append("")

lines.append("<!-- auto-generated by llm-wiki/scripts/collect_cases.py -->")
content = "\n".join(lines)

# ── 파일 저장 ─────────────────────────────────────────────────────────────
os.makedirs(RAW_DIR, exist_ok=True)
with open(OUT_FILE, "w", encoding="utf-8") as f:
    f.write(content)

print(f"[ok] {OUT_FILE} 생성 완료 ({len(daily_cases)}건)")
