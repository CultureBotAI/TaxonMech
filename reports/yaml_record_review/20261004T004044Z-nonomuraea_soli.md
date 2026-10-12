# YAML Record Review: Nonomuraea soli

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/nonomuraea_soli.yaml`
- Started UTC: 2026-10-04T00:36:33Z
- Finished UTC: 2026-10-04T00:40:44Z
- Verdict: needs curation

## Target

Read all 1,067 lines of generated `TaxonRecord` NCBITaxon:1032476,
Nonomuraea soli. It carries `SPECIES`, `BACTERIA`, `EXACT`, `SEEDED`,
code 11, LPSN nomenclature, one GTDB mapping, two related synonyms,
eight source attestations and one BacDive strain. The strain has 19
assembly assertions, 11 typed genome assertions including one ATB
assembly, and 47 related assertions. These are source assertions, not
19 independent genomes or additive biological-isolate counts. No YAML,
source inventory, history or status changed.

## Validation

| Check | Result |
| --- | --- |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/nonomuraea_soli.yaml` | Passed; no issues found. |
| `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/nonomuraea_soli.yaml` | Passed; one file, zero ERROR rows; diagnostic `reports/instance_validation_failures.tsv`. |
| Backbone/scope comparison | Exact identity, code, parent, nine-entry lineage, synonyms, path, source counts and seed reason agree. |
| Strain assertion comparison | Full-field multisets match: 19 assembly, 10 non-ATB genome and 47 related assertions. |
| StrainInfo native evidence | All six nested evidence objects agree with their own eligible deposits, statuses, DOI and explicit sequence-deposit assignments. |
| ATB native evidence | All 17 metadata fields, seven original sample assertions and five genome crosslinks agree; 13 source-specific evidence pairs checked. |
| History/products | Embedded seed event agrees; no target standalone history entry found with ignored-inclusive searches. No causal graph/product grounding requires checking. |

