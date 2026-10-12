# YAML Record Review: 'Gerbera jamesonii' phytoplasma

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/gerbera_jamesonii_phytoplasma.yaml`
- Started UTC: 2026-10-06T17:51:02Z
- Finished UTC: 2026-10-06T17:54:03Z
- Verdict: pass

## Target

The fully read generated `TaxonRecord` denotes `NCBITaxon:1035244`, 'Gerbera jamesonii' phytoplasma, rank SPECIES, domain BACTERIA, parent `NCBITaxon:3042590`, genetic code 11, grounding EXACT and status SEEDED. It contains ten ancestors, zero inventoried BacDive strains, one NCBITAXON NAME attestation and one seed event. No synonyms, xrefs, nomenclature, mappings, strain entries, genome links, definition, record-level evidence, host/phenotype claim, discussion or graph is present.

The unique path-lock row is `data/taxa/PATHS.tsv:14454`; scope is `curation/seed_scope.tsv:322238`. The name refers to the bacterium associated with the named host, not the eukaryotic plant. Eukaryota was not reopened. HEAD remained `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

## Validation

The review skill and checklist were reread. Curation guidance, CLAUDE.md, justfile, CURATION, HARMONIZATION, SCHEMA, history guidance, source boundaries, relevant schema and seeder had been inspected at this unchanged revision. Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache`.

- `uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/gerbera_jamesonii_phytoplasma.yaml`: exit 0, no issues.
- `uv run --offline python scripts/validate_strict.py data/taxa/bacteria/gerbera_jamesonii_phytoplasma.yaml --out /private/tmp/gjp-strict.tsv`: exit 0, one file, zero errors. The actual TSV was read and contains only its header.
- Manual bounded source checks confirmed identity, every ancestor, path/scope, attestation and event. These are not a focused corpus-reproduction validator.
- Not run: `just verify-corpus`, full-corpus strict validation, `just qc`, tests, provenance/site gates or global `just validate-history`. Corpus reproduction has no target selector; no corpus-wide reproducibility/reference-integrity claim is made.
- `just validate-products` was not run: configured curator-added graph grounding is absent, and the gate skips NCBITaxon. Taxonomic identifiers were checked against pinned and live authority data instead.
- Ignored-inclusive content/path searches found no target external history artifact in the searched history tree. No history event or status promotion was made.
- Before web follow-up, `uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets` succeeded. All 28 dataset rows were inspected; none covers Phytoplasma. Not applicable, not negative biological evidence.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:221963` supports the identity, rank, parent, code 11, empty synonyms and 2026-09-13 snapshot. The complete scientific-name row is `data/catalog/ncbi_names-0005.jsonl.gz:31431`. Exact type-material, merged-ID and dropped-record scans found no target rows.

Complete [NCBI taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035244&retmode=xml) and [NCBI Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035244) agree. The pinned root-first chain matches every stored ancestor label and rank: root (1), cellular organisms (131567), Bacteria (2), Bacillati (1783272), Mycoplasmatota (544448), Mollicutes (31969), Acholeplasmatales (186329), Acholeplasmataceae (2146), Candidatus Phytoplasma (33926), 16SrI (Aster yellows group) (3042590). The immediate parent is a SPECIES_GROUP, not a species asserted equivalent to this target. XML omits root in LineageEx; Datasets includes it.

A near-homonym without the host quotation marks is a separate active source concept: Gerbera jamesonii phytoplasma, `NCBITaxon:244213`. Its complete pinned rows are `data/raw/ncbitaxon_taxa.tsv:47904`, `data/catalog/ncbi_names-0001.jsonl.gz:26396` and `curation/seed_scope.tsv:168077`. Its [live NCBI taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=244213&retmode=xml) and Datasets response independently retain that identifier and the same 16SrI parent. Neither punctuation stripping nor shared parentage establishes a merge or biological equivalence. This comparison is identity context, not a second completed record review.

