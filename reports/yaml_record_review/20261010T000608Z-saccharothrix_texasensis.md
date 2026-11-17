# YAML Record Review: Saccharothrix texasensis

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/saccharothrix_texasensis.yaml`
- Started UTC: 2026-10-09T23:59:40Z
- Finished UTC: 2026-10-10T00:06:08Z
- Verdict: pass

## Target

Entire 1,074-line generated `TaxonRecord` read, including every nested evidence object and seed event. `NCBITaxon:103734` denotes Saccharothrix texasensis, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2071`, genetic code 11, grounding `EXACT`, status `SEEDED`.

The record has nine ancestors, two source-qualified synonyms, LPSN nomenclature, a GTDB mapping, eight source attestations, and one BacDive type-strain entry with 11 culture identifiers. Ten assembly, seven genome and 53 related-record assertions total 70 source-qualified assertions, not 70 independent biological entities.

## Validation

Repository commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1` and `uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/saccharothrix_texasensis.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/saccharothrix_texasensis.yaml --out /private/tmp/taxonmech-saccharothrix-texasensis-20261009-validation.tsv --workers 1`: one file, zero errors. Output reread: header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Bounded structured comparisons matched the pinned identity, complete lineage, scope/index entries, seed text, source counts and exact multiset of all 70 own-strain assertions. No missing or extra own inventory assertion was found. Retained culture joins satisfy the maintained whole-deposit CAFI matcher.
- Material native BacDive, StrainInfo, BV-BRC, NCBI assembly, GTDB and GOLD records were independently read in full. Public taxonomy, LPSN, BacDive, assembly/sample metadata, BioProjects, marker metadata, DataCite and inspected literature abstracts provide additional checks. Inventory agreement alone is not independent native-source verification.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering or publication gates. `just validate-products` has no applicable causal-graph nodes.
- Public GTDB tree retrieval failed. Direct retrieval of the species paper encountered HTTP 403 and tool retrieval failures; the publisher's issue page supplied its abstract and DOI instead. Full experimental papers and genome sequence payloads were not compared. PubMed browser access to the 6-C paper encountered a challenge, but NCBI EFetch successfully supplied its complete abstract and bibliography.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18560` agrees with inspected [NCBI taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=103734) and [taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103734&retmode=xml). The root-first chain is root, cellular organisms, Bacteria, Bacillati, Actinomycetota, Actinomycetes, Pseudonocardiales, Pseudonocardiaceae and Saccharothrix. The full pinned backbone scan found no immediate child; exact own-ID merge/drop scans found no target entry.

Both native NCBI name rows, `data/catalog/ncbi_names-0000.jsonl.gz:38615` and the following row, support the scientific name and authority-bearing related synonym. Live NCBI additionally lists Actinosynnema texasense as a misspelling. The YAML attributes that spelling to GTDB, not to the pinned NCBI synonym inventory.

