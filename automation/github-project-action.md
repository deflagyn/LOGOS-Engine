# GitHub Project Action Setup

This guide explains how to create and manage the LOGOS Engine Roadmap Project through GitHub Actions.

Do not paste GitHub tokens into chat, issues, commits or documentation.

Use GitHub repository secrets.

---

## Required Secret

Create a repository secret:

```text
GH_PROJECT_TOKEN
```

The token must have access to manage GitHub Projects and issues.

Recommended permissions:

```text
Projects: Read and write
Issues: Read and write
Contents: Read
Metadata: Read
```

For classic tokens, the usual required scopes are:

```text
project
public_repo
```

If the repository becomes private, use:

```text
repo
project
```

---

## Workflow

The workflow file is:

```text
.github/workflows/setup-logos-project.yml
```

It is triggered manually through:

```text
Actions → Setup LOGOS GitHub Project → Run workflow
```

---

## What the workflow does

1. Finds or creates the GitHub Project:

```text
LOGOS Engine Roadmap
```

2. Creates custom fields:

```text
Type
Client
Language
Phase
Confidence
LOGOS Status
Metric Score
Target Date
Experiment Week
```

3. Adds initial issues:

```text
#1 EXP-0001
#3 HT-0001
#4 BS-0001
#5 SCRIPT-0001
#9 ROADMAP-0001
```

---

## Notes

The GitHub CLI supports creating projects with `gh project create`, creating fields with `gh project field-create`, and adding issues with `gh project item-add`.

Some visual Project view settings may still need manual adjustment in the GitHub UI.

---

## Security Rule

If a token was ever pasted into chat or a public place, treat it as compromised and revoke it.

Create a new token and store it only as a GitHub secret.
