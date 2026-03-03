Personal AI Employee - Silver Tier
- 2 Watchers: File System + CSV Drop
- Claude Code integration for Plan.md, Dashboard update
- Human-in-the-Loop approval workflow
- LinkedIn post draft generation
- Local-first, no cloud billing


# Personal AI Employee - Gold Tier

**Tagline:** Your life and business on autopilot. Local-first, agent-driven, human-in-the-loop.

**Features Completed:**
- 2 Watchers: File System + CSV Drop (detects files in Inbox/DropBox → Needs_Action)
- Claude Code integration: Reads vault, creates Plan.md, moves files to Done/completed
- Human-in-the-Loop: Pending_Approval → Approved → execute
- LinkedIn post drafts in Social_Drafts
- Ralph Wiggum loop: Autonomous multi-step task completion (retry until TASK_COMPLETE.txt)
- Weekly CEO Briefing: Generates Monday Morning report from Business_Goals.md + /Done
- Auto-run via Task Scheduler (weekly trigger)

**Tech Stack:**
- Obsidian vault (local Markdown)
- Claude Code (reasoning engine)
- Python watchers (Playwright not used due to stability)
- Windows Task Scheduler for automation
- No external APIs/billing (local-first privacy focus)

**Demo:** [Add video link here if uploaded]

**Lessons Learned:**
- Playwright WhatsApp automation unstable in 2026 (anti-bot measures)
- File-based triggers reliable & privacy-safe
- Explicit completion markers (TASK_COMPLETE.txt) essential for loop exit

**Next:** Odoo integration for accounting, social posting MCP.
