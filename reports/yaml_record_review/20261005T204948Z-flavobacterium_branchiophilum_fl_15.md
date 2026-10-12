# YAML Record Review: Flavobacterium branchiophilum FL-15

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacterium_branchiophilum_fl_15.yaml`
- Started UTC: 2026-10-05T20:41:49Z
- Finished UTC: 2026-10-05T20:49:48Z
- Verdict: needs curation

## Target

The complete 90-line generated `TaxonRecord` was read before judgment. It denotes `NCBITaxon:1034807`, Flavobacterium branchiophilum FL-15, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:55197`, grounding `EXACT`, and lifecycle `SEEDED`. It has one GTDB species mapping, three exact synonyms, a GTDB xref, `strain_count: 0`, and NCBI, GTDB, and Madin attestations.

The record resolves uniquely at `data/taxa/PATHS.tsv:14161`, `curation/seed_scope.tsv:36161`, and `curation/legacy_page_paths.tsv:843`. This review concerns FL-15, not the species-level record or the distinct type-strain taxon `NCBITaxon:1218110`. Those records were consulted only to resolve placement and evidence ownership.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/flavobacterium_branchiophilum_fl_15.yaml`: exit 0, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/flavobacterium_branchiophilum_fl_15.yaml --out /private/tmp/fbf-strict-20261005.tsv`: exit 0, one file scanned, zero error rows. The TSV contains only its header.
- Structured comparisons checked the complete backbone, all twelve ancestors, seven taxon-attestation inventories, pinned path, scope, source counts, and seed-event wording. Identity and lineage match; faithfully reproducing the GTDB input does not prove its biological scope.
- Read-only execution of `normalize_culture_identifier` confirmed that `CIP 109950` and `CIP-109950` normalize to the registered key, while `FL-15` and separator-free `CIP109950` return an empty key under the current rules.
- Authority checks used live NCBI Taxonomy EFetch/Datasets, Assembly Datasets, Nuccore, PubMed, LPSN, BacDive, the CIP catalog, and the primary genome publication on 2026-10-05.
- `just validate-products` is not applicable: no curator-added causal graph is present. References were checked directly; no single-record reference validator was invented.
- Not run: `just verify-corpus`, `just qc`, full tests, full-corpus strict validation, provenance hashes, full history validation, generated-site drift, documentation statistics, publication-size budget, and vendored synchronization.

## Identity and Grounding

The pinned backbone at `data/raw/ncbitaxon_taxa.tsv:221691` agrees with live [NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034807): FL-15 is a strain under species 55197, with genetic code 11. The root-first lineage is:

`1 > 131567 > 2 > 3379134 > 1783270 > 68336 > 976 > 117743 > 200644 > 49546 > 237 > 55197`.

All labels and ranks agree with the pinned chain; live Datasets returns the same ancestor IDs. No descendants, type-material rows, retired status, or merged-ID redirect for this exact target were found in the inspected inventories. This does not make FL-15 the species type.

The two NCBI exact synonyms retain the strain qualifier and match the source's equivalent-name classes at `data/catalog/ncbi_names-0005.jsonl.gz:31085` through line 31087. The GTDB-derived bare species synonym has a different scope and is finding F1.

