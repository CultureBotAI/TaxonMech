# YAML Record Review: uncultured Thioprofundum sp.

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_thioprofundum_sp.yaml`
- Started UTC: 2026-10-07T10:26:06Z
- Finished UTC: 2026-10-07T10:34:51Z
- Verdict: pass

## Target

Read the entire generated `TaxonRecord`: `NCBITaxon:1035800`, uncultured Thioprofundum sp., `SPECIES`, `BACTERIA`, parent `NCBITaxon:1035799`, ten root-first ancestors, genetic code 11, `EXACT`, `SEEDED`, `strain_count: 0`, NCBI and GOLD attestations and one seed event.

No synonyms, nomenclature, mappings, strains/deposits, genomes, definition, literature evidence, datasets or causal graph are asserted. This is an environmental-sample taxonomic placeholder at NCBI species rank, not an identified culture or a formal binomial. Generated YAML is read-only; maintained extraction inputs and `src/taxonmech/extract.py` / `src/taxonmech/seed.py` own future source or harmonization fixes. Scope and slug ownership remains with `curation/seed_scope.tsv` and `data/taxa/PATHS.tsv`.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and offline uv resolution.

| Check | Result |
| --- | --- |
| `just validate data/taxa/bacteria/uncultured_thioprofundum_sp.yaml` | Exit 0; No issues found. |
| `just validate-strict data/taxa/bacteria/uncultured_thioprofundum_sp.yaml --out /private/tmp/unculturedThioprofundum-strict.tsv` | Exit 0; one file, zero ERROR rows. |
| Actual strict TSV read | Header only. |
| Complete backbone/lineage, seven inventories, path/scope, attestations and event | Bounded comparisons agree. |
| Type-material, merged-ID and dropped-record scans | No target rows. |
| Live NCBI taxonomy EFetch and Datasets | Identity, parent, rank, code and ancestry agree. |
| Exact-taxid Assembly/nuccore searches | Assembly 0 with phrase-not-found warning; nuccore 41, all returned IDs fetched. |
| All 41 nucleotide records | Source/features/reference projections and all non-sequence top-level headers inspected; all are partial 16S with explicit target taxid and environmental-sample qualifier. |
| GOLD input lineage | Inventory and extraction logic inspected; original KG-Microbe edge recount unavailable, detailed below. |
| Entire target reread | Byte-identical to initial read. |

Not checked: full-corpus `just verify-corpus`, `just qc`, schema-all, tests, complete provenance hashing, generated-page drift, documentation statistics and vendored gates. Focused comparisons do not substitute for these gates.

`just validate-products` was not run: no curator-added graph nodes exist and OAK excludes NCBI taxonomy. The YAML asserts no literature or internal evidence references requiring citation validation. The embedded seed event was checked. `just validate-history` was not run because ignored-independent content and filename searches found no target history artifact within the bounded roots below.

## Identity and Grounding

The complete backbone row, `data/raw/ncbitaxon_taxa.tsv:222177`, agrees on identifier, label, rank, parent, code, empty synonyms and snapshot 2026-09-13. The full native scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31661`. Unique path and scope rows are `data/taxa/PATHS.tsv:14675` and `curation/seed_scope.tsv:57256`; the scope reason names two sources including NCBI. The legacy page row at `curation/legacy_page_paths.tsv:876` preserves the same slug.

Every ancestor ID, label, rank and position agrees: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Chromatiales, Thioprofundaceae, Thioprofundum and environmental samples. Live EFetch confirms parent 1035799, species rank, code 11 and non-root ancestry; Datasets includes root. EFetch's division is Environmental samples, which does not contradict the bacterial domain derived from ancestry. No alternate names are supplied. [NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035800&retmode=xml), [NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035800)

`EXACT` means the record denotes this NCBI concept. It does not establish nomenclatural validity, a homogeneous cultured species, or equivalence to every member of Thioprofundum. Inspected lifecycle inventories contain no target retirement, merge or type-material row.

## Evidence

The NCBI attestation agrees on identifier, label, count 1, unit `NAME` and snapshot. The GOLD attestation agrees with `data/raw/gold_organisms.tsv:485`: target 1035800, organism count 2, with the label taken from the backbone. `src/taxonmech/seed.py` emits this inventory value using unit `ORGANISM`. Counts from different source units are not additive and neither count establishes cultured deposits or genomes.

