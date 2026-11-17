# YAML Record Review: Actinokineospora diospyrosa

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinokineospora_diospyrosa.yaml`
- Started UTC: 2026-10-09T22:58:35Z
- Finished UTC: 2026-10-09T23:05:11Z
- Verdict: pass

## Target

Entire 1,291-line generated `TaxonRecord` read. `NCBITaxon:103728` denotes Actinokineospora diospyrosa, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:39845`, code 11, grounding `EXACT`, status `SEEDED`. All nine ancestors, nomenclature, mapping, synonym, xrefs, one BacDive strain, eight source attestations and complete seed event were inspected. The nested strain contains 19 assembly assertions, ten genome-record assertions and 66 related-record assertions. These are source/field-specific links, not 95 independent genomes or cultures.

HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`; YAML SHA-256 `40b6ba360f1601bca7b06db822254d1ced1931c25d99344b15dd8534ecb1937d`. Ignored-inclusive filename resolution found exactly one target and no prior report. Local guidance, schema, seeder, extraction and history implementation were confirmed unchanged from their preceding complete reads.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/actinokineospora_diospyrosa.yaml`: passed, including a final repeat.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/actinokineospora_diospyrosa.yaml --out /private/tmp/taxonmech-actinokineospora-diospyrosa-20261009-validation.tsv --workers 1`: one file, zero errors, including a final repeat; header-only TSV read.
- `uv run --offline python scripts/validate_history.py history`: 17 valid records and zero invalid links during this review.
- Complete own-ID source inventory, nine-ancestor, scope, type/status and slug comparisons passed. Full-field comparisons recovered exactly 19 assembly, ten genome-record and 66 related-record assertions with no missing or extra assertion; normalized whole-deposit identities agreed. These bounded checks do not certify full-corpus reproduction and were supplemented by independent native-source inspection.
- Public NCBI taxonomy, four focused assembly responses, marker metadata, Crossref, DataCite and PubMed bibliography/abstract reads succeeded. LPSN, BacDive and both cited publisher pages were inspected within the limits below. GTDB genome browser pages, StrainInfo browser access and direct DOI-resolver opens failed; complete native snapshots and successful authority APIs supplied the relevant evidence.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18554`, native names `data/catalog/ncbi_names-0000.jsonl.gz:38591` and the next authority row, `data/taxa/PATHS.tsv:15253`, scope `curation/seed_scope.tsv:2031` and legacy page mapping row 914 agree. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103728&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103728) independently confirm the species identity, parent, authority and code.

All nine ancestor IDs, labels and ranks match the pinned backbone: root; cellular organisms; Bacteria; Bacillati; Actinomycetota; Actinomycetes; Pseudonocardiales; Pseudonocardiaceae; Actinokineospora. Current taxonomy confirms the ancestor IDs including root. Complete own-ID status scans found no child, merged-ID or dropped-ID row. Seventeen type-material rows beginning at `data/raw/ncbi_type_material.tsv:1980` were read in full, including alternative formats and VKM/YU8-1 designations.

