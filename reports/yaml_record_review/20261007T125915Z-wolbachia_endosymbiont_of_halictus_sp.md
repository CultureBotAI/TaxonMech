# YAML Record Review: Wolbachia endosymbiont of Halictus sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_halictus_sp.yaml`
- Started UTC: 2026-10-07T12:57:11Z
- Finished UTC: 2026-10-07T12:59:15Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord` for `NCBITaxon:1035900`,
Wolbachia endosymbiont of Halictus sp. It is a bacterial species-rank
taxonomic node, not the Halictus host genus. The record has
`grounding_status: EXACT`, `mapping_status: SEEDED`, 11 lineage
entries, genetic code 11, `strain_count: 0`, one NCBITAXON name
attestation, and one inline seed event.

There are no synonym, nomenclature, type-strain, mapping, strain/genome,
literature-evidence, or graph objects. The YAML is a generated product;
future corrections belong to maintained inputs/transforms, not this
read-only review.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_halictus_sp.yaml`: passed; no LinkML issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_halictus_sp.yaml --out /private/tmp/wol-halictus-strict.tsv`: passed; one file, zero errors. Read the complete header-only TSV.
- Parsed-source comparisons passed for identity, all ancestor labels/ranks/links, source units, path/scope, and inline event wording. They are bounded evidence checks, not replacements for the documented corpus reproduction gate.
- Live NCBI EFetch and Datasets reads succeeded. The NCBI browser HTML page was unavailable through the web tool; the authoritative structured responses supplied the identity evidence.
- `just validate-products`: not applicable; no curated graph grounding/label pairs. Taxonomic labels and identifiers were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent history-content and filename searches found no target artifact. Inline history was validated by schema/strict checks and source comparison.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, or the test suite. This report is not full-corpus acceptance evidence.

## Identity and Grounding

The [NCBI EFetch response](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035900&retmode=xml)
and [Datasets response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035900)
confirm active taxon 1035900, its exact scientific name, species rank,
bacterial placement, and parent `NCBITaxon:2640676`, unclassified
Wolbachia. EFetch confirms genetic code 11 and provides no other names.
Datasets includes root in its lineage; EFetch supplies the remaining
labeled ancestors. All 11 local lineage entries agree with the pinned
backbone and current authority.

The full local backbone row at `data/raw/ncbitaxon_taxa.tsv:222199`
matches the YAML, including empty synonym columns, no retirement
successor, and snapshot date 2026-09-13. The unique path index entry is
`data/taxa/PATHS.tsv:14698`; the explicit scope decision is
`curation/seed_scope.tsv:322459`. The scientific-name source row was
read in full at `data/catalog/ncbi_names-0005.jsonl.gz:31703`.

There were no target children, type-material entries, merge entries, or
dropped-inventory rows in the parsed local inventories. An unspecified
host species does not make this node identical to every Wolbachia taxon
whose host is in Halictus.

## Evidence

- The NCBITAXON attestation correctly records one `NAME` assertion for the exact target ID and label, with the pinned taxonomy date.
- Exact-target scans of the raw BacDive, LPSN, GTDB, GOLD, MediaDive, Madin, and BactoTraits inventories found no applicable rows. With no target descendants, the zero inventoried BacDive count is consistent.
- The inline `seed_from_sources` / `SEEDED_FROM_SOURCES` event matches the source and scope wording. Its `2026-09-13T17:54:04Z` timestamp is the latest extraction time across the raw, ATB, and StrainInfo manifests read during this review.
- Exact Assembly and Nuccore queries for `txid1035900[Organism:noexp]` each returned zero records, with organism-phrase-not-found/no-items warnings. A second Nuccore query using the quoted full label in All Fields also returned zero, with a quoted-phrase-not-found warning and an incorrect-translation diagnostic. These are bounded index results, not proof that no sequence could exist under another identifier, spelling, or unreleased submission.
- No sequence, genome, literature citation, direct quotation, or mechanistic claim is asserted by the YAML. Broad literature search leads were not used as evidence for an exact-taxon mechanism.

All 28 local search candidates were read in full. Their scope matters:

| Candidate group | Inspected source evidence | Interpretation |
|---|---|---|
| Target | Backbone, scope, and native scientific-name row for 1035900 | Supports this YAML |
| Seven near-name taxa | Separate backbone, scope, and scientific-name rows for 1094256, 1126469, 1126470, 1126884, 1631901, 1648165, and 3473539 | Other species-rank nodes, not target aliases or descendants |
| H. tumulorum-associated Wolbachia M175 | `data/bvbrc/bvbrc-0004.jsonl.gz:27748` and `data/catalog/ncbi_genbank-0033.jsonl.gz:28875`; `GCA_035916915.1`, `SAMN30983938`, taxon 1631901, isolate M175 | Not a target strain/genome link |
| H. nicosiae-associated Wolbachia w-HalNico | `data/catalog/ncbi_refseq-0010.jsonl.gz:26599` and `data/catalog/ncbi_genbank-0065.jsonl.gz:32497`; paired `GCF_978021855.1`/`GCA_978021855.1`, `SAMEA120911062`, taxon 3473539 | Not a target strain/genome link |

The seven near-name labels specify H. seladonia, H. scabiosae,
H. subauratus, H. quadricinctus, H. tumulorum, H. ligatus, and
H. nicosiae, respectively. Each has its own ID and the same
unclassified-Wolbachia parent. Shared host-genus wording does not
establish identity. The complete local genome rows were sufficient to
exclude those candidates from this record; their external accessions
were not adopted as target assertions.

## Completeness

Complete enough for this NCBI-only seeded identity record. Zero BacDive
strains does not mean zero biological infections, and an exact-taxid
search returning zero is not evidence that the source taxon should be
deleted or marked deprecated. Current EFetch/Datasets evidence still
supports the active node.

The ignored-inclusive, compressed-content search used
`rg --no-ignore --hidden -n -z -i` with the numeric ID, slug,
and a broad Wolbachia/Halictus name pattern across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`,
`data/seqcode/`, `data/straininfo/`, `data/atb/`,
`curation/`, and `history/`. It returned eight backbone,
eight scope, eight scientific-name, and four genome rows. Only three
were exact-target assertions; the other 25 were resolved as near-name
taxa and their genome metadata.

