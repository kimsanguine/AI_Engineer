# CURATION_POLICY.md — AI_Engineer 큐레이션 원칙

## 목적

AI_Engineer는 좋은 AI/Agent 레퍼런스를 내 관점으로 재정의하는 Lab이다.
따라서 외부 자료를 "많이 모으는 것"보다 "왜 중요한지, 어떻게 실행하는지,
어디까지 검증했는지"가 더 중요하다.

## 선택 기준

레퍼런스는 아래 5개 질문 중 3개 이상에 답할 수 있을 때 채택한다.

1. 비개발자, PM, 1인 빌더가 배울 수 있는 명확한 패턴이 있는가?
2. 실제 파일, 코드, 데이터, 도구 연결 중 하나 이상을 다루는가?
3. 제품화할 때 비용, 안전, 운영 리스크를 토론할 수 있는가?
4. 한국어 교육 또는 기업 AX 맥락으로 번역할 가치가 있는가?
5. 실행, 테스트, eval, validation log로 바꿀 수 있는가?

## 재사용 수준

| Level | Meaning | Allowed use |
|---|---|---|
| L0 Link | 원본 링크와 요약만 제공 | 라이선스 불명확하거나 코드 복사 불필요 |
| L1 Concept | 아이디어를 내 언어로 설명 | 출처 표기 필수, 코드 복사 없음 |
| L2 Adapted Exercise | 원본 패턴을 새 실습으로 재작성 | 출처와 차이점 표기 |
| L3 Derived Code | 원본 코드 일부를 변형 | 라이선스 확인, NOTICE/주석 필요 |
| L4 Integrated Kit | 원본 구조를 starter kit에 통합 | license compatibility와 변경 기록 필수 |

기본값은 L1 또는 L2다. L3 이상은 반드시 라이선스를 먼저 확인한다.

## Case Study 표준

각 case study는 다음 섹션을 가진다.

1. 왜 골랐나
2. 원본이 잘하는 것
3. 생근님 관점의 재정의
4. 초보자가 배워야 할 핵심 패턴
5. 직접 해볼 실습
6. 제품화 관점의 판단
7. 검증 체크리스트
8. 원본 출처와 라이선스

## Starter Kit 표준

각 starter kit은 다음을 포함한다.

- `README.md`
- 샘플 데이터 또는 fixture
- 실행 명령
- 최소 테스트 또는 수동 검증 절차
- `validation-log.md`
- public-first safety note
- 다음 확장 과제

## Public-first 규칙

공개 repo에는 넣지 않는다.

- 실제 고객/회사/수강생/조 번호/점수/제출물
- 내부 URL, QR 코드, private repo link
- `.env`, API key, access token, credential
- 실제 계약, 약관, 고객 상담 원문, proprietary workflow

예제는 `ACME Life`, `Sample Bank`, `Fictional Retail Co.`처럼 가상의 이름과
합성 데이터를 사용한다.

## 변경 보고 원칙

외부 레퍼런스에서 배운 내용을 반영할 때는 다음을 함께 남긴다.

- 어떤 source를 봤는가
- 무엇을 그대로 쓰지 않고 바꿨는가
- 왜 이 레포의 독자에게 더 적합한가
- 어떤 검증을 했는가
