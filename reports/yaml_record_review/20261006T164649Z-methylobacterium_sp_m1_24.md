# YAML Record Review: Methylobacterium sp. M1-24

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_m1_24.yaml`
- Started UTC: 2026-10-06T16:44:02Z
- Finished UTC: 2026-10-06T16:46:49Z
- Verdict: pass

## Target

The complete generated `TaxonRecord` denotes `NCBITaxon:1035226`, Methylobacterium sp. M1-24: rank SPECIES, domain BACTERIA, parent `NCBITaxon:2615210`, genetic code 11, grounding EXACT, mapping status SEEDED. It contains ten root-first ancestors, `strain_count: 0`, one NCBITAXON NAME attestation, and one seed event. It has no synonyms, xrefs, nomenclature, taxonomy mappings, strain entries, genome links, definition, literature evidence, phenotype claims, or causal graphs.

The unique identifier/slug association is `data/taxa/PATHS.tsv:14438`; the scope row is `curation/seed_scope.tsv:322222`. Generated fields are owned by maintained extraction/seeding inputs, not hand-edited YAML. The verified repository revision is recorded under Additional Notes.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline project dependencies.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_m1_24.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_m1_24.yaml --out /private/tmp/mm124-strict.tsv`: exit 0; one file scanned, zero ERROR rows. The actual TSV was read and contains only its header.
- Bounded structured comparisons of the target, every ancestor, scope, path lock, attestation and event text against pinned inputs passed. These manual comparisons are not a replacement for corpus reproduction.
- `just verify-corpus`, full-corpus strict validation, `just qc`, provenance/test/site gates, and global `just validate-history` were not run for this individual read-only review. Corpus reproducibility and global reference integrity therefore remain unproven here.
- `just validate-products` was not run: its configured OAK target is curator-added graph grounding, absent here; `conf/id_label_targets.yaml` explicitly excludes NCBITaxon from OAK resolution. Taxonomic identifiers were checked against pinned and live NCBI instead.
- No target-specific external history artifact was found in the ignored-inclusive searches below, so no focused history file was available to validate. No history entry or status promotion was made.
- The required structured adapter was run before web follow-up: `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. All 28 returned dataset rows were inspected; none covers Methylobacterium or Methylorubrum. Not applicable, not evidence against a trait.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221947` supplies the exact label, species rank, parent, code 11, empty synonym fields, and 2026-09-13 snapshot. `data/catalog/ncbi_names-0005.jsonl.gz:31415` independently retains the scientific-name row for this taxid. Neither the exact type-material, merged-ID, nor dropped-record table scan yielded a target row.

Current [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035226&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035226) were fully inspected and agree with identity and placement. The ten stored ancestors are root (1), cellular organisms (131567), Bacteria (2), Pseudomonadati (3379134), Pseudomonadota (1224), Alphaproteobacteria (28211), Hyphomicrobiales (356), Methylobacteriaceae (119045), Methylobacterium (407), and unclassified Methylobacterium (2615210), with the stored labels and ranks matching the pinned chain. NCBI XML omits root from LineageEx; Datasets includes it.

