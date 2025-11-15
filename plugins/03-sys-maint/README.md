# System Maintenance Plugin

A Claude Code plugin for system maintenance and cleanup tasks. Helps you reclaim disk space and manage Docker resources through interactive, safe cleanup workflows.

**Platform**: macOS only (tested on macOS)

## Overview

The `sys-maint` plugin provides intelligent system maintenance commands that analyze your system, show you what can be cleaned up, and execute cleanup operations only after your explicit confirmation. Every command follows a safe workflow: Analyze → Preview → Confirm → Execute → Report.

## Available Commands

### `/sys-maint:docker-cleanup`

Analyze Docker resource usage and clean up containers, images, volumes, and build cache.

**What it does:**
1. Shows current Docker disk usage
2. Identifies stopped containers, dangling images, unused volumes
3. Previews what will be removed and estimates space savings
4. Asks for confirmation before deleting anything
5. Executes cleanup operations
6. Reports total space reclaimed

**Usage:**
```bash
/sys-maint:docker-cleanup
```

**Requirements:**
- Docker Desktop installed and running
- Docker CLI available in PATH

**Safety features:**
- Never removes running containers
- Never removes tagged/used images (only dangling ones)
- Shows detailed preview before deletion
- Requires explicit user confirmation
- Provides selective cleanup options

**Example workflow:**
```
> /sys-maint:docker-cleanup

Docker Resource Analysis
========================
Resource Type  | Total Size | Reclaimable | Count
---------------|------------|-------------|-------
Images         | 5.2 GB     | 2.1 GB      | 15 dangling
Containers     | 1.8 GB     | 1.8 GB      | 8 stopped
Volumes        | 0.5 GB     | 0.3 GB      | 3 unused
Build Cache    | 3.2 GB     | 3.2 GB      | -

Total Reclaimable Space: 7.4 GB

What would you like to clean up?
1. Clean All (Recommended) - 7.4 GB freed
2. Selective Cleanup
3. Cancel

[User selects option, cleanup proceeds with confirmation]

Docker Cleanup Complete!
Space Reclaimed: 7.4 GB
```

---

### `/sys-maint:disk-analyze`

Analyze disk usage, identify large files and directories, and provide categorized cleanup recommendations.

**What it does:**
1. Shows overall disk usage
2. Finds largest directories in your home folder
3. Identifies cleanup targets: old downloads, caches, logs, trash, etc.
4. Provides risk-categorized recommendations (Safe/Moderate/Careful)
5. Estimates space savings for each recommendation
6. Optionally executes approved cleanup operations
7. Reports total space freed

**Usage:**
```bash
/sys-maint:disk-analyze
```

**Requirements:**
- macOS (uses macOS-specific paths)
- Standard Unix utilities (du, df, find)

**Safety features:**
- Read-only analysis by default
- Categorizes operations by risk level (Safe/Moderate/Careful)
- Shows preview of files before deletion
- Requires explicit confirmation for each cleanup operation
- Never deletes from unknown locations

**Example workflow:**
```
> /sys-maint:disk-analyze

Disk Usage Summary
==================
Main Disk: Macintosh HD
Capacity: 500 GB
Used: 425 GB (85%)
Available: 75 GB

Cleanup Recommendations
=======================

SAFE (Low Risk)
---------------
1. Empty Trash (~/.Trash) - 2.3 GB
2. Old Downloads (>30 days) - 5.1 GB
3. Temporary files (/tmp) - 0.2 GB

MODERATE (Medium Risk)
----------------------
4. Application Caches - 8.7 GB
5. System Logs - 0.4 GB

What would you like to do?
1. Review and clean specific items
2. Quick clean (Safe items only) - ~7.6 GB
3. Generate detailed report only
4. Cancel

[User selects option, cleanup proceeds with individual confirmations]
```

---

## Installation

### Add this marketplace to Claude Code:
```bash
/plugin marketplace add /Users/irfanputra/Personal/my-claude-code-marketplace
```

### Install the sys-maint plugin:
```bash
/plugin install sys-maint@my-claude-code-marketplace
```

### Verify installation:
```bash
/help
```

You should see:
- `/sys-maint:docker-cleanup` - Docker cleanup command
- `/sys-maint:disk-analyze` - Disk analysis command

