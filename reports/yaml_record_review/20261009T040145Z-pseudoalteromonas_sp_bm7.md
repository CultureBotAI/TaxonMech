# YAML Record Review: Pseudoalteromonas sp. BM7

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoalteromonas_sp_bm7.yaml`
- Started UTC: 2026-10-09T03:56:48Z
- Finished UTC: 2026-10-09T04:01:45Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1036584`: species rank, Bacteria, parent `NCBITaxon:194690`, ten root-first ancestors, code 11, `EXACT` grounding and `SEEDED` status. It has zero represented BacDive strains, one NCBITAXON name attestation and one seed event dated 2026-09-13T17:54:04Z. Optional synonyms, nomenclature, mappings, strain/genome links, evidence and graphs are unasserted.

Ignored-inclusive filename inventory of `data/taxa`, `reports/yaml_record_review` and `history` resolved one target YAML and no prior target report. Generated YAML is not the maintained correction surface.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pseudoalteromonas_sp_bm7.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/pseudoalteromonas_sp_bm7.yaml --out /private/tmp/taxonmech-bm7-review-strict.tsv`: passed, one file and zero errors; complete TSV was header-only.
- Structured comparisons matched backbone, all ancestors, attestation, PATHS, scope and seed wording. Seven supplementary raw inventories plus type-material, merged-ID and dropped tables were scanned for exact target identifiers.
- Own marker consistency passed: declared/actual length 1058, submitted rRNA transcription equals DNA and no non-ACGT symbols. This checks annotation, not independent alignment or species assignment.

Not checked: `just verify-corpus`, full-corpus schema/provenance/history gates, full tests, `just qc`, vendored synchronization, site drift and publication builds. Individual checks do not prove corpus reproduction. Embedded history was inspected; ignored-inclusive searches found no separate target history artifact. Graph-product validation is inapplicable without nodes.

## Identity and Grounding

Complete [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036584&retmode=xml) and [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036584) agree with identifier, label, rank, parent, code and lineage. Datasets confirms all ten root-first ancestor IDs; EFetch supplies matching labels/ranks while omitting root from its displayed chain.

The chain includes Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Alteromonadales, Pseudoalteromonadaceae, Pseudoalteromonas and unclassified Pseudoalteromonas. EFetch has no other names; pinned synonym fields are empty. Exact pinned scans found no type-material, merged-ID or dropped row and no backbone children. Species rank for an unnamed strain-associated concept does not establish formal nomenclatural standing. Exact grounding does not equate different BM7 labels or nearby species.

## Evidence

Complete own rows inspected:

- `data/raw/ncbitaxon_taxa.tsv:222538`: identity, rank, parent, code, empty synonyms and 2026-09-13 snapshot.
- `data/catalog/ncbi_names-0005.jsonl.gz:32082`: scientific-name object with empty unique name.
- `data/taxa/PATHS.tsv:15047`: identifier/slug.
- `curation/seed_scope.tsv:322785`: admission date/reason matching the seed event.

One `NAME` attestation counts a source name, not an experiment or genome. Exact raw scans returned no target BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits row. `strain_count: 0` counts represented BacDive entries, not all externally described strains.

Exact Nuccore query `txid1036584[Organism:noexp]` returned only UID 219819358. Complete [EU939694.1](https://www.ncbi.nlm.nih.gov/nuccore/EU939694.1) XML was read, including references, every feature and sequence. This 1058-base partial 16S marker has both feature-end partial flags. Eight source qualifiers identify the organism, genomic DNA, strain BM7, a sea-anemone host, taxon 1036584, Weihai in Shandong Province, coordinates 37.5348 N 122.0507 E and PCR primers. Only source and rRNA features occur, without a deposit or genome qualifier. The marker cites an unpublished study by Zhang, Xia and Du and a 31-JUL-2008 direct submission from Shandong University at Weihai. Host and locality are explicit qualifiers here, not deductions from the title or submitter's address.

The [publisher record](https://link.springer.com/article/10.1007/s13131-010-0023-1) verifies Du et al.'s 2010 paper, DOI 10.1007/s13131-010-0023-1. The [author-uploaded full text](https://www.researchgate.net/publication/225606700_Isolation_and_diversity_analysis_of_heterotrophic_bacteria_associated_with_sea_anemones) was inspected after an initial retrieval failure. Table 1 explicitly pairs BM7 with EU939694, reporting 99.59% similarity to Pseudoalteromonas sp. MB6-05 and 99.50% to P. haloplanktis; neither value establishes exact species or strain identity. Methods identify BM isolates as surface-associated and the sampled host as Anthopleura midori. Table 2 records BM7's proteolytic clearing/colony ratio as 2.13 and its lipolytic test as negative under the reported assays, not a universal phenotype. Antibacterial results highlighted for NQ8 must not be transferred to BM7. The paper's study coordinates, 37.5331 N 122.0619 E, differ from GenBank's strain coordinates; preserve this unresolved precision discrepancy in any future habitat curation. Current YAML asserts neither coordinates nor assay results.

## Completeness

Complete enough for supported taxonomy-seed claims. Optional nomenclature, deposits, genome links and graphs are appropriately unasserted without explicit identity/evidence chains. Verified strain-level literature is an optional enrichment opportunity, not a missing required slot.

Gitignore-independent `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial terms included word-bounded taxid 1036584, label/slug and BM7 with optional hyphen, space or underscore. Expansion added EU939694 and word-bounded UID 219819358. Both searches returned the same 37 rows: three own taxonomy/name/scope rows and 34 excluded candidates. Every candidate row was read completely in native structured form, including common fields and lossless per-row differences. Five SOURCE.json files were fully parsed for each term set without matches; history filenames were independently inventoried.

