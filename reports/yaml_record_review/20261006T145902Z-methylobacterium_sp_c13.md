# YAML Record Review: Methylobacterium sp. C13

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c13.yaml`
- Started UTC: 2026-10-06T14:56:07Z
- Finished UTC: 2026-10-06T14:59:02Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035200`, label `Methylobacterium sp. C13`, rank SPECIES, domain BACTERIA. The entire YAML was read before judging it and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with ten root-first ancestors, genetic code 11, zero listed BacDive strains, one NCBI source attestation and one inline seed event. It asserts no synonyms, xrefs, GTDB mappings, nomenclature, genome links, definition, publication citations, phenotype or causal graph. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c13.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c13.yaml --out /private/tmp/mc13-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: all identity and lineage fields, code, source count, scope and seed provenance agree with their pinned inputs. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology graph requires term validation. The documented product checker excludes taxonomy fields and delegates them to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope; no external history validator was run against an invented artifact.
- No DOI, PMID, evidence quotation or publication reference occurs in the YAML. The sequence-linked publication was checked as completeness context, not as evidence for a claim absent from this record.

## Identity and Grounding

Pinned backbone `data/raw/ncbitaxon_taxa.tsv:221921`, [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035200&retmode=xml), and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035200) agree on the label, SPECIES rank, bacterial domain, parent `NCBITaxon:2615210` and code 11. Both APIs were inspected in full. The XML contains no alternate names. The root-inclusive dataset lineage agrees with all ten record ancestors, and their labels/ranks match the pinned backbone.

The no-rank parent is explicitly `unclassified Methylobacterium`, below genus `NCBITaxon:407`. Carrying this node is correct under the repository's NCBI-lineage contract. The strain qualifier C13 on a sequence does not change NCBI's SPECIES rank for this taxon. EXACT means the record denotes the exact NCBI concept, not that its placeholder label is a validly published species name.

The inspected [LPSN genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, concerns Methylobacterium and identifies M. organophilum as its type species. It provides genus-level nomenclature, not a species identity, type-deposit assignment or formal name for C13. No genus nomenclature or neighboring named species was transferred to the record.

No descendants, exact type-material row, merged-ID row or dropped row were found in the inspected pinned tables. The legacy taxonomy browser route failed, but the two independent NCBI API responses supplied the identity and lineage evidence.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221921` supports the taxon identity, parent, rank, code, absence of aliases and NCBI-only source list.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31389` identifies the exact scientific name and taxid, with empty unique-name field.
- `data/taxa/PATHS.tsv:14412` resolves the record slug. `curation/seed_scope.tsv:322196` adds this identifier on 2026-09-13 for a one-source NCBI attestation. The 2026-09-13T17:54:04Z inline seed event agrees.
- The sole source attestation counts one NAME. It is not a genome, deposited-strain or phenotype count.

An exact-taxid NCBI Entrez search used `txid1035200[Organism:noexp]`. Assembly returned zero with the "No items found" / phrases-not-found diagnostic. This is a bounded no-hit result, not proof that no genome exists anywhere. Nuccore returned exactly one UID, 347300697; the returned count and complete ID list agreed.

Complete [GenBank metadata for FR869796.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869796.1) identifies a 1,335-nt partial 16S rRNA sequence, strain C13, and exact taxon 1035200. Its source qualifiers state host leaf surface and host Cerastium holosteoides. No culture-collection identifier, BioSample, BioProject or genome assembly occurs in this sequence metadata. Bases were omitted from the metadata inspection; all source/features/reference metadata were retained. A partial marker cannot be placed in a genome slot.

The sequence cites Wellner, Lodders and Kampfer, PMID 22000032, DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml) confirm the bibliographic pairing and a study of phyllosphere bacterial communities across two host plants and differing sites/land uses. The abstract does not identify C13 or establish a C13-specific growth, phenotype or geographical conclusion. Full text and supplements were not inspected; no such biological claim is introduced here.

## Completeness

Exact structured scans found no target row in the BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits transformed inventories. Ignored-inclusive searches for the taxid, label and slug found only backbone, scientific-name and scope records. An expanded search using FR869796, its UID, and C13/C-13 co-occurrence with Methylobacterium or Methylorubrum found the same three rows, with no additional source candidate.

These searches include native and compressed BacDive, BV-BRC, GOLD, StrainInfo, SeqCode, assembly/GTDB catalogs and the ATB catalog. Within this bounded identity search, no eligible culture-deposit, StrainInfo sequence-deposit or genome linkage was established. Absence here does not prove a universal absence of cultures or sequences.

Zero listed strains is consistent with `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: the seeder gathers BacDive strains filed at this taxon or descendants, and neither exists in the inspected pinned inputs. The real sequence's bare C13 designation is not an authority-qualified deposit key. No existing strain record or explicit SI-DP attribution was established to receive the optional marker sequence.

The omission of FR869796 and its publication is therefore not independently classified as a missing required representation under the current generated-record contract. The evidence is retained in this report for an authorized future enrichment. Identity, code, lineage and source provenance already cover the record's current assertions.

The structured `imodulondb datasets` adapter returned 28 datasets before open-ended web follow-up, with no covered Methylobacterium/Methylorubrum dataset. It is not applicable; absence is not negative biological evidence. Search leads concerning carbon-13 labeling, C13 peptidase families or similarly named isolates were not used as evidence about this strain. Optional definitions, phenotypes and causal graphs can remain empty.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and inspected source scope. The generated record makes restrained identity/provenance claims supported by pinned inputs and live NCBI metadata. The pass is not a whole-corpus reproducibility result or a validation of unasserted phenotype, nomenclatural status or genome quality.

## Recommended Edits

None required for the current record.

Any future enrichment should first establish explicit culture/source identity and the appropriate maintained input or importer. Preserve the marker as a typed non-genome sequence link only if an authorized model/import path supports it; do not fabricate an SI deposit, genome assembly or species equivalence. Such work belongs upstream of generated YAML, not in a manual edit of this file.

Do not promote mapping status to REVIEWED or append curation history merely because this read-only report passes.

## Follow-up Checks

- On the next source refresh, repeat the exact NCBI identity/lineage/status checks and this target's schema and strict commands.
- After any authorized source/import change, run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`. The bounded comparisons here do not replace them.
- Before introducing biological claims from PMID 22000032, inspect full text/supplements for an explicit C13-specific result. The abstract's community-level observations are insufficient.
- Require an evidenced whole-deposit key for any strain/genome join and preserve FR869796.1 as a partial marker, outside genome counts.
- Retry the unavailable browser routes if needed; inspected structured NCBI responses currently supply the bounded evidence. No record-level blocker remains.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial search found three candidates and the accession/context expansion found those same three. All three were read in full with structured native/TSV decoding. Separate exact scans covered backbone lineage/status, all transformed source tables, PATHS and scope. Five SOURCE.json files were searched structurally and history filenames separately checked. All absence findings state this bounded source scope and include ignored files.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. NCBI taxonomy/sequence/PubMed APIs and LPSN genus page were inspected. Taxonomy and nucleotide browser routes failed; the PubMed browser route returned a challenge page, so the successful structured PubMed response was used instead.

No YAML/code/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.

