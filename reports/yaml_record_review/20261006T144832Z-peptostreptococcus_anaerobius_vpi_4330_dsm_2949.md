# YAML Record Review: Peptostreptococcus anaerobius VPI 4330 = DSM 2949

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/peptostreptococcus_anaerobius_vpi_4330_dsm_2949.yaml`
- Started UTC: 2026-10-06T14:40:20Z
- Finished UTC: 2026-10-06T14:48:32Z
- Verdict: needs curation

## Target

One generated `TaxonRecord`, `NCBITaxon:1035196`, label `Peptostreptococcus anaerobius VPI 4330 = DSM 2949`, rank STRAIN, domain BACTERIA. The entire YAML was read before findings and checked byte-for-byte unchanged before reporting. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record is EXACT / SEEDED with ten root-first ancestors, one GTDB mapping, four synonyms, one equivalent xref, genetic code 11, one BacDive strain, seven source attestations and one inline seed event. The strain contains eleven culture identifiers, sixteen assembly assertions, thirteen genome-record assertions and seventy-six related-record assertions. These are provenance-bearing assertions, not counts of distinct biological genomes. Only this new report is written.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/peptostreptococcus_anaerobius_vpi_4330_dsm_2949.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/peptostreptococcus_anaerobius_vpi_4330_dsm_2949.yaml --out /private/tmp/pavpi-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: backbone identity, all ten ancestors, aliases, code, scope, seed provenance, source counts and nested source assertions agree with the inspected pinned inputs. This is not a focused corpus-reproduction validator.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc`, and the test suite. No full-corpus success is claimed.
- No curator-added ontology graph requires term validation. The documented product checker excludes taxonomy fields and delegates those checks to corpus reproduction.
- No separate target history artifact was found by the ignored-independent history filename search. Inline history passed schema validation and agrees with scope. No external history validator was run against an invented artifact.
- The StrainInfo DOI and all twelve nucleotide accessions were inspected through public structured metadata. There are no quoted evidence snippets or experimental phenotype claims requiring a separate citation verdict.

## Identity and Grounding

Pinned backbone `data/raw/ncbitaxon_taxa.tsv:221919`, [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035196&retmode=xml), and the [taxonomy dataset response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035196) agree on this strain, species parent `NCBITaxon:1261` and code 11. The three NCBI aliases are DSM 2949, DSM 2949 = VPI 4330, and VPI 4330 with their species prefix. All ten lineage entries agree with the pinned backbone. No descendants or exact target type-material row were found in the inspected tables.

`data/raw/ncbi_merged_ids.tsv:4152` merges old taxid 1122950 into 1035196. This explains the old taxid embedded in `patric:1122950.3`; it does not authorize rewriting that genome accession.

