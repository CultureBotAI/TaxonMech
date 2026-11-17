# YAML Record Review: Enteractinococcus coprophilus

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/enteractinococcus_coprophilus.yaml`
- Started UTC: 2026-10-03T11:35:43Z
- Finished UTC: 2026-10-03T11:39:26Z
- Verdict: pass with minor issues

## Target

Generated `TaxonRecord` for `NCBITaxon:1027633`, Enteractinococcus
coprophilus, rank SPECIES, domain BACTERIA, parent `NCBITaxon:1164863`.
The entire 946-line YAML was read, including the initially truncated
middle section in a separate read. It has EXACT grounding, SEEDED mapping
status, one LPSN name, one GTDB mapping, three synonyms, two xrefs,
one BacDive strain, eight source attestations and one embedded seed event.
The strain carries 19 assembly assertions, 12 genome-record assertions
and 44 related-record assertions; these are not counts of distinct genomes.

## Validation

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/enteractinococcus_coprophilus.yaml` | PASS; no issues found, exit 0. |
| `just validate-strict data/taxa/bacteria/enteractinococcus_coprophilus.yaml` | PASS; one file, zero ERROR rows, exit 0. |
| `just verify-corpus` | Not run: full-corpus reproduction check without a focused record selector. |
| `just validate-products` | Not applicable: no causal graph or curator-added graph grounding pairs. |
| `just validate-history` | Not run: ignored-inclusive identifier, label and slug searches found no target history entry. Strict validation covered the embedded event. |

All nine lineage entries matched the full pinned taxonomy table. Complete
subtree traversal found only this taxon; scanning the entire BacDive
inventory found exactly strain 7794 classified here. Structured comparison
confirmed that all 18 raw assembly, 12 raw genome and 42 raw related-record
assertions reproduce in the YAML exactly. The additional StrainInfo
assembly and two related assertions were checked against its native object.

## Identity and Grounding

Raw taxonomy row 218913 and the inspected
[NCBI taxonomy page](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1027633)
agree on species identity, parent lineage, domain and code 11. Native NCBI
name records classify the author-bearing name as authority and Yaniella
sp. YIM 100590 as includes; RELATED_SYNONYM placement preserves their scope.

