# YAML Record Review: Rickettsiella pyronotae

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/rickettsiella_pyronotae.yaml`
- Started UTC: 2026-10-05T08:43:23Z
- Finished UTC: 2026-10-05T08:46:27Z
- Verdict: pass

## Target

The entire 61-line `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034384`, Rickettsiella pyronotae, rank `SPECIES`, domain `BACTERIA`, with `grounding_status: EXACT` and `mapping_status: SEEDED`. This is a generated record. Source capture/transforms, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, and `curation/seed_scope.tsv` own future changes according to their respective responsibilities; generated YAML is not a manual curation surface.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/rickettsiella_pyronotae.yaml`: exit 0, no issues found.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/rickettsiella_pyronotae.yaml --out /private/tmp/pyronotae-strict-20261005.tsv`: exit 0; one file scanned, zero error rows.
- Read-only structured comparisons checked the identity, complete lineage, synonyms, all direct source inventory rows, unique PATHS/scope entries, attestation, and inline seed event. Full scans of the backbone and merged/dropped/type-material tables were also completed.
- `just verify-corpus`: not run. It is a full-corpus reproduction gate; `--max-diffs` caps diagnostics rather than narrowing the record scope. These bounded source comparisons do not establish full reproduction.
- `validate-products`: not applicable, with no curator-added causal graph. `validate-history`: not run; ignored-inclusive filename and content searches found no target history artifact. The inline event was checked separately. No undocumented single-record term/reference validator was substituted.

## Identity and Grounding

The pinned backbone row `data/raw/ncbitaxon_taxa.tsv:221582`, live [NCBI Taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034384&retmode=xml), and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034384) agree on the species identity and parent `NCBITaxon:59195` (Rickettsiella). EFetch confirms genetic code 11. Every root-first ancestor matches the pinned backbone: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Legionellales, Coxiellaceae, Rickettsiella. The live Datasets ancestor IDs agree. The full backbone scan found no children.

The complete name objects at `data/catalog/ncbi_names-0005.jsonl.gz:30955` through line 30958 distinguish the scientific name, the Kleespies et al. 2011 authority, and two names of class `includes`: Rickettsiella symbiont of Pyronota setosa and Rickettsiella symbiont of Pyronota sp. Live EFetch confirms those classes. All three alternate names are correctly represented as `RELATED_SYNONYM`, not inflated to exact equivalence.

The merged-ID table at `data/raw/ncbi_merged_ids.tsv:1010` maps old `NCBITaxon:1034383` to this target. A separate [EFetch request for the old ID](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1034383&retmode=xml) returns taxon 1034384 and lists 1034383 under AkaTaxIds; Datasets independently resolves the same query to 1034384. The old ID has no row in the current backbone, PATHS index, or scope. The target is the active destination, not a retired taxon requiring deprecation. Neither the dropped table nor the type-material table contains the target.

[LPSN record 31720](https://lpsn.dsmz.de/species/rickettsiella-pyronotae) lists the Kleespies et al. 2011 name as not validly published and preferred rather than correct, with nomenclatural type cf2-8 and 16S marker HM017957. Exact NCBI grounding does not assert valid nomenclatural publication; the YAML makes no conflicting publication-status claim.

## Evidence

- The single `NCBITAXON` attestation matches the backbone: target ID, label, one `NAME`, and 2026-09-13 snapshot. This counts the source taxon concept, not isolates, experiments, or genomes.
- Complete direct inventory scans returned no target rows in BacDive, LPSN, GTDB mappings, GOLD organisms, MediaDive, Madin, or BactoTraits. A separate whole-table LPSN scan found neither `lpsn:31720` nor the name. Consequently no existing mapped LPSN row was lost during seeding. The live page is a possible upstream enrichment, not a populated inventory assertion that can be pasted into this generated record.
- The original description was verified through the full PubMed XML and abstract for [PMID 21640120](https://pubmed.ncbi.nlm.nih.gov/21640120/), DOI `10.1016/j.jip.2011.05.017`, Kleespies and colleagues, Journal of Invertebrate Pathology 107(3):206-211 (2011). Its microscopy and 16S/ftsY analysis place the studied organism in Rickettsiella and propose the pyronotae pathotype, probably synonymous with R. popilliae under the classification then in use. That historical interpretation is not silently substituted for the current NCBI species node.
- The follow-up was independently checked through PubMed XML and abstract for [PMID 22856625](https://pubmed.ncbi.nlm.nih.gov/22856625/), DOI `10.1111/j.1365-2672.2012.05419.x`, Leclerque and colleagues, Journal of Applied Microbiology 113(5):1228-1237 (2012). It treats the Costelytra- and Pyronota-associated organisms as related but nonidentical pathotypes and discusses their synonymy with R. popilliae. This does not authorize exchanging strain designations, nucleotide accessions, or genomes between the records. Both studies were checked at abstract/bibliographic level, not full text.
- NCBI Assembly query `txid1034384[Organism:noexp]` returned zero records with a phrases-not-found warning. This is a bounded query result, not proof that no genome exists anywhere. The corresponding Nuccore query returned seven IDs. All seven records' complete metadata, source qualifiers, references, and feature annotations were inspected, excluding sequence bases and protein translations.
- Each nucleotide record identifies strain cf2-8 and taxon 1034384: [HM017957.1](https://www.ncbi.nlm.nih.gov/nuccore/HM017957.1), 1,357 bp partial 16S; [HQ589037.1](https://www.ncbi.nlm.nih.gov/nuccore/HQ589037.1), 996 bp complete ftsY CDS; [JN565691.1](https://www.ncbi.nlm.nih.gov/nuccore/JN565691.1), 786 bp partial gidA; [JN565692.1](https://www.ncbi.nlm.nih.gov/nuccore/JN565692.1), 885 bp partial sucB; [JN695775.1](https://www.ncbi.nlm.nih.gov/nuccore/JN695775.1), 894 bp partial rpsA; [JF519848.1](https://www.ncbi.nlm.nih.gov/nuccore/JF519848.1), 912 bp partial 23S; and [JF708250.1](https://www.ncbi.nlm.nih.gov/nuccore/JF708250.1), 253 bp partial 23S with an intervening sequence. None is an assembly. The 16S/ftsY records cite the 2011 paper and retain host Pyronota sp.; the three later protein markers cite the 2012 paper and retain Pyronota setosa. The two 23S records also say Pyronota setosa but retain an unpublished reference and direct submission. These source-specific host labels and references were not normalized into one unsupported assertion.
- The complete pinned SeqCode object at `data/seqcode/names.jsonl.gz:34915` supplies ID 36802, the matching name, and its resource/API URLs. This minimal catalog object does not supply an NCBI mapping or a type-genome claim, so it does not create a taxon xref or genome association.

## Completeness

The zero strain count agrees with the BacDive inventory; there are no descendant taxa from which additional BacDive strains could be gathered. A literature/type designation and gene sequences do not by themselves establish a BacDive strain, eligible culture-deposit join, or assembly. The current record is not missing an identified, eligible genome link.

Ignored-inclusive, compressed-aware searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. They covered current and merged taxon IDs, name/slug, both host-associated names, cf2-8 spelling variants, the LPSN ID, and all seven marker accessions. The primary search returned eight contexts, the old-ID/type-marker search four, and the expanded numeric/accession search thirteen. No target-specific strain/deposit, genome/sample chain, mapped LPSN entry, or history artifact was found in those roots. Searches included ignored files and compressed native catalogs.

False positives were inspected and rejected: NEAU-CF28 belongs to Micromonospora; SAMEA1034383 and SAMEA1034384 are BioSamples associated with Streptococcus equi subsp. zooepidemicus, not the corresponding NCBI taxonomy IDs; 1034383 in an unrelated genome's size statistics is not a taxon match. None supplies a strain or genome join.

Optional literature, phenotype, definition, and causal-graph slots do not require speculative filling. The unimported live LPSN name is a bounded enrichment opportunity. Neither the inventory's incompleteness relative to the live name page nor an inaccessible paper body proves a defect in the assertions actually generated here.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within this record review. Identity, related-name scope, attestation, strain count, and seed history are supported. Nomenclatural qualification and the literature/NCBI taxonomic distinction remain explicit in this report. This verdict is not human sign-off or a promotion to `mapping_status: REVIEWED`.

## Recommended Edits

None required for the current generated record. Optional future enrichment belongs to the upstream kg-microbe LPSN/LPSN-API capture and mapping for name 31720, imported by `src/taxonmech/extract.py:420` into derived `data/raw/lpsn_names.tsv` and emitted by `src/taxonmech/seed.py:386`. Establish an explicit mapping and preserve non-valid/preferred status, the cf2-8 designation, and HM017957 as a marker. The exact reason for the missing upstream name cannot be diagnosed from the available transformed inputs.

Retain the current NCBI identity and related-synonym scopes. Do not merge this record with R. costelytrae or R. popilliae, invent a culture collection or assembly for cf2-8, or add an alias as a new record merely because an old taxonomy ID existed.

## Follow-up Checks

After a separately authorized source refresh, verify the LPSN name/status mapping, marker provenance, and handling of merged NCBI IDs before regeneration. Rerun both focused validators; use `just verify-corpus` to prove full reproduction after an authorized regeneration. Any newly proposed strain-genome link requires explicit deposit or sample/provenance evidence, not species similarity. No further action is needed to accept this bounded review.

## Additional Notes

- `data/taxa/PATHS.tsv:14046` uniquely maps the target to this stem. `curation/seed_scope.tsv:321894` supplies the 2026-09-13 scope reason. The 2026-09-13T17:54:04Z inline seed event correctly names NCBITAXON and the one-source scope rule.
- Ignored-inclusive filename searches found no pre-existing target report or history artifact; history content was searched as well. The preceding R. costelytrae report was not used as this record's verdict.
- The review skill was reread. Previously inspected CLAUDE guidance, curation skill/checklist, justfile, curation/harmonization/schema/history documentation, and schema remained unchanged in the current tracked worktree.
- The NCBI browser failed, while EFetch and Datasets succeeded for both current and old IDs. ScienceDirect returned 403 and the Oxford browser request for the follow-up failed; both PubMed XML records supplied their complete abstracts and citations. No full-text access, literature completeness, or sequence-identity calculation is claimed.
- An ignored-inclusive filename search of the configured kg-microbe checkout found no `nodes.tsv` or `edges.tsv`; original transformed LPSN inputs were unavailable there. This prevents diagnosing the source-capture omission, not reviewing the current NCBI-backed record.
- iModulonDB is not applicable: no gene, regulator, pathway, stress-response, or transcriptomic assertion is present in the YAML. Marker metadata were inspected only for identity and the gene/genome distinction.
- Tracked and staged diffs were empty before report creation. No taxon YAML, source inventory, code, page, lifecycle status, curation event, prior report, or history entry was edited. No paid research, external contact, or GitHub mutation was performed.