The [LPSN species page](https://lpsn.dsmz.de/species/actinokineospora-diospyrosa) and `data/raw/lpsn_names.tsv:14915` support `lpsn:772679`, valid publication under the ICNP, legitimacy and correct-name status. The heading attributes the name to Tamura et al. 1995 and the page separately lists the Nouioui et al. 2018 emendation, supporting the combined authority. The returned page bears a 2026-03-12 print date; it is not claimed to be an independently dated October nomenclature snapshot. The authority-bearing NCBI name is retained as `RELATED_SYNONYM`, not a separate biological species.

The GTDB species identifier and two-genome mapping match `data/raw/gtdb_mappings.tsv:1479` and `data/raw/gtdb_species.tsv:4701`. LPSN links the same GTDB species. `skos:closeMatch` preserves source scope. Native GTDB places these genomes in Mycobacteriales whereas the NCBI-backed lineage uses Pseudonocardiales. This is a preserved source-classification difference, not evidence that the NCBI lineage should be overwritten.

## Evidence

Source-attestation counts and units match complete own-ID inventory rows:

| Source | Count and unit | Maintained inventory evidence |
| --- | --- | --- |
| NCBITAXON | 1 NAME | `data/raw/ncbitaxon_taxa.tsv:18554` |
| LPSN | 1 NAME | `data/raw/lpsn_names.tsv:14915` |
| GTDB | 2 GENOME | `data/raw/gtdb_species.tsv:4701` |
| BACDIVE | 1 STRAIN | `data/raw/bacdive_strains.tsv:13040` |
| MEDIADIVE | 2 MEDIUM | `data/raw/mediadive_taxa.tsv:138`, media 65 and J43 |
| GOLD | 7 ORGANISM | `data/raw/gold_organisms.tsv:518` |
| MADIN | 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:704` |
| BACTOTRAITS | 4 TRAIT_ASSERTION | `data/raw/bactotraits_taxa.tsv:103` |

These are inventory-specific assertion counts, not abundance or independent biological-strain counts. The YAML does not turn aggregate trait counts into particular phenotype claims. The complete seed sentence correctly lists all eight sources and the admission reason. Raw extraction, StrainInfo and ATB manifest timestamps were 17:50:44Z, 17:29:00Z and 17:54:04Z on 2026-09-13; the inspected latest-source timestamp rule supports `2026-09-13T17:54:04Z`. `SEEDED` does not imply human review approval.

Complete native BacDive `data/bacdive/records.jsonl.gz:13039` supports strain 13199, taxon 103728, type status and all ten normalized collection identifiers: DSM 44255, IFO 15665, IMSNU 22098, JCM 9921, KCTC 9569, MTCC 2687, NBRC 15665, NCIMB 13657, NRRL B-24047 and VKM Ac-1984. The encoded IMSNU identifier preserves the complete designation. The inspected identity/type/deposit portion of the [BacDive page](https://bacdive.dsmz.de/strain/13199) agrees; the complete web page was not read. Native references 66792 and 124043 explicitly support the DSM and JCM assemblies respectively. Reference 66792 also supports IMG 2596583538 and BV-BRC 103728.3. Unversioned BacDive accessions are preserved rather than silently upgraded.

Two assembly pairs have independent whole-deposit evidence:

| Deposit | GenBank / RefSeq | BioSample | Organism project | Native assembly size |
| --- | --- | --- | --- | --- |
| DSM 44255 | GCA_024171925.1 / GCF_024171925.1 | SAMN03080616 | PRJNA262058 | 39 contigs, 30 scaffolds, 8,112,504 total bases |
| JCM 9921 | GCA_039534305.1 / GCF_039534305.1 | SAMD00645420 | PRJDB10510 | 67 contigs, 38 scaffolds, 8,102,888 total bases |

Complete native NCBI evidence was read at `data/catalog/ncbi_genbank-0022.jsonl.gz:19158`, `ncbi_refseq-0004.jsonl.gz:19025`, `ncbi_genbank-0036.jsonl.gz:4935` and `ncbi_refseq-0006.jsonl.gz:2965`, all under `data/catalog`. The corresponding focused [DSM GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_024171925.1/dataset_report), [DSM RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_024171925.1/dataset_report), [JCM GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039534305.1/dataset_report) and [JCM RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_039534305.1/dataset_report) responses support current status, exact taxon, deposit and paired identical assemblies. Both pairs are scaffold level and type-material derived. Native ungapped lengths are 8,110,286 and 8,101,773 bases respectively; these are not confused with total lengths. WGS accessions are JAMTCO000000000.1 and BAAAVB000000000.1. The pinned RefSeq/GTDB project PRJNA224116 is a source-specific association and is not overwritten by the live API's organism-project projection. The JCM live response also identifies parent project PRJDB9057.

Native BV-BRC `data/bvbrc/bvbrc-0000.jsonl.gz:3424` and row 3425 independently give DSM 44255/DSM:44255 and JCM 9921/JCM:9921, their exact assemblies, samples and projects, as genome records 103728.3 and 103728.4. Complete GTDB `data/catalog/gtdb_genomes-0016.jsonl.gz:9920` and `gtdb_genomes-0011.jsonl.gz:4909` independently identify the DSM and JCM RefSeq genomes, both under this species and taxon. DSM is the GTDB representative and JCM is not. The two explicit genome rows support the count of two; they do not imply two unrelated biological type strains.

All seven native GOLD organisms were inspected: Go0028503 associates YU8-1 explicitly with NRRL B-24047; Go0103584 denotes DSM 44255; Go0606204 through Go0606208 denote IFO 15665, JCM 9921, KCTC 9569, MTCC 2687 and NBRC 15665. Native project and analysis records support the chains `Ga0056961 -> Gp0103584 -> Go0103584` and `Ga0682029 -> Gp0854938 -> Go0606205`, with the DSM and JCM assembly/sample/project pairs above. Analysis direct-organism fields are empty, but the inspected explicit project-to-organism links supply identity; no shared-taxon-only inference was used. IMG 2596583538 occurs on the DSM analysis; it is not transferred to the JCM analysis.

Complete native StrainInfo `data/straininfo/records.jsonl.gz:38339` supports strain 50537, BacDive 13199, published-online status, version 3 and eight available type deposits: DSM 44255/169365, IFO 15665/169366, JCM 9921/169367, KCTC 9569/169368, NCIMB 13657/211646, VKM Ac-1984/211647, NRRL B-24047/221597 and NBRC 15665/335998. The [DataCite record](https://api.datacite.org/dois/10.60712/si-id50537.3) confirms active/findable DOI `10.60712/SI-ID50537.3`, version 3, issue date 2025-02-25 and these deposit associations. Native sequence evidence attaches unversioned GCA_024171925 only to DSM deposit 169365 and AF114797 only to NRRL deposit 221597. The YAML preserves that deposit-specific scope and the source's unversioned identifiers. Relation-only designations MTCC 2687, IMSNU 22098 and YU8-1 are not invented as additional StrainInfo deposit records.

Complete own-link inventory comparisons used all 18 raw assembly rows starting at `data/raw/strain_assemblies.tsv:22328`, the one StrainInfo assembly row at `data/straininfo/assemblies.tsv:2076`, all ten genome-record rows starting at `data/raw/strain_genome_records.tsv:17708`, 49 raw related rows starting at `data/raw/strain_related_records.tsv:62696`, and 17 StrainInfo related rows starting at `data/straininfo/related_records.tsv.gz:31792`. Full source, source-field, matching-deposit and StrainInfo evidence fields were checked, not only identifier sets. Repeated assemblies or related IDs from distinct sources/fields retain separate provenance legitimately. NCBI snapshot reference names resolve in the maintained raw manifest; this was not a complete provenance replay or source-hash recomputation.

The [original species description](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-2-371), DOI `10.1099/00207713-45-2-371`, is Tamura et al., 1995, volume 45(2), pages 371-378. Its inspected abstract explicitly associates type strain YU8-1 with IFO 15665. The [notification page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-3-621), DOI `10.1099/00207713-45-3-621`, is the July 1995 notification at volume 45(3), page 621. Both Crossref records agree. The first abstract and both bibliographic pages were inspected; full articles and the notification's full name table were not. LPSN independently supports the nomenclatural association and AF114797.

[GenBank AF114797.1](https://www.ncbi.nlm.nih.gov/nuccore/AF114797.1), GI 5915957, independently identifies taxon 103728 and NRRL B-24047T, with explicit type-material status. It is a 1,512-base partial 16S marker, not an assembly. Complete features and bibliography were read; declared and actual nucleotide lengths agree, alphabet is acgnt, and the lowercase sequence SHA-256 is `691069d058b4c269e9113e8c3d5aba6be07d44e83223b74f9dea32bb2435030f`. Its [PMID 10826820](https://pubmed.ncbi.nlm.nih.gov/10826820/), DOI `10.1099/00207713-50-1-331`, describes historical partial-16S phylogenetic analysis and a family proposal; its inspected abstract does not replace the current NCBI family. The JCM assembly-associated [PMID 30832757](https://pubmed.ncbi.nlm.nih.gov/30832757/), DOI `10.1099/ijsem.0.003276`, is a GCM type-strain sequencing-program paper, not standalone experimental evidence for every phenotype of this genome. Both abstracts and bibliographies were read, not full texts.

## Completeness

The initial `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using bounded taxon 103728, the full species name/slug, all ten collection designations with separator variants, and AF114797. All 190 candidate rows were read completely, including lossless common-field/delta views and full grouped own-link rows. Five SOURCE.json files and history filenames were separately parsed/searched. The BacDive metadata request-number hit is not a taxon assertion. No own history filename was found. A supplementary ignored/hidden/compressed search for SAMN03080616, SAMD00645420, HUT 6568 and YU8-1 returned 33 rows; all were read, including the additional ATB exclusion.

The exact-sample ATB candidate is present at `data/atb/assemblies.tsv:3716` and `data/catalog/allthebacteria.tsv.xz:1062398`: SAMN03080616, run SRR4136488, available FASTA, no assembly accession, `asm_pipe_filter=META_FAIL`, `hq_filter=META_FAIL`, Sylph species match passing. `data/atb/exclusions.tsv:2039` explicitly gives `metadata_identity_flags:META_FAIL`. Inspected eligibility documentation in `docs/STRAIN_GENOMES.md` and `src/taxonmech/atb_catalog.py` rejects identity-quality failures even when FASTA is available. Its omission from eligible strain links is therefore correct. This is not a claim that every non-PASS assembly/HQ filter is disqualifying.

Conspecific StrainInfo 218710, deposit 537637/HUT 6568, at `data/straininfo/records.jsonl.gz:161326` is published offline, non-type, without a BacDive link or sequence. It does not establish a missing eligible entry in the BacDive-based nested strain inventory. Minimal SeqCode name record 1286 at `data/seqcode/names.jsonl.gz:1052` contains a name/URI lead, not an additional validation or phenotype assertion. LPSN also lists VKM Ac-1984 and YU8-1 beyond the five nomenclature-slot designations in the pinned projection; VKM is already represented among strain collections and YU8-1 is independently documented. No consequential missing required identity representation was found.

Numeric/namespace false hits were read and kept separate: BacDive 103728 is Rhodococcus ST002160/taxon 194249; DSM 103728 is unrelated unclassified LC8/BacDive 132037 with its own StrainInfo record; CP103728 belongs to Klebsiella 2289/GCA_024918835.1; AF103728 belongs to Sindbis virus; MGBC103728 belongs to Ligilactobacillus murinus/GCA_949000905.1. Other native hits are an N90 statistic in Lysinibacillus odysseyi or unrelated Prochlorococcaceae, Salmonella, Escherichia and Campylobacter strain/bin names. The remaining ATB checksum hit is Klebsiella sample SAMN07503065/run SRR5931350/ERZ5162152, not this species. No bare matching number or substring was transferred into the target.

Optional definition, functional evidence and graph slots may remain empty. Aggregate source trait counts do not establish a required gene or expression claim. iModulonDB is inapplicable because the YAML asserts no gene, regulator, pathway, functional trait identity or expression dataset. All absence and completeness conclusions are bounded to the inspected roots, snapshots, keys, maintained eligibility rules and returned authority responses; they are not a claim to cover all possible biological knowledge.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, nomenclature, collection identity, source-scoped sequence/genome links, aggregate attestations and generation history are supported. Source hierarchy differences and correct ATB eligibility exclusions were preserved rather than treated as defects.

## Recommended Edits

None required for the represented claims. Future source refreshes should update maintained source inventories/transforms and regenerate through the seeder and validated writer, not manually patch this generated YAML. Preserve versioned versus unversioned source accessions, complete collection identifiers, StrainInfo sequence-to-deposit scope and distinct source assertions. Do not admit the excluded ATB record without resolving its upstream identity-quality flags.

## Follow-up Checks

For a future refresh, independently verify whole-deposit identity, source-native accession links and ATB eligibility; re-run schema and strict validation, history validation when history changes, and the full corpus/QC gates after maintained inputs change. Retry unavailable GTDB/StrainInfo browser pages when useful; inspected native records and authority APIs already support the current claims. No unresolved blocker remains for this review.

## Additional Notes

Only NCBITaxon:103728 is judged using its entire YAML and independently inspected evidence; no adjacent-record verdict was inherited. Eukaryota YAMLs were not reopened. This new report is the only repository write for this target. YAMLs, sources, scope, history, generated products, status, branches, all ten worktrees and GitHub remain unchanged. The other session was not contacted. No paid research was used. Public-page/full-text and full-corpus-check limitations above remain explicit.
