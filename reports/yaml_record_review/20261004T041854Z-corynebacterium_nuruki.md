# YAML Record Review: Corynebacterium nuruki

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/corynebacterium_nuruki.yaml`
- Started UTC: 2026-10-04T04:15:00Z
- Finished UTC: 2026-10-04T04:18:54Z
- Verdict: pass with minor issues

## Target

The entire 506-line generated `TaxonRecord` was read. It identifies `NCBITaxon:1032851`, Corynebacterium nuruki, a bacterial species under `NCBITaxon:1716`, with nine ancestors, genetic code 11, `EXACT` grounding and `SEEDED` status. It contains one LPSN name, one GTDB mapping, two NCBI authority-name synonyms, one descendant-filed BacDive type strain, five assembly assertions, eight other genome assertions and 21 related-record assertions. Counts of source assertions are not counts of distinct biological genomes.

Maintained owners are the upstream source transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and `curation/seed_scope.tsv`. The generated YAML is not a manual-edit target.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/corynebacterium_nuruki.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/corynebacterium_nuruki.yaml`: passed, one file, zero errors; refreshed the standard strict-validation TSV.
- Structured checks matched the full backbone lineage, names, rank/parent/code, scope/PATHS entries, NCBI attestation and seed text. Full-field multisets matched all 5 assembly, 8 genome-record and 21 related-record assertions to their maintained inventories. Both StrainInfo evidence objects matched their native record/deposit fields, status, DOI and taxonomy.
- Not checked: full-corpus `verify-corpus`, QC/test suite, global term/reference/history/provenance/product gates or rendered pages. These source comparisons are evidence audits, not substitutes for those gates. No canary or regeneration was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220927`, `data/catalog/ncbi_names-0005.jsonl.gz:30236-30238`, PATHS row 13327 and scope row 26079 agree on the species. Live NCBI Taxonomy XML and Datasets agree on its name, rank, code, genus parent and all nine ancestor IDs: 1, 131567, 2, 1783272, 201174, 1760, 85007, 1653, 1716. The two authority strings are retained as related rather than exact synonyms. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032851)

The only direct child in the inspected backbone and live Datasets response is strain S6-4, `NCBITaxon:863239`; local row 181577 explicitly supplies the species parent. BacDive's `classified_as` therefore preserves a supported strain-level classification instead of treating the species and culture as identical.

LPSN record 789493 confirms the validly published correct name, Shin et al. 2011 authorship and the Nouioui et al. 2018 emendation. DSM 45695 and JCM 17162 in the YAML are supported, but the source also lists KACC 15032, which is missing from this particular nomenclature field; see m1. [LPSN](https://lpsn.dsmz.de/species/corynebacterium-nuruki)

## Evidence

| Assertion | Inspected evidence |
| --- | --- |
| NCBITAXON, 1 NAME | Backbone/name catalog and live taxonomy agree; the snapshot date is 2026-09-13. |
| LPSN, 1 NAME | `data/raw/lpsn_names.tsv:26541` reproduces name, status flags, authority, identifiers, publications and marker accession. Live LPSN supports name-level identity and status. |
| GTDB, 7 GENOME | `gtdb_mappings.tsv:1352` and `gtdb_species.tsv:46322` reproduce the mapping and count. A complete metadata-catalog scan found seven cluster members, all individually inspected. |
| BACDIVE, 1 STRAIN | `bacdive_strains.tsv:84193` and native `data/bacdive/records.jsonl.gz:84192` identify BacDive 161956, S6-4 and its three deposits, filed at child taxid 863239. One descendant strain is gathered, as the attestation note states. |
| MADIN, 1 TRAIT_ASSERTION | `madin_taxa.tsv:615` supports the species-direct count. The child's four assertions at row 31456 are deliberately not gathered. No named phenotype is asserted. |

The scope reason records four directly attesting sources; the seed event correctly lists five after gathering the descendant BacDive strain. That difference is explained by the documented aggregation rule, not an inconsistent seed event.

GTDB's seven-member cluster contains four genomes with NCBI species taxid 1032851, two S6-4 genomes under child 863239, and one genome NCBI calls uncultured Corynebacterium sp. (159447). Its representative is RS_GCF_007970465.1. The remaining accessions are RS_GCF_036842625.1, RS_GCF_047445925.1, RS_GCF_000213935.1, GB_GCA_945928095.1, GB_GCA_030459895.1 and GB_GCA_003524425.1. Thus seven is the GTDB cluster total, not seven type-strain genomes or an exact NCBI assembly census. The LPSN species-to-GTDB link supplies independent name-level support for the species mapping. GTDB's Mycobacteriaceae placement differs from NCBI's Corynebacteriaceae; the YAML correctly retains NCBI lineage rather than reconciling the two.

The strain's type status and DSM 45695/JCM 17162/KACC 15032 identities are supported by the native BacDive record, its live page, NCBI type-material rows 1636-1641 and the original species-description abstract. `medium_count: 2` matches the raw inventory, but its original MediaDive edge derivation was not available for independent recounting. The live BacDive page displays one named medium; that is a different source surface, so no unsupported replacement count is proposed. [BacDive 161956](https://bacdive.dsmz.de/strain/161956)

All nested genome and related-record fields match `strain_assemblies.tsv:73022-73026`, `strain_genome_records.tsv:57006-57013`, `strain_related_records.tsv:225112-225130` and `data/straininfo/related_records.tsv.gz:147059-147060`. Source-native chains were also inspected:

- BacDive reference 67770 supplies unversioned GCA_000213935, PATRIC 863239.6 and IMG 2547132106; reference 124043 supplies unversioned GCA_007970465, PATRIC 863239.11 and IMG 8005226431. Their reference IDs and contig/complete labels are preserved. Co-occurrence is not asserted to prove sequence equivalence.
- GOLD Go0011122 explicitly names JCM 17162. Its Gp0011122 -> Ga0019604 chain supplies unversioned GCA_000213935, IMG 2547132106, PRJNA66913 and SAMN02470217. Gp0118689 -> Ga0078123 supplies IMG 2623620532, PRJNA274424 and SAMN03328695, but no GenBank assembly. Gp0551386 -> Ga0490434 supplies GCA_007970465.1, IMG 8005226431, PRJNA558581 and SAMN12496158. All three analyses explicitly reference those projects, which reference the organism; empty direct analysis-organism fields do not break the unambiguous project chains.
- GOLD Go0614858 and Go0614859 explicitly name KACC 15032 and DSM 45695. They remain organism references, not invented genome links. Native organism rows 9769/445578/445579, project rows 9633/68816/405151 and analysis rows 11755/49810/317795 were read in full.
- Native BV-BRC row `data/bvbrc/bvbrc-0027.jsonl.gz:36083` explicitly gives KACC:15032 for 863239.11, GCA_007970465.1, PRJNA558581 and SAMN12496158. Row 36084 for 863239.6 lacks a collection accession and has only a bare strain description, so it does not independently justify another culture-identifier join.
- Native StrainInfo row 304387 is SI-ID406498, own available DSM 45695 deposit SI-DP913805, species taxid 1032851, published status and version DOI 10.60712/SI-ID406498.3. The source contains no sequence list. Both YAML assertions preserve that species-level source classification and deposit provenance; the JCM/KACC group aliases are not promoted to own deposits or genome evidence. DataCite independently resolves the DOI as version 3 of this StrainInfo dataset. [Record-version DOI](https://doi.org/10.60712/SI-ID406498.3)

Live NCBI Datasets confirms GCA_000213935.2 paired with GCF_000213935.1, strain S6-4, taxid 863239, contig level, PRJNA66913 and SAMN02470217. It separately confirms GCA_007970465.1/GCF_007970465.1, complete-genome level, the same strain taxid, PRJNA558581, SAMN12496158 and explicit KACC:15032 in the BioSample. These checks resolve source identifiers without rewriting the unversioned BacDive/GOLD values or declaring the two assemblies identical. [Draft assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000213935.2/), [complete assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_007970465.1/)

PubMed XML for PMID 21075904 and Crossref agree on the Shin et al. species-description article, DOI 10.1099/ijs.0.027763-0, IJSEM 61:2430-2434 (2011), electronically published in 2010. Its abstract explicitly identifies S6-4 as KACC 15032/JCM 17162. Crossref verifies DOI 10.1099/ijs.0.038901-0 as the January 2012 IJSEM notification list, 62:5-6; LPSN places that list with this name. The publisher full text was unavailable, so the notification entry itself was not independently read. [Species description](https://pubmed.ncbi.nlm.nih.gov/21075904/), [notification list](https://doi.org/10.1099/ijs.0.038901-0)

NCBI Nuccore confirms HM165487.1 as a 1,443-base partial 16S sequence from S6-4/type material, taxid 863239, with the same PMID/DOI and a direct submission dated 2010-04-27. The YAML appropriately preserves the unversioned nomenclatural marker accession rather than counting it as an assembly. No phenotype from the article or predictions on BacDive was imported. [Marker sequence](https://www.ncbi.nlm.nih.gov/nuccore/HM165487.1)

## Completeness

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, covering bounded species/child taxids, name/stem and the three deposit designations. All 119 matched lines and structured contexts were inspected; source SOURCE.json files were separately scanned. No separate target history or target retirement/drop was found within these bounds.

A complete structured culture-token scan, using the repository's CAFI normalization rules, checked 4,111,794 NCBI current/historical assembly rows, 1,419,549 BV-BRC rows, 901,341 GTDB rows and 531,961 GOLD organism rows. The fields inspected were NCBI strain/isolate, BV-BRC culture_collection/strain, GTDB ncbi_strain_identifiers and GOLD ORGANISM CULTURE COLLECTION ID. It found no eligible NCBI or GTDB collection token, the one BV-BRC KACC match, and the three GOLD matches already represented. GTDB's S6-4 labels are bare aliases, not culture-collection identifiers. All 314,470 StrainInfo native rows were checked for own-deposit or target-taxid matches; only SI-ID406498 matched, with no sequences.

An additional ignored-inclusive compressed search of `data/atb` and `data/catalog/allthebacteria.tsv.xz` for the three supported BioSamples and three BioProjects returned no matches. No ATB link is therefore justified from those chains in this snapshot. This is not a claim that the species has no other genomes or samples.

Numeric collisions were excluded using source context: SAMEA1032851 belongs to Streptococcus equi EQUI0153; SI-DP863239 is Clavibacter LMG 25590; KV863239 is a Ralstonia solanacearum PSS4 sequence; an isolate numbered 863239 belongs to Streptococcus pneumoniae; ASM863239v1 belongs to Vibrio cholerae; ERR863239 belongs to a Staphylococcus sample. Other C. nuruki isolates and the uncultured GTDB member are species context, not evidence for the type culture.

The sole identified completeness issue is the missing LPSN type designation below. Functional fields and causal graphs are optional and unsupported here; iModulonDB is not applicable to these identity-only assertions.

## Findings

Counts: 0 blocker, 0 major, 1 minor.

1. **m1 - Minor: incomplete LPSN type-strain designation list.** YAML lines 48-50 and `data/raw/lpsn_names.tsv:26541` contain DSM-45695 and JCM-17162 but omit KACC-15032. Current LPSN lists all three culture-collection numbers; PMID 21075904 explicitly establishes KACC 15032 as type material, and the record already carries that deposit in its strain entry at line 85. This is a non-blocking nomenclatural provenance/completeness gap, not wrong strain identity. The schema describes this field as the collection numbers LPSN supplies. Maintained owners: upstream kg-microbe LPSN type-strain edges and the ingestion path in `src/taxonmech/extract.py:448`, followed by seeding. The generated YAML faithfully reproduces the incomplete inventory, so it must not be patched directly. [LPSN type designations](https://lpsn.dsmz.de/species/corynebacterium-nuruki), [original description](https://pubmed.ncbi.nlm.nih.gov/21075904/)

## Recommended Edits

1. Refresh or correct the maintained LPSN input so lpsn:789493 carries the source-supported KACC-15032 type-strain edge alongside DSM-45695/JCM-17162. Check whether upstream extraction omitted it or the pinned source predates the complete list; do not infer new collection accessions from bare S6-4.
2. Re-extract and regenerate through the documented workflow after the maintained correction. Add a focused regression asserting all three supported type collection IDs while preserving the descendant strain classification and existing source-specific genome/provenance fields.

No changes are recommended to the NCBI identity, authority synonym scope, GTDB cluster count, assembly versions, StrainInfo ownership rules or functional slots.

## Follow-up Checks

After an authorized source fix, inspect the LPSN inventory diff, run `just seed-canary NCBITaxon:1032851 --force`, inspect the generated record and rerun both focused validators. Confirm KACC appears under nomenclature without losing its existing strain-level presence. The canary was not run here.

Restore the pinned upstream MediaDive/Madin/GTDB transformed inputs before independently reproducing their edge counts, including medium_count 2. Recheck the notification entry when publisher text becomes accessible. Run corpus-wide QC/reproduction/provenance/history/product gates and relevant tests before broader regeneration/publication.

## Additional Notes

- The configured `../../kg-microbe/data` directory was inventoried with ignored files included and contained only two NLP files, not the transformed source edges. `data/raw/MANIFEST.yaml` records their upstream provenance. Aggregate matches are not claimed as independent re-audits of the unavailable MediaDive/Madin edges.
- The live GTDB tree and DOI landing page for StrainInfo were inaccessible to the web tool. The complete pinned GTDB metadata, native StrainInfo record and successful DataCite response supply the stated bounded evidence. The citation-list full-text limitation remains explicit above.
- The review preserves the distinction between source-level classification differences, culture identity, sequence identity and count units. Higher-rank GTDB/NCBI differences and source-specific assembly versions were not silently harmonized.
- A preliminary local audit's displayed output was truncated; its process was confirmed terminal before repeating the audit with fully captured results. No completeness claim relies on that truncated display.
- Only this new report was manually written. No YAML, source input, curation event, mapping status, separate history, generated page or GitHub item was changed. Existing reports were not edited.
