# YAML Record Review: Rickettsia conorii subsp. heilongjiangensis 054

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rickettsia_conorii_subsp_heilongjiangensis_054.yaml`
- Started UTC: 2026-10-04T04:06:05Z
- Finished UTC: 2026-10-04T04:11:34Z
- Verdict: needs curation

## Target

Full generated `TaxonRecord` read: `NCBITaxon:1032845`, Rickettsia conorii subsp. heilongjiangensis 054, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:226665`. Grounding is `EXACT`, mapping status is `SEEDED`, genetic code is 11, and the recorded BacDive-subtree strain count is zero. The seed event is dated 2026-09-13T17:54:04Z and names NCBITAXON, GTDB, GOLD and MADIN.

Future fixes belong in maintained source inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py` and associated tests/documentation, not this generated YAML. `curation/seed_scope.tsv:26078` owns the inclusion decision; no scope change is indicated.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rickettsia_conorii_subsp_heilongjiangensis_054.yaml`: passed, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rickettsia_conorii_subsp_heilongjiangensis_054.yaml`: passed, one file scanned, zero error rows. The command refreshed its standard `reports/instance_validation_failures.tsv` output.
- Structured comparisons checked the complete local backbone chain, names, direct children, seven source inventories, scope/PATHS registration, seed text, NCBI attestation, type-material, merged-ID and dropped-ID tables. These are evidence checks, not substitutes for documented corpus validators.
- Not checked: full-corpus `verify-corpus`, QC, test suite, global term/reference/history/provenance/product gates, or rendered pages. No regeneration, canary run, review-status promotion or history event was performed.

## Identity and Grounding

The local backbone row 220926, `data/catalog/ncbi_names-0005.jsonl.gz:30232-30235`, PATHS row 13325 and live NCBI Taxonomy XML/Datasets agree on the identifier, label, strain rank, parent, code and all 13 root-first ancestors. The three NCBI synonyms retain the strain designation or deposit and are supported. The target has no direct children in the inspected backbone. [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1032845)

The parent is the currently accepted subspecies, not the individual culture. LPSN record 13660 treats R. conorii subsp. heilongjiangensis as the correct name and the historical species R. heilongjiangensis as a homotypic synonym at a different rank. Its type designations include ATCC VR-1524, CSUR 54, HLJ-054 and strain 054. Those name-level facts support culture context, not an exact mapping from this strain to the whole subspecies. [LPSN subspecies](https://lpsn.dsmz.de/subspecies/rickettsia-conorii-heilongjiangensis)

The GTDB assignment is real, but its use as exact strain identity is not supported; see finding M1.

## Evidence

| Assertion | Inspected support and scope |
| --- | --- |
| NCBITAXON, 1 NAME | Exact backbone/name rows and live taxonomy agree. |
| GTDB mapping and 221 GENOME | `data/raw/gtdb_mappings.tsv:1351` and `gtdb_species.tsv:154898` reproduce the YAML. A complete structured scan of `data/catalog/gtdb_genomes-*.jsonl.gz` found 221 members of `s__Rickettsia rickettsii`, distributed across 57 NCBI taxon IDs. Only one member has taxid 1032845. The count is a cluster total, not 221 genomes of strain 054. |
| GOLD, 1 ORGANISM | `data/raw/gold_organisms.tsv:426` and native `data/gold/organisms.jsonl.gz:10223` identify Go0011633, strain 054, taxid 1032845 and ATCC VR-1524. Native project row 10079 connects Gp0011633 to PRJNA66907/SAMN02602971; analysis row 20360 connects Ga0030145 to GCA_000221205.1, CP002912 and IMG 650716082. These are distinct organism/project/analysis/accession scopes. |
| MADIN, 1 TRAIT_ASSERTION | `data/raw/madin_taxa.tsv:614` supports the aggregate count. The YAML makes no named phenotype claim. The original transformed edge was not independently rechecked because it is unavailable in the configured checkout; see limitations below. |

The target GTDB row, `data/catalog/gtdb_genomes-0005.jsonl.gz:32699`, is RS_GCF_000221205.1, with NCBI strain 054, taxid 1032845, species taxid 781, GCA_000221205.1 and SAMN02602971. Other members include genomes assigned by NCBI to R. rickettsii, R. japonica, R. aeschlimannii and multiple other species/strains. The complete raw mapping-table scan also found this cluster linked by `closeMatch` to 57 different NCBI IDs, contradicting the generator's assumed one-to-one identity condition.

Live NCBI Assembly search returned one assembly record. ESummary UID 296258 confirms ASM22120v1, strain 054, taxid 1032845, complete-genome/type-material status, GCA_000221205.1 and GCF_000221205.1 as the paired accessions, and SAMN02602971. It distinguishes GenBank BioProject PRJNA66907 from RefSeq BioProject PRJNA224116. The pinned GenBank and RefSeq catalog rows are respectively shard 0000 rows 3807 and 3277. [NCBI assembly](https://www.ncbi.nlm.nih.gov/datasets/genome/GCF_000221205.1/)

Exact-taxid Nuccore search returned 14 records, all fetched and inspected: NC_015866.1, NR_074469.2, EU503185.1, EU503184.1, AY331396.1, AY260451.1, EF123268.1, HG790396.1, HG790395.1, HG518962.1, NR_075925.1, CP002912.1, EF123267.1 and EF123264.1. Complete genome CP002912.1/NC_015866.1 is 1,278,471 bp; the remaining marker, spacer, rRNA and tmRNA records are not additional assemblies. AY331396.1 explicitly connects strain 054 with ATCC VR-1524. [GenBank genome](https://www.ncbi.nlm.nih.gov/nuccore/CP002912.1), [deposit-linked sequence](https://www.ncbi.nlm.nih.gov/nuccore/AY331396.1)

PubMed XML for PMID 21914880 and Crossref metadata agree on Duan et al., Journal of Bacteriology 193(19):5564-5565 (2011), DOI 10.1128/JB.05852-11. The abstract names strain 054 and PubMed's sequence-accession field names CP002912. This verifies genome/publication identity only; no clinical or mechanistic claim is imported. [Publication](https://pubmed.ncbi.nlm.nih.gov/21914880/), [DOI](https://doi.org/10.1128/JB.05852-11)

## Completeness

The zero strain count is reproducible under the documented exact-taxon-plus-descendants rule, not evidence that strain 054 lacks a deposited culture or genome. `data/bacdive/records.jsonl.gz:88805` (BacDive 166570) is explicitly HLJ-054/054, ATCC VR-1524/CSUR 054, but its general taxonomy is filed at the parent subspecies 226665. Its sequence section independently names genome taxid 1032845. The live BacDive page confirms these identities and describes the genome linkage as automatically annotated. [BacDive 166570](https://bacdive.dsmz.de/strain/166570)

Related maintained evidence exists in `bacdive_strains.tsv:88806`, `culture_collection_strains.tsv:8339`, `strain_assemblies.tsv:82352-82353`, `strain_genome_records.tsv:64652-64654` and `strain_related_records.tsv:250120-250124`. Parent-level type-material rows 90203-90211 and LPSN rows 2544/22804 add name/type context. A future explicit culture-identity crosswalk could expose this supported context at the strain record, but blindly inheriting ancestor strains would be wrong. Because this is an optional enrichment outside the current documented subtree contract, it is not counted as a second finding.

The ignored-inclusive search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded numeric ID, full epithet, slug and ATCC VR-1524 variants. All 300 matched lines were captured and their structured contexts inspected. No target-specific StrainInfo record or separate history reference was found in these searched roots. Complete own-ID status-table scans found no target merged/dropped/type-material row; the parent has type-material rows. Direct exact-ID inventory scans found no BacDive, LPSN, MediaDive or BactoTraits entry for 1032845, which does not negate the parent-filed culture evidence.

No causal graph, phenotype, resistance, pathway or transcriptomic assertion requires an additional representation. iModulonDB is not applicable to this taxonomy-only record and its absence supplies no negative biological evidence. Optional functional slots should remain empty unless separately supported.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **M1 - Major: a many-taxon GTDB cluster is promoted to exact strain identity.** YAML lines 64-69 declare `Rickettsia rickettsii` an `EXACT_SYNONYM` and add its GTDB identifier to the identity xrefs. Lines 48-53 and 79-84 retain a `closeMatch` with no scope explanation. The 221-member cluster spans 57 NCBI IDs; only RS_GCF_000221205.1 belongs to this target. Membership in that cluster does not make its species name an exact synonym of a particular NCBI strain. `src/taxonmech/seed.py:449` treats every `closeMatch` as identity, and lines 466-469 consequently emit both assertions. `docs/harmonization.md:122` describes a one-to-one condition not satisfied by these rows. Maintained owners: upstream GTDB-to-NCBI mapping production, `src/taxonmech/extract.py`, the identity-promotion logic in `src/taxonmech/seed.py`, and the mapping documentation/tests. The NCBI identity itself remains sound, so this is major scope inflation rather than a blocker/wrong target.

## Recommended Edits

1. Fix the maintained GTDB identity-promotion rule so source `closeMatch` alone cannot establish an exact synonym/xref for a strain or a cluster spanning multiple NCBI concepts. Preserve the supported genome-cluster association and source provenance. Review the upstream predicate against its actual direction and cardinality; do not mechanically substitute a predicate without establishing those semantics.
2. Regenerate this record only after that maintained fix. Remove the unsupported exact species synonym and identity-only xref while retaining the GTDB mapping as an explicitly qualified association. Clarify that 221 is the cluster-wide genome count; do not silently replace it with one, because that changes the currently documented count definition.
3. As optional follow-up, evaluate a narrowly evidenced ATCC VR-1524/054 crosswalk in maintained extraction/seeding logic. Preserve BacDive's parent classification, distinguish unversioned GCA_000221205 from explicitly versioned GCA_000221205.1, and keep GOLD project/analysis identifiers separate from assemblies. Do not copy all parent-level cultures or nomenclatural names into this strain.

## Follow-up Checks

- Add a focused generator regression covering this strain and the 57-ID/221-genome cluster: association retained, unsupported exact identity absent, cluster count scope preserved, and the three NCBI strain synonyms unchanged. Include a genuinely supported species-identity control.
- After an authorized maintained-input fix, run the documented `just seed-canary NCBITaxon:1032845 --force`, inspect the resulting YAML diff, then repeat the two focused validators above. This review did not run the canary.
- If the optional culture crosswalk is implemented, require explicit strain/deposit/assembly evidence and test that sibling cultures do not transfer. Recheck BacDive 166570, the parent type designations and the paired NCBI assembly metadata.
- Before a broader release, run the documented corpus QC, provenance/history/reference/product checks and relevant tests. Restore the pinned upstream GTDB/Madin inputs before independently reproducing their transformed-edge derivation.

## Additional Notes

- GTDB's live tree URL could not be retrieved by the web tool; the inspected primary-source metadata catalog and raw mappings support the bounded cluster finding. The initial cluster scan incorrectly compared an underscore-normalized identifier with GTDB's space-containing taxonomy label and returned zero; it was corrected and fully rerun before judgement. The corrected scan found all 221 members.
- `conf/sources.yaml` points at `../../kg-microbe`. An ignored-inclusive file inventory of its `data` directory found only two NLP files, not the transformed GTDB/Madin inputs. `data/raw/MANIFEST.yaml` records the pinned upstream commit and input hashes. Thus the local Madin aggregate was verified, but not the original trait edge; no trait meaning is inferred.
- A broad preliminary search containing bare `054` exceeded output limits and was not used to establish absence. The complete narrowed search described above superseded it. SOURCE.json files were separately searched for the numeric target and bare designation; no useful target context was returned. This is not a claim that all source manifests or possible aliases were exhaustively audited.
- SAMEA1032845 belongs to Streptococcus equi EQUI0012, not this taxon; its assembly/sample context disambiguates the numeric collision. Other heilongjiangensis epithets, ATCC 1524-prefix matches, parent-only SeqCode names, sibling Rickettsia strains and parent-only ATB samples were not transferred. Bare 054 is not an identity key.
- Some NCBI source qualifiers spell the host `Dysmicoccus sylvarum`, whereas the LPSN etymology refers to a `D. silvarum` tick. This external source discrepancy is preserved as unresolved context. The YAML makes no host assertion, so it is not a record finding and no correction or biological extrapolation was made.
- PubMed's HTML view was uninformative; the successful EFetch XML and Crossref responses supported the publication check. A guessed PMC URL was not relied on. Other citations embedded in the 14 sequence records were inspected as source annotations, not independently audited as evidence for new biological claims.
- Only this new report was manually written. The target YAML, maintained inputs, mapping status, both history surfaces, generated site and GitHub were left unchanged. Earlier reports were not modified.
