---
description: Analyze disk usage, identify space hogs, and provide cleanup recommendations with optional execution (macOS only)
allowed-tools: Bash(df:*), Bash(du:*), Bash(find:*), Bash(ls:*)
---

# Disk Analysis and Cleanup Command

**IMPORTANT**: This command is designed and tested for macOS only. It uses macOS-specific paths and utilities.

Your task is to help the user analyze disk usage, identify large files and directories consuming space, provide categorized cleanup recommendations, and optionally execute approved cleanup operations.

## Context: Current Disk Status

First, check the current disk usage:

!`df -h`

This shows the overall disk space availability on all mounted filesystems.

## Step 1: System Analysis

Perform a comprehensive disk analysis:

### 1.1 Overall Disk Usage

Parse the `df -h` output and identify:
- The main disk (usually `/` or `/System/Volumes/Data` on macOS)
- Total capacity
- Used space
- Available space
- Percentage used

Present this information clearly:

```
Disk Usage Summary
==================
Main Disk: [name]
Capacity: X.XX GB
Used: X.XX GB (XX%)
Available: X.XX GB
```

### 1.2 Find Largest Directories

Run these commands to identify space hogs:

1. **Top 10 largest directories in home folder**:
   ```bash
   du -h -d 1 ~ 2>/dev/null | sort -hr | head -10
   ```

2. **Large directories in common locations**:
   ```bash
   du -h -d 1 ~/Library 2>/dev/null | sort -hr | head -10
   du -h -d 1 ~/Downloads 2>/dev/null | sort -hr | head -5
   ```

Present the findings:

```
Largest Directories
===================

Home Directory (~):
1. [directory] - X.XX GB
2. [directory] - X.XX GB
...

Library (~Library):
1. [directory] - X.XX GB
2. [directory] - X.XX GB
...
```

### 1.3 Identify Specific Cleanup Targets

Check common space hogs:

1. **Old Downloads** (files older than 30 days):
   ```bash
   find ~/Downloads -type f -mtime +30 -exec ls -lh {} \; 2>/dev/null | head -20
   ```
   Count and calculate total size

2. **Application Caches**:
   ```bash
   du -sh ~/Library/Caches 2>/dev/null
   ```

3. **System Logs**:
   ```bash
   du -sh ~/Library/Logs 2>/dev/null
   ```

4. **Trash**:
   ```bash
   du -sh ~/.Trash 2>/dev/null
   ```

5. **Temporary files**:
   ```bash
   du -sh /tmp 2>/dev/null
   ```

## Step 2: Provide Cleanup Recommendations

Based on the analysis, present categorized recommendations:

```
Cleanup Recommendations
=======================

SAFE (Low Risk)
---------------
These operations are generally safe and reversible:

1. Empty Trash (~/.Trash)
   Estimated space: X.XX GB
   Risk: Low - items can be restored before emptying

2. Old Downloads (files >30 days old)
   Estimated space: X.XX GB
   Risk: Low - review list before deletion

3. Clear temporary files (/tmp)
   Estimated space: X.XX MB
   Risk: Low - system recreates as needed


MODERATE (Medium Risk)
----------------------
These require some review before deletion:

4. Application Caches (~/Library/Caches)
   Estimated space: X.XX GB
   Risk: Medium - apps will rebuild caches, may slow down temporarily

5. System Logs (~/Library/Logs)
   Estimated space: X.XX MB
   Risk: Medium - useful for troubleshooting recent issues


CAREFUL (Higher Risk)
---------------------
These require careful review and may affect functionality:

6. Large files in specific directories
   [List specific large files found]
   Risk: Varies - requires manual review
```

## Step 3: Ask for User Confirmation

Present cleanup options:

```
What would you like to do?

1. Review and clean specific items
   - I'll show you each category and you can approve individually

2. Quick clean (Safe items only)
   - Empty Trash
   - Clear temporary files
   - Estimated space freed: X.XX GB

3. Generate detailed report only
   - No cleanup, just save findings to a file

4. Cancel
   - Exit without making changes
```

**Ask the user**: "Which option would you like? (Enter 1, 2, 3, or 4)"

Wait for the user's response.

## Step 4: Cleanup Phase (if approved)

### Option 1: Review and Clean Specific Items

For each recommendation, ask the user:

**For Trash:**
```bash
ls -lh ~/.Trash | head -10
```
Show first 10 items, then ask: "Empty trash (~/.Trash)? This will permanently delete X.XX GB. (y/n)"

