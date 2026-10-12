# YAML Record Review: Flavobacteriaceae bacterium HQM

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/flavobacteriaceae_bacterium_hqm.yaml`
- Started UTC: 2026-10-10T02:40:11Z
- Finished UTC: 2026-10-10T02:42:47Z
- Verdict: pass

## Target

The entire 57-line generated `TaxonRecord` was read. `NCBITaxon:1037408` denotes Flavobacteriaceae bacterium HQM, rank `SPECIES`, domain `BACTERIA`, parent `NCBITaxon:61432`, genetic code 11, grounding `EXACT` and mapping status `SEEDED`.

The record contains eleven ancestors, zero inventoried strains, one NCBITAXON name attestation and one seed event. It asserts no genus, formal nomenclature, culture deposit, genome, physiological trait or causal graph. HQM is not HQM10 or an isolate with a numeric suffix such as HQM.1.

## Validation

Commands used `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache UV_OFFLINE=1 uv run --offline`:

- `linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/flavobacteriaceae_bacterium_hqm.yaml`: pass, no issues.
- `python scripts/validate_strict.py data/taxa/bacteria/flavobacteriaceae_bacterium_hqm.yaml --out /private/tmp/taxonmech-flavobacteriaceae-hqm-20261010-validation.tsv --workers 1`: one file, zero errors; output reread, header only.
- `python scripts/validate_history.py history`: 17 valid records, zero invalid links.
- Structured comparisons verified identity, all ancestors, code, empty synonyms, own source inventories, unique index/scope resolution, attestation and exact seed reason. Complete backbone scanning found no immediate child. Own type-material, merged-ID and dropped-record inventories had no rows.
- The complete native NCBI name row was read. Other native search candidates were inspected for identity and all matching fields. Live EFetch/Datasets responses and three nucleotide-search responses were read.
- Not checked: full-corpus `just verify-corpus`, `just validate-all`, `just qc`, tests, source replay, rendering and publication gates. No graph is present for `just validate-products`. Focused agreement does not establish corpus reproduction.
- NCBI and DDBJ target browser pages were unavailable through the web reader. Structured NCBI taxonomy APIs succeeded. Nucleotide searches returned indexing warnings, documented below; no sequence or literature-based biological characterization was established for this target.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222745`, [NCBI EFetch taxonomy](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1037408&retmode=xml) and [Datasets taxonomy](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1037408) agree on the exact name, species rank and lineage. EFetch confirms parent 61432 and code 11.

The full root-first chain agrees with the backbone: root, cellular organisms, Bacteria, Pseudomonadati, FCB group, Bacteroidota/Chlorobiota group, Bacteroidota, Flavobacteriia, Flavobacteriales, Flavobacteriaceae and unclassified Flavobacteriaceae. Both intermediate groups correctly retain `CLADE`; the unclassified parent retains `NO_RANK`. EFetch confirms the chain below root, and Datasets includes root 1. The absence of a genus is faithful to the source, not a missing lineage element to fill with a guessed genus.

The complete native row `data/catalog/ncbi_names-0005.jsonl.gz:32376` is a scientific name with an empty unique-name qualifier. EFetch supplies no alternate names. NCBI species rank for this informal family-level label does not constitute formal ICNP nomenclature.

The related-looking HQM10 label resolves separately to `NCBITaxon:980583` in `data/raw/ncbitaxon_taxa.tsv:204476`; that source row was read as disambiguation context, not as another record review. Its shared parent does not establish identity with HQM.

`EXACT` means grounding to this NCBI identifier, not resolution to a named genus/species or experimental characterization. The one-NAME attestation correctly represents the 2026-09-13 snapshot, and the seed event agrees with the maintained scope reason.

## Evidence

The live nucleotide query `txid1037408[Organism:exp]` returned count zero together with a `phrasesnotfound` entry. Exact full-name queries in both the Organism and All Fields search fields also returned zero; their responses included an incorrect-translation marker and quoted-phrase warnings. These are current search outcomes with indexing limitations, not proof that no historical, suppressed, differently annotated or otherwise unindexed sequence exists.

