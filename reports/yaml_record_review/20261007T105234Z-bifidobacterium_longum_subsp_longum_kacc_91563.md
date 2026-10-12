# YAML Record Review: Bifidobacterium longum subsp. longum KACC 91563

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bifidobacterium_longum_subsp_longum_kacc_91563.yaml`
- Started UTC: 2026-10-07T10:45:00Z
- Finished UTC: 2026-10-07T10:52:34Z
- Verdict: needs curation

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035817`, a bacterial strain under `NCBITaxon:1679` (Bifidobacterium longum subsp. longum), itself under species `NCBITaxon:216816`. The record has `grounding_status: EXACT`, `mapping_status: SEEDED`, genetic code 11, 11 root-first lineage entries, one GTDB mapping, three synonyms, a GTDB xref, zero listed BacDive strains, four source attestations, and one seed event.

The target is uniquely indexed at `data/taxa/PATHS.tsv:14677` and scoped at `curation/seed_scope.tsv:26088`. Generated YAML is read-only; future behavioral corrections belong in the seeder and, for source mapping semantics, the upstream transform.

## Validation

- `just validate data/taxa/bacteria/bifidobacterium_longum_subsp_longum_kacc_91563.yaml`: passed; no issues.
- `just validate-strict data/taxa/bacteria/bifidobacterium_longum_subsp_longum_kacc_91563.yaml --out /private/tmp/bifidoKacc91563-strict.tsv`: passed; one file, zero error rows. The actual TSV contains only its header.
- Parsed comparisons verified the complete backbone lineage, two NCBI synonyms, scope, path index, all four attestation values, and supporting inventory rows. These checks do not replace corpus reproduction.
- Live NCBI Taxonomy EFetch and Datasets responses agree on identifier, scientific name, strain rank, parent, lineage, and genetic code. Exact-taxid Assembly and Nuccore searches and their returned summary metadata were inspected.
- `just validate-products`: not applicable to this record; no curator-added graph nodes. NCBI lineage is carried taxonomy, not an OAK reconciliation target.
- `just validate-history`: not run; bounded ignored-inclusive content and filename searches found no target-specific external history artifact. The embedded seed event was inspected.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just test`, full-corpus schema validation, raw-provenance, generated-page, documentation-statistics, publication-budget, and vendored-sync gates.
- The target remained byte-identical to its initial full read. No regeneration, status promotion, history write, or GitHub mutation was performed.

Schema validity does not resolve the semantic synonym-scope finding below.

## Identity and Grounding

The pinned row at `data/raw/ncbitaxon_taxa.tsv:222178` and three native NCBI name rows at `data/catalog/ncbi_names-0005.jsonl.gz:31662` through line 31664 support the scientific name and the two exact designation variants containing `str. KACC 91563` and `strain KACC 91563`. Fresh [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035817&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035817) independently support this strain-level identity. An older browser search snippet showing an unranked node was not substituted for those inspected current responses.

All 11 lineage IDs, labels, and ranks match the pinned backbone and live NCBI chain, including Bacillati and Bifidobacteriales. The strain is distinct from its subspecies and species ancestors. No target row was found in the fully parsed `ncbi_type_material.tsv`, `ncbi_merged_ids.tsv`, or `dropped.tsv`; this does not establish a type-strain designation.

The GTDB identifier resolves within the pinned inventories to the species cluster `s__Bifidobacterium longum`, not to a strain synonym. Classification of a KACC 91563 genome in that cluster is supported. Identity of the entire species cluster with this single strain is not.

## Evidence

- **NCBI name and seed provenance:** the NCBI attestation is one `NAME` at the 2026-09-13 snapshot, not three names counted from its synonym rows. The seed event's four-source list and scope reason match the inventories. Its 2026-09-13T17:54:04Z timestamp agrees with the latest contributing manifest timestamp, from ATB; the raw and StrainInfo manifests precede it.
- **GTDB mapping and count:** `data/raw/gtdb_mappings.tsv:1443` reproduces the GTDB ID, label, `skos:closeMatch`, and count 1,131; `data/raw/gtdb_species.tsv:17232` identifies the species and genus. A complete exact-species census across the compressed native GTDB genome shards found 1,131 members spanning 60 NCBI taxid/name groups. Only three member rows carry taxid 1035817. The representative is `RS_GCF_000196555.1`, explicitly JCM 1217, taxid 565042, BioSample `SAMD00060951`. Thus 1,131 is the source species-cluster count, not the count of genomes established as KACC 91563.
- **Exact-strain genome evidence:** `GCA_000219455.1` and `GCF_000219455.1` at native GenBank line 3734 and RefSeq line 3216 of their respective `-0000.jsonl.gz` shards describe ASM21945v1, strain KACC 91563, `SAMN02603656`, and 2,395,764 bp across one chromosome and two plasmids. The GenBank project is `PRJNA66401`. Live Assembly metadata additionally gives culture collection `KACC:91563`. Native GTDB row `gtdb_genomes-0017.jsonl.gz:27737` classifies the same accession in the broader species cluster.
- **GOLD chain:** full primary rows at `data/gold/organisms.jsonl.gz:10152`, `projects.jsonl.gz:10006`, and `analyses.jsonl.gz:18284` connect `Go0011555` to `Gp0011555` and `Ga0027836`. The organism names KACC 91563; the project carries PRJNA66401; the analysis lists IMG `651053008` and CP002794-CP002796 with GCA_000219455.1. The analysis organism field is empty, so its organism connection is through the explicit project chain. Go/Gp/Ga are related records, not three extra genomes. This is consistent with the one-organism inventory attestation.
- **Literature:** the full [2011 genome announcement](https://journals.asm.org/doi/10.1128/jb.05620-11), DOI 10.1128/JB.05620-11, PMID 21742881, describes this deposited strain from healthy-neonate feces and reports a 2,385,301-bp chromosome plus 4,233-bp and 6,230-bp plasmids, deposited as CP002794-CP002796. Its sequencing and assembly account supports those accession-level observations. Dated annotation counts and introductory health-benefit statements are not independent current gene-function or strain-specific clinical evidence.
- **Other attestations:** `data/raw/gold_organisms.tsv:486` gives one organism and `data/raw/madin_taxa.tsv:677` gives four trait assertions. Counts and units are faithfully carried, not summed into a biological score. Original GOLD/Madin KGX edges were unavailable in the configured checkout, so the individual Madin assertions and an original-edge recount were not independently verified. The YAML does not assert their individual phenotype contents.

The live GTDB taxon page could not be retrieved, and its API schema request timed out. The GTDB conclusions above are explicitly about the inspected pinned primary metadata, not a claimed live-release comparison. GOLD's web page also failed; its local primary rows were available and fully read.

## Completeness

No direct descendants or target BacDive/LPSN/MediaDive/BactoTraits rows were found in the fully parsed corresponding inventories. Under the current model, `strain_count: 0` counts BacDive records in the target subtree; it does not deny that the NCBI taxon is a strain or that a deposited culture and genome exist. With no existing BacDive/deposit owner found for this target, the native genome evidence does not authorize fabricating a strain entry or joining on taxid alone.

Ignored and hidden files were included using `rg --no-ignore --hidden -z` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. The taxid, KACC designation variants, and slug search yielded 37 rows, all inspected in full using structured TSV/JSON readers, including compressed sources. An expanded search for the original GenBank/RefSeq accessions, chromosome/plasmid accessions, BioSample/project, GOLD identifiers, and the three other assembly/sample pairs yielded 24 rows, all already in that inspected set. All five source `SOURCE.json` files were separately parsed in full for target identifiers. Target history filenames and existing report filenames were checked independently of ignore rules. These are bounded local searches, not a claim that no external collection record exists.

The record makes no explicit definition, causal-graph, gene, regulator, transcriptomic, or clinical claim. Their optional slots need not be filled for this review; iModulonDB is not applicable. The missing exact-species/strain scope guard is consequential, whereas absence of optional enrichment alone is not another finding.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a species-cluster name is promoted to an exact synonym of a single strain.** The `synonyms` entry for `Bifidobacterium longum` is explicitly `EXACT_SYNONYM` of NCBITaxon:1035817. The target is a strain beneath both subspecies 1679 and species 216816. Native GTDB evidence places its genome in a 1,131-member species cluster whose representative is another named strain, JCM 1217. Species membership cannot support exact strain-name equivalence. The maintained owner is `src/taxonmech/seed.py`, the GTDB identity-promotion block around lines 450-469: an upstream `skos:closeMatch` alone sets `identity` and unconditionally adds the species xref and exact synonym without checking taxon scope. The raw predicate explains reproducibility, but not biological equivalence. The same assumption's mapping/xref presentation is part of this finding, not an additional counted defect. The retained upstream predicate warrants separate source-level review in kg-microbe; no locally invented replacement predicate or lineage reconciliation is prescribed.

No blocker was found in the core NCBI identity. No independent minor finding was established. Unavailable live GTDB and original KGX evidence are limitations, not fabricated additional defects.

## Recommended Edits

1. In `src/taxonmech/seed.py`, require scope-compatible identity evidence before deriving GTDB exact synonyms and identity xrefs. For this strain, keep the two NCBI strain-designation synonyms and stop emitting the species name as an exact synonym. Preserve the GTDB species classification and its supplied predicate/count as provenance, with an explicit non-equivalence scope explanation where appropriate. Do not hand-edit this YAML or silently alter the carried NCBI hierarchy.
2. Add regression coverage in `tests/test_seed.py` for a strain or other infraspecific NCBI target mapped to a broader GTDB species with `skos:closeMatch`. Confirm it retains the source mapping and cluster count without deriving a species-as-strain exact synonym. Preserve existing valid species-level mapping behavior and pooled-mapping tests. Review the originating predicate in kg-microbe separately if a corrected upstream mapping is pursued.
3. Only in an authorized implementation change, dry-run `just seed`, run `just seed-canary NCBITaxon:1035817`, and inspect the written canary before any broader regeneration. A reviewed or proposed status/history change is not authorized by this report.

## Follow-up Checks

- Run `uv run pytest tests/test_seed.py` after the maintained seeder fix, including the new rank/scope regression and existing species-level cases.
- Repeat the focused schema and strict commands above on the regenerated canary. Manually confirm the offending exact synonym is gone, the two NCBI synonyms remain, and the source GTDB mapping is still traceable without asserting equivalence.
- Recheck that the pinned GTDB cluster still has 1,131 members for this snapshot, while the target accession remains a member rather than the identity of the whole cluster.
- Before accepting a broader implementation, run the documented full-corpus reproduction and QC gates, including necessary generated-product checks. They were not run by this read-only review.
- If resolving source uncertainties, retrieve the original KGX mapping and four Madin assertions from the manifest-pinned transform and retry GTDB live metadata. Do not infer phenotype contents or silently replace the pinned source snapshot.

## Additional Notes

Exact-taxid NCBI searches returned five Assembly entries, including historical/replaced metadata, and 65 Nuccore entries. The five Assembly summaries were inspected in full; the Nuccore identity/accession/title/length/status summary fields were inspected for every returned entry. Whole-genome feature tables and sequence payloads were not downloaded or validated. The 65 entries comprise six original chromosome/plasmid GenBank/RefSeq records, one OZ183259 entry, two WGS master entries, 54 WGS contig entries, and two 397-base TPA tmRNA records. These are not 65 independently established genomes or strain deposits.

The other exact-taxid assembly entries retain distinct samples and isolate designations: GCA_964259395.1/CC00591/SAMEA114263563, GCA_964259695.1/CC00553/SAMEA114263533, and GCA_964259555.2/CC00571/SAMEA114263544. The latter is only 37,813 bp and carries unverified-source-organism and too-small-genome exclusions; its earlier .1 version is replaced. Historical RefSeq counterparts are suppressed. These source states were preserved rather than promoted through a shared taxid into culture equivalence with KACC 91563.

All six matching BV-BRC rows were read: the original full genome and its plasmid records are distinct database entries, and the CC00591/CC00571/CC00553 entries retain their own sample chains. The three corresponding ATB sample rows have available assemblies and PASS pipeline states, but do not establish an eligible existing culture-deposit owner here. Three additional ATB rows assigned the taxon retain their own filter states: two have unavailable FASTA and ASM_LEN; one has available FASTA but failed quality classification. Non-HQ status alone is not a blanket exclusion rule. An ATB match for ERR1035817 belongs to an unrelated Staphylococcus aureus sample and is only a numeric run-ID collision.

GTDB uses Actinomycetales in these source classifications, whereas the NCBI lineage carries Bifidobacteriales. This preserved source distinction is not a request to curate or reconcile lineage. Different GenBank, RefSeq, and publication annotation counts are dated source annotations, not evidence that the original assembly identity changed.

The configured kg-microbe checkout had no files under the searched gold, madin_etal, or gtdb transform directory patterns, including ignored/hidden files. That bounds the original-edge verification limitation; it is not an assertion that the source datasets do not exist elsewhere.

This review adds only its new timestamped report. Existing reports, YAML, maintained inputs, history, status, branches, and worktrees were not edited.
