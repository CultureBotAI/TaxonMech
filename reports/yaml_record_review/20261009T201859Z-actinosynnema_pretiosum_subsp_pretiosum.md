# YAML Record Review: Actinosynnema pretiosum subsp. pretiosum

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinosynnema_pretiosum_subsp_pretiosum.yaml`
- Started UTC: 2026-10-09T20:10:50Z
- Finished UTC: 2026-10-09T20:18:59Z
- Verdict: pass

## Target

Read the entire 1,645-line generated `TaxonRecord`, `NCBITaxon:103721`, including all nested source evidence. Initial large outputs were truncated; subsequent overlapping file reads covered the omitted middle. This is a subspecies, not the parent species `NCBITaxon:42197` or the sibling auranticum. It has ten ancestors, one LPSN nomenclature entry, two GTDB mappings, four sourced synonyms, one LPSN xref and one listed type strain. The strain carries 19 assembly assertions, 13 other genome-record assertions and 76 related-record assertions. These are source assertions, not counts of unique biological genomes.

HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. YAML SHA-256, verified before saving: `066895f4c4e904bcd36abf5a64371ca5ebd839c740144399867066cd5f72b8e9`. Ignored-inclusive filename search resolved one target and no previous report for its stem.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1`:

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/actinosynnema_pretiosum_subsp_pretiosum.yaml`: passed, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/actinosynnema_pretiosum_subsp_pretiosum.yaml --out /private/tmp/taxonmech-actino-103721-20261009-validation.tsv --workers 1`: one file, zero errors; TSV read and header-only.
- `uv run --offline python scripts/validate_history.py history`: reused this turn's 17-valid/zero-invalid-link result after a fresh empty tracked diff for history/schema. No second execution is claimed.
- Bounded structured comparisons verified the entire lineage, own backbone row, source attestation, slug and scope sentence. All 19/13/76 nested link assertions exactly match the committed raw, StrainInfo and ATB inventories, with no missing or extra assertion. Cross-source matched cultures are present in the strain's deposit list and pass existing CAFI whole-identifier normalization. These comparisons are not corpus reproduction or substitutes for primary-source review.
- Live NCBI taxonomy, identity fields for four versioned assemblies, complete annotations for six nucleotide accessions, StrainInfo strain/deposit data and ENA analysis metadata were inspected. LPSN, BacDive and the publisher's bibliography/abstract were inspected.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw/StrainInfo/ATB provenance replay and hashes, rendering or publication-size gates. `just validate-products` has no applicable causal-graph nodes here.
- Not checked: independent current IMG, GOLD and BV-BRC page availability, ATB FASTA/archive downloads, assembly sequence identity, or scientific article full text. GTDB tree pages failed in the web tool; pinned primary GTDB metadata supplied the checks below. The StrainInfo web page required JavaScript, but its public rich API succeeded. The DOI resolver failed in the web tool; the publisher page succeeded.

## Identity and Grounding

Backbone `data/raw/ncbitaxon_taxa.tsv:18550`, native names `data/catalog/ncbi_names-0000.jsonl.gz:38582` through `38584`, `data/taxa/PATHS.tsv:15214` and `curation/seed_scope.tsv:31675` agree with the YAML. The rank is `SUBSPECIES`, domain `BACTERIA`, parent `NCBITaxon:42197`, code 11, grounding `EXACT`, lifecycle `SEEDED`. The two NCBI synonyms preserve equivalent-name versus authority distinctions. Exact-ID scans found no merged or dropped entry and no child in the complete backbone; 19 pinned type-material rows were read.

[NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103721&retmode=xml) confirms identity, parent, rank, code, names and all named ancestors. [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103721) confirms the complete ancestor-ID chain including root. The pinned root-first chain through Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae, Actinosynnema and A. pretiosum agrees. No successor was returned.

