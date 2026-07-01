# LOGOS Experiment Scoring Model

This document defines a simple scoring model for LOGOS experiments.

The goal is not to reward vanity metrics.

The goal is to understand whether a meaning movement worked.

---

## Total Score

```text
Total Score = Attention + Retention + Action + Meaning Signal + Learning Quality
```

Each block is scored from 0 to 20.

Maximum score: 100.

---

## 1. Attention Score

Question:

```text
Did the experiment earn attention?
```

Signals:

- views;
- reach;
- hook performance;
- first seconds retention;
- open rate or click rate for non-video formats.

Score:

```text
0  = no attention
10 = acceptable attention
20 = strong attention
```

---

## 2. Retention Score

Question:

```text
Did people stay with the meaning long enough?
```

Signals:

- average watch time;
- completion rate;
- scroll depth;
- read time;
- repeat viewing.

Score:

```text
0  = people leave immediately
10 = average retention
20 = strong retention
```

---

## 3. Action Score

Question:

```text
Did the experiment create useful action?
```

Signals:

- saves;
- shares;
- comments;
- profile clicks;
- follows;
- form submissions;
- message requests;
- internal next-step actions.

Score:

```text
0  = no action
10 = weak but visible action
20 = strong action
```

---

## 4. Meaning Signal Score

Question:

```text
Did people recognize or repeat the meaning?
```

Signals:

- comments showing recognition;
- people quoting the phrase;
- people tagging others;
- people asking deeper questions;
- objections that reveal the belief boundary;
- repeated use of the Meaning Atom.

Score:

```text
0  = no meaning signal
10 = some recognition
20 = strong meaning signal
```

---

## 5. Learning Quality Score

Question:

```text
Did the experiment teach us something useful?
```

Signals:

- clear conclusion;
- clear reason why it worked or failed;
- next iteration defined;
- possible Law Candidate identified;
- no unsupported conclusion.

Score:

```text
0  = no learning
10 = basic learning
20 = strong learning
```

---

## Score Interpretation

```text
0-30   weak result
31-50  usable but unclear
51-70  promising
71-85  strong
86-100 exceptional
```

---

## Test Plan

Purpose:

```text
Check whether the model can score a sample experiment consistently.
```

Input:

```text
Sample metrics and qualitative notes.
```

Expected output:

```text
Five partial scores and one total score.
```

Manual test:

```text
Take one sample experiment, score all five blocks, write the reason for every score.
```

Acceptance criteria:

```text
The total score is explainable and points to a next action.
```

Evidence:

```text
A scored experiment or weekly learning report.
```

Future automation:

```text
n8n or Python can calculate score from structured metrics.
```