If yes:
```bash
rm -rf ~/.Trash/*
```

**For Old Downloads:**
```bash
find ~/Downloads -type f -mtime +30 -exec ls -lh {} \;
```
Show the list and ask: "Delete these files from Downloads? (y/n)"

If yes:
```bash
find ~/Downloads -type f -mtime +30 -delete
```

**For Application Caches:**
Show size and ask: "Clear application caches (~/Library/Caches)? Apps will rebuild as needed. (y/n)"

If yes:
```bash
rm -rf ~/Library/Caches/*
```

**For System Logs:**
Ask: "Clear system logs (~/Library/Logs)? (y/n)"

If yes:
```bash
rm -rf ~/Library/Logs/*
```

**For Temporary Files:**
Ask: "Clear temporary files (/tmp)? (y/n)"

If yes:
```bash
sudo rm -rf /tmp/*
```

### Option 2: Quick Clean (Safe Items Only)

First, show the user what will be cleaned:

```
Quick Clean Summary
===================
The following items will be deleted:

1. Trash (~/.Trash)
   - Size: X.XX GB

2. Temporary files (/tmp)
   - Size: X.XX MB

Total Space to be Freed: X.XX GB
```

**Ask for final confirmation**: "Proceed with quick clean? This will permanently delete the items listed above. (y/n)"

Wait for user response.

**If user confirms (y):**

Execute these commands in sequence:

1. **Empty Trash**:
   ```bash
   rm -rf ~/.Trash/*
   ```
   Report: "✓ Emptied Trash"

2. **Clear temporary files**:
   ```bash
   sudo rm -rf /tmp/*
   ```
   Report: "✓ Cleared temporary files"

Report total space freed.

**If user declines (n):**

Respond: "Quick clean cancelled. No changes were made."

### Option 3: Generate Detailed Report

Create a report file:

```bash
cat > ~/disk-analysis-report.txt <<EOF
Disk Analysis Report
Generated: $(date)

[Include all analysis findings]
EOF
```

Tell user: "Report saved to ~/disk-analysis-report.txt"

### Option 4: Cancel

Respond: "Disk analysis complete. No changes were made."

## Step 5: Final Report

After any cleanup operations:

1. **Run final disk check**:
   ```bash
   df -h
   ```

2. **Calculate space freed**:
   - Compare before/after disk usage
   - Show specific space reclaimed

3. **Present final report**:

```
Disk Cleanup Complete!
======================

Space Reclaimed: X.XX GB

Current Disk Status:
- Total: X.XX GB
- Used: X.XX GB (XX%)
- Available: X.XX GB

Items Cleaned:
✓ [Item 1] - X.XX GB freed
✓ [Item 2] - X.XX GB freed
...

Next Steps:
- Run this command monthly to maintain disk space
- Consider removing large unused applications
- Review Downloads folder regularly
- For more aggressive cleanup, consider:
  - `docker system prune -a` (if using Docker)
  - Clearing Xcode derived data (if using Xcode)
  - Clearing Homebrew cache: `brew cleanup`
```

## Error Handling

If commands fail:

1. **Permission errors**:
   - "Permission denied error occurred"
   - "Some operations may require administrator access"
   - "Try running specific commands with 'sudo' if needed"

2. **File not found**:
   - Skip that item gracefully
   - Continue with other cleanup operations
   - Note in final report which items were skipped

3. **Disk full**:
   - "Disk is critically low on space"
   - "Recommend starting with Trash and Downloads cleanup"
   - "Consider moving large files to external storage"

If critical commands fail:
- Show the error message
- Suggest manual alternatives
- Provide command examples user can run directly

## Validation Criteria

Success indicators:
- Disk usage analysis completes successfully
- Recommendations are clear and categorized by risk
- Space savings estimates are accurate
- User receives explicit confirmation prompts
- Final report shows actual space freed

Safety checks:
- Never delete files without explicit confirmation
- Show preview of files before deletion
- Categorize operations by risk level
- Provide undo suggestions where possible
- Only delete from known safe locations (Trash, tmp, caches)

## Additional Tips for User

Include in final output:

```
Pro Tips for Disk Management:
- Use `du -sh * | sort -hr | head -20` to find large items in any directory
- macOS Storage Management: System Settings > General > Storage
- Consider cloud storage for large media files
- Regular maintenance prevents critical low-disk situations
- Check for large files: `find ~ -type f -size +1G 2>/dev/null`
```