---

## Usage Tips

### Best Practices

1. **Run regularly**: Execute these commands monthly to prevent disk space issues
2. **Start with analysis**: Use disk-analyze first to understand your disk usage
3. **Review before confirming**: Always review the preview before confirming cleanup
4. **Safe first**: Start with "Safe" recommendations before moving to "Moderate" or "Careful"

### When to Use Each Command

**Use `docker-cleanup` when:**
- Docker Desktop is taking up significant disk space
- You've been building/testing many container images
- Docker warns about low disk space
- You want to maintain Docker performance

**Use `disk-analyze` when:**
- Your system warns about low disk space
- You want to understand what's consuming space
- Before major software updates (which need free space)
- Regular monthly maintenance

### Common Scenarios

**Scenario 1: "My disk is almost full!"**
```bash
# Step 1: Analyze the situation
/sys-maint:disk-analyze

# Step 2: Choose "Quick clean (Safe items only)"
# This empties trash and temp files

# Step 3: If using Docker, clean that too
/sys-maint:docker-cleanup
```

**Scenario 2: "Docker is slow/using too much space"**
```bash
/sys-maint:docker-cleanup

# Choose "Clean All" to remove everything unused
```

**Scenario 3: "I want to see what's using space without deleting"**
```bash
/sys-maint:disk-analyze

# Choose "Generate detailed report only"
# Review the report at ~/disk-analysis-report.txt
```

---

## Safety & Permissions

### What Gets Deleted (and what doesn't)

**Docker Cleanup - WILL DELETE:**
- Stopped containers
- Dangling/untagged images
- Unused volumes
- Build cache

**Docker Cleanup - NEVER DELETES:**
- Running containers
- Tagged images (unless you select advanced options)
- Volumes in use by containers

**Disk Analyze - WILL DELETE (only with confirmation):**
- Trash contents
- Files in Downloads older than 30 days (you review the list first)
- Application caches
- System logs
- Temporary files
- Selected node_modules folders (you choose which ones)

**Disk Analyze - NEVER DELETES:**
- System files
- Applications
- Documents, Photos, or other user data folders
- Files without explicit confirmation

### Required Permissions

Some operations may require administrator access:
- Clearing system temp files (`/tmp`)
- Cleaning system caches

You'll be prompted for your password if needed.

---

## Troubleshooting

### "Docker does not appear to be running"
- Start Docker Desktop
- Verify Docker is running: `docker ps`

### "Permission denied" errors
- Some cleanup operations may need `sudo`
- The command will notify you which operations failed
- You can run specific commands manually if needed

### "Command not found" errors
- Ensure Docker CLI is installed (for docker-cleanup)
- Ensure standard Unix tools are available (for disk-analyze)

### Cleanup didn't free expected space
- Some applications recreate caches immediately
- Trash might not fully empty (restart Finder)
- Docker may reserve space even after cleanup

---

## Future Roadmap

Planned features for upcoming releases:

### Phase 2: Additional Cleanup Options (v1.1.0)
- `/sys-maint:cache-cleanup` - Clean package manager caches (brew, etc.)
- Additional cleanup targets based on user feedback

### Phase 3: macOS Specific (v1.2.0)
- `/sys-maint:xcode-cleanup` - Clean Xcode derived data and archives
- `/sys-maint:brew-cleanup` - Homebrew maintenance and cleanup

### Phase 4: Advanced Features (v2.0.0)
- `/sys-maint:schedule` - Schedule regular automated maintenance
- `/sys-maint:health-check` - Comprehensive system health report
- `/sys-maint:safe-delete` - Safe file deletion with undo capability

---

## Contributing

Found a bug or have a feature request? Please open an issue in the marketplace repository.

### Ideas for New Commands

We're considering adding:
- Package manager cache cleanup (brew)
- Large file finder and manager
- Duplicate file detector
- Xcode cleanup utilities
- Log rotation and cleanup

---

## Version History

### v1.0.0 (Current)
- Initial release
- Docker cleanup command
- Disk analysis and cleanup command
- Interactive preview and confirmation workflows
- Risk-categorized recommendations

---

## License

MIT License - see repository root for details

## Author

Created by irfansofyana as part of the my-claude-code-marketplace plugin collection.
