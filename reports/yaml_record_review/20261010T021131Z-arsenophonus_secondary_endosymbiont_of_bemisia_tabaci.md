# YAML Record Review: Arsenophonus secondary endosymbiont of Bemisia tabaci

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/arsenophonus_secondary_endosymbiont_of_bemisia_tabaci.yaml`
- Started UTC: 2026-10-10T02:09:07Z
- Finished UTC: 2026-10-10T02:11:31Z
- Verdict: pass

## Target

The entire 54-line generated `TaxonRecord` was read. `NCBITaxon:1037383` denotes Arsenophonus secondary endosymbiont of Bemisia tabaci, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2627083`, genetic code 11, grounding `EXACT`, status `SEEDED`.

It contains ten ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It is the bacterial taxon, not its eukaryotic host. No host YAML was opened.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/arsenophonus_secondary_endosymbiont_of_bemisia_tabaci.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/arsenophonus_secondary_endosymbiont_of_bemisia_tabaci.yaml --out /private/tmp/taxonmech-arsenophonus-bemisia-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified own identity, full lineage, genetic code, empty synonym columns, source inventories, unique index/scope resolution and exact seed reason. Complete backbone scanning found no immediate child; own type-material, merged-ID and dropped inventories had no rows.
- Complete native NCBI name and ATB candidate rows were read. Four live exact-taxonomy nucleotide records were inspected with complete annotation metadata, sequence lengths, alphabets and hashes.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering and publication gates. There is no graph to which `just validate-products` applies. Focused agreement does not establish corpus reproduction.
- The NCBI taxonomy browser page was unavailable through the web reader; live EFetch and Datasets taxonomy APIs succeeded. No phylogenetic reanalysis, microscopy, experimental host-association validation or independent mechanism assessment was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222739`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037383&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037383) agree on the full label, species rank, parent and code.

All stored ancestor IDs, labels and ranks match the backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Enterobacterales, Morganellaceae, Arsenophonus and unclassified Arsenophonus. EFetch verifies the chain below root; Datasets includes root 1. The unclassified parent is deliberately retained at `NO_RANK`, not replaced with the genus.

The complete native name row `data/catalog/ncbi_names-0005.jsonl.gz:32370` is a scientific name with no unique-name qualifier. Live taxonomy supplies no alternate names. NCBI's species rank and this informal host-associated label do not establish a validly published ICNP species name, a cultured type strain or exact equivalence to every Arsenophonus associated with the host.

`EXACT` describes grounding to this NCBI identifier, not a claim of experimental certainty about endosymbiosis. The sole attestation is correctly one NAME from the 2026-09-13 NCBI snapshot.

## Evidence

The live NCBI nucleotide query `txid1037383[Organism:exp]` returned four records, all inspected. Each source annotation explicitly names this taxon and Bemisia tabaci as host:

| Accession | Length | Annotated context |
| --- | --- | --- |
| [JQ305709.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ305709.1) | 480 bases | Kurigram, Bangladesh; okra isolation source; indigenous Bangladesh whitefly 2 |
| [JQ305708.1](https://www.ncbi.nlm.nih.gov/nuccore/JQ305708.1) | 480 bases | Kurigram, Bangladesh; eggplant isolation source; indigenous Bangladesh whitefly 2 |
| [JN018061.1](https://www.ncbi.nlm.nih.gov/nuccore/JN018061.1) | 453 bases | Patuakhali, Bangladesh; brinjal isolation source; non B/Q note |
| [JN018060.1](https://www.ncbi.nlm.nih.gov/nuccore/JN018060.1) | 487 bases | Patuakhali, Bangladesh; bean isolation source; non B/Q note |

All four are partial 23S rRNA markers, not genomes. Declared and actual lengths agree and their alphabets contain only A/C/G/T. The two JQ records have identical sequence hashes but distinct source records; that does not prove identical biological isolates or justify merging their provenance.

Their references are unpublished studies and direct submissions by Jahan and Lee in 2011. No DOI or PMID is supplied in these inspected annotations, so none is invented. The source records support a bounded taxon/host annotation context; they do not establish a universal host range, inheritance pattern, cellular localization, ecological benefit or causal mechanism.

These accessions are review evidence, not existing YAML references or eligible BacDive/StrainInfo strain-genome joins. Their absence from the generated record is not a required-field defect. Preserve marker-versus-genome and source-record-versus-biological-isolate distinctions in any future curation.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, complete label and slug.

Four lines matched: the backbone, scope, native NCBI name and one ATB checksum collision. The complete ATB row `data/catalog/allthebacteria.tsv.xz:1499200` identifies Pasteurella multocida, sample SAMN10284280, run SRR8100121 and assembly ERZ25578581. The digits 1037383 occur only in its SeqKit checksum; this is not a genome link for the reviewed taxon.

Complete structured scans of the BacDive, LPSN, GTDB, GOLD, MediaDive, Madin and BactoTraits inventories found no own-taxonomy row. The source search supplied no own cultured-strain or genome link. Thus `strain_count: 0` describes inventory coverage, not absence of biological diversity or sequence evidence.

A second ignored-inclusive search across the same roots found no occurrence of JQ305708/JQ305709/JN018060/JN018061. Five SOURCE.json files were independently enumerated and parsed, with no target match. Gitignore-independent filename enumeration found the unique target YAML and no prior target report; history filenames had no target-specific match. These are bounded repository results, not claims of global source absence.

Optional nomenclature, mappings, synonyms, deposits, definitions, mechanistic evidence and graphs can remain empty. iModulonDB is not applicable to the taxonomy/name assertions here; partial ribosomal markers do not create a transcriptomic-module claim.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertion scope. Identity and full lineage agree with pinned and live NCBI taxonomy. The record does not overstate marker evidence, invent culture deposits, or promote the host-associated label to formal nomenclature.

## Recommended Edits

None required. Leave the generated YAML, seed status and curation history unchanged.

Any future enrichment should be separately authorized and owned by maintained source inventory, extraction or harmonization inputs before regeneration. Do not hand-add these markers as genomes, infer culture accessions from a host name, or merge this taxon with another host-associated Arsenophonus on label similarity.

## Follow-up Checks

For future biological enrichment, resolve each proposed host/mechanism claim to primary evidence and preserve the actual sampled isolate, host and experimental scope. Do not reinterpret the four sequence records as four genomes or four proven independent strains.

If maintained source inputs change, rerun the documented canary, schema/strict/history checks and full-corpus reproduction/QC gates. No curator action is required merely to retain the currently supported NCBI-only record.

## Additional Notes

- YAML SHA-256: `1dfa62f964926524471644163008c6764c923eda0e34b484b890a96c46c7bc6c`.
- `data/taxa/PATHS.tsv:15289` and `curation/seed_scope.tsv:322961` uniquely resolve the target. The seed retains 2026-09-13T17:54:04Z and its exact single-source reason.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, source input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
