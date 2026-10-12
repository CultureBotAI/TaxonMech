# YAML Record Review: Streptococcus parasanguinis SK236

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/streptococcus_parasanguinis_sk236.yaml`
- Started UTC: 2026-10-06T13:40:19Z
- Finished UTC: 2026-10-06T13:45:35Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035185`, label `Streptococcus parasanguinis SK236`, rank `STRAIN`, domain `BACTERIA`. The entire YAML was read before judging it, and its bytes were checked unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is `EXACT` / `SEEDED`, with one GTDB mapping, three synonyms, one GTDB xref, three source attestations, zero listed BacDive strains, and one seed event. It is not a human-reviewed or manually curated record. This review changes only this new report.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/streptococcus_parasanguinis_sk236.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/streptococcus_parasanguinis_sk236.yaml --out /private/tmp/spsk236-strict.tsv`: one file scanned, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual source comparison: identity, both NCBI synonyms, all 11 root-first lineage entries, genetic code, source counts, index entry and scope/event agreement. This is not a replacement for corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No focused substitute for these gates is claimed.
- Ontology-node validation is not applicable to this target: it has no curator-added grounded graph nodes. `conf/id_label_targets.yaml` excludes taxonomic fields and delegates their inventory agreement to corpus reproduction.
- History validation is not applicable to an external target history artifact: the ignored-independent history filename search found none for this target. Its inline seed event was schema-checked and compared with the inventory and scope row. No history was scaffolded.
- No separate record-specific citation/reference validator was identified in the documented commands; this record has no DOI, PMID, quoted evidence, definition citation or causal edge to validate.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221910` and inspected live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035185&retmode=xml) agree on the exact strain label, rank, parent `NCBITaxon:1318`, both equivalent names and genetic code 11. The inspected [NCBI taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035185) independently returns rank STRAIN and the same ancestor IDs.

All 11 root-first ancestors match the pinned backbone, including `NCBITaxon:3706788`, the Streptococcus parasanguinis group. Live XML supplies the matching non-root labels/ranks; the dataset lineage includes root. No exact target entry was found in the pinned merged-ID, type-material or dropped tables. No child taxon was found in the full backbone scan.

The strain remains classified under S. parasanguinis in NCBI. Pinned GTDB classifies its genome under S. dentalis. That disagreement must remain source-scoped; it does not authorize changing the NCBI lineage or declaring the strain equivalent to an entire species.

## Evidence

- NCBI identity and synonyms: the backbone row and all three native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31353`, `31354` and `31355` agree with the live authority. The NCBI attestation is one NAME, not a genome count.
- GTDB membership: `data/catalog/gtdb_genomes-0013.jsonl.gz:16858` explicitly names SK236, taxid 1035185, accession `RS_GCF_000222725.1`, GenBank assembly `GCA_000222725.2`, and species S. dentalis. This supports genome classification within that species, not exact strain/species equivalence.
- GTDB counts: `data/raw/gtdb_species.tsv:168758` contains 15 for the species cluster; `data/raw/gtdb_mappings.tsv:1414` repeats 15 for this target. Six other mapping rows carry the same species total for other NCBI targets, including species 1318. `src/taxonmech/extract.py:501` derives the count from genome-to-species edges. The number is faithfully copied but is not a census of SK236 genomes.
- MADIN: `data/raw/madin_taxa.tsv:663` supports one TRAIT_ASSERTION attestation for this taxon. No particular trait value, experimental phenotype or mechanism is asserted by the YAML; none is inferred from that count.
- Scope and lifecycle: `data/taxa/PATHS.tsv:14401`, `curation/seed_scope.tsv:36167`, and the inline event agree on this target and its three-source seed inclusion. The event timestamp is `2026-09-13T17:54:04Z`; the scope row was added on 2026-09-12.
- Genome completeness context: the inspected [NCBI assembly dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000222725.2/dataset_report) explicitly associates SK236 with current `GCA_000222725.2` and paired current `GCF_000222725.1`: 18 contigs, 1,988,691 bp. The complete [BioSample XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN00621706&retmode=xml) names SK236 and provides no culture-collection deposit. These identifiers are leads for the exact strain, not an established BacDive deposit join.
- The inspected [BioProject PRJNA67179 page](https://www.ncbi.nlm.nih.gov/bioproject/67179) identifies the same monoisolate and links `SAMN00621706`, `GCA_000222725.2`, WGS master `AFUC00000000`, GOLD project `Gp0009702` and IMG record `2529292877`. This supports the sequencing context, not type-strain status.
- Native corroboration: `data/catalog/ncbi_genbank-0000.jsonl.gz:3868` and `data/catalog/ncbi_refseq-0000.jsonl.gz:3327` agree with the current assembly pair. `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:1183` records older `GCA_000222725.1` as suppressed; it must not be presented as current.
- Additional native leads: `data/bvbrc/bvbrc-0000.jsonl.gz:3309` associates `1035185.3` with SK236, the current GenBank assembly and the same sample/project. GOLD organism `Go0009702` has strain SK236 but an empty culture-collection field; project `Gp0009702` links that organism, and analysis `Ga0013918` links that project to IMG 2529292877 and unversioned `GCA_000222725`. Complete rows were read at `data/gold/organisms.jsonl.gz:8557`, `data/gold/projects.jsonl.gz:8415`, and `data/gold/analyses.jsonl.gz:7511`. A version must not be invented for the unversioned GOLD value.

## Completeness

The inventory supports zero listed BacDive strains; that means no included source strain record, not absence of a biological strain or genome. No exact target row was found in the BacDive, LPSN, transformed GOLD, MediaDive or BactoTraits taxon inventories. Native GOLD sequencing evidence exists separately from the transformed GOLD taxon attestation surface.

Ignored and compressed files were included in both candidate searches using `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The initial pattern covered taxid 1035185 and SK236 with separator variants. Expansion covered observed assembly, sample, WGS, project, GOLD, IMG and BV-BRC identifiers. All 26 initial candidate rows and all 30 newly encountered rows from the 38-row expansion were read in full using lossless structured decoding. Substring collisions, including unrelated assembly numbers, PRJNA671791/PRJNA671799, and longer WGS prefixes, were rejected rather than transferred. Five SOURCE.json metadata files were searched structurally, and history filenames were searched separately.

