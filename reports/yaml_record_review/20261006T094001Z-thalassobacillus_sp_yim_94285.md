# YAML Record Review: Thalassobacillus sp. YIM 94285

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/thalassobacillus_sp_yim_94285.yaml`
- Started UTC: 2026-10-06T09:38:21Z
- Finished UTC: 2026-10-06T09:40:01Z
- Verdict: pass

## Target

Read the entire 54-line generated `TaxonRecord` for `NCBITaxon:1035051`, Thalassobacillus sp. YIM 94285. It carries species rank, bacterial domain, parent `NCBITaxon:2621135`, ten root-first ancestors, genetic code 11, `EXACT` grounding and `SEEDED` mapping status. There are zero imported strains, one NCBI name attestation and one inline seed event. No optional synonyms, nomenclature, mappings, strain list, genome links, evidence objects, causal graph or discussions are asserted. This report reviews the record without changing it or promoting its status.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/thalassobacillus_sp_yim_94285.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/thalassobacillus_sp_yim_94285.yaml --out /private/tmp/thbyim94285-validation.tsv`: exit 0, one file scanned, zero errors; read the header-only diagnostic TSV.
- Structured comparisons verified identity, genetic code, full lineage, unique PATHS/scope entries, source attestation and inline event wording. Exact target scans in the type-material, merged-ID and dropped-record inventories returned no rows.
- Before report creation, `rg --no-ignore --hidden` searched identifier, full name and slug in `reports/yaml_record_review/` and `history/`, finding no prior report or separate history artifact. The inline seed event is present and schema-valid; this read-only review does not authorize another curation event.
- Not checked: full-corpus `just qc`, `just verify-corpus`, `just validate-all`, `just test`, `just validate-history`, generated-site drift and publication gates. Focused source comparisons are not complete corpus reproduction or release certification. No focused term/reference/history validator was invented. `just validate-products` is inapplicable because this record has no curator-added graph nodes.

## Identity and Grounding

The complete source rows at `data/raw/ncbitaxon_taxa.tsv:221862` and `data/catalog/ncbi_names-0005.jsonl.gz:31288` agree with the target. Its unique PATHS row is `data/taxa/PATHS.tsv:14343`; its scope row is `curation/seed_scope.tsv:322154`. The pinned backbone supplies no synonyms, replacement or classified children for this identifier.

Read full live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035051&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035051). They confirm the identifier, designation, species rank and bacterial placement; EFetch also confirms genetic code 11 and parent unclassified Thalassobacillus (`2621135`). All ten ancestors agree: root (`1`), cellular organisms (`131567`), Bacteria (`2`), Bacillati (`1783272`), Bacillota (`1239`), Bacilli (`91061`), Caryophanales (`1385`), Bacillaceae (`186817`), Thalassobacillus (`331971`) and unclassified Thalassobacillus (`2621135`). Datasets includes root; EFetch supplies the remaining labels and ranks. `EXACT` is identifier grounding, not a nomenclatural assertion of validly published species status.

## Evidence

The single NCBITAXON attestation correctly records one imported `NAME` with this source ID and designation from snapshot `2026-09-13`. The `2026-09-13T17:54:04Z` `SEEDED_FROM_SOURCES` event matches the maintained scope reason and attesting source. Counts represent imported source coverage, not biological abundance or proof of absence.

