# Public Safety Checklist

공개 repo, 강의 자료, starter kit에 포함하기 전 확인한다.

## 금지 데이터

- [ ] 실제 고객명, 회사명, 수강생명, 조 번호, 점수, 제출물 없음
- [ ] 사번, 계약번호, 전화번호, 이메일, 주소, 계좌, 결제 정보 없음
- [ ] 내부 URL, QR 코드, private repo link 없음
- [ ] `.env`, API key, access token, credential 없음
- [ ] 실제 약관, 계약, 고객 상담 원문, proprietary workflow 없음

## 허용 데이터

- [ ] fictional company name 사용
- [ ] synthetic sample data 사용
- [ ] public API 또는 공개 문서만 사용
- [ ] private context는 익명화 또는 제거

## 공개 전 확인

- [ ] README에 public-first boundary가 있다.
- [ ] sample data가 synthetic임을 명시했다.
- [ ] validation log에 secret 값을 출력하지 않았다.
- [ ] 외부 source의 license와 attribution을 확인했다.
