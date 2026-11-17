# YAML Record Review: marine sediment bacterium BB0608_AND_5.2_6S0

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_2_6s0.yaml`
- Started UTC: 2026-10-04T14:04:23Z
- Finished UTC: 2026-10-04T14:05:23Z
- Verdict: pass

## Target

Entire generated `TaxonRecord` read: `NCBITaxon:1033566`, species, Bacteria,
`EXACT`, `SEEDED`, genetic code 11, four ancestors, zero inventoried strains,
one NCBITAXON NAME attestation and one seed event. BB0608_AND_5.2_6S0
distinguishes this record from neighboring AND_5.2 isolates.

## Validation

- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_2_6s0.yaml`: passed, no issues.
- `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache just validate-strict data/taxa/bacteria/marine_sediment_bacterium_bb0608_and_5_2_6s0.yaml`: passed, one file, zero ERROR rows; validation TSV refreshed.
- Full backbone, lineage, synonyms, attestation, scope and seed-text comparisons passed. Exact type-material, merged-ID and dropped scans found no target rows; direct children: zero.
- Not checked: full-corpus `just verify-corpus`, `just qc`, tests, global term/reference checks, provenance/history/product gates and rendering. Bounded comparisons do not replace those gates.

## Identity and Grounding

Backbone row 221200 and scientific-name row 30508 in
`data/catalog/ncbi_names-0005.jsonl.gz` agree with the YAML. Live NCBI
[EFetch](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1033566&retmode=xml)
and [Datasets](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1033566)
confirm identity and species rank; EFetch confirms parent 49928 and code 11.
Root-first lineage matches root (1), cellular organisms (131567), Bacteria
(2) and unclassified Bacteria (49928). Species rank does not establish valid
nomenclatural publication or finer taxonomic placement.

## Evidence

Exact Nuccore search returned one sequence, [JF750109.1](https://www.ncbi.nlm.nih.gov/nuccore/JF750109.1),
UID 333384456, a 452-base partial 16S rRNA gene. Source qualifiers name
strain BB0608_AND_5.2_6S0, taxon 1033566, coastal marine sediment,
Australia: Gulf of Carpentaria and June 2008 collection. The qualifier is
strain, not clone or environmental sample. This locus is not a genome,
culture deposit or independent taxonomic classification.

Both references were inspected: Cornall, Beyer, Streten-Joyce, McGuinness,
Parry and Gibb's marine-sediment cryopreservation study marked unpublished,
and Cornall's direct submission dated 2011-04-01. Neither supplies a DOI
or PMID. Full manuscript text was not obtained; no phenotype was inferred
from the title. Exact Assembly search returned zero with phrase-not-found
and no-items warnings. The NAME attestation and 2026-09-13 snapshot match
the inventory; the count is not independent experiments.

## Completeness

Complete exact-ID scans found no target rows in BacDive, LPSN, GTDB, GOLD,
MediaDive, Madin or BactoTraits inventories. Empty optional slots reflect
bounded coverage; zero inventoried strains does not mean never cultured.

Ignored-inclusive `rg --no-ignore --hidden -n -z` searched the digit-bounded
numeric ID and complete label/stem designation, allowing dots/underscores,
across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`,
`data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`.
All eight matches were inspected: target scope, backbone and scientific
name, three unrelated ATB rows and two unrelated assembly-length matches.
Both native JSON objects were read in full. Recursive structured
SOURCE.json scans found no matches. These checks do not establish
universal absence.

- ATB row 64922 in `data/catalog/allthebacteria.tsv.xz`: SAMEA1033566, run ERR068169, analysis ERZ3068964; scientific name and both Sylph fields Streptococcus pneumoniae. Only the BioSample suffix matches.
- ATB row 1018815: SAMN02298226, runs SRR1033566 and SRR1171464, analysis ERZ4066934; scientific name and both Sylph fields Salmonella enterica. Only one run suffix matches.
- ATB row 2580318: SAMN34218323, run SRR24189259, analysis ERZ26322907; scientific name and both Sylph fields Salmonella enterica. Only SeqKit signature `seqkit.v0.1_DLS_k0_3fb51d085a90bc1033566d64a705acc9` matches; this signature is not MD5.
- GenBank `data/catalog/ncbi_genbank-0063.jsonl.gz:23657` and GTDB `data/catalog/gtdb_genomes-0010.jsonl.gz:43610`: GCA_964491185.1 and GB_GCA_964491185.1 with explicit GenBank link, uncultured Gammaproteobacteria bacterium, taxon/species 86473, isolate SRP342105_co2_162, SAMEA117382540, PRJEB82487 and CAZBFH000000000.1. This metagenome-derived scaffold assembly has 106 contigs, 85 scaffolds and no RefSeq pair. Only total length 1033566 matches; ungapped length is 1032096, a 1470-base difference, also carried as GTDB's gap length. GTDB places it in Patescibacteriota, species 2-01-FULL-39-10-A sp964491185, whereas its carried NCBI taxonomy is Pseudomonadota/Gammaproteobacteria. These differing classifications concern the unrelated assembly and are not reconciled here.

All three ATB rows have available FASTAs, assembly/Sylph/HQ filters PASS
and prior-HQ T. Exclusions are identity-based, not quality-based. None
supports a target strain/deposit/genome chain. Source versions and
explicit accession links are preserved.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the record and stated checks.

## Recommended Edits

None. Future corrections belong in maintained source inputs and
`src/taxonmech/extract.py` / `src/taxonmech/seed.py`; scope ownership is
`curation/seed_scope.tsv:321552`. Do not hand-edit generated YAML.

## Follow-up Checks

After an authorized correction, verify exact strain/deposit evidence,
inspect inventory deltas, run `just seed-canary NCBITaxon:1033566 --force`,
both focused validators, `just verify-corpus` and remaining QC gates.
No canary or regeneration was run.

## Additional Notes

Unique path: `data/taxa/PATHS.tsv:13649`. Seed event remains
2026-09-13T17:54:04Z. NCBI's browser page was inaccessible; EFetch and
Datasets succeeded. iModulonDB was not applicable to this taxonomy-only
record. Only this report and the documented validation TSV were written;
YAML, maintained inputs, scope, history, status and GitHub were unchanged.

