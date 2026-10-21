# Run 2026-10-21 · super-board-demo

| Card | Lanes | Status | Column | Detail |
|---|---|---|---|---|
| #1 | build:failed | failed | Ready | codex not found in PATH (exit 1), no work done |
[00:45:44] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[00:45:47] initial Ready count: 1
[00:45:49] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[00:45:53] dispatch lane=build issue=#1 pid=99582 claim=K4iBrX
[00:47:56] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[00:49:59] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[00:52:01] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[00:54:04] reaped stale lock + swept assignee on #1 (pid=99582)
[00:54:06] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#1) q_idle=1(#_) r_idle=1(#_)
[00:54:11] dispatch lane=build issue=#1 pid=11608 claim=K4iBrX
[00:54:31] STOP 📋 1 in-flight worker(s) to wrap up
[00:54:31] STOP 
[00:54:31] STOP ─── #1 (lane=build, pid=11608) ───
[00:54:33] STOP   💬 issue comment posted on #1
[00:54:38] STOP   🔓 released assignee + lane labels on #1
[00:54:39] STOP   ☠ worker(build/#1) pid=11608 SIGTERMed
[00:54:39] STOP 
[00:54:39] STOP 🛑 stopping dispatcher loop
[00:54:40] STOP   ☠ dispatcher pid=99242 SIGTERMed
[00:54:40] STOP 
[00:54:40] STOP 🧽 cleared .claude/super-board/inflight
[00:59:35] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[00:59:38] initial Ready count: 1
[00:59:40] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[00:59:44] dispatch lane=build issue=#1 pid=20878 claim=K4iBrX
[01:01:47] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[01:03:49] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[01:05:52] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[01:07:55] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[01:09:57] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#1) q_idle=1(#_) r_idle=1(#_)
[01:09:57] 🛑 halt — RUNAWAY: no card reached Done in 6 dispatch cycles
[01:09:57]    dispatches=1 reaps=0 cards-landed-this-run=0
[01:09:57]    most re-dispatched issues (count issue):
[01:09:57]      1 1
[01:09:57]    → inspect worker logs in docs/super-board/runs/2026-10-21-super-board-demo-workers/
[01:09:57] super-board run finished. manifest: docs/super-board/runs/2026-10-21-super-board-demo.md
[01:49:41] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[01:49:45] initial Ready count: 0
[01:49:47] tick — Ready=0 Building=0 QA=1 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[01:49:50] dispatch lane=qa issue=#1 pid=84654 claim=K4iBrX
[01:51:53] tick — Ready=0 Building=0 QA=1 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=0(#1) r_idle=1(#_)
[01:53:55] tick — Ready=0 Building=0 QA=1 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=0(#1) r_idle=1(#_)
[01:54:55] STOP 📋 1 in-flight worker(s) to wrap up
[01:54:55] STOP 
[01:54:55] STOP ─── #1 (lane=qa, pid=84654) ───
[01:54:57] STOP   💬 issue comment posted on #1
[01:55:01] STOP   🔓 released assignee + lane labels on #1
[01:55:03] STOP   ☠ worker(qa/#1) pid=84654 SIGTERMed
[01:55:03] STOP 
[01:55:03] STOP 🛑 stopping dispatcher loop
[01:55:04] STOP   ☠ dispatcher pid=84214 SIGTERMed
[01:55:04] STOP 
[01:55:04] STOP 🧽 cleared .claude/super-board/inflight
[01:55:24] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[01:55:27] initial Ready count: 0
[01:55:29] tick — Ready=0 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[01:55:29] ✅ all active-pipeline columns empty and all lanes idle — exiting cleanly
[01:55:29] super-board run finished. manifest: docs/super-board/runs/2026-10-21-super-board-demo.md
[01:57:39] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[01:57:42] initial Ready count: 1
[01:57:44] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[01:57:47] dispatch lane=build issue=#2 pid=97773 claim=K4iBrX
[01:59:50] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:01:52] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:03:55] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:05:58] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:07:47] STOP 📋 1 in-flight worker(s) to wrap up
[02:07:47] STOP 
[02:07:47] STOP ─── #2 (lane=build, pid=97773) ───
[02:07:49] STOP   💬 issue comment posted on #2
[02:07:54] STOP   🔓 released assignee + lane labels on #2
[02:07:55] STOP   ☠ worker(build/#2) pid=97773 SIGTERMed
[02:07:55] STOP 
[02:07:55] STOP 🛑 stopping dispatcher loop
[02:07:56] STOP   ☠ dispatcher pid=97297 SIGTERMed
[02:07:56] STOP 
[02:07:56] STOP 🧽 cleared .claude/super-board/inflight
[02:09:55] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[02:09:58] initial Ready count: 1
[02:10:00] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[02:10:04] dispatch lane=build issue=#2 pid=12732 claim=K4iBrX
[02:12:07] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:14:10] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:16:12] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:18:15] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:20:18] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:20:18] 🛑 halt — RUNAWAY: no card reached Done in 6 dispatch cycles
[02:20:18]    dispatches=1 reaps=0 cards-landed-this-run=0
[02:20:18]    most re-dispatched issues (count issue):
[02:20:18]      1 2
[02:20:18]    → inspect worker logs in docs/super-board/runs/2026-10-21-super-board-demo-workers/
[02:20:18] super-board run finished. manifest: docs/super-board/runs/2026-10-21-super-board-demo.md
[02:26:47] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=6 max_dispatches=0
[02:26:49] reaped stale lock + swept assignee on #2 (pid=12732)
[02:27:00] ↩ stranded #2: Building → Ready (branch none)
[02:27:01] initial Ready count: 1
[02:27:04] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[02:27:08] dispatch lane=build issue=#2 pid=35067 claim=K4iBrX
[02:29:10] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:31:13] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:33:16] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:35:18] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:37:21] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:37:21] 🛑 halt — RUNAWAY: no card reached Done in 6 dispatch cycles
[02:37:21]    dispatches=1 reaps=1 cards-landed-this-run=0
[02:37:21]    most re-dispatched issues (count issue):
[02:37:21]      1 2
[02:37:21]    → inspect worker logs in docs/super-board/runs/2026-10-21-super-board-demo-workers/
[02:37:21] super-board run finished. manifest: docs/super-board/runs/2026-10-21-super-board-demo.md
[02:44:48] super-board run started — config=super-board-demo base=main tick=120s max_workers=3 no_progress_cycles=20 max_dispatches=0
[02:44:50] reaped stale lock + swept assignee on #2 (pid=35067)
[02:45:00] ↩ stranded #2: Building → Ready (branch none)
[02:45:01] initial Ready count: 1
[02:45:03] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#_) q_idle=1(#_) r_idle=1(#_)
[02:45:07] dispatch lane=build issue=#2 pid=58008 claim=K4iBrX
[02:47:10] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:49:12] tick — Ready=1 Building=0 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:51:15] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:53:17] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[02:55:20] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=0(#2) q_idle=1(#_) r_idle=1(#_)
[03:06:23] reaped stale lock + swept assignee on #2 (pid=58008)
[03:06:26] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:08:28] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:10:31] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:12:33] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:14:36] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:16:38] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:18:41] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:20:44] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:22:46] tick — Ready=0 Building=1 QA=0 Review=0 Blocked=0 lanes: b_idle=1(#2) q_idle=1(#_) r_idle=1(#_)
[03:23:38] STOP 
[03:23:38] STOP 🛑 stopping dispatcher loop
[03:23:39] STOP   ☠ dispatcher pid=57123 SIGTERMed
