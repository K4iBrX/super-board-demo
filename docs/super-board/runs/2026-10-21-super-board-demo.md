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
