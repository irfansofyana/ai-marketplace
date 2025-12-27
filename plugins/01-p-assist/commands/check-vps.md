---
description: Check VPS resource utilization
---

# Check VPS Utilization

Check the current resource utilization of your VPS.

**Instructions:**

1. Use `mcp__plugin_p-assist_n8n_pa__check_vps_utilization` to get VPS stats

2. Format and present the results in a clear format

**Output Format:**

```
VPS Utilization Report

**CPU Usage:** [percentage]%
**Memory Usage:** [used]/[total] ([percentage]%)
**Disk Usage:** [used]/[total] ([percentage]%)
**Network:** [in/out] MB/s
**Uptime:** [duration]

**Status:** [Healthy/Warning/Critical based on thresholds]
```

**Error Handling:**
- If VPS is unreachable, notify user
- If API call fails, notify user

**Quick Actions:**
- Restart VPS: /p-assist:restart-vps
