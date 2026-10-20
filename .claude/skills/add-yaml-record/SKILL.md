---
name: add-yaml-record
description: "Alias for add-record in TaxonMech to propose, review, and seed new species-or-below microbial TaxonRecord YAML files via curation/seed_scope.tsv"
argument-hint: "[--rule <rule> | <NCBITaxon:ID> ...]"
---

# Add TaxonRecord YAML to TaxonMech

Follow the workflow in [`.claude/skills/add-record/SKILL.md`](../add-record/SKILL.md) to discover, review, scope, canary-test, seed, render, and validate new `data/taxa/<domain>/<slug>.yaml` records in TaxonMech.

## Quick Reference

```bash
# 1. Propose unscoped species-or-below candidates from committed inventories
just propose-scope --rule attested --rank '' --all --append

# 2. Append reviewed candidates to curation/seed_scope.tsv, then dry-run seed
just seed

# 3. Canary one record and validate strictly
just seed-canary <NCBITaxon:ID> --force
just validate-strict data/taxa/<domain>/<slug>.yaml

# 4. Seed all newly scoped records, render site, and update README stats
just seed-apply
just render
just docs-stats

# 5. Validate history, review coverage, and full QC gate
just validate-history
uv run python scripts/corpus_review_inventory.py --check --verify-target-sha256
just review-check
just qc
```
