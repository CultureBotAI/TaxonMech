# YAML Record Review: Pseudoduganella namucuonensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pseudoduganella_namucuonensis.yaml`
- Started UTC: 2026-10-07T09:12:02Z
- Finished UTC: 2026-10-07T09:24:59Z
- Verdict: pass with minor issues

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035707`, Pseudoduganella namucuonensis: rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1522432`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It contains one LPSN nomenclature entry, one GTDB mapping, six source-scoped synonyms, one GTDB xref, one BacDive strain, eight assembly assertions, seven other genome assertions, 22 related-record assertions, eight source attestations and one seed event.

The target is an NCBI taxon, not an LPSN name, culture deposit or assembly. YAML is generated and read-only. Harmonization wording belongs to `src/taxonmech/seed.py`; source-link changes belong to maintained extraction/overlay inputs, not this YAML. Scope and slug ownership remain `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`. No definition, causal graph, discussion, replacement or independent phenotype claim is asserted.

## Validation

Offline commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/pseudoduganella_namucuonensis.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/pseudoduganella_namucuonensis.yaml --out /private/tmp/namucuonensis-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/namucuonensis-strict.tsv` | Actual TSV inspected; header only. |
| Backbone, full lineage, scope/path, seven source inventories and attestations | Bounded comparisons passed. |
| Complete imported strain-link dictionary comparisons | Eight assembly, six non-ATB genome and 20 raw related assertions match; two StrainInfo related assertions match. |
| CAFI and ATB evidence comparisons | Both registered deposits match full templates; bare designation is ineligible; all ATB metadata and six sample links match. |
| Live NCBI, LPSN, BacDive, StrainInfo and ENA checks | Material identity/link assertions agree, with source-specific nomenclature and project differences described below. |
| Full target reread | Byte-identical to the initial read. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. The bounded comparisons are not byte-for-byte corpus reproduction.

`just validate-products` was not run: its configured OAK targets are curator-added graph nodes, absent here, and NCBI Taxonomy is excluded. Literature identifiers were manually checked below; no separate record-level evidence/internal-reference objects occur. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the stated scope.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222161` and native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31641` through 31645 agree with the identity and all four NCBI synonyms, preserving scientific-name, synonym, includes and authority distinctions. Unique path and scope rows are `data/taxa/PATHS.tsv:14661` and `curation/seed_scope.tsv:4046`.

All ten ancestors match the pinned parent chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Betaproteobacteria, Burkholderiales, Oxalobacteraceae, Telluria group and Pseudoduganella, including IDs, ranks and order. Live EFetch confirms identity, parent 1522432, species rank, code 11 and all non-root ancestors; Datasets includes root. The inspected backbone has no direct children or retired target mapping, and exact lifecycle scans found no merged/dropped target row. Six pinned type-material entries agree with the live source's spelling variants. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035707&retmode=xml), [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035707)

Three source classifications intentionally coexist. NCBI uses Pseudoduganella; LPSN prefers Massilia; pinned GTDB uses Rugamonas. GTDB additionally places the genome in Gammaproteobacteria and Burkholderiaceae_D, whereas NCBI carries Betaproteobacteria and Oxalobacteraceae. These disagreements do not authorize changing the NCBI lineage. The GTDB species mapping is a close match, not a claim of identical higher classification or genome equivalence.

## Evidence

**Nomenclature and literature.** `data/raw/lpsn_names.tsv:5623` supports `lpsn:30128`, the 2022 combination, its authority, parsed legitimate/valid/synonym status, DSM type designation, two DOIs, PMID and JF799985. The linked correct-name row at line 27391 is `lpsn:790435`, Massilia namucuonensis Kong et al. 2013. Its own NCBI mapping field is empty; representing it as a linked synonym rather than manufacturing another mapped nomenclature entry follows the input.

Current LPSN pages confirm both record numbers, the shared type, JF799985 and their homotypic relationship. Pseudoduganella is validly published but a synonym under LPSN's preferred classification; LPSN also explains when it would be the correct combination under a separate Pseudoduganella genus. The YAML preserves that conflict through explicit status flags. Its generic chronological note is the minor issue below. [LPSN Pseudoduganella](https://lpsn.dsmz.de/species/pseudoduganella-namucuonensis), [LPSN Massilia](https://lpsn.dsmz.de/species/massilia-namucuonensis)

| Reference | Inspected support |
| --- | --- |
| DOI `10.1099/ijsem.0.005407`; PMID `36063369` | PubMed explicitly pairs these identifiers with Lu et al.'s September 2022 paper. The publisher abstract explicitly proposes transferring M. namucuonensis to Pseudoduganella. |
| DOI `10.1099/ijsem.0.005681` | Publisher identifies Oren and Goker's notification for volume 72, part 9, with online date 20 December 2022; LPSN cites it for this combination. The notification's target table row was not independently read. |
| DOI `10.1099/ijs.0.039255-0`; PMID `22447703` | Additional protologue context: PubMed's abstract explicitly identifies type strain 333-1-0411 = CGMCC 1.11014 = DSM 25159. This is not an extra required YAML citation. |

The 2022 paper's publisher abstract, not its PubMed record, supplied the abstract text; PubMed returned no abstract for 36063369. Publisher full-text endpoints for both cited 2022 items returned HTTP 403 after browser-tool failures. Full papers, figures and the notification table were not inspected. No detailed phylogenomic result or phenotype is inferred from their titles. [2022 publisher abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005407), [notification publisher page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.005681), [PubMed 36063369](https://pubmed.ncbi.nlm.nih.gov/36063369/), [protologue abstract](https://pubmed.ncbi.nlm.nih.gov/22447703/)

JF799985 resolves to `JF799985.1`, a 1,490-nt partial 16S rRNA sequence for strain 333-1-0411 with explicit taxid 1035707 and type-material qualification. Its reference pairs the protologue DOI and PMID above. All returned metadata were inspected except sequence/translation payloads. Preserve the source-supplied unversioned accession in nomenclature; this marker is not a genome. [GenBank JF799985.1](https://www.ncbi.nlm.nih.gov/nuccore/JF799985.1)

**Strain identity and mapping.** `data/raw/bacdive_strains.tsv:11191`, `data/bacdive/records.jsonl.gz:11190` and the live BacDive page support BacDive 11342, designation 333-1-0411, CGMCC 1.11014, DSM 25159 and type-strain status. The derived type flag intersects the pinned LPSN DSM designation. One strain is not two strains because two collection deposits are listed. Both deposit strings pass the pinned CAFI full-accession rule; bare 333-1-0411 does not. BacDive's genome reference 66792 identifies an automated DiASPora annotation, not an independent experimental study. [BacDive 11342](https://bacdive.dsmz.de/strain/11342)

`data/raw/gtdb_mappings.tsv:1442`, `data/raw/gtdb_species.tsv:156850` and `data/catalog/gtdb_genomes-0009.jsonl.gz:29871` support the Rugamonas species spelling, close-match predicate, genome count one and representative `RS_GCF_900116645.1`. The exact deposit in native `ncbi_strain_identifiers` supports the strain link. The live GTDB genome page could not be retrieved, so current GTDB release status was not independently confirmed; the judgment rests on inspected pinned primary metadata.

**Genome and project assertions.** Every imported assertion was compared field by field with the uncapped inventories: `data/raw/strain_assemblies.tsv:5644` through 5651, `strain_genome_records.tsv:4226` through 4231, and `strain_related_records.tsv:16763` through 16782.

| Source | Native evidence and supported chain |
| --- | --- |
| BacDive | Unversioned GCA_900116645, PATRIC 1035707.5 and IMG 2671180040 are explicitly listed under reference 66792; no version is invented. |
| BV-BRC | `data/bvbrc/bvbrc-0000.jsonl.gz:3337`: 1035707.5, CGMCC 1.11014, GCA_900116645.1, SAMN05216552 and PRJEB17581. |
| NCBI Assembly | `data/catalog/ncbi_genbank-0056.jsonl.gz:40321` and `ncbi_refseq-0009.jsonl.gz:28018`: GCA/GCF_900116645.1, explicit paired accessions, identical paired sequence comparison, scaffold level, strain, sample and source-specific projects. |
| GTDB | Native accession and separate GenBank field support GCF and GCA respectively, plus sample and project; the GCA counterpart is not guessed from a prefix. |
| GOLD | `data/gold/organisms.jsonl.gz:37144`, `projects.jsonl.gz:69794`, `analyses.jsonl.gz:50734`: Go0044292 -> Gp0120036 -> Ga0079888, carrying CGMCC 1.11014, GCA_900116645.1 and IMG 2671180040. The analysis's organism field is empty but its explicit project resolves to that organism without conflict. |

GOLD's culture-collection and strain fields independently supply the same deposit string; retaining both provenance assertions is intentional. Go0614305 explicitly names DSM 25159. Go0614306 has only the bare 333-1-0411 designation, so it contributes to the three-organism attestation but does not supply a deposit-based genome link. Projects, organisms and analyses remain related records, outside genome counts. Native rows for all three organisms were inspected.

Live NCBI Datasets confirms both assemblies as current, paired, scaffold-level and from CGMCC 1.11014/type material, with 103 scaffolds and 112 contigs. Both live Datasets reports expose submission project PRJEB17581, while the pinned RefSeq and GTDB fields retain PRJNA224116. The latter resolves to NCBI's prokaryotic annotation project, not a target-only sequencing study. Keep source-field provenance rather than silently substituting one project for another. The oversized raw BioProject response was truncated; the relevant identity and description were recovered from its public page, not a claim of auditing every linked project. [GenBank Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_900116645.1/dataset_report), [RefSeq Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_900116645.1/dataset_report), [PRJNA224116](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116)

Live BioSample SAMN05216552 explicitly carries CGMCC 1.11014, taxid 1035707, JGI Gp0120036 and PRJNA323123, agreeing with GOLD's sample/project chain. This supports related-record assertions, not equivalence among every co-listed genome. [BioSample metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=biosample&id=SAMN05216552&retmode=xml)

**ATB.** `data/atb/assemblies.tsv:4461`, `strain_links.tsv:88`, `genome_links.tsv:411` through 415 and `data/catalog/allthebacteria.tsv.xz:1160675` agree on the 2025-05 local assembly ID, 661k dataset, sample, SRR4218301, ERZ9467011, SeqKit sum, URLs, archive filename and filters. All six prior sample assertions and five genome crosslinks retain their originating source chains; the relationship is shares_biosample, not sameAs.

The assembly passes the assembly filter and has an available-FASTA flag, but its HQ filter is `CHECKM2_MAX_CONTAM`. The YAML correctly preserves that warning. Non-HQ alone is not an exclusion under the repository's ATB rules. No claim of a high-quality assembly is warranted.

ENA's live run metadata confirms SRR4218301 -> SAMN05216552 -> PRJNA323123. The complete ERZ9467011 analysis XML independently names the same sample and run and identifies a Shovill assembly; it is distinct from the original ALLPATHS assembly described by NCBI. Its FASTA checksum is not the YAML's SeqKit sum. Mutable AWS contents, OSF archive bytes and sequence identity were not downloaded or verified. [ENA run metadata](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=SRR4218301&result=read_run&fields=run_accession,sample_accession,secondary_sample_accession,study_accession,secondary_study_accession,tax_id,scientific_name&format=json), [ENA ERZ9467011](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ9467011)

**StrainInfo.** `data/straininfo/records.jsonl.gz:304273`, `strain_links.tsv:4069` and `related_records.tsv.gz:10497` through 10498 agree with the live rich API: SI-ID 406384, version DOI `10.60712/SI-ID406384.3`, own available deposit SI-DP 913679 / DSM 25159, published-online status and BacDive 11342. The DOI denotes a strain-record version, not a paper. The API contains no sequence assertion; CGMCC 1.11014 occurs as a relation designation, not another eligible own deposit. Thus two related records and no StrainInfo assembly assertion are appropriate. The HTML/DOI routes were uninformative, but the exact API endpoint returned HTTP 200 and the full record was inspected. [StrainInfo rich API](https://api.straininfo.dsmz.de/v2/data/strain/max/406384)

**Attestations and audit.** Source rows support NCBI 1 NAME, LPSN 1 NAME, GTDB 1 GENOME, BacDive 1 STRAIN, MediaDive 1 MEDIUM, GOLD 3 ORGANISM, Madin 12 TRAIT_ASSERTION and BactoTraits 23 TRAIT_ASSERTION. The latter four rows are `data/raw/mediadive_taxa.tsv:124`, `gold_organisms.tsv:484`, `madin_taxa.tsv:676` and `bactotraits_taxa.tsv:95`. Units are not interchangeable. MediaDive's taxon-level medium 830 does not require a positive strain-level medium count absent from the strain inventory. The seed event retains the eight-source scope reason and the inventory-derived timestamp 2026-09-13T17:54:04Z; this review does not promote its status.

## Completeness

No required identity, strain or imported-link gap was found. All listed strain assertions agree with their source inventories and overlays. Optional record-level literature evidence, a definition, discussion and causal graph need not be invented. No gene-regulatory, pathway, stress-response or transcriptomic assertion calls for iModulonDB; the 16S accession is being checked for taxonomic provenance, not expression-module membership.

The local search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included complete-digit taxid 1035707, the epithet/slug, deposit and designation spellings, GCA/GCF stem, JF799985, SAMN05216552 and explicit GOLD/project/run/analysis/StrainInfo identifiers. All 86 returned addresses were read in full, including compressed catalogs. Five excluded `SOURCE.json` files were separately parsed; history filenames were independently traversed. Neither metadata values nor history paths supplied a target match. Negative findings are limited to these roots and terms and include ignored files.

Three overbroad search hits were fully read and excluded: `data/catalog/allthebacteria.tsv.xz:551290` is an E. coli sample with run ERR1035707; `data/gold/analyses.jsonl.gz:28287` is Staphylococcus aureus VET0426R / Ga0044292; line 277800 is Chelativorans xinjiangense lm93 / Ga0444292. Matching digits or a permissive GOLD pattern do not establish target identity. SeqCode name entries 11902 and 29425 were inspected as catalog context; their limited fields do not supply another NCBI mapping.

Current GTDB release status, independent live GOLD/BV-BRC/IMG pages, full-paper tables/figures, genome sequence equivalence and exhaustive literature retrieval were not established. Inspected native source projections support their bounded imported assertions, not those broader claims.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: ambiguous chronology in the generated deprecated-name note.** YAML line 59 says the name is a synonym of a "later correct name." LPSN's accepted Massilia namucuonensis dates to 2013 and is the basonym of the 2022 Pseudoduganella combination. A later choice of preferred classification is possible, but the inspected `deprecated` flag does not encode that chronology, and the note does not distinguish it from publication date. This is weak wording, not a wrong taxon or invalid synonym flag. Maintained owner: `src/taxonmech/seed.py:418`, where the same phrase is emitted solely from `deprecated == "1"`. The LPSN source rows and pages above support a chronological-neutral statement.

The NCBI/LPSN/GTDB naming disagreements, non-HQ ATB warning, different project contexts and duplicated source-field provenance are retained evidence distinctions, not additional curation defects.

## Recommended Edits

For a later authorized curation change, replace the generic phrase in `src/taxonmech/seed.py` with chronology-neutral wording, for example "LPSN marks this name deprecated (a synonym rather than its preferred correct name)." Add a regression case in `tests/test_seed.py` in which the accepted name predates the deprecated combination. Do not infer the publication order from a boolean or hand-edit this YAML.

Preserve the current identity, NCBI lineage, source-specific names, supplied accession versions, type flag, contamination warning and all explicit provenance chains. Do not collapse sample/project/deposit references into genomes or transfer a StrainInfo sequence through relation aliases.

## Follow-up Checks

For the proposed wording fix, run `just test tests/test_seed.py`, then the documented dry-run and canary workflow: `just seed`, `just seed-canary NCBITaxon:1035707`, and inspect the emitted YAML. Only under separate curation authorization should the full corpus be re-emitted with `just seed-apply --force`.

Then run `just validate` and `just validate-strict` on this exact record, followed by `just verify-corpus` and `just qc`. A shared seeder wording change affects other deprecated names, so a single canary cannot prove corpus-wide consistency. None of these proposed edits or regeneration steps was performed by this review.

Optional evidence follow-up is to read the inaccessible full papers/notification table and recheck the live GTDB page during a controlled source refresh. Retain the pinned metadata until that refresh is explicit; no unresolved access limitation establishes a broken YAML reference.

## Additional Notes

Review completed on branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The entire YAML was reread and remained byte-identical to the initial target. The sole repository write for this review is this new timestamped report. No inventory, record, old report, status, history, schema, generated page, worktree, cross-repository output or GitHub item was modified.

