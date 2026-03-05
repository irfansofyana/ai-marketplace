---
description: Restart your VPS
argument-hint: [confirm]
---

# Restart VPS

Restart your VPS server.

**Instructions:**

1. If user hasn't confirmed, ask for confirmation:
   "Are you sure you want to restart your VPS? This will temporarily interrupt all services."

2. On confirmation, use `mcp__plugin_p-assist_n8n_pa__restart_my_vps` to restart

3. Monitor and report the restart status

**Output Format:**

```
VPS Restart Initiated

**Status:** Restarting...
**Expected Downtime:** ~2-5 minutes

The VPS will be back online shortly. You can check status with: /p-assist:check-vps
```

**Error Handling:**
- If restart fails, notify user with error details
- If VPS is already restarting, inform user

**Warnings:**
- This will interrupt all services on the VPS
- Make sure no critical work is in progress