No exact SK236 BacDive or StrainInfo deposit assertion was found within those searched roots. NCBI species-level linkouts and bare laboratory strain names do not establish deposit identity. Under `docs/STRAIN_GENOMES.md`, existing strain assertions or validated whole culture-deposit identifiers are required for these joins. Consequently, the available genome leads are documented here, but the lack of nested genome links is not classified as a missing eligible deposit mapping. Do not fabricate a BacDive record or relax the accession matching rules.

The exact ATB sample row at `data/catalog/allthebacteria.tsv.xz:1004103` is NOT_PROCESSED, has no assembly accession, no run accession or assembly URL, and `asm_fasta_on_osf: 0`. It does not justify an ATB assembly link. The initial hit at line 569655 was a different sample whose run number happened to contain 1035185.

Optional definition, nomenclature, citations, phenotype details and causal graph can remain empty. There is no named gene, regulator, pathway, stress response or transcriptomic dataset in the target that calls for an iModulonDB query; the generic MADIN count does not name such a claim. No phenotype or experimental mechanism was transferred from related streptococci.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: GTDB species membership is promoted to exact strain identity.** The mapping `GTDB:s__Streptococcus_dentalis` is copied as `skos:closeMatch`, while the species label becomes an EXACT_SYNONYM and the species identifier becomes an equivalent xref. The native GTDB row supports classifying one SK236 genome in that species cluster; NCBI and the full YAML identify an individual strain. Those are different entity scopes. The 15-genome cluster total does not resolve that difference. The schema at `src/taxonmech/schema/taxonmech.yaml:180` reserves xrefs for true equivalences. The maintained local owner is the rank-insensitive GTDB identity promotion in `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe GTDB mapping that feeds `data/raw/gtdb_mappings.tsv` also needs a direction- and rank-aware predicate review. This is one scope-inflation finding, not three independent findings for mapping, synonym and xref.

Blocker findings: None found. Minor findings: None found. The NCBI record identity itself is supported.

## Recommended Edits

1. In `src/taxonmech/seed.py`, prevent a source GTDB species closeMatch from automatically yielding an exact synonym or equivalent xref for a strain-ranked NCBI record. Preserve the genome classification as a source-scoped mapping with an explicit explanation. Have the kg-microbe mapping owner review the appropriate directed relationship; do not mechanically substitute a broad/narrow predicate without checking its direction and the upstream transform's pooling semantics.
2. Add a focused fixture to `tests/test_seed.py` for SK236 or an equivalent strain/species case. Assert that species-cluster membership and its upstream count remain available while unsupported exact identity claims do not. Preserve legitimate species-level equivalence behavior.
3. Regenerate affected inventory/records through maintained extraction and seeding commands only after the correction is authorized. Do not hand-edit this generated YAML, its raw inventory rows or rendered page. Keep the NCBI lineage, two NCBI synonyms, counts with their source units, and seed provenance intact.
4. Treat the documented genome/sample leads as a bounded future enrichment task. Add genome assertions only after obtaining an eligible source strain/deposit identity or deliberately extending the maintained data model with appropriate evidence and tests; no ad hoc bare-name join.

## Follow-up Checks

- Run focused `uv run pytest tests/test_seed.py` after implementing the rank-aware fix; verify both negative strain-equivalence and positive species-equivalence cases.
- Inspect this exact target after regeneration: no GTDB species exact synonym/equivalent xref, the two NCBI aliases retained, unchanged NCBI identity/lineage, and a source-scoped species mapping whose 15 count remains explicitly a cluster count.
- Rerun the exact schema and strict validation commands above, then the documented full `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` gates. Do not label the manual comparisons in this report as those gates.
- Resolve the GTDB taxon page at an accessible authority endpoint and record the release before any taxonomy update. The live page could not be inspected through the web tool; the conclusion here relies on the pinned native GTDB row and documented schema semantics, not a claim about a newer release.
- Before later genome enrichment, establish explicit culture-deposit or source-strain identity, preserve assembly versions and historical status, and recheck ATB availability. Do not count BioSample, BioProject or GOLD context records as genomes.

## Additional Notes

The source manifest records extraction on 2026-09-13 from kg-microbe commit `30405b70ef762aa46c08278b2b3e06bffb0b34cd`; relevant GTDB metadata input hashes are recorded there. The full manifest hash gate was not rerun.

Browser attempts to open the live GTDB tree, HOMD genome page and NCBI dataset/BioSample pages were unavailable. Direct read-only NCBI HTTP requests successfully retrieved the full assembly JSON and BioSample XML. Search snippets were used only as leads; a cached taxonomy rank and a HOMD classification snippet were not substituted for inspected authority responses.

No external messages, paid research, source edits, generated-page edits, history events, review-status promotions or Git mutations were performed. The other Codex session is closed; the existing dedicated review branch is the only worktree. Eukaryota coverage was checked without reopening its completed reviews.
