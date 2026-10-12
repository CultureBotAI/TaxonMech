# YAML Record Review: Pelagimonas phthalicica

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/pelagimonas_phthalicica.yaml`
- Started UTC: 2026-10-10T00:57:55Z
- Finished UTC: 2026-10-10T01:03:52Z
- Verdict: pass

## Target

The complete 787-line generated `TaxonRecord` was read. `NCBITaxon:1037362` denotes Pelagimonas phthalicica, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:1434029` (Pelagimonas), genetic code 11, grounding `EXACT`, status `SEEDED`.

The record contains nine ancestors, one correct-name nomenclature entry, one GTDB mapping, six source-qualified synonyms, two xrefs and one BacDive type strain, KU27E1. That strain has 10 assembly-link assertions, 8 genome-record assertions and 30 related-record assertions. These counts describe provenance-bearing entries, not distinct biological genomes. Eight source attestations and one seed event complete the record.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/pelagimonas_phthalicica.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/pelagimonas_phthalicica.yaml --out /private/tmp/taxonmech-phthalicica-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured source scans matched identity, full lineage, code, source names, scope/index and seed-event text. Complete backbone scanning found no direct child; own type-material rows were inspected, and exact own-ID merged/dropped scans found none.
- Exact multiset comparison against all own-strain raw and StrainInfo link rows plus the ATB assembly/sample overlay matched all 10 assembly, 8 genome-record and 30 related-record assertions, including nested evidence. No missing or extra link was found. Every imported culture match passed the repository's pinned CAFI whole-accession matcher and matched an existing culture ID.
- Full relevant native BacDive, StrainInfo, GTDB, BV-BRC, GOLD, NCBI names/assembly and ATB candidate rows were inspected independently of the derived-link comparison. Taxonomy, nomenclature, type material, selected genome/project metadata and cited publication identities were checked against primary authorities.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, original-source replay, rendering, publication gates, sequence-level genome equivalence or all experimental results in the cited papers. Focused agreement is not corpus reproduction. No causal graph is asserted, so `just validate-products` has no applicable nodes.
- Access limits: the GTDB genome page returned an unpopulated loading shell; StrainInfo's web page supplied no record text and the version DOI was inaccessible through the web tool. Their pinned native records were inspected instead. The Frontiers page timed out, but its relevant primary-paper text was read through PMC. The validation-list bibliography was accessible; its full-text endpoint returned HTTP 403, so its complete table was not audited.
- No genome FASTAs or archive payloads were downloaded; ATB URL/eligibility evidence was verified in committed metadata, not by a fresh archive-integrity check. Not every source's current live API was queried.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222728` agrees with [NCBI taxonomy EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037362&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037362): species Pelagimonas phthalicica, parent 1434029, code 11.

Every ancestor ID, label and rank matches the pinned chain: root, cellular organisms, Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria, Rhodobacterales, Roseobacteraceae and Pelagimonas. EFetch confirms the chain below root; Datasets includes root 1.

The six native NCBI name rows at `data/catalog/ncbi_names-0005.jsonl.gz:32342` onward support the scientific name, two exact synonyms and three related names. Authority strings and the includes-name Tropicibacter sp. KU27E1 remain related rather than being promoted to exact synonyms. The pinned NCBI authority uses ASCII Hordt; live NCBI uses an accented spelling. LPSN's accented authority is retained in the YAML nomenclature entry. This is source spelling, not a change in identity.

