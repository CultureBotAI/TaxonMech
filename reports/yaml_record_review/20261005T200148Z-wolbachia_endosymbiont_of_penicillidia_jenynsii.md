# YAML Record Review: Wolbachia endosymbiont of Penicillidia jenynsii

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_penicillidia_jenynsii.yaml`
- Started UTC: 2026-10-05T19:58:13Z
- Finished UTC: 2026-10-05T20:01:48Z
- Verdict: pass

## Target

The entire 57-line generated `TaxonRecord` was read. It denotes
`NCBITaxon:1034762`, Wolbachia endosymbiont of Penicillidia jenynsii,
rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:2640676`,
genetic code 11, `EXACT` grounding, `SEEDED` status, and
`strain_count: 0`. This is the bacterial taxon, not its host,
another bacterium from that host, or a culture-deposit identifier.

Owning rows are `data/raw/ncbitaxon_taxa.tsv:221685` and
`curation/seed_scope.tsv:321996`.
`data/taxa/PATHS.tsv:14155` agrees in identifier and slug.

## Validation

- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/wolbachia_endosymbiont_of_penicillidia_jenynsii.yaml`: exit 0, no issues.
- `UV_OFFLINE=1 UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_penicillidia_jenynsii.yaml --out /private/tmp/wpj-strict-20261005.tsv`: exit 0; one file, zero error files and zero error rows. The output TSV was read and contains only its header.
- Structured comparisons checked the complete backbone row and eleven ancestors, PATHS, scope, attestation, and seed event. Seven raw inventories and exact type-material, merged-ID, and dropped-record tables were checked.
- `rg --no-ignore --hidden -n -z -i` searched the target ID, full label, slug, and host name across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation`, and `history`. Ignored, hidden, and compressed content were included; `SOURCE.json` manifests were excluded from candidate-row scanning. All ten candidates were read fully with TSV headers or JSON decoding.
- A separate search across those roots for AB632590, AB632591, OP797997, PeJe1, PeJe2, and WolPenjensii17 found no row. Ignored-inclusive content and filename searches in `reports` and `history` found no prior target report or separate target history artifact, including marker/alias matches, before this report.
- Live NCBI Taxonomy EFetch/Datasets, exact nonexpanded Assembly/Nuccore searches, full metadata for all three Nuccore records, four PubMed queries, and the original study's PubMed record were inspected. Bounded web searches and relevant primary article text were read as detailed below.
- Not checked: full-corpus `just verify-corpus`, `just qc`, full tests, full strict validation, provenance hashes, full history validation, site drift, documentation statistics, publication-size gates, and vendored synchronization. Focused comparisons do not establish whole-corpus reproduction.
- iModulonDB and curator-added graph ID/label checks are inapplicable: the YAML asserts no gene, regulator, protein, phenotype, transcriptomic result, or causal graph. No separate applicable focused term/reference validator was available beyond schema and authority checks.

## Identity and Grounding

