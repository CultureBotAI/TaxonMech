# YAML Record Review: Otariodibacter oris

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/otariodibacter_oris.yaml`
- Started UTC: 2026-10-04T01:22:46Z
- Finished UTC: 2026-10-04T01:28:54Z
- Verdict: pass

## Target

Read the complete 781-line generated TaxonRecord for `NCBITaxon:1032623`, Otariodibacter oris. It is a SPECIES in BACTERIA under Otariodibacter (1249016), with nine lineage entries, EXACT grounding, SEEDED status, code 11, LPSN nomenclature, a GTDB close mapping, one BacDive type strain and eight source attestations. The strain contains 11 assembly assertions, nine non-ATB genome assertions, one ATB assembly and 26 related-record assertions. These are provenance-bearing assertions, not counts of distinct strains or genomes.

## Validation

`UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/otariodibacter_oris.yaml` passed with no issues. The corresponding `just validate-strict data/taxa/bacteria/otariodibacter_oris.yaml` passed for one file with zero errors and refreshed `reports/instance_validation_failures.tsv`. Both commands were repeated successfully after the evidence checks.

Read-only structured comparisons checked backbone identity, complete lineage, nomenclature, mappings, all eight source counts, scope, paths and seed text. Full-field multiset comparisons matched all 11 assembly, nine non-ATB genome and 26 related-record assertions to raw/StrainInfo inventories. Native-source checks validated all five StrainInfo evidence objects, all ATB metadata fields, seven sample assertions and 13 same-source-chain pairs behind five genome links.

Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global provenance/history/product gates and rendering. No undocumented focused substitute was invented. There are no curator-added causal graphs or separate history references requiring a target-specific gate. An initial auxiliary `uv run` hit the restricted default cache; rerunning with the approved temporary cache succeeded.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:220871` and native names `data/catalog/ncbi_names-0005.jsonl.gz:30163` onward agree with the YAML. Inspected live [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1032623&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1032623) confirm identity, parent, rank, code 11 and all nine root-first lineage identifiers. The NCBI chain includes Pseudomonadati, Pseudomonadota, Gammaproteobacteria, Pasteurellales and Pasteurellaceae.

NCBI treats Bisgaard taxon 57 as a synonym. The authority string and 13 former Pasteurellaceae strain-style `includes` names remain RELATED_SYNONYM, avoiding species-wide exact identity for each constituent isolate name. Six type-material source rows at `data/raw/ncbi_type_material.tsv:1625` onward cover DSM, CCUG and Baika1 representations. The full backbone has no current child taxon for this record.