GOLD provenance has a material verification limit, not a demonstrated YAML mismatch. `src/taxonmech/extract.py:count_subjects_by_object` counts matching `gold:Go` subject / `biolink:subclass_of` / NCBI object edges in KG-Microbe's `data/transformed/gold/edges.tsv`. The raw manifest pins KG-Microbe commit `30405b70ef762aa46c08278b2b3e06bffb0b34cd` and records edge-file SHA256 `b793c4f84278789f5dc7c68173b1f08364fd68c5d52a555c4037793006010a12`. These are inspected manifest values, not hashes recomputed here.

The configured KG-Microbe checkout lacks the original GOLD edge/node files; an ignored-independent filename search there found no GOLD directory files. An alternate `kg-microbe-projects/data` search remained permission-denied after an approved read-only retry. The original two Go identifiers and their edge count therefore remain unverified. Absence is established only within the configured, successfully searched checkout, not the inaccessible alternate location.

The separate primary GOLD organism projection supplied no exact target hit. A broader genus search located five rows in `data/gold/organisms.jsonl.gz`, all read in full: Go0031220 and Go0630241 identify T. hispidum, taxid 394805; Go0031804, Go0599721 and Go0599722 identify T. lithotrophicum, taxid 571898. They are different taxonomic concepts and cannot replace the two upstream target edges or supply target culture links. The differing source representations warrant follow-up, but do not by themselves prove the committed taxon count wrong.

