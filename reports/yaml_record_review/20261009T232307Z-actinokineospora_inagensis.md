# YAML Record Review: Actinokineospora inagensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/actinokineospora_inagensis.yaml`
- Started UTC: 2026-10-09T23:15:40Z
- Finished UTC: 2026-10-09T23:23:07Z
- Verdict: pass

## Target

Entire 989-line generated `TaxonRecord` read. `NCBITaxon:103730` denotes Actinokineospora inagensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:39845`, genetic code 11, grounding `EXACT`, status `SEEDED`. All nine ancestors, nomenclature, authority synonym, xrefs, the single nested BacDive strain, four source attestations and seed event were inspected. Its 9 assembly, 7 genome-record and 45 related-record assertions are 61 source/field-specific assertions, not 61 independent genomes or cultures.

The target is the species, not its separately indexed child `NCBITaxon:1120935`, Actinokineospora inagensis DSM 44258. The child taxonomy and native evidence were checked for the species' descendant-strain gathering; no child-record review is claimed.

## Validation

Commands used the repository environment with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/actinokineospora_inagensis.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/actinokineospora_inagensis.yaml --out /private/tmp/taxonmech-actinokineospora-inagensis-20261009-validation.tsv --workers 1`: one file, zero errors; TSV reread and contains only its header.
- `python scripts/validate_history.py history`: 17 history records valid, zero invalid links.
- Structured comparisons independently matched the complete nine-ancestor chain, exact scope/index rows, seed text and every own strain-link assertion against the raw, StrainInfo and ATB inventories: no missing or extra assertions. These bounded comparisons are not corpus reproduction.
- Public NCBI taxonomy, focused assembly and BioProject metadata, sequence metadata, ENA, DataCite, SeqCode, LPSN and BacDive checks succeeded within the scopes below. Both ATB artifact HEAD requests returned HTTP 200. Live GTDB page access was unsuccessful; an attempted species API route returned 404 and is not evidence that the species is absent.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, raw-provenance replay, rendering and publication-size gates. `just validate-products` has no applicable graph nodes. No independent genome assembly, sequence-equivalence, or downloaded-artifact checksum validation was performed.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18556` agrees with the identity, authority synonym, rank, parent and code. The complete root-first lineage matches the pinned 2026-09-13 backbone. Live [NCBI species taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103730) and [child-strain taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1120935), plus their EFetch XML, confirm that DSM 44258 is a strain directly below this species. No exact own-ID merge or dropped row was found in the complete corresponding raw tables.

`data/raw/lpsn_names.tsv:14918` supplies `lpsn:772682`, the authority with the 2018 emendation, legitimate/validly published/correct-name status, five type-deposit identifiers, two publication DOIs and AF114799. The current [LPSN species page](https://lpsn.dsmz.de/species/actinokineospora-inagensis) supports the name, marker, original publication, notification and emendation. Its displayed type list also includes VKM Ac-1982 and YU4-1; the generated nomenclature faithfully retains its pinned five-deposit input, while the nested BacDive entry already includes VKM Ac-1982. This is not a wrong-type-strain finding.

The original [Tamura et al. 1995 paper](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-2-371) explicitly identifies YU4-1 (= IFO 15663) as the type of this species. The second DOI resolves to the [1995 notification](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/00207713-45-3-621), not another strain experiment. Publisher identity/abstract information was inspected, not both full texts. [SeqCode record 1291](https://api.seqco.de/v1/names/1291.json) independently corroborates the ICNP name and type-deposit chain; it does not make this a SeqCode-only name.

The GTDB xref is explicitly supplied by the pinned LPSN row. There is no direct species-level GTDB mapping row: `data/raw/gtdb_mappings.tsv:4409` belongs to the child strain. Its one genome agrees with `data/raw/gtdb_species.tsv:4706` and the complete native `data/catalog/gtdb_genomes-0012.jsonl.gz:42985` record, RS_GCF_000482865.1. Accordingly, no child GTDB mapping/count is promoted into a species-level attestation. GTDB's Mycobacteriales placement is preserved separately from NCBI's Pseudonocardiales lineage.

## Evidence

The four attestations preserve their different units and scopes:

| Source | Count and unit | Support |
| --- | --- | --- |
| NCBITAXON | 1 NAME | Own backbone row and 2026-09-13 snapshot |
| LPSN | 1 NAME, closeMatch | Own LPSN row 772682 |
| BACDIVE | 1 STRAIN | BacDive 13202 gathered from child taxon 1120935, explicitly recorded in `classified_as` and the attestation note |
| GOLD | 6 ORGANISM | Six native organism records filed directly under species 103730; descendant organisms are not counted |

The six direct GOLD organisms are Go0218756 (HUT-6566) and Go0606214 through Go0606218 (IFO 15663, JCM 9923, KCTC 9571, MTCC 2685 and NBRC 15663). The DSM organism Go0013928 is filed under child 1120935 and is not added to the species' direct-only count. Likewise, the child's MediaDive, Madin and BactoTraits counts are not propagated. This matches `src/taxonmech/seed.py` and does not discard the explicitly gathered BacDive strain.

`data/bacdive/records.jsonl.gz:13042`, `data/raw/bacdive_strains.tsv:13043` and the live [BacDive 13202 page](https://bacdive.dsmz.de/strain/13202) agree on the type flag, species/strain taxon IDs and all nine culture identifiers: DSM 44258, IFO 15663, JCM 9923, KCTC 9571, MTCC 2685, NBRC 15663, NCIMB 13659, NRRL B-24050 and VKM Ac-1982. The source's most-specific strain classification is retained in `classified_as`.

BacDive reference 67770 supplies unversioned GCA_000482865, IMG 2528768220 and BV-BRC 1120935.3. Complete native BV-BRC row `data/bvbrc/bvbrc-0000.jsonl.gz:12254` independently links DSM 44258 to GCA_000482865.1, SAMN02441427 and PRJNA188797. Its generic culture-collection value `DSM Z` is not used as an exact deposit match; its full strain field is.

Complete GOLD analysis/project/organism rows (`data/gold/analyses.jsonl.gz:1318`, `projects.jsonl.gz:12061`, `organisms.jsonl.gz:12288`) support Ga0002695 -> Gp0013928 -> Go0013928, IMG 2528768220 and the same assembly/sample/project. Both full-deposit organism fields remain separate provenance assertions. The five additional direct-species culture-deposit organisms have their own preserved links; they are not counted as five additional sequenced genomes.

Native NCBI assembly rows `data/catalog/ncbi_genbank-0000.jsonl.gz:15454` and `ncbi_refseq-0000.jsonl.gz:12995` match the stored links and exact DSM deposit. Focused live [GenBank](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000482865.1/dataset_report) and [RefSeq](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCF_000482865.1/dataset_report) responses confirm the current paired scaffold assemblies, child taxon, DSM 44258 and SAMN02441427. The pinned RefSeq and GTDB rows use PRJNA224116, whereas current Datasets responses project PRJNA188797. Focused [BioProject XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=224116,188797&retmode=xml) confirms the former is a multispecies RefSeq annotation project and the latter the DSM strain sequencing project with the target assembly/sample linkage. These source-specific associations should not be silently rewritten.

Complete StrainInfo native row `data/straininfo/records.jsonl.gz:38342` supports SI-ID 50540, DOI 10.60712/SI-ID50540.3, published-online status and eight available, non-erroneous deposits. The full designation/CAFI matches are DSM 44258/169377, IFO 15663/169378, JCM 9923/169379, KCTC 9571/169380, NCIMB 13659/211650, VKM Ac-1982/211651, NRRL B-24050/221603 and NBRC 15663/336000. [DataCite identity metadata](https://api.datacite.org/dois/10.60712/SI-ID50540.3) independently confirms version 3, the species, eight deposits and 2025-02-25 issuance. It is not substituted for the native deposit-level evidence.

StrainInfo's genome explicitly references DSM deposit 169377; AF114799 explicitly references NRRL deposit 221603. Both same-deposit checks pass. MTCC 2685 appears as an alias/designation, not a ninth StrainInfo deposit, so no SI-DP is invented. The unversioned assembly and nucleotide accessions remain unversioned. [NCBI AF114799 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AF114799) resolves to AF114799.1, a 1,507-base partial 16S sequence for NRRL B-24050T, taxon 103730 and type-strain qualifier. Its [Labeda and Kroppenstedt paper](https://pubmed.ncbi.nlm.nih.gov/10826820/) concerns partial 16S phylogeny; its historical family proposal is not substituted for the current NCBI lineage.

ATB catalog row `data/catalog/allthebacteria.tsv.xz:1029788` matches `data/atb/assemblies.tsv:2887` and the YAML: release 2025-05, dataset 661k, SAMN02441427, SRR1801766, ERZ4057352, PASS assembly/sylph/HQ filters and an available FASTA. The complete SeqKit value is `seqkit.v0.1_DLS_k0_8e175c5eceaa6ff7e542ecde0d40267d`; it is not an MD5. Six exact DSM/BioSample provenance assertions in `data/atb/strain_links.tsv:779` are retained. Five `shares_biosample` genome-link rows (3412-3416) were inspected with their source-native evidence. Shared BioSample does not establish identical sequences or an equivalent NCBI assembly.

Live [ENA analysis ERZ4057352](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ4057352) names SAMN02441427, SRR1801766 and the Shovill assembly under PRJEB45982; the [ENA run report](https://www.ebi.ac.uk/ena/portal/api/filereport?accession=SRR1801766&result=read_run&fields=run_accession,sample_accession,secondary_sample_accession,study_accession,tax_id,scientific_name,experiment_title&format=json) confirms DSM 44258, child taxon 1120935 and original project PRJNA188797. These are reassembly versus original sequencing contexts, not contradictory taxon assignments. The generic ENA analysis-type label is not evidence of a clinical habitat claim. HEAD checks succeeded for the [AWS FASTA](https://allthebacteria-assemblies.s3.eu-west-2.amazonaws.com/SAMN02441427.fa.gz) and [OSF archive](https://osf.io/download/667155860f8c8017d33c9426/); the latter returns filename `atb.assembly.r0.2.batch.93.tar.xz`. No archive or FASTA payload was downloaded or checksum-recomputed.

## Completeness

The exhaustive bounded candidate search used `rg --no-ignore --hidden -n -z -i`, including ignored, hidden and compressed files in `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It searched the species label/slug, both taxonomy IDs, BacDive key, full culture identifiers, assembly, sample, run, analysis and marker. All 304 candidate rows were inspected through complete native/TSV rows, with compact rereads where initial output truncated. Five SOURCE.json files were separately parsed and matching metadata inspected. No matching target history filename was found in the ignored-independent history inventory.

