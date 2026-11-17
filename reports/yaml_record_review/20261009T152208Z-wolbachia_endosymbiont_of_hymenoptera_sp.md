# YAML Record Review: Wolbachia endosymbiont of Hymenoptera sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_hymenoptera_sp.yaml`
- Started UTC: 2026-10-09T15:19:05Z
- Finished UTC: 2026-10-09T15:22:08Z
- Verdict: pass

## Target

This independent review resolves one generated `TaxonRecord`, `NCBITaxon:1036783`, and reads its entire YAML. It carries rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676` (unclassified Wolbachia), genetic code 11, grounding `EXACT`, mapping status `SEEDED`, 16 synonyms, zero inventoried strains and one NCBITAXON name attestation.

The ignored-inclusive target/report inventory found this exact YAML and no prior own report. SHA-256: `4d4910de825a8a03189cdb2afe2fa8f44e993d1e8f6da276e8b117f9084c58ee`. The subject is the bacterial source-taxonomy node, not the eukaryotic host order.

## Validation

Commands used the existing offline environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/wolbachia_endosymbiont_of_hymenoptera_sp.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/wolbachia_endosymbiont_of_hymenoptera_sp.yaml --workers 1 --out /private/tmp/taxonmech-whym-20261009-validation.tsv`: passed, one file and zero errors; the inspected TSV contains only its header.
- `uv run --offline python scripts/validate_history.py history` passed earlier in this turn, with 17 valid records and zero invalid links. History was not modified; this target's external history absence and own seeding event were checked independently.
- Read-only own-row comparisons passed for identity, all 11 lineage entries, attestation, PATHS/scope and event wording. A separate complete structural comparison confirmed equality of all 16 source/text/scope synonym assertions.
- Not checked: full-corpus reproduction, schema, provenance/QC/tests and generated-site drift were not rerun. The documented `just verify-corpus` command has no single-record selector. The bounded comparisons do not certify corpus reproduction.
- Not applicable: OAK graph-node checks and iModulonDB gene/component checks. The YAML carries no curator-added graph or gene, pathway, phenotype or transcriptomics assertion. External marker examples below do not add such claims.
- Live NCBI EFetch and Datasets taxonomy responses were accessible and fully inspected. The browser page failed through the web tool; it was not treated as an identity failure.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222623` supports the current identity, rank, parent, genetic code, all source synonyms and the sole source attestation. The 17 native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:32201` through row 32217 were read completely.

Live [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036783&retmode=xml) confirms the label, rank, genetic code and parent; [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036783) independently agrees. The carried root-first chain is root 1; cellular organisms 131567; Bacteria 2; Pseudomonadati 3379134; Pseudomonadota 1224; Alphaproteobacteria 28211; Rickettsiales 766; Anaplasmataceae 942; Wolbachieae 952; Wolbachia 953; unclassified Wolbachia 2640676. Every ID, label, rank and parent edge matches the source backbone; the live response confirms the same lineage.

The exact synonyms are `Wolbachia endosymbiont of Hymenoptera` and `Wolbachia sp. Hymenoptera`. Both are NCBI `synonym` names. The 14 `Wolbachia sp. Hymenoptera_ASGLE...` names are NCBI `includes` names, correctly mapped to `RELATED_SYNONYM`, not exact synonyms. Their complete suffix set is 1047-10, 1440-10, 1478-10, 1705-10, 1746-10, 402-10, 529-10, 558-10, 589-10, 646-10, 648-10, 881-10, 935-10 and 943-10. The live EFetch response confirms every one.

Neither the species-rank node nor its exact synonyms establishes a formal named species, type strain, host-species identity or equivalence among all Wolbachia infecting Hymenoptera. The record retains source taxonomy without adding these stronger interpretations.

## Evidence

The one name attestation is directly supported by the own backbone row and its 2026-09-13 snapshot. One attested name is not a total count of aliases, strains or nucleotide accessions. The 16 synonyms do not require changing `assertion_count: 1`.

A live exact, non-expanded NCBI query for `txid1036783[Organism:noexp]` returned a count of 295 nucleotide records and the first 100 IDs. This review does not claim to have fetched or validated all 295. The live [genome dataset query](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/taxon/1036783/dataset_report) returned an empty object. Those are bounded query observations, not proof of universal assembly absence or a requirement to create 295 strain objects.

Two source-specific nucleotide examples were fully inspected, including metadata, features, references and sequence-length/alphabet checks:

- [JN625801.1](https://www.ncbi.nlm.nih.gov/nuccore/JN625801.1), returned by the exact-taxon plus ASGLE1047-10 query, is a 641-base partial COI record. It explicitly names taxon 1036783, host `Hymenoptera sp. ASGLE1047-10`, specimen voucher `ASGLE1047-10.w` and BOLD cross-reference `ASWSB084-11.COI-5P`. Its source records Ontario, Canada, collection on 2010-07-25 and translation table 11. This directly corroborates one specimen-associated includes name; the other includes names were verified at the taxonomy authority, not inferred from this sequence.
- [MN594762.1](https://www.ncbi.nlm.nih.gov/nuccore/MN594762.1), the first ID in the returned nucleotide page, is a 423-base partial fbpA record, isolate WEVG_343, taxon 1036783, host Hymenoptera sp., with source locality Punjab, India, collection in October 2015 and translation table 11. It is a direct sequence submission, not an eligible culture-collection accession or a genome assembly.

Both lengths agree with their sequence content, and both sequences contain A/C/G/T only. These examples establish marker and source-association context, not functional validation, a whole-genome inventory, equivalent strains or evidence that the broad source node is biologically homogeneous. The YAML does not make those claims.

JN625801's reference names the Smith DNA-barcoding manuscript as unpublished. The [publisher's primary barcoding study](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514), inspected in this turn, provides context for bacterial COI recovered during insect barcoding. No specimen-specific phenotype or supplementary-table claim was derived from it for this target. The YAML itself has no publication-dependent biological assertion.

The local catalog search returned one incidental assembly hit at `data/catalog/ncbi_genbank-0062.jsonl.gz:7070`. Its complete row is `GCA_963529385.1`, uncultured Selenomonas sp., taxon 159275, a 128-contig metagenome-derived assembly. The apparent match is its genome length, 1,036,783 bp, not its taxon. It supplies no Wolbachia genome relationship and is correctly absent from the YAML.

## Completeness

The first gitignore-independent search included hidden and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It used the bounded taxon ID, both label patterns and all 14 ASGLE designations, yielding 20 rows: backbone, scope, 17 names and the unrelated genome-length match. Every row was read fully. All five source `SOURCE.json` files were parsed for matching metadata.

An additional ignored-inclusive compressed-content search for JN625801, MN594762, ASWSB084 and WEVG_343 found no local source candidates in those roots. Independent ignored-inclusive history content and filename searches found no target history item. These are bounded local findings; no claim is made that the marker records are absent from external databases.

Complete relevant inventory scans found no own BacDive strain, LPSN name, GTDB mapping, GOLD/MediaDive/Madin/BactoTraits assertion, type material, merged-ID row, dropped row or child node. The inspected source catalogs supply no eligible own culture/genome/sample/deposit association. Zero inventoried strains is therefore consistent with the available BacDive inventory even though NCBI has specimen and isolate-associated nucleotide records.

Optional formal nomenclature, taxonomy mappings, xrefs, strains, genomes, phenotype evidence and causal graph slots are correctly unpopulated. No includes name should be converted into a culture deposit simply to populate those fields.

`data/taxa/PATHS.tsv:15151` owns the exact slug. `curation/seed_scope.tsv:322856` supplies the 2026-09-13 one-source inclusion. The sole seeding event at 2026-09-13T17:54:04Z exactly matches source/scope-generated text and remains `SEEDED`, with no fabricated human review status.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the reviewed YAML and inspected sources. The two marker checks are supplementary evidence, not a claimed audit of every nucleotide assigned to this source taxon.

## Recommended Edits

None required. Preserve the exact-versus-related synonym distinction and source-taxonomy scope. Do not add the unrelated Selenomonas assembly, treat ASGLE specimen identifiers or WEVG_343 as validated culture deposits, or infer genome equivalence from this shared taxonomy ID.

Any future authorized change belongs in the maintained source inventory/extraction, seeder or scope owner, followed by regeneration, not a manual edit to this generated YAML.

## Follow-up Checks

Before later authorized regeneration, run the documented full-corpus reproduction, provenance, strict-schema, tests and publication gates. If nucleotide enrichment becomes an explicit curation task, retrieve and inspect the complete accession set with specimen-level provenance; the count and two examples in this report do not establish complete sequence coverage.

## Additional Notes

Only this new report was written for this target. No data record, source snapshot, scope/history entry, generated product, branch, worktree or GitHub item was modified. Eukaryota remains fully covered and outside this review queue. No paid research was performed.