Raw LPSN row 27260 and the inspected
[LPSN name page](https://lpsn.dsmz.de/species/enteractinococcus-coprophilus)
support name 790282, Cao et al. 2012, valid publication and correct-name
status. The raw status additionally retains legitimate=True. The page
lists DSM 24083, JCM 17352 and YIM 100590 as type designations; the last
is missing from the nomenclature subsection, although present on the strain.

GTDB's Yaniella coprophila is retained as a source-qualified alternate
species concept. It does not replace the NCBI Enteractinococcus lineage
or claim that this combination is LPSN's correct name. Native GTDB also
uses Actinomycetales rather than NCBI Micrococcales. Source classification
differences are preserved rather than silently reconciled.

## Evidence

**GTDB scope.** Ignored-inclusive decompressed search of every native
GTDB genome shard found exactly three members of `s__Yaniella coprophila`,
all bearing NCBI taxid and species taxid 1027633. Representative
RS_GCF_006716305.1 names DSM 24083. RS_GCF_039537445.1 names JCM 17352,
and RS_GCF_042729755.1 names NPDC060095. This supports the species-level
closeMatch and count 3 in raw mapping row 1218. Unlike a strain-level
record, this target has matching species scope. The GTDB web endpoint
was inaccessible; native RS232 objects supplied the inspected evidence.

**Type-strain identity.** Raw BacDive row 7669, the complete native
BacDive object and the inspected
[BacDive page](https://bacdive.dsmz.de/strain/7794) agree on identifier
7794, target classification and the three deposits. Native type status
is yes. The seeder's type flag follows overlap with the two available
LPSN type IDs, so the missing third nomenclature designation does not
make the flag false. Raw medium_count is zero; its omission from the
strain is not a statement that the strain cannot grow on any medium.

The inspected [JCM catalog](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_number?JCM=17352)
and [original publication abstract](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijs.0.034249-0)
independently support the three type-strain designations. JCM's
[reference record](https://www.jcm.riken.jp/cgi-bin/jcm/jcm_ref?REF=9201)
explicitly links the publication to PMID 22228667 and DOI
10.1099/ijs.0.034249-0. Direct PubMed/PMC retrieval was challenged or
empty; the publisher abstract was inspected instead. The second DOI,
10.1099/ijs.0.050401-0, resolves in publisher metadata to the notification
list matching LPSN's citation, but repeated body retrieval timed out;
the notification's full list was not independently checked.

The inspected [NCBI nucleotide record](https://www.ncbi.nlm.nih.gov/nuccore/JF507603)
identifies JF507603.1 as the YIM 100590 partial 16S rRNA sequence, with
the historical Enteractinicoccus spelling. LPSN and JCM independently
cite JF507603. The YAML correctly preserves the source's unversioned
INSDC accession and does not treat a marker sequence as a genome.

**Genome and sample chains.** Complete current/historical native NCBI
assembly searches for the target taxid found these pairs:

| Deposit or designation | GenBank / RefSeq pair | Sample | GenBank project |
| --- | --- | --- | --- |
| DSM 24083 | GCA/GCF_006716305.1 | SAMN11512782 | PRJNA538388 |
| JCM 17352 | GCA/GCF_039537445.1 | SAMD00645572 | PRJDB10510 |
| NPDC060095 | GCA/GCF_042729755.1 | SAMN43798418 | PRJNA1106891 |

RefSeq and GTDB retain PRJNA224116 for each relevant genome. The first
two assemblies have explicit type-material/deposit evidence. Native
BV-BRC 1027633.3 and 1027633.8 reproduce the corresponding DSM/JCM
assemblies, samples and projects, separately preserving strain and
culture_collection fields. The parser recognizes DSM 24083, JCM 17352
and YIM 100590 as full culture identifiers. NPDC060095 does not match a
listed deposit and must not acquire links through shared species identity.

Native GOLD chains are Go0043463 -> Gp0304919 -> Ga0264279 for DSM 24083,
and Go0613490 -> Gp0855008 -> Ga0682099 for JCM 17352. Their explicit
deposits, samples, projects and assemblies match the table. Analyses
supply IMG 2816332111 and 8148049081 respectively. Empty analysis-organism
fields are resolved by the explicit project chains, not a name join.
Go0613489 supplies a separate YIM 100590 organism assertion without an
invented sequencing/analysis chain. BacDive reference 67770 independently
supplies unversioned GCA_006716305, BV-BRC 1027633.3 and IMG 2816332111;
reference 124043 supplies unversioned GCA_039537445. Supplied versions
and repeated source assertions remain distinct.

**StrainInfo and ATB.** Native SI-ID 397882 owns available DSM 24083,
SI-DP 904548, with type true, target taxonomy and DOI
10.60712/SI-ID397882.3. Its sole genome sequence GCA_006716305 explicitly
names that deposit. JCM/YIM appear as related designations, not own
deposits authorizing extra sequence links. The YAML preserves those
boundaries. Direct DOI retrieval was unavailable; the native archive
and record both retain the version DOI.

ATB queries for SAMN11512782 and SAMD00645572 could not use the local
SQLite index because it is unavailable. As a read-only fallback, an
ignored-inclusive decompressed search scanned the entire pinned
`data/catalog/allthebacteria.tsv.xz` for both whole accessions and found
neither. The committed ATB inventories likewise have no sample/strain
match. Missing ATB links are therefore supported for this snapshot,
not inferred merely from an unavailable index.

**Attestations and audit.** Raw NCBI, LPSN, GTDB, BacDive, MediaDive,
GOLD, Madin and BactoTraits rows support the respective counts 1 NAME,
1 NAME, 3 GENOME, 1 STRAIN, 2 MEDIUM, 3 ORGANISM, 25 TRAIT_ASSERTION
and 24 TRAIT_ASSERTION. The MediaDive row names 92 and J28. JCM lists
medium 28 and BacDive DSMZ medium 92, consistent contextual evidence,
not new phenotype assertions. Scope row 4037 and the seed event name
the same eight sources. Units are not added together.

## Completeness

The single source-classified strain is fully listed; the genome evidence
retains the supported identifier systems and separate project/sample
references. No supported NPDC-to-type-strain relationship was found in
the inspected native GTDB/NCBI objects or strain inventory. Its genome
remains native species context, not a missing type-strain link.

Ignored-inclusive searches covered target ID, label and slug in raw
inventories, curation, history and review-report filenames. No previous
report or target history entry was found. YIM-100590 is present in
the raw culture inventory, BacDive object, NCBI type-material rows and
YAML strain list; the omission is specifically the LPSN type-designation
projection, not absence from TaxonMech overall.

Empty definition, discussion, curator evidence and causal-graph slots
are acceptable. iModulonDB was not applicable to a nomenclatural 16S
marker and genome-identity record with no regulator, expression-module
or functional pathway assertion.

## Findings

**Minor m1: incomplete LPSN type-designation projection.** LPSN explicitly
lists YIM 100590 alongside DSM 24083 and JCM 17352. Raw LPSN row 27260
and the YAML nomenclature list only the latter two. The original
publication and JCM corroborate the third designation, and its existing
CURIE is available in the culture inventory. This is non-blocking because
strain identity, the type flag and supported genome joins remain correct.

Maintained owners: upstream kg-microbe LPSN type-strain edges feeding
`data/raw/lpsn_names.tsv`, consumed by `src/taxonmech/extract.py:445`
and projected by `src/taxonmech/seed.py:405`. The configured upstream
edge files were unavailable at their configured paths; whether the
upstream loss began in parsing or an older snapshot remains unresolved.
The seeder faithfully copies the incomplete committed list.

Finding counts: 0 blocker, 0 major, 1 minor. No wrong genome join or
species/strain scope inflation was demonstrated for this record.

## Recommended Edits

1. Refresh or repair the upstream LPSN type-designation projection for
   name 790282 so the explicitly supported YIM-100590 association survives
   extraction. Preserve its exact identifier and source provenance.
2. Re-extract the affected inventory and re-seed through the documented
   workflow. Do not hand-edit the generated YAML or copy the NCBI type
   row into LPSN evidence without source-specific support.
3. Retain source-specific taxonomy, accession versions, supported deposit
   joins and the NPDC exclusion. No broader identity refactor is justified
   by this record's evidence.

## Follow-up Checks

1. Compare all three explicit LPSN designations with the maintained
   source edges and regenerated nomenclature list. Verify the unchanged
   BacDive type flag and all existing genome evidence.
2. Add a focused regression fixture for a type designation present in
   source text and the culture inventory but lost from the LPSN edge list.
3. After maintained changes, run the documented dry-run/canary workflow,
   both focused validators and `just verify-corpus`. Retry the notification
   list and StrainInfo DOI endpoint if their full live resolution is needed.

## Additional Notes

Only this new report was manually written. No generated record, source
inventory, status or history event was changed. Strict validation emitted
its normal diagnostic TSV. No paid research, GitHub mutation or source
index rebuild was performed. Eukaryota was untouched.