[LPSN 783844](https://lpsn.dsmz.de/species/flavobacterium-branchiophilum) describes the parent species and identifies BGD-7721 / ATCC 35035 / DSM 24789 and corresponding deposits as its type, not FL-15. Its local row `data/raw/lpsn_names.tsv:21914` maps to 55197, not 1034807. Omitting an LPSN nomenclatural entry from this strain record is appropriate; do not copy the type strain into it.

## Evidence

The GTDB species count is supported by `data/raw/gtdb_species.tsv:63523` and six complete native genome objects, all inspected. Their distinct strain contexts demonstrate that the species is broader than FL-15:

| GTDB genome | Native row in `data/catalog/` | Source strain context |
|---|---|---|
| `RS_GCF_000253275.1` | `gtdb_genomes-0014.jsonl.gz:6897` | FL-15; NCBI taxon 1034807 |
| `RS_GCF_965138885.1` | `gtdb_genomes-0004.jsonl.gz:40401` | CIP109950; species taxon 55197 |
| `RS_GCF_002217205.1` | `gtdb_genomes-0013.jsonl.gz:9486` | ATCC 35035; type-strain taxon 1218110; GTDB representative |
| `RS_GCF_007990815.1` | `gtdb_genomes-0006.jsonl.gz:46840` | NBRC 15030; type-strain taxon 1218110 |
| `RS_GCF_006716585.1` | `gtdb_genomes-0014.jsonl.gz:29070` | DSM 24789; species taxon 55197, type material |
| `RS_GCF_002530755.1` | `gtdb_genomes-0000.jsonl.gz:12386` | ATCC 35036; species taxon 55197 |

The raw GTDB mapping row at `data/raw/gtdb_mappings.tsv:1398` supplies the target's closeMatch and count. Rows 12329 and 296228 also map this same GTDB species to the type-strain taxon and parent species respectively. Six is a cluster-wide assembly count, not six FL-15 isolates. Only one member carries exact NCBI strain taxon 1034807; the additional CIP-labeled assembly must remain a separate assembly assertion, not be collapsed into the 2011 sequence.

[BacDive 136852](https://bacdive.dsmz.de/strain/136852), the [CIP 109950 catalog entry](https://catalogue-crbip.pasteur.fr/fiche_catalogue.xhtml?crbip=CIP+109950), and the native object at `data/bacdive/records.jsonl.gz:59155` identify FL-15 with CIP 109950. BacDive classifies it at species taxon 55197 and supplies no genome sequence in the captured object. The raw row `data/raw/bacdive_strains.tsv:59156` follows that classification. Its zero count in the target is therefore mechanically correct under the current subtree-gathering rule, not evidence that the culture is unknown.

The [primary genome study, DOI 10.1128/AEM.05625-11](https://journals.asm.org/doi/10.1128/aem.05625-11), explicitly identifies the sequenced FL-15 as CIP 109950 and deposits chromosome FQ859183 and plasmid FQ859182. The introduction, accession section, and genome-results section were inspected; [PubMed 21926215](https://pubmed.ncbi.nlm.nih.gov/21926215/) independently verifies the citation and abstract. This is evidence for the particular sequenced strain, not an assertion about every species member.

Live [NCBI assembly GCA_000253275.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_000253275.1/) confirms FL-15, taxon 1034807, current status, and an explicit current RefSeq pair GCF_000253275.1. Complete native summary rows are at `data/catalog/ncbi_genbank-0000.jsonl.gz:5136` and `data/catalog/ncbi_refseq-0000.jsonl.gz:4326`. Total sequence length is 3,563,292 bases. Inspected sequence metadata identifies the 3,559,884-base chromosome FQ859183.1 / NC_016001.1 and the 3,408-base pFB1 plasmid FQ859182.1 / NC_018751.1. RefSeq explicitly states the corresponding GenBank sequence identity. Two replicons are not two whole-organism assemblies.

The same assembly chain names BioSample SAMEA3138411 and BioProject PRJNA67123. RefSeq's PRJNA224116 is separate project context. Full native BV-BRC rows `data/bvbrc/bvbrc-0000.jsonl.gz:3283` and line 3284 retain `1034807.16` (plasmid) and `1034807.5` (complete/chromosome context), both naming GCA_000253275.1. The identifier prefix does not override the latter row's species-level taxon field.

GOLD's native chain is `Go0011963 > Gp0011963 > Ga0023908`, inspected at `data/gold/organisms.jsonl.gz:10535`, `projects.jsonl.gz:10393`, and `analyses.jsonl.gz:14916`. It supplies GCA_000253275.1 and IMG 2561511155, but its organism has only the bare FL-15 designation, not a culture-deposit match. The distinct CIP organism Go0283869 is represented in the generated parent record; it must not inherit the former analysis just because both names concern this strain.

Madin's five TRAIT_ASSERTIONs match `data/raw/madin_taxa.tsv:652`. NCBI's one NAME assertion, snapshot note, scope reason, and seed-event source list match their inputs. The Madin count is not five independently reviewed phenotypes: the configured original KGX edge file was unavailable, so the individual assertions were not recounted.

## Completeness

Candidate searches used `rg --no-ignore --hidden -n -z -i` over `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`, excluding per-file `SOURCE.json` manifests. Queries included identifier, species/strain names, FL-15 variants, CIP 109950 spellings, BacDive/SI identifiers, both relevant assembly pairs, samples, sequence accessions, and the GOLD chain. All 163 distinct candidate rows were read in full using TSV headers or decoded JSON. A final ignored-inclusive search for NC_018751, NR_076062, and HG789015 returned no additional native row.

The parent record at `data/taxa/bacteria/flavobacterium_branchiophilum.yaml:1786` retains BacDive 136852 / CIP 109950 and four related-source assertions, but no genome link on that strain entry. StrainInfo's complete native record at `data/straininfo/records.jsonl.gz:293565` confirms SI-ID 395565 / SI-DP 900661 / CIP 109950 / FL-15, with record-version DOI 10.60712/SI-ID395565.2; it supplies no sequence. Its supported deposit assertions are retained in `data/straininfo/strain_links.tsv:21128` and `related_records.tsv.gz:51882` and line 51883. Nothing was lost through a listing cap.

A newer [CIP109950 assembly GCA_965138885.1](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_965138885.1/) and its explicit RefSeq pair are also present natively and live: species taxon 55197, BioSample SAMEA117660485, project PRJEB85433, 132 contigs in 122 scaffolds. Its source spelling lacks the separator required by the current culture matcher. BV-BRC 55197.24 and the full ATB row at `data/catalog/allthebacteria.tsv.xz:379817` concern this newer sample; the latter has an available FASTA, PASS filters, and ENA analysis ERZ26976577. They are additional curation candidates, not automatic equivalents of the 2011 assembly.

For the original sample SAMEA3138411, the bounded ignored-inclusive search found no ATB row. Other species-level ATB samples and the type-strain links were inspected but do not transfer to FL-15. Numeric collisions with Listeria strain 1034807, a tuberculosis run, a Streptococcus sample, a Salmonella assembly-name suffix, and the unrelated Brasilonema FL15-MK94 were rejected.

Exact, non-expanded NCBI searches returned one Assembly result and eleven Nuccore results. All eleven nucleotide summaries were read: four entries are the paired chromosome/plasmid sequences, five are patent sequences, one is tmRNA, and one is 5S rRNA. The latter seven are not additional genomes. No claim of global sequence absence is made.

Optional definitions, phenotype lists, causal graphs, discussions, and record-level evidence are not blanket requirements. The genome-link gap in F2 is material to the repository's explicitly prioritized strain-to-genome use case, rather than a demand to populate every optional field. iModulonDB is not applicable to the target's claims.

## Findings

Counts: 0 blocker, 2 major, 0 minor.

1. **Major F1: a GTDB species is promoted to exact identity with an NCBI strain.** Target lines 45-55 and 62-63 retain a species closeMatch, emit the bare species as EXACT_SYNONYM, and expose its identifier as an equivalent xref. The GTDB attestation at lines 73-78 repeats that mapping. The six-member evidence above includes the distinct type strain and ATCC 35036; cluster membership does not establish species/strain equivalence. The source mapping belongs to upstream kg-microbe's GTDB transform, imported by `src/taxonmech/extract.py:501`. The local amplification occurs in `src/taxonmech/seed.py:454`, which treats closeMatch as identity without a rank guard. The count six itself is valid at species-cluster scope.

2. **Major F2: the published FL-15/CIP strain-to-reference-genome relationship is not available in the generated strain representation.** Target line 65 has no attached strain; the existing parent-species strain entry has deposit identifiers but no genome links. The CIP catalog, original paper, exact NCBI assembly, and retained native genome rows provide a concrete evidence chain. This is a curation-completeness gap, not a claim that the seeder dropped an eligible current input: BacDive files the culture at the parent species and lacks genome assertions, while other imports reject the bare alias or separator-free deposit spelling. A maintained correction belongs first in BacDive's explicit taxon/genome fields, captured through `scripts/fetch_bacdive.py` and consumed by `src/taxonmech/bacdive_v2.py` and `src/taxonmech/extract.py`. Any alternative local alias/evidence mechanism would require explicit provenance and reviewed tests; loosening `src/taxonmech/genome_sources.py:83` into a generic name matcher is not the fix.

## Recommended Edits

1. Correct the upstream GTDB species-to-strain mapping or retain it only as a clearly scoped membership relationship. Keep species-wide cluster metadata on species 55197. Add rank-aware protection to the GTDB identity branch in `src/taxonmech/seed.py` so a closeMatch cannot automatically produce a bare-species exact synonym or equivalent xref on a strain. Preserve both valid NCBI strain synonyms. Do not merely replace six with one.
2. Use the inspected CIP and publication evidence to curate an explicit FL-15/CIP-to-assembly assertion in the maintained source. Preserve the original GCA/GCF pair and the newer CIP-labeled assembly as distinct records, with their own samples, projects, and versions. Refresh and re-extract only after that correction is authorized. Validate other database links through their own source chains; do not copy type-strain genomes, infer assembly identity from a species name, or treat GOLD/SI/sample/project identifiers as genomes.
3. Re-seed affected records only through the validated writer after the maintained inputs and regression tests are corrected. Do not hand-edit either generated taxon YAML, source snapshots, or pages.

## Follow-up Checks

For F1, extend `tests/test_seed.py` with a STRAIN target receiving a GTDB species closeMatch and verify that membership cannot produce exact identity. Test the shared cluster against both FL-15 and type-strain targets while preserving its six-member count at species scope.

For F2, require an explicit sourced deposit/strain/assembly chain and test the original reference pair, newer assembly separation, source-specific BioSample chains, and rejection of unrelated bare aliases. Existing test surfaces include `tests/test_genome_sources.py`, `tests/test_genome_integration.py`, and `tests/test_source_expansion.py`. A source-only correction should be demonstrable without relaxing collection-authority matching.

After an authorized fix, run the documented extraction and seed dry runs, `just seed-canary NCBITaxon:1034807`, focused schema/strict checks, corpus reproduction, relevant tests, and full QC. Confirm the parent species still exposes the appropriate strain and provenance and that the type strain is not merged with FL-15.

## Additional Notes

- Worktree and HEAD remained `codex/record-review-extensimonas-20261003` / `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.
- The seed timestamp 2026-09-13T17:54:04Z is the newest of the raw, ATB, and StrainInfo manifest timestamps, as implemented by `src/taxonmech/seed.py:139`; it is not a claim of human review.
- GTDB species/genome pages and the GOLD analysis page could not be retrieved through the web tool; their statements above are explicitly from inspected pinned native metadata, not a verified current online census. StrainInfo's web page returned a JavaScript shell; native evidence was read in full. The PMC page returned a browser check, so the readable publisher article was used.
- The configured Madin edge path was tested directly and was unavailable. An ignored-inclusive filename search of the configured kg-microbe checkout found no Madin-named file. An exploratory parent-directory search encountered permission-denied directories; no claim about all alternate checkouts is made.
- Before creation, an ignored-inclusive target search of review reports and history found no prior match. This is a new report, not a modification of an earlier review.
- No YAML, source inventory, scope, history, status, generated product, or Eukaryota record was changed. No provider credits, external contacts, or GitHub mutations were used. The review writes only this report; validator output is in `/private/tmp`.