The five native `SOURCE.json` files were separately parsed completely;
history filenames were checked independently. No additional applicable
source attestation, culture deposit, strain-genome link, or standalone
history was found in these bounded local sources. This is not a claim
of absence from all publications or external databases.

Optional nomenclature, type-strain, synonym, GTDB, strain, genome,
literature, phenotype, and graph slots may remain empty. iModulonDB is
not applicable: no gene, regulator, strain-specific expression dataset,
component, or transcriptomic claim is present.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, source units, empty optional fields,
zero inventoried BacDive count, and the seeded audit state agree
within the inspected scope.

## Recommended Edits

None required. Keep the generated YAML unchanged and retain
`mapping_status: SEEDED`. Do not transfer strains, assemblies,
or biological effects from other Halictus-associated Wolbachia records.

If future authority evidence changes the identity or retirement state,
the maintained owners are the NCBI/source inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`.
Scope changes belong in `curation/seed_scope.tsv`. Enrichment
requires exact source-supported identity and explicit strain/genome joins.

## Follow-up Checks

No corrective action is required.

Any optional future sequence/genome enrichment should first verify
the authority identifier, record status, and specimen/strain scope.
Resolve the current search warnings with stronger accession-based
evidence before making a global absence claim.

After a later authorized maintained-input correction, rerun the
appropriate extraction/seeding workflow and the documented schema,
strict, corpus-reproduction, provenance, and QC gates. Run graph/history
validators if that curation introduces those objects.

## Additional Notes

- Baseline: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`, branch `codex/record-review-extensimonas-20261003`.
- EFetch exposes creation date 2011-05-25, update date 2020-07-08, and publication date 2026-05-06. These source metadata do not by themselves prove a biological change or invalidate the active taxonomy node.
- The entire YAML was reread unchanged before writing this report.
- This review creates only this new report; no source, YAML, generated product, history, GitHub object, branch, or worktree was changed.
- Eukaryota is already fully covered and was not re-reviewed.
