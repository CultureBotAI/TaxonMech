# YAML Record Review: uncultured Eudoraea sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_eudoraea_sp.yaml`
- Started UTC: 2026-10-07T07:30:06Z
- Finished UTC: 2026-10-07T07:41:53Z
- Verdict: needs curation

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035614`, uncultured Eudoraea sp., rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1035613`, twelve root-first ancestors and genetic code 11. It carries `EXACT` grounding, `SEEDED` mapping status, fourteen GTDB taxonomy mappings, one NCBI synonym, `strain_count: 0`, two source attestations and one seed event.

No nomenclature, culture deposits, strain-linked genomes, definition, literature evidence, discussions, datasets, replacement or causal graphs are asserted. This is an environmental taxonomic bucket, not a single cultured isolate. Generated YAML is read-only. Maintained source/extraction inputs and `src/taxonmech/seed.py` own future fixes; scope and slug ownership are in `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv dependency resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/uncultured_eudoraea_sp.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/uncultured_eudoraea_sp.yaml --out /private/tmp/eu-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| `cat /private/tmp/eu-strict.tsv` | Actual TSV read; header only. |
| Structured backbone, complete lineage, seven source inventories, scope, path and attestation comparisons | Bounded comparisons agree. |
| Exact type-material, merged-ID and dropped-record scans | No target row. |
| Complete GTDB mapping/species inventories and native cluster membership | IDs, predicates, order and counts agree; twelve explanatory notes are contradicted. |
| Live NCBI Taxonomy EFetch and Datasets | Exact identity and complete ancestry agree. |
| Exact-taxid Assembly search and selected live assembly identity fields | Fifteen assemblies; all exact taxids, GenBank versions and four explicit RefSeq counterparts agree with native metadata. |
| Official GTDB RS232 bacterial taxonomy download | All nineteen relevant genome accessions/classifications and all fourteen cluster counts agree with the native catalog. |

Not checked: `just verify-corpus`, `just qc`, full-corpus schema validation, tests, provenance hashing, generated-page drift, documentation statistics and vendored checks. Bounded comparisons do not prove byte-for-byte corpus reproduction.

`just validate-products` was not run: configured OAK targets are curator-added graph nodes, absent here; NCBI taxonomy is excluded. There are no literature/internal evidence references in the YAML. The seed event was checked. `just validate-history` was not run because ignored-independent content/path searches found no target history artifact; none is created here.

## Identity and Grounding

The complete backbone row at `data/raw/ncbitaxon_taxa.tsv:222142` agrees on ID, label, rank, parent, genetic code, exact synonym and snapshot `2026-09-13`. Complete native name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31621` and `data/catalog/ncbi_names-0005.jsonl.gz:31622` independently carry the scientific name and synonym. Unique path and scope rows are `data/taxa/PATHS.tsv:14643` and `curation/seed_scope.tsv:66007`.

All twelve ancestors match the committed parent chain in identifier, label, rank and order. Live EFetch confirms the target, parent, code, synonym and eleven non-root ancestors; Datasets confirms the same chain including root. The direct parent is environmental samples within Eudoraea. NCBI's Environmental samples division does not change the bacterial domain. No retirement or replacement was found in the inspected lifecycle sources. [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035614&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035614)

`EXACT` grounds the NCBI concept; it does not establish one biological species, valid publication of this provisional name, or identity to any GTDB cluster. The NCBI synonym is correctly filed as `EXACT_SYNONYM` with its own source. NCBI's Flavobacteriia lineage is preserved independently of GTDB's Bacteroidia classification.

## Evidence

All fourteen mapping rows were read in full at `data/raw/gtdb_mappings.tsv:1428` through line 1441, along with every row for those GTDB IDs elsewhere in the complete inventory and the corresponding `gtdb_species.tsv` rows. All predicates are `skos:broadMatch`. No pooled GTDB label has been incorrectly promoted to a synonym or xref.

The following table covers every mapping. Counts are whole GTDB-cluster genome counts, not the number of genomes NCBI assigns to this target. Other NCBI IDs are from the complete local crosswalk, corroborated by complete native genome metadata.

