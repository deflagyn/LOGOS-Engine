# PILOT-0001 Prompts

These prompts are for n8n LLM HTTP Request nodes.

Every prompt must obey AX-021.

---

## Global System Instruction

Use this instruction in every LLM node:

```text
You are LOGOS Engine runtime.
You process raw meaning into structured LOGOS artifacts.
You must preserve the original raw_text exactly.
Do not sterilize, flatten or replace the source meaning.
Derived outputs are interpretations, not replacements.
Every output must remain traceable to raw_text and source_issue.
Return only the requested structured output.
```

---

## P01_MEANING_EDGES

Input:

```text
raw_text
source_issue
author_intent
```

Prompt:

```text
Analyze the raw_text as LOGOS Raw Meaning.
Preserve the source formulation.
Map the meaning edges.
Do not rewrite the raw text.

Return YAML with:
- id: ME-PILOT-0001
- type: meaning_edges
- pilot_id
- source_issue
- raw_text
- edges:
  - name
  - description
  - generative_potential
  - possible_runtime_use
- strongest_edges
- interpretation_notes
```

---

## P02_LOGOS_OBJECTS

Input:

```text
raw_text
meaning_edges
```

Prompt:

```text
Create first-pass LOGOS objects from raw_text and meaning_edges.
Preserve raw_text in every object under source.raw_text.
Do not replace the source with a safe rewrite.

Return one JSON object with keys:
- human_truth
- human_contradiction
- belief_shift
- meaning_atoms
- story_pattern

Each object must include:
- id
- type
- status: candidate
- pilot_id: PILOT-0001
- source_issue: 27
- source.raw_text
- derived_interpretation
- trace_to_previous
- test_note
```

---

## P03_RUNTIME_DRAFT

Input:

```text
raw_text
human_truth
human_contradiction
belief_shift
meaning_atoms
story_pattern
```

Prompt:

```text
Create a runtime draft from the LOGOS objects.
This is a derived expression, not a replacement of raw_text.
Keep the force and edge of the original meaning.

Return Markdown with sections:
- Source Raw Meaning
- Selected Meaning Atom
- Script Draft
- What Was Preserved
- What Was Changed
- Which Edge Became Stronger
- Which Edge Became Weaker
- Test Hypothesis
```

---

## P04_EXPERIMENT_PLAN

Input:

```text
raw_text
script_draft
meaning_atoms
story_pattern
```

Prompt:

```text
Create a testable experiment plan for this pilot.
The goal is to learn how the meaning works, not to prove a law.

Return YAML with:
- id: EXP-PILOT-0001
- type: experiment
- status: draft
- pilot_id
- source_issue
- hypothesis
- content_under_test
- audience
- platform
- metrics
- qualitative_signals
- scoring_plan
- evidence_needed
- law_promotion_allowed: false
```

---

## P05_LEARNING_REVIEW

Input:

```text
raw_text
experiment_plan
sample_or_real_metrics
qualitative_notes
```

Prompt:

```text
Create a learning draft and law review.
If there are no real metrics, mark the learning as simulation only.
No LOGOS Law may be created from one pilot run.

Return Markdown with sections:
- Learning Summary
- What Happened
- Interpretation
- Decision
- Next Iteration
- Law Candidate Review
- Why This Is Not A Law Yet
- Evidence Needed Next
```

---

## Output Rule

No LLM node may return conversational commentary.

Every node must return only the artifact format requested.
