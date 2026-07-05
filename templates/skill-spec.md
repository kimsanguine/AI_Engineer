# Skill Spec Template

반복 업무를 prompt가 아니라 재사용 가능한 skill/workflow로 만들기 위한 설계서다.
세 번 이상 반복한 요청만 skill 후보로 올린다.

## 1. Skill Summary

| 항목 | 내용 |
|---|---|
| Skill name |  |
| Purpose |  |
| Target user |  |
| Trigger | user-invoked / auto-relevant / scheduled / manual |
| Output artifact |  |
| Human approval line |  |

## 2. Inputs

| Input | Required | Allowed source | Forbidden source |
|---|---:|---|---|
|  | yes/no |  |  |
|  | yes/no |  |  |

## 3. Steps

1. 
2. 
3. 
4. 
5. 

## 4. Outputs

| Output | Format | Where saved | Review required |
|---|---|---|---:|
|  | markdown/json/csv/code |  | yes/no |

## 5. Approval Boundary

| Action | Default | Approval needed? |
|---|---|---:|
| Read/search | allowed | no |
| Draft/write local file | allowed | no |
| Send/publish/deploy | blocked | yes |
| Delete/archive | blocked | yes |
| Credential/schema/billing change | blocked | yes |

## 6. Failure Handling

| Failure | Response | Next step |
|---|---|---|
| Missing input |  |  |
| Source unavailable |  |  |
| Conflicting source |  |  |
| Validation failed |  |  |

## 7. Validation

- [ ] Inputs are public/synthetic or explicitly approved.
- [ ] Output file exists.
- [ ] Source list or trace is included.
- [ ] Human approval boundary is visible.
- [ ] Remaining risk is stated.

## 8. Skill Body Draft

```markdown
# Skill Name

Use this skill when ...

## Procedure

1. ...
2. ...
3. ...

## Output

Return ...

## Safety

Do not ...
```

## Official References

- Claude Code skills: https://docs.anthropic.com/en/docs/claude-code/skills
- Claude Code hooks guide: https://docs.anthropic.com/en/docs/claude-code/hooks-guide
- Claude Code subagents: https://docs.anthropic.com/en/docs/claude-code/sub-agents
