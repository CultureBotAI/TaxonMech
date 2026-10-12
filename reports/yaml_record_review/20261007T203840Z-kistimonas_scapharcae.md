# YAML Record Review: Kistimonas scapharcae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/kistimonas_scapharcae.yaml`
- Started UTC: 2026-10-07T20:28:47Z
- Finished UTC: 2026-10-07T20:38:40Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1036133`, Kistimonas scapharcae, rank `SPECIES`, domain `BACTERIA`. The whole YAML was read. It carries nine ancestors, genetic code 11, exact grounding, seeded status, one LPSN name, one GTDB mapping, two related synonyms, six source attestations and one listed type strain. That strain has nine assembly assertions, five genome-record assertions and 26 typed related-record assertions. These are provenance-bearing assertions, not 40 distinct genomes. No record-level evidence, causal graph, discussion or dataset is asserted.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/kistimonas_scapharcae.yaml`: exit 0, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/kistimonas_scapharcae.yaml --out /private/tmp/ksc-strict.tsv`: exit 0, one file and zero errors. The diagnostic TSV was read; it contains only its header.
- Structured checks verified all backbone fields, the complete lineage, source rows, unique path mapping and seed reason. Full field equality was verified for all 9/5/26 strain links against the three raw inventories. Every deposit-based link matched the whole JCM accession through the repository's CAFI-aware matcher.
- Exact type-material search returned six NCBI designations for this species. No pinned descendants, merged-ID or dropped-ID entries were found.
- Not checked: full-corpus `verify-corpus`, `provenance-check`, `qc`, `validate-all`, tests, render/docs and vendored gates. Focused comparisons are not corpus reproduction. There is no target graph; the bounded history search found no standalone target history record.
- Configured external kg-microbe transformed LPSN, BacDive and Madin files could not be opened at their configured paths. The medium and trait counts were checked against committed inventories, not independently re-extracted from those unavailable transforms.

## Identity and Grounding

Live NCBI Taxonomy and Datasets agree on the ID, label, species rank, bacterial domain/division, code 11, parent Kistimonas (`NCBITaxon:1036132`) and all nine ancestor IDs, including root. Names and ranks match: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Oceanospirillales, Endozoicomonadaceae and Kistimonas. The authority and former A36 designation remain related, not exact, synonyms. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1036133), [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036133).

LPSN record 790325 identifies Lee et al. 2012 as the authority, valid publication under the ICNP and correct-name status. It lists A36, JCM 17805 and KACC 16204. The YAML's JCM-only nomenclature list is incomplete, as described below; the identity and type flag are not wrong. [LPSN](https://lpsn.dsmz.de/species/kistimonas-scapharcae).

The public GTDB genome-card API verifies representative RS_GCF_039540975.1, species Kistimonas scapharcae, one genome in its species cluster, JCM 17805 and NCBI taxon 1036133. The species-level `skos:closeMatch` is supported. GTDB uses Pseudomonadales where NCBI uses Oceanospirillales; the YAML correctly carries NCBI's lineage without reconciling the trees. [GTDB source card](https://gtdb-api.ecogenomic.org/genome/GCF_039540975.1/card).

## Evidence

- Backbone `data/raw/ncbitaxon_taxa.tsv:222269` agrees with the YAML. Native name rows `data/catalog/ncbi_names-0005.jsonl.gz:31785` through 31787 distinguish authority, scientific name and includes-name. `data/taxa/PATHS.tsv:14770` uniquely maps the ID/slug. `curation/seed_scope.tsv:10803` carries the six-source reason and inclusion date 2026-09-12.
- LPSN `data/raw/lpsn_names.tsv:27302` supports the stored name, booleans, citations, marker and JCM type designation. GTDB mapping row 1450 and species row 107833 support the mapping and count. BacDive row 56108 supports A36, both deposits and medium count 1. GOLD row 491 counts one organism; Madin row 680 counts nine trait assertions. These units are distinct and were not summed.
- BacDive's complete native object at `data/bacdive/records.jsonl.gz:56107` supports taxon 1036133, type status, both deposits and the unversioned assembly accession under reference 124043. The public page confirms those details. JCM independently confirms A36 = JCM 17805 = KACC 16204, type status, marker and assembly links. [BacDive 133798](https://bacdive.dsmz.de/strain/133798), [JCM 17805](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17805).
- Fresh PubMed metadata and the publisher abstract verify PMID 22247211 and DOI 10.1099/ijs.0.038422-0, the 2012 species description. It explicitly identifies A36 as the type and both deposits. The 2013 notification DOI 10.1099/ijs.0.050427-0 resolves to its publisher citation/abstract and is also listed by LPSN; its full notification table was not retrieved. [Species-description abstract](https://pubmed.ncbi.nlm.nih.gov/22247211/), [Notification article](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.050427-0).
- Complete non-sequence metadata verify JF811908.1, a 1,473-base partial 16S marker from A36, taxon 1036133, linked to the species description. NR_109422.1 explicitly derives from that sequence and names JCM:17805. These are marker records, not additional genomes. [JF811908.1](https://www.ncbi.nlm.nih.gov/nuccore/JF811908.1), [NR_109422.1](https://www.ncbi.nlm.nih.gov/nuccore/NR_109422.1).
- NCBI's complete live assembly reports confirm current paired GCA_039540975.1/GCF_039540975.1, JCM 17805, type material, contig-level assembly, SAMD00645709 and PRJDB10510. Both reports describe 481 contigs totaling 5,697,988 bases. Pinned GenBank/RefSeq native rows are `data/catalog/ncbi_genbank-0036.jsonl.gz:5268` and `data/catalog/ncbi_refseq-0006.jsonl.gz:3218`. BacDive's version-unspecified accession is correctly retained without appending a version. [NCBI assembly reports](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039540975.1,GCF_039540975.1/dataset_report).
- BV-BRC native row `data/bvbrc/bvbrc-0000.jsonl.gz:3351` and its live API record confirm genome 1036133.3, the versioned GenBank assembly, JCM 17805/JCM:17805, SAMD00645709 and PRJDB10510. Distinct source-field paths are preserved. [BV-BRC API](https://www.bv-brc.org/api/genome/?eq(genome_id,1036133.3)&http_accept=application/json).
- GOLD native organism Go0044403 names JCM 17805 and the exact taxon. Projects Gp0151287 and Gp0829485 both explicitly reference that organism. Analysis Ga0675102 references Gp0829485 and supplies IMG 8129975259 and GCA_039540975.1. Its blank direct organism field is not a conflict: the explicit project chain resolves it. Complete native objects were read at `data/gold/organisms.jsonl.gz:37241`, `projects.jsonl.gz:96280`, `projects.jsonl.gz:608887` and `analyses.jsonl.gz:451289`.
- ENA independently confirms SAMD00645709 as JCM 17805 and SAMN05363651 as an A36/JCM 17805 sample obtained for the older project. PRJNA328086 names this species and A36. PRJDB10510 is the broader JCM sequencing project; PRJNA224116 is the RefSeq annotation umbrella, not a distinct strain-specific sequencing project. The YAML does not transfer the older sample to the newer assembly. [SAMD00645709](https://www.ebi.ac.uk/ena/browser/view/SAMD00645709), [SAMN05363651](https://www.ebi.ac.uk/ena/browser/view/SAMN05363651), [PRJNA328086](https://www.ebi.ac.uk/ena/browser/view/PRJNA328086), [PRJDB10510](https://www.ebi.ac.uk/ena/browser/view/PRJDB10510), [PRJNA224116](https://www.ebi.ac.uk/ena/browser/view/PRJNA224116).
- The seeded event matches the inventory/scope reason. Its 2026-09-13T17:54:04Z timestamp follows the latest extraction manifest among raw, ATB and StrainInfo, consistent with `src/taxonmech/seed.py:139`. It does not claim human review.

## Completeness

The one listed strain equals the exact BacDive inventory count; there are no pinned descendants. MediaDive and BactoTraits have no exact target taxon rows. The per-strain medium count and taxon-level MediaDive attestation have different source scopes; their difference is not a contradiction.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It covered the taxon, label/slug, full JCM/KACC deposits, BacDive/LPSN IDs, marker, assembly, both samples, GOLD chain, IMG ID and cited PMID/DOIs. All 132 candidate rows were read completely: 107 TSV rows, 16 catalog/BV-BRC objects and nine other native objects. Five SOURCE.json files and history filenames were checked separately.

No target ATB association or own-deposit StrainInfo evidence was found in these roots. BacDive references SI-ID132039, but an ignored-inclusive search of `data/straininfo` found no such rich record and the live rich-record endpoint returned 404. This does not authorize a join by BacDive reference alone. SeqCode native name 10061 and its live API agree on identity/type, but name-only catalog entries do not automatically create an NCBI mapping.

The type-deposit provenance gap is minor because both deposits and correct type status already occur on the strain. Optional phenotype/graph slots need not be populated. No gene, regulator, transcriptomic or iModulon claim is present; iModulonDB is not applicable.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **Minor: incomplete LPSN type-deposit representation.** `nomenclature[0].type_strain_designations` contains only `kgmicrobe.strain:JCM-17805`, whereas the inspected LPSN page and original species-description abstract explicitly include KACC 16204. The missing deposit is already represented under `strains[0].culture_collection_ids`, so identity, type status and the present genome joins remain intact. The omission is already in `data/raw/lpsn_names.tsv:27302`; `src/taxonmech/seed.py:405` copies that list faithfully. The maintained owner is the upstream kg-microbe LPSN type-deposit extraction feeding `src/taxonmech/extract.py:416` and `conf/sources.yaml`, not generated YAML. The exact upstream parser fault was not established because the configured transformed inputs were unavailable.

## Recommended Edits

For a later authorized curation, preserve all verified LPSN culture-deposit identifiers, including KACC 16204, in the upstream LPSN transform. Confirm that `extract_lpsn` receives and retains the corresponding complete `biolink:close_match` edges. Re-extract the inventory and regenerate through the documented pipeline. Do not manufacture a collection CURIE for bare A36, patch generated YAML, or change the correct type flag.

No other edit is required by this review. Do not add an SI-ID link without its own eligible deposit evidence, equate the two BioSamples, turn umbrella projects into genome identifiers, or reconcile GTDB's order into the NCBI lineage.

## Follow-up Checks

A future fix should demonstrate both JCM and KACC type designations in the maintained input, resulting inventory and generated nomenclature, with the strain count still one and genome/source paths unchanged. Add a focused extraction regression test for a type-deposit list containing linked and plain-text collection numbers if that proves to be the upstream failure mode. Run schema/strict validation and the full corpus/provenance gates after regeneration.

Recheck current GOLD/IMG pages when accessible; their identities here are supported by the pinned primary native chain rather than a successful live page retrieval. Full publication text or new strain-specific experiments would be needed before adding claims beyond the inspected abstract.

## Additional Notes

- HEAD was `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The YAML remained byte-identical before report creation; branches and worktrees were preserved.
- Exact NCBI search returned one Assembly result and 966 Nucleotide results. Only the relevant two 16S records and complete assembly/sample metadata were read; this was not a review of all contig annotations or a genome-quality audit.
- Native GTDB row `data/catalog/gtdb_genomes-0008.jsonl.gz:30281` preserves the RefSeq umbrella PRJNA224116. Current NCBI Datasets also exposes the original sequencing project for the RefSeq assembly. These are different metadata contexts, not evidence that a project identifier is wrong.
- Collisions included unrelated SI-DP133798/Enterococcus faecium, SI-DP790325/Neurospora crassa, BacDive 177630/Agromyces endophyticus with SI-ID133798, NCBI taxon 133798/EBAC391, Acetatifactor MGBC133798, Salmonella PNUSAS133798, numeric GTDB assembly statistics, and ATB runs ERR133798 and ERR790325. Other LPSN names matched the shared notification DOI; their full rows were inspected without transferring their identity to this species.
- GTDB, BV-BRC and SeqCode browser pages were unavailable, but their public APIs supplied the relevant complete records. GOLD and IMG live pages were inaccessible. The defining article was checked through its publisher abstract and fresh PubMed record; the notification through its publisher citation/abstract and LPSN association, not its unavailable full table.
- ENA initially rejected a JSON Accept header; XML retrieval succeeded after correcting it. PRJDB10510's 1,570 locus-prefix entries were parsed but excluded from the context display; the genome's prefix was not in that enumeration. The assembly/BioSample records, not that broad list, establish this strain's project association.
- The external transformed-input paths and local snapshot-directory path were unavailable at the configured locations. No finding relies on claiming that they are absent everywhere on disk.
- Only this new report was written. No YAML, source inventory, history/lifecycle or GitHub state changed.