EXACT identifies the NCBI source concept, not valid nomenclature. The inspected [LPSN Candidatus Phytoplasma asteris page](https://lpsn.dsmz.de/species/phytoplasma-asteris), record 800060, concerns a broader named species and gives MIAY/OAY and M30790 as nomenclatural context. Its displayed status distinguishes not validly published/lectotype from pro-valid publication and pro-correct naming. None of those statuses or type designations is automatically this host-associated taxon's nomenclature. No exact target LPSN mapping was found in the pinned inventory.

## Evidence

The NCBITAXON attestation exactly matches identifier, label, count 1, unit NAME and snapshot. The seed event at 2026-09-13T17:54:04Z, curator `seed_from_sources`, action SEEDED_FROM_SOURCES and one-source scope reason agree. This count is one source-name assertion, not a genome or biological strain count.

No exact target rows occur in the inspected `data/raw/bacdive_strains.tsv`, `lpsn_names.tsv`, `gtdb_mappings.tsv`, `gold_organisms.tsv`, `mediadive_taxa.tsv`, `madin_taxa.tsv` or `bactotraits_taxa.tsv`. No backbone child has this taxon as parent. Zero BacDive records agrees with the own/subtree gathering rule in `src/taxonmech/seed.py:488`, without making a general claim about culture availability.

The exact live query `txid1035244[Organism:noexp]` returned zero assemblies with phrases-not-found/no-items diagnostics and one nucleotide UID, 334145777. Full [JF795864.1 metadata](https://www.ncbi.nlm.nih.gov/nuccore/JF795864.1), excluding bases, was inspected. The 1803-nt record is a ribosomal-region marker: partial 16S and 23S genes, complete intergenic spacer and tRNA-Ile. It gives isolate pgerbera2010, explicit `taxon:1035244`, host Gerbera jamesonii Bol., Italy, collection May 2010, infected plant source and clone labels 37; 38; 39. Submitted 11 April 2011; created/updated 1 July 2012. No culture deposit, BioSample, BioProject or assembly identifier is supplied. Genomic DNA is not an assembly claim.

The marker itself contains only a direct-submission bibliography. The [CNR institutional record](https://iris.cnr.it/handle/20.500.14243/271911) supplies the complete abstract of the 2011 Spano and colleagues report and explicitly identifies JF795864 in gerbera from Apulia, interpreting it as Candidatus Phytoplasma asteris-related evidence. The [publisher archive entry](https://www.sipav.org/en/16/Archive/2361) verifies the title, five authors, 2011 volume 93 supplement and DOI 10.4454/jpp.v93i4.2361. The DOI resolver failed through the web tool; the publisher page and institutional abstract succeeded. No separate original PDF or supplements were inspected.

The abstract reports January 2010 symptom observations and two sequenced clones, whereas the nucleotide qualifiers give a May collection and three clone labels. These source statements are retained separately; observation date need not be collection date, and clone-count correspondence was not resolved. Neither discrepancy is a claim in the YAML, and neither justifies silently changing source metadata.

The inspected [2015 New Disease Reports article](https://www.ndrs.org.uk/article.php?id=31024), DOI 10.5197/j.2044-0588.2015.031.024, distinguishes its Indian GYLu1/JX674049 and GYLu2/KC880350 samples from Italian JF795864 used for comparison. It does not make those samples equivalent. Host sharing, 16SrI membership and sequence similarity do not transfer Indian sample provenance or other gerbera-associated phytoplasma groups to this target. No experimental protocol or phenotype assertion is added to TaxonMech.

## Completeness

Ignored and compressed content was included with `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Taxid, quoted/unquoted label pattern and slug returned 18 rows, all fully inspected: three target rows, three near-homonym rows and twelve unrelated numeric matches. Five discovered SOURCE.json files were separately parsed in full without a target value; history filenames were enumerated independently of ignore rules.

A same-root search for `pgerbera[- _]?2010|JF795864` found no local hit. The five source metadata documents and history filenames were also checked for these new identifiers with no match. These are bounded input-root results, not claims about every original ignored snapshot or remote database. The culture normalizer returns empty for pgerbera2010; a bare isolate label is not an eligible deposit join key.

No supported owning-strain/own-deposit bridge or required missing genome relationship was established. The marker and associated literature can support optional identity context but do not create a BacDive owner, culture deposit, assembly or same-deposit StrainInfo link. Empty optional evidence, definition and graph slots need not be filled. Host/disease/phenotype curation belongs in the corresponding sibling repositories, with its own claim-level evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found in the existing seeded assertions and bounded completeness checks. The near-homonym and source-specific collection/clone details remain explicit follow-up cautions, not proven record defects. Pass does not certify unrun corpus gates or universal completeness.

## Recommended Edits

None required. Retain the exact NCBI identifier, label punctuation, parent chain and SEEDED status. Do not merge taxon 244213 on normalized names, promote the species-group parent to equivalence, or transfer broader LPSN nomenclature/type flags.

Future supported additions belong in maintained extraction/matching/seeding logic under `src/taxonmech/`, with regression tests. Scope changes belong in `curation/seed_scope.tsv`; authoritative mapping corrections belong upstream in kg-microbe or NCBI. Do not hand-edit generated YAML or pages.

## Follow-up Checks

Before deduplication, require explicit authority evidence relating the two taxon identifiers; name normalization and common host/lineage are insufficient. Before adding strain/genome links, require an eligible complete collection accession and source-specific chain. Keep marker, clone, isolate, taxon, deposit, sample, project and genome identities separate. StrainInfo must name the same matched SI-DP, GOLD must resolve the same organism/project/analysis chain, and ATB needs existing BioSample evidence; shared sample does not imply genome equivalence.

Reconcile the original study's clone/sample context before curator-authored claims that depend on it. After any authorized maintained-input change, run target schema/strict validation and relevant join tests, followed by `just verify-corpus` and `just qc`.

## Additional Notes

- Four excluded Lacticaseibacillus rhamnosus rows identify taxid 47715, strain 1001270st1_A4_2201SCRN_220225, GCA/GCF_040924945.1, BV-BRC 47715.1897 and SAMN41035244: `data/bvbrc/bvbrc-0020.jsonl.gz:45786`, `data/catalog/gtdb_genomes-0007.jsonl.gz:465`, `data/catalog/ncbi_genbank-0037.jsonl.gz:20851`, `data/catalog/ncbi_refseq-0006.jsonl.gz:19997`.
- `data/bvbrc/bvbrc-0006.jsonl.gz:6264` is Mycobacterium tuberculosis, taxid 1773, BV-BRC 1773.18457, run ERR1035244. `data/catalog/allthebacteria.tsv.xz:569714` concerns that run, SAMEA3558777 and ERZ3502630. Available FASTA/PASS filters do not supply a target association.
- `data/catalog/ncbi_genbank-0009.jsonl.gz:6456` is Campylobacter jejuni, taxid 197, strain PNUSAC014888, GCA_010352445.1 and SAMN13763562.
- `data/catalog/ncbi_genbank-0023.jsonl.gz:12325` identifies Salmonella enterica subsp. enterica serovar Paratyphi B var. L(+) tartrate +, taxid 224729, isolate MS160175, GCA_025080235.1 and SAMEA103524418. The ATB row `data/catalog/allthebacteria.tsv.xz:66148` uses serovar Java, run ERR1865245 and ERZ3070649 for that sample. The source names are preserved, not used to infer phytoplasma identity or genome equivalence.
- Three rows concern GCA/GCF_040608205.1, SAMN41498391, NCBI taxid 3156715 and Streptomyces sp. NPDC005209: `data/catalog/ncbi_genbank-0037.jsonl.gz:6037`, `data/catalog/ncbi_refseq-0006.jsonl.gz:14894`, `data/catalog/gtdb_genomes-0002.jsonl.gz:16914`. GTDB calls the cluster Streptomyces olivochromogenes_A; the numeric match is within genome length 10352443. No label or genome is transferred.
- The full target was reread byte-identical. Only this report was written; no YAML, source inventory, history, status, generated product, Git or GitHub mutation was made.