| GTDB source ID | Cluster genomes | Other mapped NCBI taxids |
| --- | --- | --- |
| `GTDB:s__Eudoraea_sp947490415` | 4 | 1898104, 1979955 |
| `GTDB:s__JAHEJJ01_sp947258405` | 3 | 1871037 |
| `GTDB:s__Eudoraea_sp905479615` | 1 | None |
| `GTDB:s__Eudoraea_sp947258525` | 1 | None |
| `GTDB:s__Eudoraea_sp947258925` | 1 | None |
| `GTDB:s__Eudoraea_sp947260015` | 1 | None |
| `GTDB:s__Eudoraea_sp964536335` | 1 | None |
| `GTDB:s__Eudoraea_sp964636005` | 1 | None |
| `GTDB:s__Eudoraea_sp965363995` | 1 | None |
| `GTDB:s__Eudoraea_sp965364275` | 1 | None |
| `GTDB:s__Eudoraea_sp965366915` | 1 | None |
| `GTDB:s__HDS-28_sp947258555` | 1 | None |
| `GTDB:s__Lentiprolixibacter_sp965365215` | 1 | None |
| `GTDB:s__Muriicola_sp965368835` | 1 | None |

The official RS232 taxonomy file was fetched and parsed in full, filtering these fourteen species. Its nineteen matching rows agree exactly with the nineteen native genome accession/classification pairs. Fourteen of those genomes have native `ncbi_taxid: 1035614`; the other five comprise one 1898104, two 1979955 and two 1871037 entries. Each of the fourteen target-taxid genomes is its cluster's GTDB representative. [Official RS232 bacterial taxonomy](https://data.gtdb.ecogenomic.org/releases/release232/232.0/bac120_taxonomy_r232.tsv.gz)

The five non-target members were read completely at `data/catalog/gtdb_genomes-0017.jsonl.gz:26293`, `data/catalog/gtdb_genomes-0005.jsonl.gz:32930`, `data/catalog/gtdb_genomes-0012.jsonl.gz:22187`, `data/catalog/gtdb_genomes-0014.jsonl.gz:7328` and `data/catalog/gtdb_genomes-0003.jsonl.gz:8915`. They are GCA_042584465.1, GCA_049667645.1, GCA_049664545.1, GCA_049669765.1 and GCF_049667705.1 respectively. Their shared GTDB placement does not transfer their NCBI identity to this record.

The NCBI attestation correctly counts one NAME. The GTDB attestation selects the four-genome primary cluster and names thirteen further mappings, as the seeder specifies. Counts and units are not summed across sources. Summing all cluster counts to nineteen would not be an exact-taxid genome count.

Complete native NCBI metadata comprises fifteen GenBank assembly rows and four explicitly identical RefSeq counterparts, not nineteen independent assemblies. Live exact-taxid Assembly search returns fifteen. Selected live identity fields for all fifteen confirm the exact taxid, accession versions, BioSamples, isolate aliases, latest flags, lack of type designation and the four identical GCA/GCF pairs. GCA_964348345.1 is the additional target assembly outside the fourteen represented GTDB clusters; its source flags include fragmented assembly. The fifteen are metagenome-derived assemblies, not evidence for cultured deposits. Five have an Inconclusive live assembly taxonomy-check status; that is retained as a source qualification, not silently upgraded to independent species verification. [NCBI exact-taxid Assembly search](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi?db=assembly&term=txid1035614%5BOrganism%3Anoexp%5D&retmode=json&retmax=1000), [Assembly summary example](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=assembly&id=26792871&retmode=json)

All eight BV-BRC rows at `data/bvbrc/bvbrc-0000.jsonl.gz:3329` through line 3336 were read in full. They carry genome IDs 1035614.10 and 1035614.3 through 1035614.9 and exact taxonomy, with MAG/isolate context. Seven explicitly name a GenBank assembly; 1035614.10 instead supplies a WGS accession without an assembly accession. This does not authorize inventing its assembly link or a culture-deposit join.

All nine AllTheBacteria rows at `data/catalog/allthebacteria.tsv.xz:1016686`, line 1016687 and lines 1016689 through 1016695 were read in full. They concern SAMN02199408, SAMN02199409 and SAMN02199411 through SAMN02199417, with available FASTAs, PASS pipeline filters and non-HQ/Sylph qualifications. Non-HQ status alone is not an exclusion. No existing strain/deposit and whole-BioSample evidence chain was established, so shared taxon labels cannot create strain-linked ATB records.

No gene, regulator, pathway, stress-response or transcriptomics assertion requires an iModulonDB lookup. The adapter is not applicable; absence from a dataset is not negative biological evidence.

## Completeness

The complete backbone scan found no direct children. Exact structured scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. Zero BacDive strains and the optional omissions are consistent with the inspected source scope. MAG isolate aliases are not culture collection accessions, and assembly availability does not require fabricating a strain entry. The consequential gap is the accuracy of mapping explanations, not missing strain links.