Full backbone scanning found no direct children. Exact scans found no target row in `bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. The unrelated ATB hit at `data/catalog/allthebacteria.tsv.xz:547461` was read completely: Staphylococcus aureus, SAMEA3339745, ERR1035800 and ERZ3254332. Matching taxid digits inside a run accession do not establish a taxonomy or genome association.

Exact-taxid nuccore returned 41 records, all fetched and inspected as structured source/features/reference projections plus complete top-level metadata excluding sequence payloads. All are partial 16S rRNA, 245-1518 nt, with `taxon:1035800` and `environmental_sample`. Feature types are source, rRNA and gene; inspected metadata contain no culture-collection or genome assembly association. Marker assembly-method comments describe sequence processing, not genome assemblies. [NCBI exact-taxid nucleotide query](https://www.ncbi.nlm.nih.gov/nuccore/?term=txid1035800%5BOrganism%3Anoexp%5D)

The complete accession set is: OK235775.1; OM836287.1; KY468690.1, KY468689.1, KY468686.1, KY468684.1, KY468676.1, KY468675.1, KY468669.1, KY468663.1, KY468659.1, KY468657.1, KY468655.1, KY468653.1, KY468644.1, KY468632.1, KY468626.1, KY468621.1; MT969006.1; MK048596.1; MF897060.1; KX525460.1; KX525430.1; MF493556.1; KX599083.1; KX599079.1; KX270045.1; KY453767.1; KR842981.1; KR833917.1; KR854581.1; KR846498.1; KF009032.1; KC934136.1; LN878316.1; KT259885.1; KP164930.1; KP183071.1; KM108712.1; KF517391.1; JF973650.1.

These represent disparate environmental samples, including soils, rhizospheres, marine chimneys, an iron mat, activated sludge, refinery feedwater, seawater, lake water and sediments. Sample context must remain accession-specific. For example, MF897060.1's similarity note to T. hispidum gps61 is not exact species identity; KP183071.1's enriched-consortium context does not prove that clone itself degrades malachite green. GenBank reference titles are not sufficient phenotype evidence.

KP164930.1, a 502-nt DGGE-band marker from Kuwaiti soil, links PMID 25716145 and DOI `10.1007/s00792-015-0739-0`. The complete PubMed abstract and citation were inspected. It distinguishes culture-dependent isolates from culture-independent community profiles and discusses hydrocarbon consumption and amendments for tested isolates. It does not establish thermophily or hydrocarbon degradation for every sequence assigned this environmental taxon. The full article and supplements were not inspected, so no target phenotype is inferred. MT969006.1 names a landfill-leachate study, but that full article was also not checked. [GenBank KP164930.1](https://www.ncbi.nlm.nih.gov/nuccore/KP164930.1), [PubMed 25716145](https://pubmed.ncbi.nlm.nih.gov/25716145/)

The seed event agrees with the scope reason and GOLD/NCBITAXON source list. The seeder selects the latest extraction time among raw, ATB and StrainInfo manifests: 2026-09-13T17:50:44Z, 17:54:04Z and 17:29:00Z. Its 17:54:04Z event is consistent without a target ATB association. No review event or status promotion was made.

iModulonDB is not applicable: the record asserts no gene function, regulator, pathway, stress response or transcriptomic module. Environmental marker sequences do not establish expression-module evidence.

## Completeness

No consequential missing representation was demonstrated. `strain_count: 0` counts BacDive source records in the taxon subtree, not environmental clones or DGGE bands. Partial markers are not genomes, and neighboring formal-species deposits cannot be transferred here. Optional definitions, literature and graphs may remain empty.

The initial identifier, label and slug search used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Ignored/hidden files and compressed catalogs were included. Six matched rows were read completely: backbone, native name, GOLD count, scope, legacy path and the unrelated ATB accession.

An expanded search for every one of the 41 marker accessions, with optional .1 suffix, returned no matches within those same roots. At each stage all five excluded `SOURCE.json` files were separately parsed and history filenames independently traversed; no target metadata value or history filename was found. An ignored-independent report-directory traversal found no prior report for this stem. These are bounded absence checks, not claims about every file or external database.

The separate broad Thioprofundum search returned 63 row addresses and was used to locate the five fully read GOLD rows. The other genus-level rows were not all read and are not treated as target evidence.

Exact-taxid Assembly returned zero with a phrase-not-found warning. That does not exclude assemblies classified elsewhere. Complete literature/supplement retrieval, similarity searches and independent phylogenetic analysis were not performed. The original GOLD edge recount remains unresolved.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the inspected YAML and committed-inventory contract. Identity, lineage, both emitted attestations, BacDive count and seed event agree. This pass is bounded by the original-GOLD-source verification limit above; it is not a claim to have independently verified the two source organism identities.

## Recommended Edits

None required from the inspected evidence. Preserve the environmental-sample label, NCBI placement and `SEEDED` status. Do not infer a cultured species, convert 41 markers into strains or genomes, join neighboring GOLD organisms, or transfer community-level phenotypes.

Before changing the GOLD count, recover and inspect the pinned KG-Microbe source edges. Any demonstrated discrepancy belongs in maintained source extraction/harmonization inputs and `src/taxonmech/extract.py` or `src/taxonmech/seed.py`, not a hand edit to generated YAML.

## Follow-up Checks

Recover the manifest-pinned GOLD edge file, verify its checksum, identify every `gold:Go` edge to `NCBITaxon:1035800`, and check their primary organism/project/analysis identities. Compare these with the separate primary GOLD snapshot before proposing a changed count or association. This source-level work is the outstanding bounded follow-up, not a confirmed record defect.

For any authorized input refresh, repeat exact NCBI identity/lineage and Assembly/nuccore queries. New deposit or genome links require an explicit verified accession chain, not a shared genus or environmental label.

If maintained inputs change, run `just seed`, an authorized `just seed-canary NCBITaxon:1035800`, inspect the complete emitted YAML, repeat focused schema/strict validation and run `just verify-corpus` plus `just qc`. No regeneration was performed here.

## Additional Notes

Branch `codex/record-review-extensimonas-20261003`, HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Guidance, schema and seeder context from prior full inspection was retained and relevant GOLD extraction/seeding code was reread. The entire target reread was byte-identical.

An initial verbose top-level nucleotide-metadata print was truncated. A subsequent compact structured read inspected all 41 remaining header records without truncation. This does not claim inspection of base-sequence payloads or every low-level reference/feature XML field. An attempted raw `SOURCE.json` read used the wrong manifest filename; the actual `MANIFEST.yaml` files were subsequently located and inspected.

This timestamped report is the only repository write for this exact-record review. No YAML, inventories, older reports, history/status, generated pages, worktrees or GitHub items were changed. Downloaded XML and strict-output artifacts are temporary.