Not checked: full-corpus `just verify-corpus`, `just qc`, global provenance,
full tests, rendered pages, exports, genome FASTA downloads, sequence
alignment or ANI. The comparisons above are bounded read-only audits,
not a substitute for corpus reproduction. No generator ran.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220861`, the
[NCBI browser](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032476),
live [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032476&retmode=xml)
and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032476)
agree on species identity, Bacteria, parent NCBITaxon:83681 and code 11.
The full root-first chain matches through Bacillati, Actinomycetota,
Actinomycetes, Streptosporangiales, Streptosporangiaceae and Nonomuraea.
Authority and includes names are retained as related, not exact synonyms.
Native name rows are `data/catalog/ncbi_names-0005.jsonl.gz:30143`
through 30145; complete backbone scans found no children.

`data/taxa/PATHS.tsv:13233`, `curation/seed_scope.tsv:4040` and legacy
page row772 agree. Scope was added September 12, 2026; the embedded
September 13 seed event reproduces its eight-source reason exactly.

[LPSN790002](https://lpsn.dsmz.de/species/nonomuraea-soli) supports the
correct, validly published name, Cao et al. 2012, and type strain
DSM45533 = JCM17347 = YIM120770. Its two collection IDs in the maintained
nomenclature inventory are present; YIM120770 also remains among the
record's strain identifiers and related name. The
[JCM17347 catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17347)
and [DSM45533 catalog](https://www.dsmz.de/collection/catalogue/details/culture/DSM-45533)
independently identify the bacterial type strain. They contradict one
StrainInfo deposit classification discussed below, not the top-level taxon.

## Evidence

- Raw source rows support the eight attestations: NCBI one NAME;
  LPSN one NAME (`lpsn_names.tsv:26993`); GTDB two GENOMEs
  (`gtdb_mappings.tsv:1345`, `gtdb_species.tsv:128494`); BacDive one
  STRAIN (`bacdive_strains.tsv:16391`); MediaDive four MEDIA
  (`mediadive_taxa.tsv:101`, IDs553/65/84/J104); GOLD three ORGANISMs
  (`gold_organisms.tsv:423`); Madin12 and BactoTraits16
  TRAIT_ASSERTIONs (`madin_taxa.tsv:607`, `bactotraits_taxa.tsv:75`).
  Units are not summed or interpreted as individual phenotype claims.
- The [original description](https://doi.org/10.1099/ijs.0.034751-0),
  [PMID21890732](https://pubmed.ncbi.nlm.nih.gov/21890732/) and live
  PubMed XML agree on the title, authors, 2012 volume62 pages1587-1591
  and type-strain relationship. The second
  [DOI10.1099/ijs.0.046219-0](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.046219-0)
  resolves to the nomenclatural notification for volume62 part7,
  published October 2012, pages2313-2314; Crossref metadata agree.
  Its full-text table did not load, so exact table membership was not
  independently inspected beyond LPSN's explicit citation. It is not
  treated as a separate experiment or phenotype source.
- Live [JF742631.1](https://www.ncbi.nlm.nih.gov/nuccore/JF742631.1)
  is the 1,524-base partial 16S sequence of YIM120770, taxon1032476,
  with the same description DOI/PMID. Live
  [KF540103.1](https://www.ncbi.nlm.nih.gov/nuccore/KF540103.1)
  is the 1,817-base partial `gyrB` sequence of DSM45533, explicitly
  DSM:45533 and taxon1032476. Its source references Meyers' study,
  DOI10.1016/j.syapm.2013.12.002 / PMID24423454. The YAML preserves
  the source-supplied unversioned sequence accessions; these are not
  counted as genomes or silently rewritten to today's versions.
- Native [BacDive16572](https://bacdive.dsmz.de/strain/16572), local
  row16390, confirms the three culture IDs, type status, GCA_013761175,
  GCA_039537425, BV-BRC1032476.3 and IMG2861178129. Their source
  reference IDs66792/124043 and original unversioned accessions agree.
  Three culture names do not inflate `strain_count: 1`.
- Both NCBI versioned GenBank/RefSeq pairs are present: DSM45533 has
  GCA/GCF_013761175.1 and SAMN14908352; JCM17347 has
  GCA/GCF_039537425.1 and SAMD00645571. Live
  [DSM assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_013761175.1/dataset_report)
  and [JCM assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_039537425.1/dataset_report)
  confirm current accessions, explicit paired assemblies, taxon, culture
  and samples. Pinned RefSeq/GTDB PRJNA224116 and current Datasets'
  sequencing-project PRJNA632293/PRJDB10510 are retained in their
  respective source contexts, not silently harmonized.
- Native BV-BRC rows3165/3166 confirm both assembly and sample chains
  through full DSM/JCM deposit tokens. GTDB rows0007:22343 and
  0003:7135 classify both genomes as N. soli; DSM's is representative.
  Two genomes and the explicit LPSN crosswalk support `skos:closeMatch`,
  not identity of classifications or inference of NCBI lineage.
  Both public GTDB genome pages failed to load; native metadata were
  inspected instead. All three culture identifiers pass the pinned
  CAFI authority/full-accession normalization rules.
- GOLD chains are explicit: Go0043927 -> Gp0456238 -> Ga0415313
  supplies DSM's GCA_013761175.1, IMG2861178129 and SAMN14908352;
  Go0613549 -> Gp0855007 -> Ga0682098 supplies JCM's
  GCA_039537425.1 and SAMD00645571. Analyses' organism fields are
  empty, but their projects identify the exact organisms; no conflict
  or unknown-organism chain was substituted. Go0613548 is YIM120770
  organism context only. Go/Gp/Ga IDs remain related records.
- Native SI-ID63335 at `data/straininfo/records.jsonl.gz:50774` and
  the [live rich API](https://api.straininfo.dsmz.de/v2/data/strain/max/63335)
  retain DOI10.60712/SI-ID63335.3. DSM45533 / SI-DP872073 explicitly
  owns GCA_013761175 and KF540103. JCM17347 / SI-DP872563 owns no
  sequence in that response. The eleven fungal sequence accessions
  assigned to other deposits in this SI-ID were all checked against
  the YAML and none was imported. The JCM deposit's fungal taxon
  label remains an upstream conflict, not permission to transfer
  either the fungal sequences or DSM's genome through the SI group.
- The ATB row at `data/catalog/allthebacteria.tsv.xz:1834069` is
  SAMN14908352, SRR12223499, ERZ26993474, release2025-05,
  Incr_release.202505, available FASTA and PASS assembly/HQ filters.
  The exact SeqKit sum, AWS URL, OSF archive URL/file and seven
  source sample assertions agree. Five `shares_biosample` crosslinks
  retain 13 provenance pairs: DSM GenBank6, RefSeq2, GTDB1, IMG2,
  BV-BRC2. GOLD pairs use the explicit organism/project chain, not
  equality between different Ga/Gp source IDs. There is no JCM
  crosslink merely because it shares a BacDive strain record.
- The structured iModulonDB catalog inspected this turn has 28 keys,
  none for Nonomuraea. It is not applicable to the carried gene lead;
  absence is not negative biological evidence. Native SeqCode14363
  is a name lead, not evidence of a required additional mapping.

## Completeness

Full native deposit scans covered 4,111,794 NCBI assembly records,
1,419,549 BV-BRC records, 901,341 GTDB records, 531,961 GOLD organisms
and 314,470 SI records. Exact eligible matches correspond to the carried
DSM/JCM genomes, the three GOLD organisms and SI63335. No additional
eligible own-deposit assembly was established on those surfaces.

The complete 3,227,665-row ATB catalog contains SAMN14908352 and no
whole SAMD00645571 row; both carried samples were checked. Its committed
overlap agrees, and no target exclusion row was found. This is a pinned
catalog result, not global absence or sequence-equivalence proof.

Ignored-inclusive identifier, name and slug searches covered raw tables,
native catalogs, BacDive, BV-BRC, GOLD, SeqCode, StrainInfo, ATB links and
exclusions, curation and history. SOURCE.json files were JSON-traversed.
No merged-ID, dropped-row or standalone history entry was found on these
surfaces. Optional definition, discussion, general evidence and causal
graph slots need not be populated; trait-attestation counts do not require
inventing phenotype assertions. The material unresolved issue is the
source identity conflict, not missing genome coverage.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: source-declared JCM17347 classification contradicts its own
   collection authority.** At YAML lines964 and1002, the two
   `source: STRAININFO` related assertions for SI-DP872563 and its
   SI-ID63335 context carry NCBITaxon:75551, Aspergillus brevipes.
   Both the pinned native response and live API explicitly assign that
   fungal taxon to the exact deposit JCM17347. The current JCM catalog,
   DSM catalog, LPSN, original description and NCBI instead identify
   that full deposit as Nonomuraea soli, NCBITaxon:1032476.
   SI63335 also mixes numerous fungal deposits with DSM45533.
   This is an upstream cross-domain identity conflict, not evidence
   of synonymy, an inferred lineage change or a generated-file drift.
   The generator correctly preserves the source's taxon assignment
   under `docs/STRAININFO.md`; no importer regression is inferred.
   Nevertheless, the biological classification of this imported source
   assertion cannot be endorsed until the upstream record is curated.
   Exact-deposit sequence guards prevented a more serious genome or
   gene transfer, and the taxon's own identity remains correct.

   Owner: StrainInfo SI-DP872563 / SI-ID63335 upstream. Local refresh
   inputs are `conf/straininfo.yaml` and the source snapshots under
   `data/straininfo/`; the maintained snapshot/link pipeline is
   `src/taxonmech/straininfo_snapshot.py` and
   `src/taxonmech/straininfo_links.py`, followed by the seeder. Do not
   hand-edit the generated YAML or rewrite source labels to hide the
   disagreement. This review did not contact the source or file an issue.

## Recommended Edits

1. With separate authorization, seek an upstream correction or explicit
   clarification of SI63335's mixed organism group and SI-DP872563's
   taxon. Keep the exact JCM17347 versus JCM1734 distinction. Preserve
   both inspected sources and their scope while the conflict remains.
2. After an authoritative source correction, refresh the pinned SI
   snapshot, rebuild its overlay and reseed through the maintained
   pipeline. Do not edit `data/taxa/bacteria/nonomuraea_soli.yaml`,
   append `.1` to SI accessions, remove valid DSM evidence, or promote
   `SEEDED` automatically. Any separately approved conflict-display
   policy belongs in maintained schema/link/render code with tests,
   not in a one-off alteration to this taxon.

## Follow-up Checks

- Re-read the exact SI-DP872563 and DSM SI-DP872073 entries against
  their collection authority; do not accept only the SI-ID group label.
- Preserve the negative canary: none of the eleven other-deposit
  fungal sequences may enter this bacterial strain. Cover explicit
  same-deposit sequences and JCM17347 versus JCM1734 in
  `tests/test_straininfo_links.py` and `tests/test_straininfo_schema_seed.py`
  for any authorized pipeline change.
- Run a snapshot/overlay dry run, then `just seed-canary NCBITaxon:1032476`
  only within an authorized curation change; inspect the full result
  and both focused validators. Recheck GOLD's organism/project joins
  and ATB's seven sample assertions and 13 evidence pairs.
- Run `just verify-corpus`, `just qc`, provenance and relevant rendering
  checks before publishing a refreshed corpus. No claim of full-corpus
  reproduction is made by this report.

## Additional Notes

Native locations: NCBI GenBank0012:20072 / 0036:5090,
RefSeq0003:2805 / 0006:3091; BV-BRC0000:3165/3166;
GOLD organisms36817/444283/444284, projects326356/620678 and
analyses256635/454828. SI links67936/67937, assembly5893 and related
rows160443-160447 agree. ATB strain link2541 and genome links10722-10726
agree. The full source-field comparisons were read-only.

An initial ad hoc ATB check incorrectly required GOLD Ga/Gp source IDs
to be identical. Inspection of `src/taxonmech/atb_links.py` and the native
chain showed that assumption was wrong. A corrected read-only check
using the documented organism/project key passed every pair; no
repository logic or data changed. A long live citation response was
also re-read in compact structured form after output truncation.

The live SI group reports countryCode AU, while DSM/JCM describe the
bacterial type strain from China. That uncarried group-level sample
context was not imported or generalized to this taxon. No Eukaryota
record was reopened or changed while checking the foreign source links.
All local absence checks included ignored files. Only free public reads
were used; no GitHub, source, YAML, history or status mutation occurred.
