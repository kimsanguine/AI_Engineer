# Release Checklist

starter kit 또는 case study를 공개 상태로 승격하기 전 확인한다.

## 문서

- [ ] README가 목적, 대상 사용자, 빠른 시작, 검증을 포함한다.
- [ ] 원본 source가 있으면 `SOURCE_MAP.md`에 등록되어 있다.
- [ ] public-first safety note가 있다.
- [ ] 제품 판단 또는 운영 리스크 섹션이 있다.

## 실행

- [ ] API key 없이 실행 가능한 기본 경로가 있다. 또는 API 필요성을 명확히 분리했다.
- [ ] 샘플 데이터가 포함되어 있다.
- [ ] 테스트, eval, 또는 수동 검증 절차가 있다.
- [ ] 실패 시나리오가 최소 1개 있다.

## 보안

- [ ] `.env`가 커밋되지 않았다.
- [ ] secret-like string scan을 수행했다.
- [ ] private URL 또는 실제 고객 정보가 없다.

## 증거

- [ ] `validation-log.md` 또는 동등한 검증 기록이 있다.
- [ ] 실행 명령과 결과가 분리되어 있다.
- [ ] "production-ready" 같은 과장 표현을 쓰지 않았다.