Excluded candidates comprised:

- Backbone, scientific-name and scope rows for Paenibacillus sp. BM-7 (283468), Burkholderia sp. BM7 (869633) and bacterium BM7 (1729921).
- Mangrovibacterium lignilyticum BM_7 (2668052), including its former-name entry, type-material rows, BacDive 166997, culture identifiers, GCA/GCF_010882175.1, BV-BRC 2668052.3 and IMG 2920171302. GOLD Go0566921 links through Gp0537282 to Ga0477967, with PRJNA589180 and SAMN13269095. These records describe a different genus, deposit chain and assembly, not this Pseudoalteromonas strain.
- Burkholderia mallei BM-7 (13373), GCA/GCF_028621495.1 and BV-BRC 13373.188, and Brucella melitensis BM_7 (29459), GCA/GCF_047612995.1 and BV-BRC 29459.1484. Their native NCBI, GTDB and BV-BRC metadata explicitly identify different organisms.
- GCA_015873645.1, Salmonella enterica serovar Enteritidis strain 1036584 (149539), where the numeric strain label is not the target NCBI taxid.

`BM7[All Fields] AND Pseudoalteromonas[Organism]` returned only the own marker. Its translation stack counted 203 unfiltered BM7 hits; those cross-organism results were not exhaustively audited. Exact non-expanded Assembly search returned zero with missing-phrase/no-items diagnostics. PubMed `BM7[All Fields] AND Pseudoalteromonas[All Fields]` returned zero without dropping BM7, and `EU939694[All Fields]` returned zero with missing-phrase diagnostics. These index misses do not negate the independently inspected exact accession in the 2010 publication.

iModulonDB was not run: no gene, regulator or expression claim is asserted and no applicable strain/dataset was identified. This is not negative database evidence. All absence statements are bounded to the stated roots, terms and indexes.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in stored claims. Identity, lineage, scope and provenance agree with pinned and live authorities. The external coordinate discrepancy is an enrichment caution, not an inconsistency in this taxonomy-only YAML. No namesake genome, nearest-neighbor identity or other isolate's phenotype has been imported.

## Recommended Edits

None required. Preserve generated YAML and `SEEDED` status. Future taxonomy corrections belong first at NCBI, then pinned inputs governed by `conf/ncbi_taxdump.yaml` and `src/taxonmech/ncbi_taxdump.py`. Projection fixes belong in `src/taxonmech/seed.py` with tests; scope changes belong in `curation/seed_scope.tsv`. Never join on the bare BM7 label or a numeric strain designation.

## Follow-up Checks

No corrective follow-up is needed for current claims. Optional enrichment should retain the explicit accession link, assay scope and unresolved source differences rather than selecting the convenient source value. Finer taxonomy requires authoritative review, not similarity-based relabeling. The full-text HTML transcription was inspected; no PDF/figure visual verification, independent alignment, complete experiment audit or genome comparison is claimed.

After an authorized input/seeder change, run focused tests, `just seed-canary NCBITaxon:1036584`, inspect output, rerun both individual validators and `just verify-corpus`, then full publication QC. No regeneration ran.

## Additional Notes

The local review skill and checklist governed this independent review. Complete YAML, own source rows, all local candidates, live taxonomy, the own marker, publisher metadata and author-provided primary methods/tables were inspected. No neighboring accession or verdict was inherited. Springer exposed an abstract/metadata preview, while the author upload supplied the inspected detailed text; no paywall was bypassed and no purchase was made.

Before/after YAML SHA-256: `ba62138de522bc7cd80a7f55f5d9df883d9d8bf2cb2533052d8ea11809897f69`. Only this new report was written for the target. This review did not modify YAML, sources, history, status, pages, GitHub objects, Eukaryota or worktrees.
