---
description: Analyze Docker resource usage and clean up containers, images, volumes, and build cache with preview and confirmation (macOS only)
allowed-tools: Bash(docker:*)
---

# Docker Cleanup Command

**IMPORTANT**: This command is designed and tested for macOS only. It requires Docker to be installed and running.

Your task is to help the user clean up Docker resources safely by analyzing current usage, showing a preview of what will be removed, getting explicit confirmation, and then executing the cleanup operations.

## Context: Current Docker Status

First, gather the current Docker resource usage by running:

!`docker system df -v`

This will show you disk usage for images, containers, volumes, and build cache.

## Step 1: Analysis Phase

Analyze the Docker system and present a clear summary to the user:

1. **Parse the output** from `docker system df -v` to extract:
   - Total space used by images
   - Total space used by containers
   - Total space used by volumes
   - Total space used by build cache
   - Amount of reclaimable space

2. **Run additional analysis commands**:
   - Count stopped containers: `docker ps -a -f status=exited -q | wc -l`
   - Count dangling images: `docker images -f dangling=true -q | wc -l`
   - List unused volumes: `docker volume ls -f dangling=true -q | wc -l`

3. **Present the analysis** to the user in a clear, formatted table:

```
Docker Resource Analysis
========================

Resource Type       | Total Size | Reclaimable | Count
--------------------|------------|-------------|-------
Images              | X.XX GB    | X.XX GB     | X items
Containers          | X.XX GB    | X.XX GB     | X stopped
Volumes             | X.XX GB    | X.XX GB     | X unused
Build Cache         | X.XX GB    | X.XX GB     | -

Total Reclaimable Space: X.XX GB
```

## Step 2: Preview Phase

Show the user exactly what will be removed:

1. **List stopped containers** (if any):
   - Run: `docker ps -a -f status=exited --format "table {{.ID}}\t{{.Names}}\t{{.Status}}"`
   - Show the first 10 (if more, indicate "... and X more")

2. **List dangling images** (if any):
   - Run: `docker images -f dangling=true --format "table {{.ID}}\t{{.Repository}}\t{{.Size}}"`
   - Show the first 10 (if more, indicate "... and X more")

3. **List unused volumes** (if any):
   - Run: `docker volume ls -f dangling=true --format "table {{.Name}}\t{{.Driver}}"`
   - Show the first 10 (if more, indicate "... and X more")

4. **Show build cache details**:
   - Run: `docker buildx du --verbose` (or indicate that build cache will be cleared)

## Step 3: Confirmation

Present cleanup options to the user:

```
What would you like to clean up?

1. Clean All (Recommended)
   - Remove all stopped containers
   - Remove all dangling images
   - Remove all unused volumes
   - Clear build cache
   - Estimated space freed: X.XX GB

2. Selective Cleanup
   - Choose specific resource types to clean

3. Cancel
   - Exit without making changes
```

**Ask the user explicitly**: "Which option would you like? (Enter 1, 2, or 3)"

Wait for the user's response before proceeding.

## Step 4: Cleanup Phase

Based on the user's choice:

### If user chose "Clean All" (Option 1):

Execute these commands in sequence, showing progress for each:

1. **Remove stopped containers**:
   ```bash
   docker container prune -f
   ```
   Report: "✓ Removed stopped containers"

2. **Remove dangling images**:
   ```bash
   docker image prune -f
   ```
   Report: "✓ Removed dangling images"

3. **Remove unused volumes**:
   ```bash
   docker volume prune -f
   ```
   Report: "✓ Removed unused volumes"

4. **Clear build cache**:
   ```bash
   docker builder prune -f
   ```
   Report: "✓ Cleared build cache"

### If user chose "Selective Cleanup" (Option 2):

Ask the user which resource types to clean:
- "Clean stopped containers? (y/n)"
- "Clean dangling images? (y/n)"
- "Clean unused volumes? (y/n)"
- "Clear build cache? (y/n)"

Then execute only the selected cleanup commands.

### If user chose "Cancel" (Option 3):

Respond with: "Docker cleanup cancelled. No changes were made."

## Step 5: Report Results

After cleanup completes:

1. **Run final analysis**:
   ```bash
   docker system df
   ```

2. **Calculate and show space freed**:
   - Compare before/after disk usage
   - Show total space reclaimed

3. **Present final report**:

```
Docker Cleanup Complete!
========================

Space Reclaimed: X.XX GB

Current Docker Disk Usage:
- Images: X.XX GB
- Containers: X.XX GB
- Volumes: X.XX GB
- Build Cache: X.XX GB

Next Steps:
- Run this command periodically to maintain disk space
- Consider removing unused images: `docker image prune -a` (removes all unused images, not just dangling)
- Monitor with: `docker system df`
```

## Error Handling

If any command fails:

1. **Capture the error message**
2. **Continue with remaining cleanup operations** (don't stop the entire process)
3. **Report which operations failed** at the end
4. **Suggest recovery actions**:
   - "Error removing containers: [error message]"
   - "You may need to manually stop running containers first"
   - "Try: `docker ps` to see running containers"

If Docker is not installed or not running:
- "Docker does not appear to be installed or running on your system"
- "Please start Docker or install it to use this command"

## Validation Criteria

Success indicators:
- Commands execute without errors
- Disk space is reclaimed (shown in final report)
- User receives clear confirmation of what was cleaned
- No running containers or tagged images are affected

Safety checks:
- Never remove running containers
- Never remove tagged/used images (only dangling ones in default mode)
- Always show preview before deletion
- Require explicit user confirmation