Live NCBI Taxonomy EFetch and Datasets agree with the exact ID and
scientific name, species rank, parent 2640676, Bacteria division,
and genetic code 11. The root-first lineage is
`1 > 131567 > 2 > 3379134 > 1224 > 28211 > 766 > 942 > 952 > 953 > 2640676`.
All labels and normalized ranks match: root, cellular organisms,
Bacteria, Pseudomonadati, Pseudomonadota, Alphaproteobacteria,
Rickettsiales, Anaplasmataceae, Wolbachieae, Wolbachia, and
unclassified Wolbachia.
[NCBI Taxonomy](https://www.ncbi.nlm.nih.gov/Taxonomy/Browser/wwwtax.cgi?id=1034762);
[NCBI Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1034762).

The exact scientific-name row is
`data/catalog/ncbi_names-0005.jsonl.gz:31073`.
The backbone has no target synonyms, retirement target, or direct
children. Exact type-material, merged-ID, and dropped-record
checks found no target row. Species rank for a host-associated
provisional name does not establish valid nomenclatural publication,
host exclusivity, or equivalence among all sequences filed under
the taxon. `EXACT` denotes taxonomic grounding, not isolate identity.

## Evidence

The sole NCBITAXON attestation agrees in ID, label, count 1, unit
`NAME`, and snapshot 2026-09-13. This is a count of source name
assertions, not a count of isolates or genomes. Scope and the
2026-09-13T17:54:04Z `seed_from_sources` /
`SEEDED_FROM_SOURCES` event agree exactly.

The exact query `txid1034762[Organism:noexp]` returned zero
Assembly items with missing-phrase/no-items diagnostics and three
Nuccore items. All three are partial 16S rRNA markers, not genomes:

| Versioned accession | UID | Length | Explicit source metadata |
|---|---|---|---|
| AB632590.1 | 383212622 | 1,426 bases | Isolate PeJe1; host Penicillidia jenynsii, bat fly; Japan: Hyogo, Sayou-gun; taxon:1034762 |
| AB632591.1 | 383212623 | 1,426 bases | Isolate PeJe2; the same host and locality text; taxon:1034762 |
| OP797997.1 | 2326829003 | 427 bases | Clone WolPenjensii17; whole mosquito body; host qualifier Anophelese mosquitoes; India; taxon:1034762 |

The first two were submitted on 19 May 2011 by the Hosokawa/Nikoh
collaboration. Their source features directly support the named
bat-fly association for those isolates. Neither provides a
culture-collection accession.
[GenBank AB632590.1](https://www.ncbi.nlm.nih.gov/nuccore/AB632590.1);
[GenBank AB632591.1](https://www.ncbi.nlm.nih.gov/nuccore/AB632591.1).

The newer clone was submitted on 8 November 2022 by Khan, Sahu,
Jain, Mishra, and Das; its reference remains marked unpublished.
Its source feature names a mosquito host despite the bat-fly-based
organism label. Preserve that discrepancy: taxonomic assignment
alone neither proves equivalence to PeJe1/PeJe2 nor establishes
natural host range, intracellular localization, or transmission.
The host wording is recorded as supplied, including its spelling.
This is a source-level uncertainty for possible enrichment, not
a contradiction in the current YAML, which reproduces the NCBI
name and asserts no exclusive host range.
[GenBank OP797997.1](https://www.ncbi.nlm.nih.gov/nuccore/OP797997.1).

The older GenBank references still say unpublished, but the matching
Hosokawa et al. study is published: DOI `10.1038/ismej.2011.125`,
PMID `21938025`, online in September 2011 and in the March 2012
ISME Journal issue. Its inspected methods and results distinguish
a minor Wolbachia-like 16S genotype in P. jenynsii from the major
gammaproteobacterial symbiont later named Candidatus Aschnera
chinzeii. The minor genotype is 1,426 bases, consistent with the
two submitted markers. The study's bacteriome, genome-reduction,
co-speciation, and uterine-transmission results concern the major
symbiont; they must not be reassigned wholesale to this Wolbachia
record. Matching host names do not collapse the two bacteria.
[Original study](https://academic.oup.com/ismej/article/6/3/577/7590034);
[PubMed 21938025](https://pubmed.ncbi.nlm.nih.gov/21938025/).

The 2024 Koga et al. genome paper, DOI
`10.3389/fmicb.2023.1336919`, explicitly studies Aschnera from
the same host. Its genome and metabolic predictions are not
Wolbachia genome evidence. This is a relevant same-host exclusion,
not a proposed merge or a review of another taxon.
[Primary Aschnera genome article](https://www.frontiersin.org/journals/microbiology/articles/10.3389/fmicb.2023.1336919/full).

The four PubMed queries were:
`"Penicillidia jenynsii"[All Fields] AND Wolbachia[All Fields]`
(zero), `10.1038/ismej.2011.125[All Fields]` (one, PMID 21938025),
`OP797997[All Fields]` (zero), and
`AB632590[All Fields] OR AB632591[All Fields]` (zero).
Translations and diagnostics were read. These searches do not
cover all full-text mentions or prove absence of publication.

## Completeness

The seven parsed inventories contain no exact target BacDive, LPSN,
GTDB, GOLD, MediaDive, Madin, or BacTraits row. Three of the ten
native candidates are exact backbone, scope, and name rows;
the seven other matches are distinguished below. No exact
culture deposit, assembly, type-material assertion, or GTDB
mapping was established by the checked sources.

Optional synonyms, nomenclature, mappings, strains, traits, and
graphs can remain empty under the local checklist.
`strain_count: 0` denotes inventory coverage; it does not deny
the existence of the named sequence isolates. The markers are
optional enrichment leads, not missing whole genomes. No missing
required field was demonstrated.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the current YAML. The mosquito-host metadata and
stale unpublished flags are external evidence cautions. The record
does not assert either universal bat-fly restriction or the
unpublished status of those studies, and it imports neither
Aschnera biology nor disputed marker provenance.

## Recommended Edits

No required edit is demonstrated. Preserve generated fields and
`SEEDED` status.

Separately authorized marker enrichment belongs in maintained
extraction inputs and logic (`scripts/extract_source_inventory.py`,
`src/taxonmech/extract.py`), with a seeder change in
`scripts/seed_from_sources.py` only if representation requires it.
Preserve accession versions, isolate/clone designations, host and
locality provenance, and the OP797997 discrepancy. Do not silently
normalize all host metadata to the taxon label or count markers as
genomes. `curation/seed_scope.tsv` owns scope, not inferred identity.
Never patch generated YAML or pages.

## Follow-up Checks

Before optional enrichment, re-read each versioned source feature,
resolve the mosquito clone's host/classification evidence, and
test that PeJe1, PeJe2, and WolPenjensii17 remain distinct source
entities. Exclude the same-host Aschnera record, unrelated sample/run
identifiers, and comparative phylogeny sequences from exact joins.

An experimental trait, transmission mechanism, genome link, or
host-range extension requires primary evidence explicitly bridged
to the represented organism. Regenerate through the maintained
pipeline and rerun focused schema and strict validation. Before
publishing regenerated products, run the documented corpus
reproduction, QC, tests, strict validation, provenance, history,
and site gates.

## Additional Notes

The seven non-target native matches were fully inspected:

- `data/raw/ncbitaxon_taxa.tsv:222110`, `curation/seed_scope.tsv:322380`, and `data/catalog/ncbi_names-0005.jsonl.gz:31589` describe bacterium endosymbiont of Penicillidia jenynsii, `NCBITaxon:1035582`, rank `FORMA_SPECIALIS`, parent 1485666. Sharing a host does not make it taxon 1034762.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6465` is Mycobacterium tuberculosis ERR1034762, taxon 1773, BV-BRC genome 1773.18640. `data/catalog/allthebacteria.tsv.xz:569232` also concerns M. tuberculosis, run ERR1034762, sample SAMEA3558295, and analysis ERZ3500519. The run's numeric suffix is not the target taxon ID.
- `data/gold/projects.jsonl.gz:156965` concerns Echinostoma caproni Egypt, project Gp0236200, organism Go0107312, BioProject PRJEB1207, and BioSample SAMEA1034762. A BioSample suffix does not establish target identity.
- `data/catalog/ncbi_genbank-0025.jsonl.gz:5939` is Thermococcus sp. taxon 35749, assembly GCA_027038075.1, whose ungapped genome length happens to be 1034762.

Additional literature was scoped as follows:

- Lee et al. (2021), DOI `10.1186/s13071-021-05016-6`, reports Wolbachia detection in Korean P. jenynsii specimens and ftsZ-based phylogenetic analysis. The inspected text supports host-associated context, not an explicit identity bridge to PeJe1, PeJe2, or the exact taxon-level sequence submissions. No prevalence, mechanism, or isolate equivalence was transferred. [Primary article](https://link.springer.com/article/10.1186/s13071-021-05016-6).
- Han et al. (2019), DOI `10.11853/j.issn.1003.8280.2019.01.004`, uses AB632590 and AB632591 as reference sequences in a Yunnan survey. The inspected methods and sequence-analysis text distinguish new survey samples from those references. Their sequence similarity does not make the survey samples the Japanese isolates. [Primary journal article](https://html.rhhz.net/ZGMJSWXJKZXZZ/2019-1-18.htm).
- Several PMC pages returned browser challenges. Publisher text was available for the original ISME study, the Korean survey, and the Aschnera genome paper. A Myanmar mosquito-study lead was not adopted as target-specific evidence after its PMC page was inaccessible. Later ISME page-offset requests also failed after the initial relevant text had been read; no inaccessible supplement was treated as verified evidence.
- Bounded exact OP797997 and WolPenjensii17 web searches did not establish a primary experimental publication for that clone.

Search misses include ignored files within the stated roots and
remain bounded, not global absence claims. No paid research,
outbound contact, GitHub mutation, record/inventory/scope/history
edit, status promotion, regeneration, or Eukaryota review occurred.
