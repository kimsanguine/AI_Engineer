# validation-log.md — FAQ Agent Lite

## 2026-07-05 — baseline

### Commands

```bash
python3 agent.py "Can I change my billing date?"
python3 -m unittest discover -s tests
```

### Observed output

```text
Q: Can I change my billing date?
A: Yes. In this fictional ACME Life sample, customers can request one billing-date change per month before the next invoice is issued.
Source: FAQ-001 | Category: billing | Confidence: 1.00

...
----------------------------------------------------------------------
Ran 3 tests in 0.002s

OK
```

### Expected checks

- Billing question returns `FAQ-001`.
- Unknown weather question abstains.
- PII/security question returns `FAQ-004`.

### Public safety

- Uses fictional company `ACME Life`.
- Uses only synthetic FAQ data in `sample_data/faqs.json`.
- No API key, private URL, customer data, or real policy text required.

### Status

Verified locally with Python 3 standard library only.