Inspected [LPSN](https://lpsn.dsmz.de/species/otariodibacter-oris) confirms record 790298, Hansen et al. 2012, valid publication, legitimacy, correct-name status, and Baika1 = CCUG 59994 = DSM 23800 as the type. Its GTDB cross-reference supports the species mapping. The complete 901,341-row GTDB inventory contains exactly two members: RS_GCF_009684715.1, the representative, and RS_GCF_003634665.1. GTDB places the species in Enterobacterales while NCBI uses Pasteurellales; the YAML preserves NCBI lineage and a separate `skos:closeMatch`, not a silent taxonomy replacement.

## Evidence

The inspected PubMed record and abstract for [PMID 22199211](https://pubmed.ncbi.nlm.nih.gov/22199211/) and Crossref metadata for [DOI 10.1099/ijs.0.039586-0](https://doi.org/10.1099/ijs.0.039586-0) identify the Hansen et al. description in IJSEM 62, 2572-2578 (2012). The abstract explicitly connects Bisgaard taxon 57 and the type-strain deposits to the new genus and species. [DOI 10.1099/ijs.0.050401-0](https://doi.org/10.1099/ijs.0.050401-0) resolves in inspected Crossref metadata to the subsequent nomenclatural notification, IJSEM 63, 399-400 (2013), not another experimental characterization. LPSN cites both in their proper roles. Full article text was not inspected.

Inspected GenBank XML for [HM626613.1](https://www.ncbi.nlm.nih.gov/nuccore/HM626613.1) confirms a 1,410-base partial 16S sequence of Baika1, taxon 1032623, type material and the original publication. The YAML correctly retains the source's unversioned HM626613 rather than inventing a source version.

Native `data/bacdive/records.jsonl.gz:11604` and the inspected [BacDive page](https://bacdive.dsmz.de/strain/11759) support one type strain, Baika1, with both complete collection identifiers. Its reference 66792 supplies two separate genome rows: scaffold GCA_003634665 with BV-BRC 1032623.3 and IMG 2770939614; complete GCA_009684715 with BV-BRC 1032623.9 and IMG 8048216895. Those source identifiers, levels, names and reference IDs are retained without synthesizing accession versions. BacDive's automated phenotype predictions were not promoted into record claims.

Native NCBI GenBank `ncbi_genbank-0002.jsonl.gz:43598` and RefSeq `ncbi_refseq-0002.jsonl.gz:4317` explicitly give strain DSM 23800 and identical paired assemblies GCA/GCF_003634665.1. BV-BRC row `bvbrc-0000.jsonl.gz:3172` independently gives both `DSM 23800` and `DSM:23800`; GTDB row `gtdb_genomes-0015.jsonl.gz:46448` gives DSM 23800. The complete authority-plus-accession matches justify these joins. Separate source fields legitimately yield separate evidence assertions.

Live [Datasets assembly metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_003634665.1/dataset_report) confirms the current DSM assembly pair, Scaffold level, SAMN09064533 and PRJNA456019. The current [Baika1 assembly](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_009684715.1/dataset_report) and its RefSeq mate are Complete Genome, associated with SAMN04539465 and PRJNA283783. These are distinct assemblies and samples, although the strain is type material. The bare Baika1 labels in NCBI, BV-BRC, GTDB and GOLD are not eligible collection keys; their direct BacDive assertions remain independently valid.

The pinned RefSeq and GTDB records explicitly cite PRJNA224116. Its inspected [BioProject page](https://www.ncbi.nlm.nih.gov/bioproject/PRJNA224116) identifies an annotation umbrella. Live Datasets instead exposes sequencing project PRJNA456019 for the DSM pair. This is source-field context, not evidence that the YAML's separately attributed project references are wrong or that the two project identifiers are interchangeable.

Native GOLD organism row 37285 supports Go0044452, DSM 23800. Project row 193928 explicitly connects Gp0290490 to that organism and SAMN09064533/PRJNA456019. Analysis row 152861 connects Ga0244548 to that project, GCA_003634665.1 and IMG 2770939614. The analysis has no direct organism ID, so the verified project edge is essential. CCUG 59994 has its own organism Go0613184 but no supported attached genome chain. Go0613185 -> Gp0761219 -> Ga0615369 describes bare Baika1 and its different assembly/sample; it was not transferred across the collection-based join. The three native organism rows explain the GOLD ORGANISM count of three without implying three BacDive strains.

Native StrainInfo row `data/straininfo/records.jsonl.gz:303864` verifies SI-ID405975, versioned DOI 10.60712/SI-ID405975.3, published-online status, BacDive 11759, correct taxon and LPSN identity, and two own available deposits: DSM 23800/SI-DP913240 and CCUG 59994/SI-DP917512. Authorities are non-deprecated and deposit relations are not erroneous. The sole genome sequence, unversioned GCA_003634665, explicitly names DSM deposit 913240. Its assembly evidence is correctly attached only to DSM; sharing SI-ID405975 does not authorize transfer to CCUG. All four typed related records and the assembly's own evidence agree with the native payload. The version DOI browser resolver was unavailable, so its value was verified against the pinned source, not a successful live landing page.

ATB release 2025-05 retains SAMN09064533 as `atb.assembly:202505.SAMN09064533`, dataset 661k, run SRR7174584 and analysis ERZ26865156. Complete catalog row 1396234 and `data/atb/assemblies.tsv:5987` agree on FASTA availability, assembly/HQ/sylph PASS, SeqKit checksum, AWS URL, OSF batch 126 archive and no exclusion. All seven BioSample assertions occur in the YAML's related records. The five external genome links contain 13 supported same-source-chain pairs and mean only `shares_biosample`; no cross-product with the Baika1 assembly was introduced.

Live [ENA analysis XML](https://www.ebi.ac.uk/ena/browser/api/xml/ERZ26865156) independently links the analysis to SAMN09064533 and SRR7174584 and identifies a public Shovill/SPAdes reassembly with a FASTA file. [ENA run XML](https://www.ebi.ac.uk/ena/browser/api/xml/SRR7174584) identifies DSM 23800 and the same SRS3308840 sample. These support the sample/run link, not sequence equivalence to an NCBI assembly. FASTA contents and remote archive payloads were not downloaded or compared.

Raw source counts match NCBITAXON 1 NAME, LPSN 1 NAME, GTDB 2 GENOME, BACDIVE 1 STRAIN, MEDIADIVE 1 MEDIUM, GOLD 3 ORGANISM, MADIN 8 TRAIT_ASSERTION and BACTOTRAITS 4 TRAIT_ASSERTION. MediaDive's inventory identifies medium 693; the YAML only claims source coverage, not a medium recipe or species-wide growth phenotype. Trait counts likewise do not assert particular phenotypes. `data/taxa/PATHS.tsv:13248`, `curation/seed_scope.tsv:4041`, legacy page row 778 and the 2026-09-13 seed event agree on identity and eight-source scope.

## Completeness

Full native deposit audits examined 4,111,794 current/historical NCBI assembly rows, 1,419,549 BV-BRC rows, 901,341 GTDB rows, 531,961 GOLD organisms and 314,470 StrainInfo records. No additional eligible own-deposit assembly association was found within those audited source fields. Both culture identifiers normalize correctly under CAFI. The complete 3,227,665-row ATB catalog contains SAMN09064533 but not SAMN04539465. This is a pinned-inventory result, not a claim about all external assemblies or future releases.

Ignored-inclusive compressed searches (`rg --no-ignore --hidden -n -z`) covered numeric identifier, label and slug across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The final compact pass accounted for all 134 matching lines; long TSV evidence objects had already been fully parsed and compared rather than judged from truncated output. Recursive SOURCE.json traversal included ignored files and found no target-specific metadata entry. No separate target history record appeared in these searched surfaces. Optional phenotype, mechanism and causal-graph slots need not be populated from source counts. iModulonDB is not applicable to the YAML's taxonomic, nomenclatural and accession claims.

The merged-ID inventory contains 12 old identifiers pointing to 1032623. None is retained in the backbone, seed scope, PATHS or legacy path table. `src/taxonmech/seed.py` derives `replaces` from retained backbone records with `retired_into`, not every historical NCBI merge. Its absence here therefore matches the current corpus contract; no current record is orphaned by those old IDs. No own-ID dropped status was found in the full structured status scan.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Source-specific classification, project and accession-version distinctions are preserved without unsupported identity transfer.

## Recommended Edits

None required. Preserve SEEDED status and the generated-file boundary. Future authority corrections belong in their maintained source inputs and extraction paths, not hand-edits to this YAML. General source mapping/count behavior belongs to `src/taxonmech/extract.py` and `src/taxonmech/seed.py`; strain/genome joins must continue to obey `docs/STRAIN_GENOMES.md`, StrainInfo own-deposit rules and ATB same-source-chain rules. Scope ownership remains `curation/seed_scope.tsv`.

## Follow-up Checks

For an authorized source refresh, recheck the affected native identifiers and deposit chains, regenerate a single canary with `just seed-canary NCBITaxon:1032623 --force`, inspect all changed evidence and rerun both focused validators. Recount the GTDB cluster independently of eligible strain joins and retain ATB sample-versus-genome semantics. Run the documented full reproduction, provenance, history, product and QC gates before publishing corpus changes. No unresolved record-level blocker was found.

## Additional Notes

Numeric-substring matches were excluded using structured identity context: SAMEA1032623 belongs to a different taxon, SAMN41032623 and SRR11032623 are unrelated accession strings, and 10326232 occurs as a different genome's length. The extra SeqCode name 14737 is a source lead, not an asserted YAML mapping or grounds for automatic enrichment.

Some browser views for PubMed, GTDB, DOI and ENA were unavailable. Primary NCBI, PubMed, Crossref and ENA structured endpoints succeeded where used; GTDB, GOLD, BV-BRC and StrainInfo evidence was checked in complete pinned native inventories. No independent live IMG resolver check was performed; its typed identifiers were verified in the inspected BacDive/GOLD records. These access boundaries do not establish absence at the external services.

Only this new report was manually written for this target. No taxon, source inventory, code, scope, history, review status, GitHub item or generated page was changed.