`data/raw/lpsn_names.tsv:19713` and the [LPSN authority](https://lpsn.dsmz.de/species/saccharothrix-texasensis) support name 780713, Labeda and Lyons 1989, valid/correct-name status, marker AF114814 and all six stored type deposits: ATCC 51593, DSM 44231, IFO 14971, JCM 9113, NBRC 14971 and NRRL B-16134. The public authority additionally lists VKM Ac-1968, already in the nested strain inventory, and laboratory designation LL-37U-77. Medical-use wording concerns naming, not efficacy or safety.

`data/raw/gtdb_mappings.tsv:1483` and `data/raw/gtdb_species.tsv:5113` support `GTDB:s__Actinosynnema_texasense`, `skos:closeMatch`, count two. The native representative is DSM 44231, `RS_GCF_003752005.1`, NCBI taxon 103734. The other genome is `RS_GCF_016695385.1`, Saccharothrix sp. 6-C, NCBI taxon 2781735; mapping row 216719 preserves its separate NCBI identity. GTDB classification under Actinosynnema is not an instruction to replace the NCBI lineage or claim exact cross-taxonomy equivalence.

## Evidence

The eight attestations preserve their respective units:

| Source | Count and unit | Inspected support |
| --- | --- | --- |
| NCBITAXON | 1 NAME | Own backbone and native name rows |
| LPSN | 1 NAME | Name 780713, raw row 19713 |
| GTDB | 2 GENOME | Species/mapping rows and two native genomes |
| BACDIVE | 1 STRAIN | Raw strain row 13320, native BacDive 13484 |
| MEDIADIVE | 2 MEDIUM | Own row 143, medium IDs 65 and J45 |
| GOLD | 7 ORGANISM | Own row 525 and seven native organisms |
| MADIN | 2 TRAIT_ASSERTION | Own row 710 |
| BACTOTRAITS | 5 TRAIT_ASSERTION | Own row 107 |

These counts are not independently curated experimental phenotypes or growth claims. BacDive's raw strain medium count is zero; omission of a strain-level count does not contradict the separate MediaDive taxon attestation.

Full `data/bacdive/records.jsonl.gz:13319` and the [BacDive authority](https://bacdive.dsmz.de/strain/13484) support the type-strain identity, all 11 culture identifiers and its assembly/IMG/BV-BRC links. The culture list is ATCC 51593, CGMCC 4.1713, DSM 44231, IFO 14971, IMSNU 21343, JCM 9113, KCTC 9399, NBRC 14971, NCIMB 13186, NRRL B-16134 and VKM Ac-1968. Internal reference 67770 is source-local provenance, not a PMID.

The DSM 44231 sequencing chain is:

| Identifier class | Value |
| --- | --- |
| GenBank / RefSeq | GCA_003752005.1 / GCF_003752005.1 |
| Assembly | ASM375200v1, Contig |
| BioSample | SAMN10363104 |
| Sequencing BioProject | PRJNA500558 |
| BV-BRC | 103734.3 |
| IMG | 2784132178 |
| GOLD analysis / project / organism | Ga0197498 / Gp0220505 / Go0373404 |

Native NCBI, GTDB, BV-BRC and GOLD rows agree on that chain. Live [GenBank assembly metadata](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_003752005.1/) and the paired RefSeq metadata confirm DSM 44231, sample identity and the November 2018 release. One contig does not warrant upgrading the explicitly supplied Contig assembly level to Complete Genome.

The [inspected BioProject XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=500558,224116&retmode=xml) distinguishes the DSM 44231 sequencing project PRJNA500558 from the multispecies RefSeq annotation umbrella PRJNA224116. Pinned RefSeq/GTDB witnesses retain the latter where their sources supplied it; current assembly metadata showing the sequencing project does not invalidate this source-specific provenance. Project objectives about natural products or plant growth are not experimental trait evidence.

All seven GOLD organism rows were read: Go0028570 for NRRL B-16134, Go0373404 for DSM 44231, and Go0606153 through Go0606157 for ATCC 51593, IFO 14971, JCM 9113, NBRC 14971 and NCIMB 13186 respectively. Both culture-collection and strain fields support separate witnesses. The 22 GOLD related-record assertions comprise 14 organism, two analysis, two project and four sample/BioProject assertions.

Full StrainInfo row `data/straininfo/records.jsonl.gz:31262` identifies SI-ID 43068, BacDive 13484 and DOI 10.60712/SI-ID43068.3. All 11 own deposits were read. The ten eligible exact matches are:

| Deposit | SI-DP |
| --- | --- |
| ATCC 51593 | 115871 |
| NRRL B-16134 | 115872 |
| DSM 44231 | 169334 |
| IFO 14971 | 169335 |
| JCM 9113 | 169336 |
| NCIMB 13186 | 169337 |
| VKM Ac-1968 | 227900 |
| KCTC 9399 | 319699 |
| NBRC 14971 | 335705 |
| CGMCC 4.1713 | 756018 |

The extra AS 4.1713/335703 deposit must not be rewritten into CGMCC 4.1713. IMSNU 21343 appears in relationship designations, not as an own deposit object. Direct execution of the maintained normalizer returns no supported key for IMSNU 21343, 6-C or LL-37U-77, and distinct keys for AS 4.1713 and CGMCC 4.1713. The YAML appropriately preserves the escaped IMSNU identifier without inventing a join.

StrainInfo explicitly binds AF114814 to NRRL B-16134/SI-DP 115872 and GCA_003752005 to DSM 44231/SI-DP 169334. Each sequence has its own matching deposit; the two sequence objects do not share a single SI-DP. The [DataCite record](https://api.datacite.org/dois/10.60712/si-id43068.3) independently confirms the findable version-three DOI and 11-deposit description, but DOI resolution alone is not sequence-binding evidence.

KCTC 9399's native StrainInfo deposit has `typeStrain=false`. This source-level difference is preserved here: the YAML's strain-level type flag is BacDive-sourced and corroborated by LPSN type deposits, not a claim that every StrainInfo deposit object carries a true flag. Its KCTC link asserts deposit identity, not the contrary SI flag.

A second full native StrainInfo row, 246504, is SI-ID 318516, published offline, same species taxon but only CGMCC 4.1186/SI-DP 755335, no sequence and no BacDive ID. That different deposit is not evidence of an omitted link to BacDive 13484.

The exact assertion split is ten assemblies (BacDive 1, BV-BRC 2, GOLD 2, GTDB 2, NCBI 2, StrainInfo 1), seven genomes (BacDive 2, BV-BRC 2, GOLD 2, GTDB 1), and 53 related records (BV-BRC 4, GOLD 22, GTDB 2, NCBI 4, StrainInfo 21). Source-specific duplicate witnesses and BacDive/StrainInfo unversioned assembly accessions are intentionally retained.

The [publisher's original-species abstract](https://www.microbiologyresearch.org/content/journal/ijsem/39/3?page=2), DOI 10.1099/00207713-39-3-355, identifies NRRL B-16134 as the texasensis type and NRRL B-16159 as the separate waywayandensis type. It supports distinguishing these species, without importing experimental details from an unretrieved full paper.

Live [AF114814 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AF114814) resolves to AF114814.1, a 1,512-base partial 16S sequence explicitly assigned to NRRL B-16134 and taxon 103734. Its bibliography matches [PMID 10826820](https://pubmed.ncbi.nlm.nih.gov/10826820/), DOI 10.1099/00207713-50-1-331. The inspected abstract is historical phylogenetic evidence, not authority to overwrite today's lineage.

The second GTDB genome's live [assembly metadata](https://www.ncbi.nlm.nih.gov/datasets/genome/GCA_016695385.1/) identifies strain 6-C, taxon 2781735, BioSample SAMN16534143 and BioProject PRJNA671555, distinct from DSM 44231. The inspected [6-C paper abstract](https://pubmed.ncbi.nlm.nih.gov/33591813/), DOI 10.1094/MPMI-10-20-0300-A, calls it S. texasensis and reports strain-specific biocontrol and genome results. Neither its species spelling nor GTDB cluster membership establishes a shared culture deposit. Those results are not transferred to the type strain or promoted into species-wide traits.

## Completeness

An ignored-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. It included target names, bounded numeric source IDs, full culture identifiers, assembly number, marker, BioSample and GOLD IDs. The 1,238 candidate lines comprised 228 native JSON and 1,010 TSV rows. Native identity/matched-field contexts were inspected, material own native records were read completely, and TSV candidate identities were grouped for collision checks. All own assertion rows were separately read losslessly.

Numeric collisions include DSM 13484 in Chitinophaga, DSM 103734 in Phreatobacter, ATCC 43068 in Acidothermus, unrelated BacDive/SI identifiers, assembly statistics and sequence hashes. Thirty ATB catalog candidates matched hash substrings, not target identities. ATB join candidates identify BacDive 17745, Chitinophaga japonensis, DSM 13484 and SAMN05660319, not the target. No own ATB assertion was found within these searched source inventories. This is not a claim of global database absence.

Five SOURCE.json files were parsed, and own BacDive/StrainInfo request-ledger entries checked. Gitignore-independent filename checks found the target YAML and no earlier target report; history filename checks found no target-specific filename. Native SeqCode entries 18465 and 42698 provide name-catalog context, not additional strain or genome evidence. No Eukaryota YAML was opened.

iModulonDB gene/module searches were not applicable to this seeded identity/inventory record: it makes no gene, regulator, pathway or transcriptomics claim. The adapter was not run and no dataset absence is asserted. Optional definition, experimental traits, record-level evidence and causal graph need not be invented from source counts or project descriptions.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and source scope. Source-classification differences, the separate 6-C genome, StrainInfo deposit distinctions and source-specific witness multiplicity do not establish a defect in this generated record. Public-access failures and skipped corpus gates remain limitations, not successful validations.

## Recommended Edits

None required. Do not hand-edit the generated YAML, attach 6-C solely by species label, rewrite AS into CGMCC, invent an IMSNU CAFI match, collapse distinct source witnesses, upgrade unversioned accessions, or substitute GTDB lineage for NCBI lineage.

Future authorized source corrections belong in maintained extraction inputs/policies, including `src/taxonmech/extract.py`, `src/taxonmech/genome_sources.py`, source-specific adapters and `src/taxonmech/straininfo.py`, followed by the documented extraction/seed workflow. No such correction is established here.

## Follow-up Checks

Retry the public GTDB tree and retrieve the complete species-description paper when accessible. A future source refresh should repeat whole-deposit matching, separate SI-DP sequence bindings, source-specific type-flag checks and schema/strict/history validation, followed by the documented full-corpus reproduction and QC gates.

Any biological claim from the 6-C study must retain that strain's scope and primary experimental evidence; it cannot be inferred for DSM 44231 from GTDB membership.

## Additional Notes

- YAML SHA-256: `b72853fbfdb3627ff86c6b543f9794e0c16a2e6ea2002e452e68233b845de99a`, unchanged on reread.
- `data/taxa/PATHS.tsv:15260` and `curation/seed_scope.tsv:2032` identify the target. The seed retains 2026-09-13T17:54:04Z and the eight-source scope reason. All 17 own NCBI type-material rows, 2089-2105, were read.
- Own raw assertion rows are assembly 36499-36507, genome 28505-28511 and related 98246-98277. StrainInfo contributes assembly 2763, related 42694-42714 and strain links 17289-17298.
- Native material addresses include BacDive 13319, StrainInfo 31262, BV-BRC shard 0000:3435, NCBI GenBank shard 0002:47929, RefSeq shard 0002:6038, and GTDB shards 0007:28751 and 0015:47202. GOLD organisms are rows 24294, 277039 and 437143-437147; analysis 125432 and project 146979.
- Read-only review against HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. The only new repository artifact is this report. Records, maintained inputs, schemas, history, pages, branches, all ten existing worktrees and GitHub state were preserved. No curation event or status promotion was performed; completed Eukaryota coverage remains untouched.