Both local search stages included ignored/hidden files and compressed catalogs with `rg --no-ignore --hidden -n -z -i`. Roots were `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. All five excluded `SOURCE.json` files were separately parsed in full per stage; history filenames were independently traversed.

The identity stage used exact taxid 1035614, label and slug and found 68 lines, all subsequently read as complete structured rows. The expanded stage used the NCBI synonym and all fourteen GTDB labels with space/underscore variants, finding 52 lines, including five additional native genomes. No matching metadata values or history paths were found. Negative findings include ignored files and are bounded to these roots and terms.

Exact-taxid nuccore search returns 470 records and all 470 UIDs were retrieved. Their individual nucleotide metadata, sequences and associated literature were not inspected; no genome equivalence, phenotype or sequence-level completeness conclusion is drawn from that count. The YAML cites no paper or nucleotide accession requiring such verification. No BioSample, run or analysis object was independently fetched to establish a new strain-genome chain.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: generated mapping explanations assert unsupported cross-taxonomy scope.** All fourteen notes claim that the GTDB species also maps to other NCBI taxa. The twelve singleton clusters in the table have only NCBITaxon:1035614 in the complete crosswalk and only one native/official GTDB genome each. Thus the extra-NCBI-taxa claim is false for twelve mappings. The actual pooling relationship is multiple GTDB species mapping onto this NCBI bucket, which does not imply the reverse multiplicity for each species. This is a systemic unsupported factual claim, not merely awkward style: `src/taxonmech/seed.py:462` emits it unconditionally for broadMatch. IDs, predicates, counts, lineage and grounding remain supported. The maintained owner is `src/taxonmech/seed.py`; regression coverage belongs in `tests/test_seed.py`. The inspected existing test checks for the word Pooled but does not establish the asserted reverse cardinality.

No wrong-identity, schema, broken-reference or culture/genome-join blocker was found.

## Recommended Edits

1. In `src/taxonmech/seed.py`, replace the unconditional reverse-cardinality statement with wording supported by the mapping itself, such as: Pooled mapping: GTDB assigns genomes bearing this NCBI taxon label to this GTDB species; this is not an identity assertion. Alternatively, only describe other NCBI mappings after explicitly checking the complete crosswalk.
2. Add focused cases in `tests/test_seed.py` for multiple GTDB species mapping to one NCBI taxon when individual clusters have no other NCBI IDs, and for clusters that genuinely contain other NCBI IDs. Preserve predicates, cluster-level counts, primary-attestation selection and the rule excluding pooled mappings from identity xrefs/synonyms.
3. After separately authorized implementation, run the dry seed and single-record canary for NCBITaxon:1035614, inspect the written YAML, then follow the guarded regeneration and history workflow. Do not hand-edit this YAML or change upstream IDs/counts to accommodate the note.

No implementation or status promotion is performed in this review.

## Follow-up Checks

- Run focused seeder tests after a maintained-code fix; assert that the twelve singleton mappings no longer claim unsupported other-NCBI membership.
- Recompare all fourteen mapping IDs, predicates, counts, order and the two attestations against the complete source inventories.
- Run both single-record validators on the canary output, then `just verify-corpus` and `just qc`; validate any new curation-history artifact. Full-corpus gates remain skipped here.
- Keep NCBI, GTDB, assembly, sample and cultured-strain identities distinct. Require explicit source/deposit chains before adding strain-linked genome records.

## Additional Notes

The GTDB species-page fetch failed and an API schema probe returned HTTP 403; those failures were not treated as negative taxonomy evidence. The official release index and bacterial taxonomy download succeeded and supplied the primary classification/count check. Individual GTDB species-page prose and current live metadata beyond the pinned RS232 release were not independently inspected.

An initial live NCBI assembly check compared a string taxid with an integer and failed locally after a successful response. The corrected bounded check normalized that type and verified all fifteen identities. The initial full JSON output was truncated; only the explicitly selected live fields are claimed as inspected for every assembly. Complete local native assembly rows were separately read.

The source manifest identifies GTDB RS232 and nineteen native catalog shards. Its primary-input paths are relative to the configured kg-microbe checkout, not a TaxonMech-local raw/gtdb directory. Full provenance hashes were not rerun.

Seed wording agrees with scope and attestation. Timestamp `2026-09-13T17:54:04Z` is the newest raw/ATB/StrainInfo manifest timestamp selected by `src/taxonmech/seed.py:_seed_timestamp`, not a review date.

The entire target was reread unchanged before report creation. An ignored-independent filename search found no previous report for this stem. Only this new repository report is added for this review; no record, inventory, page, old report, history, status, GitHub object or cross-repository artifact is changed. No paid research or outbound contact was used.
