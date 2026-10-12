# YAML Record Review: Wolbachia endosymbiont of Anacrusis aulaeodes

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/wolbachia_endosymbiont_of_anacrusis_aulaeodes.yaml`
- Started UTC: 2026-10-07T14:34:29Z
- Finished UTC: 2026-10-07T14:37:01Z
- Verdict: pass

## Target

Read the complete generated `TaxonRecord` for `NCBITaxon:1035964`,
Wolbachia endosymbiont of Anacrusis aulaeodes.
This species-rank bacterial node has `EXACT` grounding,
`SEEDED` lifecycle, genetic code 11, 11 root-first ancestors,
one NCBI synonym, zero inventoried BacDive strains,
one NCBITAXON name attestation, and one inline seed event.
There are no nomenclature, taxonomy-mapping, strain/genome,
citation, phenotype, or causal-graph objects. Seeded fields
are generated and read-only.

## Validation

- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate data/taxa/bacteria/wolbachia_endosymbiont_of_anacrusis_aulaeodes.yaml`: passed, no issues.
- `env UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 just validate-strict data/taxa/bacteria/wolbachia_endosymbiont_of_anacrusis_aulaeodes.yaml --out /private/tmp/wol-aaula-strict.tsv`: passed, one file and zero errors; complete header-only diagnostics read.
- Parsed source checks passed for identity, every ancestor label/rank/link, synonym, attestation, unique path/scope rows, and seed-event wording. These are bounded checks, not corpus reproduction.
- Live NCBI taxonomy and exact Assembly/Nuccore index queries were inspected. Complete metadata, features, and references for both returned Nuccore objects were read, excluding sequence and translation payloads.
- `just validate-products`: not applicable; no curator-added graph grounding/label pairs. Taxon identifiers and labels were checked at NCBI.
- Standalone `just validate-history`: not applicable after ignored-independent content and filename searches found no target artifact. Inline history passed schema, strict, and source checks.
- Not run: full-corpus `just verify-corpus`, `just qc`, `just validate-all`, `just provenance-check`, `just render-check`, `just docs-check`, `just vendored-check`, and the test suite.
- NCBI's browser page was unavailable through the web tool; authoritative EFetch XML and Datasets JSON were available.
- Not checked: independent BOLD records, sequence alignment, or supplementary Table S2 of the contextual primary publication.

## Identity and Grounding

[NCBI EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035964&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035964)
agree on the active taxid, exact scientific name, species rank,
bacterial lineage, and parent `NCBITaxon:2640676`
(unclassified Wolbachia). EFetch confirms genetic code 11
and the synonym Wolbachia sp. Anacrusis aulaeodes.

The complete source rows agree at
`data/raw/ncbitaxon_taxa.tsv:222223`,
`data/catalog/ncbi_names-0005.jsonl.gz:31732` and line 31733,
`data/taxa/PATHS.tsv:14721`, and `curation/seed_scope.tsv:322480`.
The native synonym has class `synonym`, mapped to
`EXACT_SYNONYM` by `src/taxonmech/ncbi_taxdump.py:91`.
It names the same bacterial node, not the insect host.

All 11 ancestor IDs, labels, ranks, and links match the pinned
backbone; Datasets supplies root and EFetch the remaining
labeled chain. The lineage includes Pseudomonadota,
Alphaproteobacteria, Rickettsiales, Anaplasmataceae,
Wolbachieae, and Wolbachia. The snapshot is 2026-09-13.
Related/broad synonyms and `retired_into` are empty.
Parsed inventories contain no target child, type-material,
merged-ID, or dropped row.

The similarly named
[Anacrusis aulaeodesDHJ03 endosymbiont](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1084938&retmode=xml)
is a distinct active species node, `NCBITaxon:1084938`.
Live EFetch/Datasets and its full local backbone, scope, and
native-name rows agree. Its shared parent and overlapping
host-name text do not establish equivalence or authorize
transferring sequence evidence between nodes.

## Evidence

The attestation counts one `NAME`, not specimens, infections,
sequences, or genomes. Exact-target raw BacDive, LPSN, GTDB,
GOLD, MediaDive, Madin, and BactoTraits scans found no applicable
rows. With no backbone descendants, zero inventoried BacDive
strains agrees with the inputs.

The inline seed wording matches scope and inventories.
The timestamp `2026-09-13T17:54:04Z` is the latest of the
inspected raw, ATB, and StrainInfo extraction timestamps,
as required by `src/taxonmech/seed.py::_seed_timestamp`.

Exact Nuccore query `txid1035964[Organism:noexp]`
returned two partial COI records, each 658 nt and explicitly
linked to `taxon:1035964`:

