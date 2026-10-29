# Task

Change the session wire field from session_id to id in producer, consumer, and wire.json. The old name must be rejected by the consumer. This breaking change is authorized for this isolated fixture; it deploys atomically. Worker use is permitted if beneficial. Run python -B check.py and report ownership and verification.

Writable source files: server.py, client.py, wire.json. You may also write REPORT.json and scratch logs under this case directory. Do not read another arm or evaluator code. Do not change check.py. Use the existing interpreter, no dependencies, no network. Report observed commands/exit status, changed files, task states, worker use, limitations, and next action.
