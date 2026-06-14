# Cost Tracking Reference

> Load this on-demand when the user asks about costs or before batch operations.

## Pricing Table

| Model | Resolution | Cost/Image |
|-------|-----------|-----------|
| 3.1 Flash | 512 | $0.020 |
| 3.1 Flash | 1K | $0.039 |
| 3.1 Flash | 2K | $0.078 |
| 3.1 Flash | 4K | $0.156 |
| 2.5 Flash | 1K | $0.039 |
| Batch API | Any | 50% of above |

## Free Tier Limits

- ~10 requests per minute (RPM)
- ~500 requests per day (RPD)
- Resets midnight Pacific

## Cost Tracker Commands

```bash
cost_tracker.py log --model gemini-3.1-flash-image-preview --resolution 1K --prompt "..."
cost_tracker.py summary
cost_tracker.py today
cost_tracker.py estimate --model gemini-3.1-flash-image-preview --resolution 1K --count 10
cost_tracker.py reset --confirm
```

Ledger stored at `~/.banana/costs.json`.
