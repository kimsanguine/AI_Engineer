# Tool Spec Template

Agent에게 외부 도구를 열어주기 전에 tool contract를 먼저 쓴다. 좋은 tool은
"무엇을 할 수 있는가"보다 "무엇을 하지 않는가"가 명확하다.

## 1. Tool Summary

| 항목 | 내용 |
|---|---|
| Tool name |  |
| Purpose |  |
| Track | 02 MCP Tools |
| Read/write level | read-only / draft / write / destructive |
| Human approval required | yes / no |
| Data scope | public / synthetic / internal / private |

## 2. When To Use

- 
- 
- 

## 3. When Not To Use

- 
- 
- 

## 4. Input Schema

```json
{
  "type": "object",
  "properties": {
    "query": {
      "type": "string",
      "description": "User question or lookup term"
    },
    "limit": {
      "type": "integer",
      "description": "Maximum number of results",
      "default": 5
    }
  },
  "required": ["query"]
}
```

## 5. Output Contract

| Field | Type | Required | Description |
|---|---|---:|---|
| `status` | string | yes | `ok`, `not_found`, `error`, `needs_approval` |
| `results` | array | no | Retrieved results |
| `source` | string | yes | File, API, or dataset used |
| `trace_id` | string | no | Run/tool trace |
| `error` | string | no | Human-readable failure reason |

## 6. Failure Modes

| Failure | Tool response | User-facing behavior |
|---|---|---|
| Input missing |  |  |
| Source unavailable |  |  |
| Permission denied |  |  |
| No result |  |  |
| Write approval missing |  |  |

## 7. Safety Boundary

- [ ] API key or credential is not embedded in code.
- [ ] Tool does not request real customer/student/patient data.
- [ ] Write action is separated from read action.
- [ ] Destructive action requires explicit human approval.
- [ ] Output includes source or trace.

## 8. Validation Cases

| ID | Input | Expected status | Expected source | Notes |
|---|---|---|---|---|
| T-001 |  |  |  |  |
| T-002 |  |  |  |  |
| T-003 |  |  |  |  |

## Official References

- MCP introduction: https://modelcontextprotocol.io/docs/getting-started/intro
- MCP tools specification: https://modelcontextprotocol.io/specification/2025-06-18/server/tools
- Claude Code MCP reference: https://docs.anthropic.com/en/docs/claude-code/mcp
