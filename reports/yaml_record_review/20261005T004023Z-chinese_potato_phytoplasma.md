# YAML Record Review: Chinese potato phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/chinese_potato_phytoplasma.yaml`
- Started UTC: 2026-10-05T00:38:18Z
- Finished UTC: 2026-10-05T00:40:23Z
- Verdict: pass

## Target

Read the entire 54-line generated TaxonRecord for NCBITaxon:1034066, Chinese potato phytoplasma: SPECIES, BACTERIA, parent NCBITaxon:3042590, EXACT grounding, SEEDED status, genetic code 11, zero inventoried strains and one NCBI NAME attestation. The target is this NCBI taxon, not all phytoplasmas infecting potatoes in China, a named culture deposit, or its plant host.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/chinese_potato_phytoplasma.yaml`; exit 0, no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run python scripts/validate_strict.py data/taxa/bacteria/chinese_potato_phytoplasma.yaml --out /private/tmp/chinese-potato-phytoplasma-strict-20261005.tsv`; exit 0, one file, zero ERROR rows.
- PASS: structured comparison of the complete backbone row, ten ancestors, seven mapped-source inventories, PATHS and scope entries, sole attestation and inline seed event. No children occur in the pinned backbone.
- PASS: exact target scans of type-material, merged-ID and dropped inventories returned no rows.
- SKIPPED: `just verify-corpus` is full-corpus only; a diagnostic limit was not treated as a focused mode.
- NOT APPLICABLE: `just validate-products`; no causal nodes or product labels.
- SKIPPED: `just validate-history`; ignored-inclusive identifier/name/slug searches found no external target history. The inline event was checked directly.
- No undocumented focused term/reference validator was substituted. Source identifiers and the supporting literature identifiers below were checked directly.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:221420` and native scientific-name object at `data/catalog/ncbi_names-0005.jsonl.gz:30772` agree on this target without additional synonyms.

All ten root-first ancestor entries agree by identifier, label and rank, including Bacillati, Mycoplasmatota, Mollicutes, Acholeplasmatales, Acholeplasmataceae, Candidatus Phytoplasma and the SPECIES_GROUP entry 16SrI (Aster yellows group). Live NCBI Taxonomy EFetch and Datasets responses independently confirm the label, species rank, parent 3042590, code 11 and lineage. The code is supported directly; no alternative translation code was inferred from the broader Mollicutes classification. [Official taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034066&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034066).

EXACT denotes correspondence with NCBITaxon:1034066. SPECIES is the NCBI rank, not a claim of valid nomenclatural publication. The name is not evidence of an exclusively Chinese geographic range. The record correctly makes neither a species-wide disease mechanism claim nor an exact identity mapping to Candidatus Phytoplasma asteris.

## Evidence

The sole NCBI NAME attestation matches the identifier, label, count, unit and September 13 snapshot note. Exact Nuccore search `txid1034066[Organism:noexp]` returned four records. All four complete metadata objects, references and feature qualifiers were read; sequence bases and translations were not reanalyzed.

| Accession | Source designation | Length | Source scope and qualification |
|---|---|---:|---|
| HQ599228.1 | CN-171 | 1804 bases | Partial 16S and 23S with intervening spacer/tRNA; host potato, geographic qualifier China, taxon:1034066. |
| HQ599229.1 | CN-171rp | 1245 bases | Ribosomal-protein region; explicitly UNVERIFIED because GenBank could not verify submitted sequence and/or annotation. |
| HQ599230.1 | CN-171B | 1452 bases | Partial 16S/spacer record; host potato, taxon:1034066; direct submission rather than a publication assignment. |
| HQ599231.1 | AK-DB7 | 1462 bases | Partial 16S/spacer record; host potato, taxon:1034066; linked to the Alaska report below. |

These are source sequence records, not four genome assemblies, culture deposits or necessarily four distinct biological strains. [HQ599228.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ599228.1), [HQ599229.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ599229.1), [HQ599230.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ599230.1), [HQ599231.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ599231.1).

- PMID:30731898 and DOI:10.1094/PDIS-12-10-0914 were verified through full PubMed metadata and abstract text. The 2011 Plant Disease report explicitly links HQ599228 to sampled potatoes in China and reports a 16SrI-B classification. It supports the source identity context and the broader 16SrI placement, without establishing that all Chinese potato phytoplasmas belong to this entity. [China primary report](https://pubmed.ncbi.nlm.nih.gov/30731898/).
- PMID:30731938 and DOI:10.1094/PDIS-12-10-0913 were independently verified through PubMed metadata and abstract text. The 2011 report explicitly links HQ599231 to a potato-associated phytoplasma detected in Alaska and assigns 16SrI-B. Thus the target's current NCBI sequence membership includes an Alaska-associated record despite the taxon label. That is source context, not a contradictory YAML geographic assertion. [Alaska primary report](https://pubmed.ncbi.nlm.nih.gov/30731938/).
- Both primary reports use molecular association/classification evidence. The review does not turn these into demonstrated mechanisms, transmission pathways, whole-genome equivalence or a nomenclatural synonym.
- Exact NCBI Assembly query returned zero items with a no-items/phrase-not-found diagnostic. This is a bounded exact-taxonomy result, not proof that no related genome exists elsewhere.
- `data/taxa/PATHS.tsv:13881` and `curation/seed_scope.tsv:321738` agree on the slug, September 13 admission and one-source rationale. The inline event matches those inputs without implying a prior review.

## Completeness

Full mapped-inventory scans found no exact target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits rows. No descendant strains need to be gathered. Zero inventoried BacDive strains does not contradict the bare strain designations found in nucleotide submissions; those designations are not BacDive or registered culture-deposit identities.

The ignored-inclusive, hidden-file-inclusive and compressed-file-aware identifier/name/slug search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, excluding only `SOURCE.json` descriptors. All three matching contexts were inspected: backbone, native name and scope. A second search for HQ599228-HQ599231 and the CN-171/CN-171B/CN-171rp/AK-DB7 designations found no matching rows in those roots.

No eligible deposit, supported strain/genome crosswalk, taxonomy mapping or missing required overlay was established. Optional marker/literature enrichment could retain the four records and their differing qualifications, but must not fabricate a strain entry or infer a Candidatus Phytoplasma asteris exact synonym from molecular similarity alone. The YAML makes no gene-function or transcriptomic assertion; iModulonDB is not applicable to this identity-only review.

Ignored-inclusive report/history searches found no previous target review or external history. General potato-phytoplasma reviews and regulatory search results were leads, not evidence used to assign this target another ribosomal group or regulatory status.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The seeded identity, lineage, source counts and provenance are supported. The externally observed UNVERIFIED annotation and mixed geographic associations limit future enrichment but contradict no represented YAML claim.

## Recommended Edits

None required. Do not hand-edit the generated YAML or promote SEEDED status.

If later adding literature or sequence context, use an explicitly maintained evidence input and a tested seeding path under separately authorized curation. Preserve each exact accession/designation, retain the UNVERIFIED qualification, and do not interpret the target label as a geographic restriction. Backbone corrections belong to the pinned NCBI extraction feeding `data/raw/ncbitaxon_taxa.tsv`; scope changes belong in `curation/seed_scope.tsv`.

## Follow-up Checks

- After authorized changes, rerun the focused schema and strict validators plus the complete target/source comparison.
- Run `just verify-corpus` separately before claiming corpus-wide reproducibility.
- Recheck HQ599229's authority status before reusing its annotations. The record currently does not assert that its sequence or proteins are verified.
- Preserve the explicit HQ599228/China and HQ599231/Alaska publication links. Do not silently merge the source designations or transfer study-specific results across all members.
- Inspect publisher full text if future claims require evidence beyond the PubMed abstracts; no such additional biological claim was made here.

## Additional Notes

The taxonomy-browser page was unavailable through the web tool. Official NCBI taxonomy and sequence APIs succeeded. Both publisher pages returned 403, and PubMed HTML routes presented browser checks; the official PubMed EFetch API supplied the complete metadata and abstracts for both primary reports. No unavailable page is presented as inspected full text.

This review checked one resolved taxon, not all potato pathogens, sequence quality by independent analysis, regulatory requirements or disease mechanisms. No paid research, source refresh, regeneration, history append, status promotion or GitHub mutation occurred. Only this timestamped report was written.