EXACT describes grounding to this NCBI taxon, not a validly published binomial or type-strain designation. The inspected [LPSN genus record](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, supplies genus context but no M1-24 identity or deposit bridge. Genus-level nomenclature and properties must not be copied to this isolate-labelled taxon. The legacy NCBI taxonomy browser was inaccessible through the web tool; the two authority APIs above succeeded.

## Evidence

The NCBITAXON attestation exactly matches its source identifier, label, count 1, unit NAME, and snapshot date. This is one source-name assertion, not a genome or strain count. The 2026-09-13T17:54:04Z `seed_from_sources` / SEEDED_FROM_SOURCES event text matches the scope reason and one-source inventory.

Exact taxon scans of `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv`, and `bactotraits_taxa.tsv` returned no rows. The backbone has no direct children under this target. Thus zero inventoried BacDive strains and empty optional source-derived slots are consistent; zero is not a claim that no isolate was cultured.

The exact live NCBI query `txid1035226[Organism:noexp]` returned zero assembly records, including the API's phrases-not-found/no-items diagnostics, and one nucleotide UID, 347300723. The full [FR869822.1 sequence metadata](https://www.ncbi.nlm.nih.gov/nuccore/FR869822.1) was inspected, excluding only nucleotide bases: a 1335-nt partial 16S rRNA gene, strain M1-24, explicit `taxon:1035226`, host Trifolium repens, and isolation source host leaf surface. It was submitted 18 May 2011, created 18 September, and updated 6 December 2011. Its metadata supplies no culture-collection accession, BioSample, BioProject, or assembly identifier. Genomic DNA is the molecule source, not evidence that this partial marker is a genome assembly.

The sequence explicitly cites [PMID 22000032](https://pubmed.ncbi.nlm.nih.gov/22000032/) and [DOI 10.1016/j.syapm.2011.08.005](https://doi.org/10.1016/j.syapm.2011.08.005). The live PubMed bibliography and complete abstract were read. They concern phyllosphere communities across two host species, locations, and land-use conditions, not named M1-24-specific phenotype or growth measurements. The isolate's host association comes from its sequence metadata; community-level results and institutional address do not establish its specific collection locality or phenotype. Full text and supplements were not inspected.

## Completeness

An ignored- and compression-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The exact taxid, scientific label and slug search returned nine rows; all candidate rows were fully read. Three are genuine taxonomy/scope/name rows. Six are unrelated numeric matches, detailed below. Source metadata excluded from the text search was separately parsed across all five discovered `SOURCE.json` files; it yielded no target match. Ignored-independent history filename enumeration yielded no target artifact.

A second search across the same roots used `(Methylobacterium|Methylorubrum).*\bM[- _]?1[- _]?24\b|\bM[- _]?1[- _]?24\b.*(Methylobacterium|Methylorubrum)`. It returned only the same three genuine rows. Spacing/spelling variants were search leads, not asserted aliases. A follow-up accession search for FR869822 returned no rows in those roots. These are bounded local-catalog results, not claims of universal database absence.

The repository's `normalize_culture_identifier` returned an empty key for M1-24, M1 24, and M124. No eligible culture-deposit or strain identity bridge was established. There is consequently no supported missing strain-to-genome association under the current join rules. The external marker is useful optional identity evidence, but does not justify creating a BacDive strain, genome link, nomenclatural synonym, or required strain-level related record without the owning strain/deposit evidence. Optional definition, evidence, and causal-graph fields need not be invented.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the inspected record. Pass is scoped to the assertions and bounded completeness checks above; it does not certify unrun corpus gates or undiscovered external evidence.

## Recommended Edits

None required. Leave the generated YAML and SEEDED status unchanged.

If later evidence establishes an eligible own-deposit or supported strain/genome chain, update the maintained source extraction or matching logic under `src/taxonmech/`, with regression coverage, and regenerate through the documented extraction/seeding workflow. Scope changes belong in `curation/seed_scope.tsv`; upstream source-mapping corrections belong in kg-microbe. Never patch `data/taxa/` or generated pages to add an inferred link.

## Follow-up Checks

Before any future link addition, inspect the entire authority source row and the target's own culture deposit. Retain the distinction between taxon, strain, deposit, sample, project, marker and assembly. For StrainInfo, require the sequence's explicit link to that same eligible SI-DP; for GOLD, require an unambiguous organism/project/analysis chain; for ATB, require existing exact BioSample evidence and an eligible available FASTA, without treating a shared sample as genome equivalence.

After an authorized maintained-input change, run the target schema and strict checks, relevant join regression tests, then `just verify-corpus` and `just qc`. Any future isolate-specific literature claim requires inspecting its actual full-text or supplementary evidence.

## Additional Notes

- Verified HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Existing review branch/worktree was retained after the parallel session closed.
- Four excluded catalog rows describe Intestinibacter bartlettii, taxid 261299, strain 2201st1_B3_2201SCRN_220225: GCA/GCF_040925295.1, BV-BRC 261299.152, BioSample SAMN41035226. They occur at `data/bvbrc/bvbrc-0015.jsonl.gz:1626`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20869`, `data/catalog/ncbi_refseq-0006.jsonl.gz:20015`, and `data/catalog/gtdb_genomes-0002.jsonl.gz:23719`. The shared digit substring is not the reviewed taxid.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6252` is Mycobacterium tuberculosis taxid 1773, genome 1773.18446, strain/run label ERR1035226, not M1-24.
- `data/catalog/allthebacteria.tsv.xz:569696` is Mycobacterium tuberculosis, run ERR1035226, BioSample SAMEA3558759, analysis ERZ3502562. Its available FASTA and PASS filters do not bridge the conflicting identity.
- Native candidate rows were losslessly read, including all source fields; no genome or sample was transferred from these numeric collisions.
- The target's bytes were re-read and remained unchanged before reporting. Only this new review report was written; no YAML, history, status, generated product, Git or GitHub state was mutated.