[LPSN 11051](https://lpsn.dsmz.de/species/pelagimonas-phthalicica) confirms the current combination, authority, ICNP publication status, correct-name status, three registered type deposits and AB636139. [LPSN 789905](https://lpsn.dsmz.de/species/tropicibacter-phthalicicus) is the homotypic former combination, not the current correct name. Local LPSN rows 2220, 26906 and 33765 preserve the current name, corrected former epithet and inaccurate original spelling. Only 11051 has the own NCBI mapping; the former combination is correctly retained as a source-qualified synonym.

GTDB's mapping/species rows specify `GTDB:s__Pelagimonas_phthalicica`, `skos:closeMatch`, count 2. Both native genomes, RS_GCF_004364805.1 and RS_GCF_900184825.1, carry that GTDB species and NCBI taxon 1037362; the former is the representative. This supports the mapping and count, not two BacDive strains. GTDB's Rhodobacteraceae family and NCBI's Roseobacteraceae remain source-specific classifications; the YAML correctly carries the NCBI lineage.

## Evidence

The original species-description abstract, [PMID 22278761](https://pubmed.ncbi.nlm.nih.gov/22278761/), DOI 10.1007/s00284-012-0085-8, explicitly identifies KU27E1 as the type strain and equates JCM 17793 and KCTC 23703. The relevant [2020 transfer description](https://pmc.ncbi.nlm.nih.gov/articles/PMC7179689/) names the basonym and equates DSM 26923, JCM 17793 and KCTC 23703. PubMed verifies PMID 32373076 and DOI 10.3389/fmicb.2020.00468 identify that same paper.

The [validation-list publisher record](https://www.microbiologyresearch.org/content/journal/ijsem/10.1099/ijsem.0.004244) and PMID 32731908 verify DOI 10.1099/ijsem.0.004244, volume 70:4043-4049 (2020). LPSN identifies this as Validation List 194 supporting the combination; the complete list table was not independently retrieved.

Primary [AB636139 metadata](https://www.ncbi.nlm.nih.gov/nuccore/AB636139) identifies AB636139.1, a 1,422-base partial 16S rRNA sequence, strain KU27E1, taxon 1037362, type material of the former combination, Japan:Okinawa. Its title retains Tropicibacter phthalicicus while its organism field is Pelagimonas phthalicica. The unversioned nomenclatural accession remains as supplied. This marker is outside genome counts. Its bibliography also links PMID 22805854, whose study-level abstract was inspected; no new phenotype or mechanism claim was added.

[BacDive 23238](https://bacdive.dsmz.de/strain/23238) and native row 23041 confirm KU27E1, its three inventoried deposits and type status. The native genome object and live sequence table explicitly provide unversioned GCA_004364805, BV-BRC 1037362.5 and IMG 2734482174 under source reference 67770. The record preserves these distinct identifiers and the source's unversioned accession.

Live [NCBI assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_004364805.1,GCF_004364805.1/dataset_report) confirms the current GenBank/RefSeq pair, strain DSM 26923, type material, contig level, 19 contigs and BioSample SAMN07621378. Native GenBank, RefSeq, GTDB and BV-BRC rows independently support their respective culture matches and provenance. Repeated accessions with different sources or source fields must not be collapsed into one assertion.

The pinned RefSeq/GTDB rows carry PRJNA224116, whereas GenBank, BV-BRC and GOLD carry PRJNA402509. Current Datasets displays PRJNA402509 for both paired assemblies. The inspected [PRJNA224116 identity and description](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=bioproject&id=224116&retmode=xml) identify the multispecies RefSeq annotation project, not a second strain. Preserve each source's project assertion. The large project's unrelated secondary-accession and locus-prefix lists were not audited.

GOLD's explicit DSM chain is Go0367410 to Gp0207631 to Ga0180970. The project supplies SAMN07621378 and PRJNA402509; the analysis supplies GCA_004364805.1 and IMG 2734482174. Its empty analysis-organism field is resolved by the explicit known project-to-organism link, with no conflicting organism. Go0044394 and Go0616119 support KCTC/JCM organism references only. GOLD organism, sequencing-project and analysis IDs stay typed related records, not genome identifiers.

StrainInfo native row 290657 explicitly records SI-ID 380604, DOI 10.60712/SI-ID380604.3 and available deposits SI-DP 872113 (JCM), 872114 (KCTC) and 904023 (DSM). The only imported sequence names DSM's own SI-DP 904023 and supplies unversioned GCA_004364805. Its version, deposit and source statuses match the YAML. The version DOI identifies the source strain record, not a publication or deposit. Native JCM/KCTC deposit type flags differ from DSM's flag; TaxonMech's strain-level type flag derives from LPSN deposit matching and does not assert agreement among those source flags.

ATB's 2025-05 SAMN07621378 assembly is supported by seven complete prior BioSample assertions. Both filters are PASS, the FASTA availability flag is set, and ERZ26863118, SRR6479435, the SeqKit sum and supplied download/archive URLs match the committed native row. All five ATB genome crosslinks retain matching source chains and `shares_biosample`, not identity. The source's SeqKit sum is not an MD5 hash, and a shared sample does not prove identical assemblies.

All eight attestation counts match their inventories: NCBITAXON 1 NAME; LPSN 1 NAME; GTDB 2 GENOME; BACDIVE 1 STRAIN; MEDIADIVE 2 MEDIUM; GOLD 5 ORGANISM; MADIN 2 and BACTOTRAITS 1 TRAIT_ASSERTION. These units must not be summed. The taxon-level MediaDive count is independent of the BacDive strain inventory's zero medium count, which is omitted in the generated strain entry. Neither trait count asserts a particular phenotype.

## Completeness

An ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` search covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Terms included bounded 1037362, current/former names, the slug, KU27E1 and whole DSM/JCM/KCTC designations. The expanded spelling search produced 112 candidate lines; their source identities and relationships were checked, with complete own-link and relevant native-row reads.

The main apparent missing genome belongs to CECT 8649: GCA/GCF_900184825.1, BV-BRC 1037362.4, GOLD Go0487755/Gp0371522/Ga0336749, IMG 2832291267 and sample SAMEA104098305. StrainInfo places that assembly specifically on SI-DP 898470. CECT 8649 is absent from this BacDive strain's committed deposit list. The documented join contract does not allow another deposit's sequence to transfer through SI-ID grouping, BacDive cross-reference, a taxon match or a shared species name. Its eligible ATB catalog row also belongs to the different sample. These candidates were not silently imported or counted as missing required links.

Native GOLD Go0616118 uses bare KU27E1 without a registered deposit; it correctly contributes to the taxon-level organism count but supplies no culture-based genome join. SeqCode names 15735, 30995 and 30996 preserve name identities without adding a name-inferred NCBI or genome mapping.

The unrelated GenBank GCA_977310805.1 candidate has ungapped length 1037362 and taxon 77133; the length is not this taxon's identifier. Five SOURCE.json files were separately parsed without a matching target name/deposit/taxon string. Gitignore-independent filename enumeration found only the target YAML and no prior report; history filename inspection found no target-specific filename. These are bounded repository checks, not global absence claims.

All classified BacDive strains are represented: one direct strain, no immediate backbone descendants and no listing cap. Optional definition, record-level evidence and causal graphs need not be invented. iModulonDB is not applicable to this identity/provenance record: counts and contextual literature do not create a gene, regulator or transcriptomics assertion. No adapter run or global dataset absence is claimed.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected record and bounded source scope. Identity, nomenclature, lineage, synonyms, type-strain identity, mapping, counts, explicit source chains and seeded history are supported. The CECT-specific records, differing source type flags and source-specific project metadata are documented context, not evidence of an incorrect current join. Live-site and full-corpus limitations above remain.

## Recommended Edits

None required for this generated record. Preserve source-specific witnesses, whole culture accessions, accession versions, unversioned BacDive/StrainInfo identifiers and related-record types. Do not transfer the CECT assembly onto DSM's deposit or count source occurrences as unique genomes.

Future authorized expansion to CECT 8649 must first establish a maintained deposit-identity input under the repository's ownership rules, then rebuild the affected source inventories and overlays. It must not bypass the own-deposit rule by hand-editing this YAML.

Any supported future defect belongs in maintained inputs, `src/taxonmech/extract.py`, `src/taxonmech/seed.py`, the source-specific inventory builders or `curation/seed_scope.tsv`, according to ownership. No supported defect requires such an edit here.

## Follow-up Checks

After an authorized source refresh, repeat exact own-strain multiset comparison, independent native-source chain checks, CAFI full-accession matching, schema/strict/history validation and full-corpus reproduction/QC gates. If CECT is admitted, require its own SI-DP, sample and GOLD project chain; retain distinct assemblies and source provenance.

Revisit the unavailable live GTDB/StrainInfo content and validation-list table when needed for a refresh. Phenotype enrichment requires strain-specific experimental evidence in the appropriate sibling repository; no pathway or phenotype was curated here.

## Additional Notes

- YAML SHA-256: `beff737eedaa604d097d6745f513f8d4a18ce7ae6f94e3765980ed8875e2bf08`.
- `data/taxa/PATHS.tsv:15276` and `curation/seed_scope.tsv:4052` uniquely resolve the record. Scope date is 2026-09-12; seed timestamp is 2026-09-13T17:54:04Z. The exact eight-source reason and seed-event text agree.
- Primary inventory anchors include BacDive row 23042, LPSN row 2220, GTDB mapping row 1485, raw assembly rows 109195-109203, genome-record rows 87794-87800, related-record rows 316086-316109, StrainInfo assembly row 7962 and ATB strain-link row 3541.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for the target. No record, maintained input, schema, history, page, branch, worktree or GitHub state was changed. No review status was promoted and no Eukaryota YAML was opened.