Unrelated hits were excluded, including BacDive 103730 (Rhodococcus), BacDive 132020-132029 prefix matches, CIP 103730 (Pasteurella), DSM 103730 (Companilactobacillus), IMI 103730 (a fungal deposit), unrelated assembly statistics and Salmonella strain 103730. ATB run-prefix matches SRR18017660-SRR18017668 belong to other samples and organisms, not SRR1801766. No eukaryotic YAML was reopened.

The native HUT 6566 entry is SI-ID 218708, deposit 537635, published offline, with no own type-strain deposit match. An additional ignored-inclusive exclusions/curation/history search confirmed `data/straininfo/exclusions.tsv:93506` records `no_eligible_own_deposit_match`. Its GOLD organism can support the direct species organism count without authorizing a BacDive strain entry or a type-strain sequence transfer.

No consequential omission was found within the represented seeded-inventory contract. Optional definition, functional traits, mechanisms and causal graph need not be invented. Child aggregate trait/medium counts do not establish species-wide biological assertions. iModulonDB was not applicable: the record has no gene-function, regulator, pathway, trait-identity or expression-module claim requiring that cross-check; the 16S marker is used for taxonomic identity.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The species/child distinction, descendant BacDive gathering, direct-only source counts, full-deposit matching, StrainInfo sequence scoping and ATB provenance are supported. Live GTDB access and full-corpus validation remain review limitations, not evidence of a defective record.