- [JN674094.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674094.1): voucher `MHMXZ2184-09.w`, GenBank-reported BOLD cross-reference `ASWLP025-11.COI-5P`, CDS protein `AEQ36758.1`. The host feature names Anacrusis aulaeodes MHMXZ2184-09; collection was 8 November 2008 at Quebrada Oro, Sector Del Oro, Area de Conservacion Guanacaste, Costa Rica, by Lucia Rios.
- [JN674093.1](https://www.ncbi.nlm.nih.gov/nuccore/JN674093.1): voucher `MHMYF1384-10.w`, GenBank-reported BOLD cross-reference `ASWLP038-11.COI-5P`, CDS protein `AEQ36757.1`. The host feature names Anacrusis aulaeodes MHMYF1384-10 and gives Costa Rica without a collection-date feature.

Both annotate translation table 11 and codon start 2.
Both retain Smith's unpublished barcoding-manuscript reference
and direct submission on 13 September 2011 to the University
of Guelph. Specimen vouchers are not culture deposits, and
partial markers are not genome assemblies or verified distinct
cultured strains. Protein and BOLD IDs above are inspected
GenBank feature values, not independently retrieved objects.

The matching-title
[Smith et al. PLOS ONE publication](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0036514),
DOI `10.1371/journal.pone.0036514`, provides study context.
Its inspected methods describe bacterial COI recovered during
insect barcoding, .w specimen identifiers, and accession details
in supplementary Table S2. The main-text search did not find
Anacrusis; Table S2 was not inspected. No accession-specific
allele, reproductive effect, or host-wide prevalence is inferred.
GenBank's unpublished reference status is retained as stored,
not interpreted as proof that no relevant paper exists.

Exact Assembly query `txid1035964[Organism:noexp]`
returned zero with phrase-not-found/no-items diagnostics.
This bounded indexing result is not proof of global or
historical genome absence.

## Completeness

Complete enough for a generated NCBI-only identity record.
Optional slots are appropriately empty without applicable
supported objects. The external marker evidence does not
contradict the BacDive inventory count.

Ignored-independent search used
`rg --no-ignore --hidden -n -z -i` across `data/raw/`,
`data/catalog/`, `data/bacdive/`, `data/bvbrc/`,
`data/gold/`, `data/seqcode/`, `data/straininfo/`,
`data/atb/`, `curation/`, and `history/`.
Ignored, hidden, and compressed content was included.
Patterns covered the taxid, host-qualified label, slug,
both marker accessions, voucher stems, and BOLD stems.

All 25 candidate rows were read completely:

- Four describe the target backbone, scope, scientific name, and synonym.
- Three describe the distinct DHJ03 node: backbone, scope, and scientific name.
- BV-BRC `670.9523` and GenBank `GCA_050920685.1` describe Vibrio parahaemolyticus VpS05; their `PRJNA1035964` project is a numeric collision, not this taxid.
- GenBank `GCA_010359645.1` describes Campylobacter jejuni FSIS12027776, taxid 197.
- Ten ATB rows at lines 143459-143468 describe Escherichia coli samples SAMEA110359640 through SAMEA110359649.
- Five ATB rows at lines 401076-401080 describe Enterococcus cecorum samples SAMEA12751055 through SAMEA12751059; their run identifiers contain the numeric search substring.

The expanded marker/voucher/BOLD search returned no new rows.
Five native `SOURCE.json` files were parsed completely and
history filenames were searched independently.
No additional applicable local source assertion, culture deposit,
strain-genome link, or standalone history artifact was found
within these bounded roots. No global absence claim is made.

iModulonDB is not applicable: the record has no regulator,
expression module, or transcriptomic dataset. Optional COI
barcoding context is not expression-module evidence.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. Identity, lineage, synonym class/source, attestation
units, zero BacDive inventory count, optional omissions, and
seed provenance are supported.

## Recommended Edits

None required. Preserve generated YAML and `mapping_status: SEEDED`.
This read-only review does not authorize lifecycle promotion
or a curation-history event.

Future source corrections belong to maintained inputs and
`src/taxonmech/extract.py`/`src/taxonmech/seed.py`;
taxonomy name-class handling belongs to
`src/taxonmech/ncbi_taxdump.py`, and scope corrections to
`curation/seed_scope.tsv`. Do not edit generated YAML or pages.
Optional enrichment must preserve the target/DHJ03 distinction.

## Follow-up Checks

No corrective follow-up is required. Before optional publication
enrichment, inspect the exact accession/voucher rows in Table S2
and authoritative BOLD records. Keep specimen evidence separate
from cultures, genomes, and taxon-wide biological conclusions.

After separately authorized maintained-input changes, rerun the
owning generator, per-file schema/strict validation, and applicable
full-corpus acceptance gates. New curated history artifacts
require `just validate-history`; new graph terms/evidence
require `just validate-products`.

## Additional Notes

The complete YAML was reread and remained byte-identical before
report creation. All bounded source reads and public retrievals
reached terminal results. No YAML, source inventory, lifecycle,
standalone history, generated page, GitHub state, branch, or
worktree was changed. Eukaryota records were not re-reviewed.
Only this new timestamped report is authorized.