Complete LPSN inventory row `data/raw/lpsn_names.tsv:15049` supports name `lpsn:772867`, authority, valid/legitimate/correct-name flags, six listed type designations and publication DOI. The [LPSN subspecies page](https://lpsn.dsmz.de/subspecies/actinosynnema-pretiosum-pretiosum) confirms these asserted names, status and designations. Its basionym/parent resolves to [LPSN 783322](https://lpsn.dsmz.de/species/actinosynnema-pretiosum), also read at `data/raw/lpsn_names.tsv:21415`. The parent name is only a related synonym, not an exact species/subspecies identity claim.

The [publisher's article page](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-33-2-314) verifies `DOI:10.1099/00207713-33-2-314`, Hasegawa et al., 1983, and the naming study. Its abstract distinguishes type strain ATCC 31281 from the additional strain ATCC 31280 and the auranticum type strain. No phenotype or mechanism was generalized from that abstract.

## Evidence

Source attestations match the inspected inventories: one NCBI name, one LPSN name, three genomes in the displayed GTDB source species, one BacDive strain and one GOLD organism. `data/raw/gold_organisms.tsv:510` and primary `data/gold/organisms.jsonl.gz:33836` support the GOLD count through `Go0040314`, ATCC 31280, taxon 103721. That organism is not substituted for the listed BacDive type strain. No own MediaDive, Madin or BactoTraits taxon-inventory row was found.

The 2026-09-12 scope reason records three sources at admission; it is historical scope text, not today's five-source count. The seed event faithfully carries that sentence and the five attesting sources. Its timestamp `2026-09-13T17:54:04Z` matches the newest raw/ATB/StrainInfo extraction timestamp under `src/taxonmech/seed.py:_seed_timestamp`, inspected this turn.

GTDB mappings `data/raw/gtdb_mappings.tsv:1470` and `1471` retain `skos:broadMatch` and explanatory pooling notes. Species inventory rows `data/raw/gtdb_species.tsv:5082` and `5085` each count three genomes. The schema defines this as volume under the source species, not three genomes specifically assigned to this subspecies. Complete native metadata corroborate the two pools:

- A. mirum: `RS_GCF_000023245.1` under NCBI 446462, plus `GB_GCA_003516205.1` and `GB_GCA_018139085.1` under NCBI 103721, both labeled ATCC 31280. Native rows are `gtdb_genomes-0006.jsonl.gz:22271`, `gtdb_genomes-0009.jsonl.gz:38419` and `gtdb_genomes-0002.jsonl.gz:10555` under `data/catalog/`.
- A. pretiosum: `RS_GCF_024171695.1` under NCBI 42197, `RS_GCF_039533475.1` under NCBI 103721 and `RS_GCF_042899395.1` under NCBI 3363910. Native rows are `gtdb_genomes-0014.jsonl.gz:3110`, `gtdb_genomes-0007.jsonl.gz:47350` and `gtdb_genomes-0009.jsonl.gz:2771`.

The inspected harmonization policy explicitly treats these broad mappings as source pooling, not synonymy. Neither GTDB pool became an exact synonym or xref, nor did its genome total propagate to the listed strain. The two ATCC 31280 assemblies are not assigned to ATCC 31281.

Complete BacDive projection `data/bacdive/records.jsonl.gz:13053` and inventory `data/raw/bacdive_strains.tsv:13054` support `bacdive:13213`, both source taxon IDs, all 14 culture identifiers and the genome assertions. The [BacDive page](https://bacdive.dsmz.de/strain/13213) independently supports the type-strain identity and deposit grouping. Listed type status also follows an exact intersection with the six LPSN type designations. No descendant adds another inventoried strain and there is no listing-cap omission.

The 18 raw assembly assertions, 12 raw genome-record assertions and 46 raw related assertions were compared field-for-field at `data/raw/strain_assemblies.tsv:22771`, `data/raw/strain_genome_records.tsv:18130` and `data/raw/strain_related_records.tsv:63761`, respectively, continuing through each strain's contiguous rows. Primary source records independently support their fields:

- DSM 44132: `GCA_024171695.1` / `GCF_024171695.1`, GTDB `RS_GCF_024171695.1`, BV-BRC `42197.8`, IMG `2596583522`, sample `SAMN03080609`, and project `PRJNA262061`. The GOLD chain is `Go0103586 -> Gp0103586 -> Ga0056966`.
- JCM 7344: `GCA_039533475.1` / `GCF_039533475.1`, GTDB `RS_GCF_039533475.1`, BV-BRC `103721.19`, IMG `8147942845`, sample `SAMD00645381`, and project `PRJDB10510`. The GOLD chain is `Go0606041 -> Gp0854917 -> Ga0682008`.
- Additional GOLD organism references `Go0029746`, `Go0606040` and `Go0606042` match ATCC 31281, IFO 13726 and NBRC 13726. They remain organism references, not genomes.

The complete native BV-BRC rows are `data/bvbrc/bvbrc-0000.jsonl.gz:3413` and `bvbrc-0020.jsonl.gz:13356`. Complete GOLD projections were read at organism rows 25258, 58298, 437030, 437031 and 437032; project rows 59591 and 620588; analysis rows 36080 and 454738. Both analysis rows resolve through their explicit project to one organism. Their exact assembly/IMG fields, whole culture matches and parent-species taxon values agree with the YAML. Source classification at species level is retained without rewriting the subspecies lineage.

Complete native NCBI rows `data/catalog/ncbi_genbank-0022.jsonl.gz:19147`, `ncbi_refseq-0004.jsonl.gz:19014`, `ncbi_genbank-0036.jsonl.gz:4893` and `ncbi_refseq-0006.jsonl.gz:2929` verify both accession pairs. Live identity views for [DSM 44132](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_024171695.1/dataset_report) and [JCM 7344](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_039533475.1/dataset_report), plus both corresponding GCF queries, report all four accessions current and explicitly paired. Pinned RefSeq/GTDB tables retain umbrella project `PRJNA224116`; the live assembly API exposes the submission projects above. Those source-specific fields are not interchangeable. Unversioned BacDive/StrainInfo accessions remain unversioned.

The complete native StrainInfo record `data/straininfo/records.jsonl.gz:70262` and [live rich API](https://api.straininfo.dsmz.de/v2/data/strain/max/92950) agree on SI-ID92950, record DOI `10.60712/SI-ID92950.3`, published status, BacDive reference and deposit-specific sequences. Twelve matched deposits each supply a strain and deposit reference. CCRC 13428 is not in the BacDive deposit list and is not silently treated as BCRC 13428. `GCA_024171695` and DQ459061-64 explicitly name DSM 44132/SI-DP169254; AB303365 names NBRC 15621/SI-DP335289; AF114800 names NRRL B-16060/SI-DP182832. All 30 related assertions and one assembly match `data/straininfo/related_records.tsv.gz:32395` through 32424 and `data/straininfo/assemblies.tsv:2102`. The KCTC/NRRL deposit classifications at parent species level remain visible.

NCBI GenBank annotations for [AB303365.1](https://www.ncbi.nlm.nih.gov/nuccore/AB303365.1), [AF114800.1](https://www.ncbi.nlm.nih.gov/nuccore/AF114800.1), and [DQ459061.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ459061.1), [DQ459062.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ459062.1), [DQ459063.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ459063.1), [DQ459064.1](https://www.ncbi.nlm.nih.gov/nuccore/DQ459064.1) were fully inspected. All carry taxon 103721 and the expected strain annotations. Lengths are 1472, 1504, 417, 417, 413 and 417 nt; declared/actual lengths agree. These are correctly typed nucleotide references, not genome assemblies. No mechanistic conclusion rests on their bibliographies.

The ATB link exactly matches `data/atb/strain_links.tsv:791` and assembly row `data/atb/assemblies.tsv:3709`: release 2025-05, `SAMN03080609`, `SRR4136502`, `ERZ26995746`, PASS filters, SeqKit sum and archive/download metadata. All seven retained BioSample evidence paths correspond to the DSM 44132 source rows. The [ENA analysis response](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=ERZ26995746&result=analysis&fields=analysis_accession,sample_accession,run_accession,study_accession&format=json) confirms that analysis/sample/run chain. ATB remains a separate assembly assertion, not a declaration of cross-database sequence identity.

## Completeness

Ignored-inclusive, hidden-inclusive and compressed-content searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identity/name/slug searches returned 169 candidate lines; exact assembly and GOLD-chain searches returned 87. These are discovery counts, not a claim that every broad numeric hit was independently reviewed. The relevant own rows, full nested inventories and primary chains cited above were inspected. No global absence claim is made from unread numerical candidates.

Fully read numeric near misses include BacDive 103721 (a Rhodococcus record), cultures CIP 103721 and DSM 103721 (other taxa), and GTDB assembly-size/N50 values. Those numbers do not supply taxon or strain links. SeqCode catalog row `data/seqcode/names.jsonl.gz:1281` is a real name lead, ID 1515, but the catalog lookup alone neither requires an attestation nor establishes a nomenclatural identity mapping. The existing legacy page mapping at `curation/legacy_page_paths.tsv:906` is consistent.

All five source metadata JSON files were parsed. The BacDive request-list match to 103721 refers to that unrelated BacDive ID, not this NCBI taxon. Ignored-inclusive history content/filename checks found no separate own history entry within the searched roots; the YAML's seed event is present and valid.

No missing required representation or unsupported existing claim was established. LPSN's displayed type list has additional aliases beyond the six retained by the pinned LPSN transform; the record's six are supported and are not stated to be exhaustive. FERM/VKM aliases also remain visible in the BacDive deposits. Optional definition, general literature evidence and causal graphs need not be invented. iModulonDB is not applicable: nucleotide-reference titles here do not assert a functional gene, regulator, pathway, trait or transcriptomic result.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, nomenclature, mapping/count semantics and all existing source-specific strain links are supported within the checked scope. Availability and full-corpus limitations remain explicit.

## Recommended Edits

None required. Preserve `SEEDED`, NCBI identity, source-specific ranks and supplied accession versions. Do not merge the species/subspecies, transfer ATCC 31280 assemblies to ATCC 31281, equate the GTDB pools, or infer CCRC/BCRC interchangeability.

Future supported enrichment belongs in maintained source inputs and their owners: `src/taxonmech/extract.py`, `src/taxonmech/genome_sources.py`, `src/taxonmech/straininfo_links.py`, `src/taxonmech/atb.py` and `src/taxonmech/seed.py`, as applicable, with focused tests and regeneration. Refresh the upstream LPSN transform for additional type aliases rather than editing generated YAML. Taxonomy corrections belong upstream at the relevant authority.

## Follow-up Checks

No finding requires corrective validation. Before future regenerated publication run documented source provenance/replay gates, `just verify-corpus` and `just qc`. Recheck every changed whole-deposit/source chain and preserve sample/project versus genome semantics. Independent availability checks and sequence comparisons are needed before claiming downloadable resources or cross-database genome identity; they are not inferred here.

## Additional Notes

Only `NCBITaxon:103721` is judged. Eukaryota was not reopened. No YAML, source inventory, scope, history, status, branch, worktree or GitHub item was changed. This new report is the only repository write for this target; previous reports remain intact. No paid research was used.