The [DSMZ deposit page](https://www.dsmz.de/collection/catalogue/details/culture/DSM-2949) identifies DSM 2949 as type material, lists the other culture numbers, and gives the deposit history through ATCC 27337, VPI 4330 and Prevot 4372. It independently supports the deposit-group identity. The [LPSN species page](https://lpsn.dsmz.de/species/peptostreptococcus-anaerobius), record 779378, identifies the valid species name and its type deposits. Its pinned row at `data/raw/lpsn_names.tsv:18983` maps to species taxid 1261, not strain taxid 1035196.

Type material is not identical to the species concept. Nor does being GTDB's representative genome make the strain identical to the species cluster. The unsupported species equivalence is the major finding below.

## Evidence

- Complete NCBI name rows `data/catalog/ncbi_names-0005.jsonl.gz:31382` through 31385 support the scientific name and three aliases. The attestation counts one NAME, not four names.
- `data/raw/bacdive_strains.tsv:11689` and complete `data/bacdive/records.jsonl.gz:11688` support BacDive 11843, designation 4372 / 10102, the eleven culture identifiers and a zero raw medium count. The [live BacDive page](https://bacdive.dsmz.de/strain/11843) confirms the deposit group and three genome entries. Reference 66792 denotes automated DiASPora annotation; 67771 denotes KCTC curators, not an experimental paper.
- GTDB mapping `data/raw/gtdb_mappings.tsv:1423` and species row `data/raw/gtdb_species.tsv:139791` count 61 genomes in the species cluster. Additional mappings at lines 14469, 14522, 15243, 49518 and 299055 include the parent species and other taxa. This is not a count of genomes from this strain. The extraction owner `src/taxonmech/extract.py:501` counts genome-to-species edges.
- The remaining exact taxon attestations are supported by `data/raw/mediadive_taxa.tsv:122` (three MEDIUM assertions: 1203a, 693, 78), `data/raw/gold_organisms.tsv:480` (two ORGANISM assertions), `data/raw/madin_taxa.tsv:672` (five TRAIT_ASSERTIONs), and `data/raw/bactotraits_taxa.tsv:93` (two TRAIT_ASSERTIONs). These counts do not assert a particular phenotype. DSMZ independently lists the three media; the omitted nested count (zero in its raw inventory) and three taxon-level MediaDive assertions are different source inventories.
- `data/taxa/PATHS.tsv:14410` and `curation/seed_scope.tsv:7212` support this target and seven-source scope. The 2026-09-12 scope date is consistent with its 2026-09-13T17:54:04Z seed event.

All assembly/genome/related rows were read in full, including transformed `data/raw/strain_assemblies.tsv:8507` through 8519, `data/raw/strain_genome_records.tsv:6548` through 6560, and `data/raw/strain_related_records.tsv:25234` through 25279. The source chains remain distinct:

| Deposit/source chain | Assemblies and genome records | Sample and project evidence |
| --- | --- | --- |
| VPI 4330 / ATCC 27337 | BacDive unversioned GCA_000318115; GOLD GCA_000318115.1; IMG 2537561951; PATRIC 1035196.3 | GOLD Go0010894 -> Gp0010894 -> Ga0016260; SAMN02436860; PRJNA67203 |
| DSM 2949 | GCA_000381525 and GCA_000381525.1; GCF_000381525.1; GTDB RS_GCF_000381525.1; IMG 2519899669; PATRIC 1122950.3 | GOLD Go0013126 -> Gp0013126 -> Ga0000358; SAMN02441325; PRJNA183057; RefSeq umbrella PRJNA224116 |
| NCTC 11460 | GCA_900454605 and GCA_900454605.1; IMG 2837383163; PATRIC 1261.19 | GOLD Go0500242 -> Gp0384442 -> Ga0352944; SAMEA4504051; umbrella PRJEB6403 |

The complete native BV-BRC rows at `data/bvbrc/bvbrc-0000.jsonl.gz:3318`, 13013 and 36679 support these respective chains. GOLD organism rows 9566, 11565 and 349590, project rows 9431, 11417 and 271918, and analysis rows 9789, 210 and 212791 were inspected. Empty analysis-level organism fields do not conflict with their explicit project chains. Other GOLD organisms Go0612511 through Go0612517 retain their VTT, LMG, KCTC, CIP, CCUG and BCRC deposit fields and species taxid.

Complete native NCBI GenBank/RefSeq rows and GTDB rows were inspected alongside live dataset responses for [GCA_000318115.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000318115.1/dataset_report), [GCA_000381525.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000381525.1/dataset_report), and [GCA_900454605.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_900454605.1/dataset_report). All three are current and retain their corresponding GCF accessions. Their assembly sizes are respectively 1,988,451 bp, 2,106,935 bp and 2,256,756 bp; contig/scaffold counts are 110/91, 72/68 and 5/5. The DSM assembly is the pinned GTDB representative. These facts support source linkage, not equivalence among all assembly or database identifiers.

The first two complete BioSample XML responses explicitly identify VPI 4330 / ATCC:27337 and DSM 2949 / DSM:2949. The NCTC assembly response embeds SAMEA4504051 with NCTC:11460 and strain NCTC11460. NCTC metadata retain species taxid 1261 rather than replacing it with this strain taxid.

StrainInfo's complete native record at `data/straininfo/records.jsonl.gz:7937` has eleven deposits. [DataCite metadata for DOI 10.60712/SI-ID7937.3](https://api.datacite.org/dois/10.60712/SI-ID7937.3) confirm version 3, published/findable status, eleven deposits and the [SI-ID 7937 landing page](https://straininfo.dsmz.de/strain/7937). Nine own deposits match the eligible BacDive inventory: ATCC 27337, BCRC 10722, CCUG 7835, CIP 104411, DSM 2949, KCTC 5182, LMG 15865, NCTC 11460 and VTT E-022078. BCRC's source taxid 1257 is preserved. CCRC 10722 and ACM 5059 are additional source deposits, not invented aliases for an eligible existing key.

The three StrainInfo genome links at `data/straininfo/assemblies.tsv:824` through 826 and thirty related assertions at `data/straininfo/related_records.tsv.gz:15416` through 15445 retain explicit SI-DP attribution. In particular, the SI association of GCA_000318115 with DSM deposit 32301 remains a source assertion; NCBI's original BioSample names ATCC, and the sources are not silently rewritten to agree.

All twelve linked nucleotide accessions resolved in complete [NCBI sequence metadata](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=AF352062,AY326462,AY691315,D14150,FJ410395,FM207102,GQ496448,GQ496449,L04168,Z28984,Z29059,Z29060&rettype=gb&retmode=xml). Bases and translations were omitted from the metadata inspection; source/features/references were retained.

| Explicit SI deposit | Accessions and bounded metadata |
| --- | --- |
| NCTC 11460 | AF352062, partial gdh, 330 nt; AY326462, partial 16S rRNA, 1,473 nt |
| ATCC 27337 | AY691315, partial cpn60, 552 nt; D14150, partial 16S rRNA, 1,366 nt; FJ410395, spacer/partial 23S rRNA, 3,122 nt; FM207102, partial 16S rRNA, 394 nt; L04168, complete 16S rRNA, 1,462 nt |
| ATCC 27337 | Z28984 / Z29059 / Z29060, intergenic clones LK16 / LK51 / LK54, 830 / 830 / 952 nt |
| CCUG 7835 | GQ496448 / GQ496449, partial intergenic clones 5 / 7, 300 nt each |

FM207102's definition says ATTC 27337, but its structured source qualifier says ATCC 27337 and StrainInfo explicitly links the ATCC deposit. The source title's typo is preserved, not used to invent a new normalization rule. Gene annotations and sequence references alone are not experimental proof of phenotype.

## Completeness

The sixteen assembly assertions comprise thirteen raw assertions plus three StrainInfo assertions; the seventy-six related assertions comprise forty-six raw plus thirty StrainInfo assertions. Source-specific duplicates, accession versions, taxon IDs, deposit IDs and project chains are correctly retained rather than collapsed into genome equivalence.

Calls to the existing culture normalizer reject bare VPI 4330, unseparated NCTC11460 and DSM Z; they accept NCTC 11460 and DSM 2949. Thus absent direct NCBI/GTDB/BV-BRC joins for VPI and unseparated NCTC are consistent with the current whole-deposit contract. Valid source-specific GOLD and BacDive links remain. Do not infer joins from names, BioSample attributes outside the current assembly-summary contract, or the GTDB representative flag.

StrainInfo's KCTC 5973 and VPI 4330 references are relational/designation aliases rather than own deposits. The absence of corresponding SI-DP links is not a missing-link defect. CCRC and BCRC remain distinct authority keys. Type status is biologically supported, but the schema's `is_type_strain` means a type designation for an LPSN name of this taxon; that species name belongs to parent 1261. Its absence on this strain-level record is not independently flagged as a contract violation.

The ATB row for SAMEA4504051 is NOT_PROCESSED, has no available assembly, and is explicitly excluded at `data/atb/exclusions.tsv:976`; complete rows at `data/atb/assemblies.tsv:1492` and `data/catalog/allthebacteria.tsv.xz:627813` agree. The available name-matching catalog row at line 1016162 instead belongs to SAMN02194843 / ERZ4064148 / SRR892431. No exact supported source sample chain to that different BioSample was found in the ignored-inclusive candidate search. A matching scientific name cannot transfer its ATB assembly to this record.

The structured `imodulondb datasets` adapter returned 28 datasets before open-ended follow-up, with no covered Peptostreptococcus dataset. It is not applicable here; absence is not negative biological evidence. Optional definitions, phenotypes and causal graphs can remain empty.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a GTDB species concept is promoted to exact strain identity.** `GTDB:s__Peptostreptococcus_anaerobius` is an equivalent xref and its species name an EXACT_SYNONYM on strain taxid 1035196. The 61-genome cluster, species parent 1261, type-strain status and representative assembly do not establish species/strain identity. This violates the true-equivalence contract at `src/taxonmech/schema/taxonmech.yaml:180`. Maintained owner: rank-insensitive GTDB promotion at `src/taxonmech/seed.py:449`, with regression coverage in `tests/test_seed.py`. The upstream kg-microbe closeMatch producer also needs rank- and direction-aware review. Mapping, synonym and xref manifestations are one finding.

Blockers: None found. Minor findings: None found. Identity and the source-specific nested links are supported. Source titles, historical taxids, type-designation scope and live quality metrics remain qualifications, not grounds for fabricating replacement identifiers.

## Recommended Edits

1. Make GTDB identity promotion in `src/taxonmech/seed.py` rank-aware. Preserve the strain's supported classification and source cluster count without emitting an equivalent species xref or exact species synonym.
2. Review rank and relation direction in the upstream kg-microbe mapping producer rather than guessing a broad/narrow replacement. Preserve the carried NCBI lineage.
3. Add strain-versus-species coverage to `tests/test_seed.py`, including type strains and GTDB representative genomes, while retaining genuine species-level equivalence. Regenerate from maintained inputs after an authorized fix; do not hand-edit this generated YAML or transformed raw tables.
4. Preserve all accession versions, explicit deposit evidence, source taxids and GOLD chains. Any future normalization expansion belongs in the maintained registry/import process and `src/taxonmech/genome_sources.py`, with guarded tests, not a name-based bypass.
5. Keep ATB enrichment in `src/taxonmech/atb_links.py` / `src/taxonmech/atb.py` constrained to exact evidenced BioSample chains and available assemblies. Do not substitute SAMN02194843 for SAMEA4504051.

## Follow-up Checks

- After an authorized change, run `uv run pytest tests/test_seed.py` and this target's documented schema and strict commands.
- Confirm that the unsupported species synonym/equivalent xref is removed while retaining NCBI identity, ten ancestors, three NCBI aliases, code 11, seven attestations and all supported nested assertions.
- Run actual full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc` after regeneration. Bounded manual comparisons do not replace those gates.
- Recheck source versions and retain distinct GenBank/RefSeq, IMG, PATRIC, sample, project and SI-DP scopes before future enrichment.
- Retry the unavailable GTDB page, ATCC product page and ENA sample endpoint if those independent routes are needed for a later curation change. Current NCBI dataset metadata and pinned source records support the bounded review.
- Assess assembly quality separately before analytical reuse: the live NCTC dataset response reports CheckM contamination 20.79%, despite ANI taxonomy status OK / species_match. This review verifies provenance links, not genome quality or experimental phenotype.

## Additional Notes

Ignored-independent searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The taxid, deposit variants, BacDive ID, DOI and slug produced 186 candidate rows. An accession/deposit expansion, excluding umbrella project PRJEB6403 as a strain identity selector, produced 101 rows with three additional rows. All 189 distinct candidates were read in full through lossless structured decoding, including compressed and ignored sources. The VPI 14330 match in unrelated StrainInfo 43819 was inspected and rejected. An earlier umbrella-project search returned 8,696 rows; that project-wide output was not exhaustively reviewed and is not used for absence or strain-equivalence claims.

Separate structured checks covered exact backbone/lineage/status, GTDB cluster mappings, LPSN, scope and source counts. Five SOURCE.json files were searched structurally and history filenames independently checked. Absence findings are bounded to these inspected sources, including ignored files.

The adapter command was `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. One initial offline UV command used a non-writable default cache and failed before searching; rerunning with the scratch cache succeeded.

A direct EUtils BioSample fetch using SAMEA4504051 returned SAMN04504051, an unrelated record; its accession mismatch was detected and that response was rejected. The exact SAMEA accession and culture attributes were verified in the assembly dataset response. The independent ENA endpoint failed through the browser tool and timed out through a bounded direct request. These failures do not indicate missing source data.

No YAML/code/generated-page edits, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations were performed. Eukaryota reviews were not reopened.
