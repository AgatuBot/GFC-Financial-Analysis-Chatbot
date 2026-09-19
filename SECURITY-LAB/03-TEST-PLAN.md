# GFC Web Application Security Test Plan

| ID | Area | Test | Expected secure behavior |
|---|---|---|---|
| GFC-01 | HTTP | Normal GET | Expected page |
| GFC-02 | HTTP | Unsupported method | Safe rejection |
| GFC-03 | Input | Empty chatbot input | Controlled validation |
| GFC-04 | Input | Missing JSON field | Controlled validation |
| GFC-05 | Input | Wrong data type | Controlled validation |
| GFC-06 | Input | Unexpected field | Safe handling |
| GFC-07 | Input | Controlled long input | No crash |
| GFC-08 | Input | Unicode/special characters | Correct handling |
| GFC-09 | Logic | Unsupported company | Controlled response |
| GFC-10 | Logic | Unsupported year | Controlled response |
| GFC-11 | Logic | Unsupported metric | Controlled response |
| GFC-12 | Session | Follow-up context | Appropriate scoping |
| GFC-13 | Session | Cookie attributes | Appropriate flags |
| GFC-14 | Headers | Security headers | Appropriate controls |
| GFC-15 | Errors | Malformed request | No stack trace/secrets |
| GFC-16 | Injection | Injection-like input | No unintended interpretation |
| GFC-17 | Access control | Direct endpoint access | Intended functionality only |
| GFC-18 | Resources | Low-volume repeated requests | Service remains stable |

## Architecture-aware testing
The application currently uses pandas and rule-based parsing rather than a database query layer. Do not claim SQL injection merely because SQL-looking characters are accepted. Determine whether input reaches an interpreter, database, shell, template or other execution sink.

## Remediation lifecycle
Reproduce -> capture evidence -> assess impact -> fix -> deploy -> repeat the original test -> record retest result.