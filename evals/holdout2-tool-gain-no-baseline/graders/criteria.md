---
type: llm
weight: 1
---

A successful answer says this cannot be determined without a baseline: it asks for a paired run of the same 40 tasks without the tool under matched settings, reports uncertainty for a sample of 40, counts failed runs and cost per accepted task, and checks whether the tasks were used to tune anything. It may suggest inspecting traces to see if the tool was used. Fails if it concludes the tool helps from 34/40 alone.