The Datasets taxonomy response omitted an assembly-count field; omission is not an explicit zero-assembly result. No accession can responsibly be invented or borrowed from the other HQM-labelled organisms. A bounded exact-name web search supplied taxonomy leads rather than an established target-specific biological paper. The YAML itself cites no biological paper or experimental claim requiring such support.

The inspected repository genome candidates are different organisms. HQM.1 is attached to a Legionellaceae bacterium, HQM.2 to Aeromicrobium, HQM.3 to a Candidatus Nanopelagicales bacterium, HQM.4 to Rugosibacter, HQM.15 to a Stutzerimonas/Pseudomonas stutzeri record, and HQM.16 to a Thermomicrobiales bacterium. Their accession/taxonomy fields do not identify taxon 1037408. Likewise, `GCA_902517315.1` denotes an uncultured Alphaproteobacteria bacterium, isolate AG-325-O18; its genome length happens to be 1,037,408 bases. A genome-size number is not a taxon-ID match.

The current record makes no unsupported phenotype, mechanism, host or habitat inference from those unrelated candidates. Its sole positive evidentiary assertion is its supported NCBI name attestation.

## Completeness

Ignored-inclusive, compressed-content-inclusive `rg --no-ignore --hidden -n -z -i` searches covered `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`, using the bounded taxon ID, full label, slug and HQM token. Nineteen lines matched: own taxonomy/name/scope rows and the unrelated genome candidates described above.

Complete structured scans found no own-taxonomy BacDive, LPSN, GTDB, GOLD, MediaDive, Madin or BactoTraits inventory row. The bounded source search established no eligible own cultured-deposit or genome join. This is a repository coverage finding, not a global biological absence claim.

Five independently enumerated SOURCE.json files were parsed with no target match. An initial gitignore-independent filename search also surfaced the HQM10 near-name. A second exact-stem search found exactly one HQM target YAML and no prior target report. History filenames had no target-specific match.

`strain_count: 0` describes inventory coverage, not proof that HQM cannot be cultured. Empty optional nomenclature, mappings, deposits, definitions and graphs are appropriate. iModulonDB is not applicable to the taxonomy/name assertions; unrelated gene or expression hits sharing a numeric ID cannot create a gene claim for this taxon.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the inspected assertion scope. The record faithfully preserves the supported NCBI identity and unresolved genus-level placement without adopting neighboring names or unrelated genome evidence.

## Recommended Edits

None required. Leave the generated YAML, seed status and curation history unchanged.

Any separately authorized enrichment belongs in maintained source inventories or a supported extraction/harmonization extension before regeneration. Do not hand-edit this generated record, merge HQM with HQM10, normalize away meaningful numeric suffixes or treat the nucleotide-search warnings as evidence of biological absence.

## Follow-up Checks

If a sequence, culture or publication is proposed, verify its exact taxon/strain linkage at the authority and retain accession versions and source provenance. Where search indexing remains incomplete, inspect the proposed source directly rather than treating an empty search as definitive.

After maintained input changes, rerun the documented canary, schema/strict/history checks and full-corpus reproduction/QC gates. The currently supported NCBI-only record needs no curator correction.

## Additional Notes

- YAML SHA-256: `c1b5323f56405e55fb850a26e56735aac3413caeade389ca97277f5797a4b8d1`.
- `data/taxa/PATHS.tsv:15297` and `curation/seed_scope.tsv:322967` uniquely resolve the target. The exact seed event retains 2026-09-13T17:54:04Z.
- Read-only review at HEAD `b6a6508faca1388b88feb5740b1095e9f64cfdb8`. Only this new report was added for this target. No tracked record, input, schema, history, page, branch, worktree or GitHub state changed. No Eukaryota YAML was opened or review status promoted.