## Recommended Edits

None required. Do not hand-edit the generated YAML, promote its status, append curation/history events, or collapse source-specific assertions. Any future enrichment belongs in maintained source inputs/overlays and the established inventory/seed workflow, not this review report or generated pages.

## Follow-up Checks

Retry live GTDB identity access when available. For later source refreshes, preserve exact culture-deposit and sample provenance, recheck the NCBI parent/child distinction, and run schema/strict validation plus the documented corpus/QC gates after maintained inputs change. Sequence equivalence or checksum claims would require independent payload validation; neither is asserted here. No unresolved blocker remains.

## Additional Notes

- YAML SHA-256 at review: `d3c25fb48c6c8adf328d76f01c3db20e407f8f7098696cd9dfbefa403bfbc124`.
- `data/taxa/PATHS.tsv:15255` and `curation/seed_scope.tsv:31676` uniquely identify the species. The scope reason counts three direct inventory sources; the fourth attestation is the explicitly gathered descendant BacDive strain. The seed event correctly names all four represented sources.
- The seed timestamp is the latest of the three inspected inventory manifests: raw 2026-09-13T17:50:44Z, StrainInfo 17:29:00Z, ATB 17:54:04Z. NCBI source-reference filenames resolve to the provenance entries in `data/raw/MANIFEST.yaml`. Original large upstream snapshot payloads and their manifest checksums were not independently replayed or recomputed.
- Initial search syntax using unsupported look-around failed and was replaced by a successful ignored-inclusive search; the failed search supports no absence claim. ENA XML initially returned 406 with a JSON Accept header and succeeded with XML Accept. BioProject browser failures were resolved through focused authority XML; the initial large umbrella-project output was truncated, so only the subsequently reread identity/scope/target-link fields are claimed as inspected.
- Read-only review against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. No record, input, schema, history, page, branch, worktree or GitHub mutation. The only new repository artifact is this timestamped report. Existing ten worktrees and completed Eukaryota coverage were preserved.
