# Track 03 — Agent Backend

Agent를 데모에서 서비스 구조로 옮길 때 필요한 backend 패턴을 다룬다.

## 핵심 질문

- FastAPI, LangGraph, queue, database, observability는 각각 왜 필요한가?
- 프로토타입과 production-ready template의 차이는 무엇인가?
- 비개발자에게 backend risk를 어떤 언어로 설명할 것인가?

## 우선 case study

- `fastapi-langgraph-agent-production-ready-template`
- API server + worker + eval harness 구조

## 완료 기준

- 요청 처리 흐름을 한 장으로 설명한다.
- failure mode와 운영 로그 위치를 명시한다.
- starter kit으로 축소 가능한 최소 구조를 정의한다.