Exact, non-expanded NCBI searches for `txid1035051[Organism:noexp]` returned zero Assembly records and one Nuccore record, UID `333798093`. All returned IDs were accounted for. Read the complete metadata, references and features, excluding bases, for [JF792167.1](https://www.ncbi.nlm.nih.gov/nuccore/JF792167.1). It is a 631-base partial 16S rRNA marker with both ends marked partial; the source explicitly names YIM 94285 and `taxon:1035051`, without culture-collection, BioSample or assembly cross-references. It was created 28 May 2011, updated 26 August 2015, and submitted by C. Chen on 7 April 2011 from Yunnan Institute of Microbiology.

The accompanying Qijiaojing Lake study is marked unpublished, with no DOI or PMID. The marker supports its submitted identity only. It does not establish a culture-deposit equivalence, genome assembly, type status, enzyme phenotype or habitat assertion. Those broader claims are not made in this YAML. iModulonDB is inapplicable to this identity-only record, which has no gene, regulatory or transcriptomic claims.

## Completeness

Exact comparisons found no target entries in the imported BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventories. Together with the broader candidate inspection and absence of classified children, this is consistent with zero imported strains. It does not imply that the sequenced isolate never existed or preclude future deposit evidence.

The gitignore-independent search used `rg --no-ignore --hidden -n -z -i` across `data/raw/`, `data/catalog/`, `data/bacdive/`, `data/bvbrc/`, `data/gold/`, `data/seqcode/`, `data/straininfo/`, `data/atb/`, `curation/` and `history/`. It included compressed catalogs, the numeric taxon ID, full name, slug and separator variants of YIM 94285, then expanded to `JF792167`. Only `SOURCE.json` provenance sidecars were excluded from this candidate-data search; unrelated directories and external unindexed sources are not covered by the exhaustive-search claim.

Both searches returned the same 25 candidate rows. Every row was read completely through header-aware TSV or native JSON parsers, and address reconciliation found no unread or extra rows. Three are the target's backbone, native scientific name and scope; the other 22 are unrelated substring matches documented below. No supported missing culture deposit or eligible genome association was found. Empty optional nomenclature, mapping and mechanism fields are appropriate; the partial marker is not a missing genome.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The identity and provenance assertions agree with maintained inventories and inspected primary authority. The search results provide no defensible new association to this record.

## Recommended Edits

None required. Do not hand-edit generated YAML, promote `SEEDED`, or add curation history from this report. A future verified association belongs in maintained source acquisition/harmonization inputs and `src/taxonmech/seed.py` with a focused regression test; scope changes belong in `curation/seed_scope.tsv`. Taxonomy corrections belong at the upstream authority. Numeric substrings and a marker alone cannot establish deposit/genome identity.

## Follow-up Checks

No blocking follow-up. On a later source refresh, recheck exact NCBI taxonomy and marker identity, requiring explicit deposit-to-sequence evidence before adding strain/genome associations. After an actual curation change, rerun focused schema and strict validation and the documented corpus reproduction, history, tests and publication gates. This report does not certify those skipped gates.

## Additional Notes

The NCBI taxonomy browser failed in the web tool; complete official EFetch and Datasets responses succeeded. The full-name search supplied only secondary taxonomy summaries, and the exact marker query returned no results. Neither search snippets nor lack of web results were used to infer global biological or literature absence.

Full-row disposition of 12 unrelated bacterial source candidates:

| Source rows inspected | Identity and reason for exclusion |
| --- | --- |
| `data/bvbrc/bvbrc-0001.jsonl.gz:18816`; `data/catalog/ncbi_genbank-0000.jsonl.gz:45133`; `data/catalog/ncbi_refseq-0000.jsonl.gz:37934`; `data/catalog/gtdb_genomes-0005.jsonl.gz:20179`; `data/gold/projects.jsonl.gz:87480`; `data/catalog/allthebacteria.tsv.xz:66031` | Six rows concern Staphylococcus haemolyticus CN1175, taxon 1283, sample `SAMEA1035051`, explicitly paired `GCA_001223905.1`/`GCF_001223905.1`, BV-BRC `1283.75`, GOLD `Gp0140538`/`Go0134655`, and ATB run `ERR085228`/analysis `ERZ3070485`. GenBank/BV-BRC/GOLD retain `PRJEB2705`; RefSeq/GTDB use umbrella `PRJNA224116`. Sample-number substring only. |
| `data/bvbrc/bvbrc-0027.jsonl.gz:21481`; `data/catalog/ncbi_genbank-0037.jsonl.gz:21041`; `data/catalog/ncbi_refseq-0006.jsonl.gz:20154`; `data/catalog/gtdb_genomes-0007.jsonl.gz:6286` | Four rows concern Bacteroides thetaiotaomicron, taxon 818, strain `RTP21277st1_E11_RTP21277_210401`, sample `SAMN41035051`, paired `GCA_040928745.1`/`GCF_040928745.1`, BV-BRC `818.3295`. GenBank/BV-BRC retain `PRJNA1093465`; RefSeq/GTDB use `PRJNA224116`. No target/YIM identity. |
| `data/bvbrc/bvbrc-0006.jsonl.gz:8499`; `data/catalog/allthebacteria.tsv.xz:569521` | Two rows concern Mycobacterium tuberculosis run/designation `ERR1035051`, BV-BRC `1773.20485`, ATB sample `SAMEA3558584` and analysis `ERZ3501766`. Run-number substring only. |

Both ATB candidates retain available FASTAs and passing pipeline, HQ and Sylph filters. Their complete SeqKit sums and supplied OSF/AWS locations were inspected, not downloaded or recomputed. SeqKit sum is not MD5. Availability cannot overcome unrelated identity, and sample co-occurrence alone was not used to infer genome equivalence.

The remaining ten candidates are separate GOLD community or plant/fungal metatranscriptome projects. Each has an empty GOLD organism field. Each full source row was read; sample-number matches do not connect them to this bacterium:

| `data/gold/projects.jsonl.gz` line | GOLD project | BioProject | BioSample | Inspected title context/suffix |
| --- | --- | --- | --- | --- |
| 198004 | `Gp0296245` | `PRJNA502624` | `SAMN10350517` | Enriched soil aggregate microbial community, Iowa State University, Ames; MC6-MC0947-MT |
| 226723 | `Gp0331483` | `PRJNA502313` | `SAMN10350519` | Pinus contorta roots inoculated with Suillus, Duke University, North Carolina; S114(MN)xP.contorta(CO)_rep1 |
| 226728 | `Gp0331488` | `PRJNA502318` | `SAMN10350518` | Pinus contorta/Suillus, Duke University; S114(MN)xP.contorta(CA)_rep3 |
| 226782 | `Gp0331542` | `PRJNA502084` | `SAMN10350516` | Pinus contorta/Suillus, Duke University; S119(CO)xP.contorta(CA)_rep3 |
| 226784 | `Gp0331544` | `PRJNA502086` | `SAMN10350515` | Pinus contorta/Suillus, Duke University; S119(CO)xP.contorta(WY)_rep2 |
| 226787 | `Gp0331547` | `PRJNA502089` | `SAMN10350514` | Pinus taeda/Suillus, Duke University; S119(CO)xP.taeda(GA)_rep2 |
| 226793 | `Gp0331553` | `PRJNA502095` | `SAMN10350513` | Pinus banksiana/Suillus, Duke University; S120(CO)xP.bank(MN)_rep2 |
| 226794 | `Gp0331554` | `PRJNA502096` | `SAMN10350512` | Pinus banksiana/Suillus, Duke University; S120(CO)xP.bank(MN)_rep3 |
| 226799 | `Gp0331559` | `PRJNA502101` | `SAMN10350511` | Pinus contorta/Suillus, Duke University; S120(CO)xP.contorta(CA)_rep2 |
| 226807 | `Gp0331567` | `PRJNA502109` | `SAMN10350510` | Pinus taeda/Suillus, Duke University; S120(CO)xP.taeda(LA)_rep1 |

These are diagnostic exclusions, not new curated associations. Only this new review report is written; records, inputs, curation history, generated products and completed Eukaryota reviews remain untouched.
