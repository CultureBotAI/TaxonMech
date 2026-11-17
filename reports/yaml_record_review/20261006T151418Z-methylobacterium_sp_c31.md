# YAML Record Review: Methylobacterium sp. C31

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/methylobacterium_sp_c31.yaml`
- Started UTC: 2026-10-06T15:12:28Z
- Finished UTC: 2026-10-06T15:14:18Z
- Verdict: pass

## Target

One generated `TaxonRecord`, `NCBITaxon:1035204`, label `Methylobacterium sp. C31`, SPECIES / BACTERIA. The whole YAML was read before findings and checked byte-for-byte unchanged. Baseline HEAD: `b6a6508faca1388b88feb5740b1095e9f64cfdb8`.

The record carries EXACT grounding, SEEDED status, ten ancestors, code 11, zero BacDive strains, one NCBI NAME attestation and one seed event. There are no synonyms, equivalent xrefs, nomenclature, GTDB mappings, genome links, definition, citations, phenotype assertions or causal graph. The review concerns the exact taxid, not any arbitrary isolate named C31.

## Validation

- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline linkml-validate -s src/taxonmech/schema/taxonmech.yaml --target-class TaxonRecord data/taxa/bacteria/methylobacterium_sp_c31.yaml`: no issues.
- PASS: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline python scripts/validate_strict.py data/taxa/bacteria/methylobacterium_sp_c31.yaml --out /private/tmp/mc31-strict.tsv`: one file, zero ERROR rows. The actual TSV was read and contains only its header.
- PASS, bounded manual comparison: exact identity, complete lineage, code, attestation, scope and inline-event content agree with pinned inputs. This does not replace full-corpus reproduction.
- Not run: full-corpus `just verify-corpus`, `just validate-products`, `just provenance-check`, `just render-check`, `just docs-check`, `just qc` and the test suite. No full-corpus gate is claimed to pass.
- There is no curator-added ontology node to check. `conf/id_label_targets.yaml` excludes taxonomic fields and delegates their inventory agreement to corpus reproduction.
- Ignored-independent history filename search found no separate target artifact. Inline history passed record validation; no external history validator was run against an invented artifact.
- No citation or quotation is asserted in the YAML. Sequence-linked bibliographic metadata were checked for completeness context.

## Identity and Grounding

Pinned `data/raw/ncbitaxon_taxa.tsv:221925`, [live NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1035204&retmode=xml) and [taxonomy dataset metadata](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1035204) agree on the target ID, exact name and SPECIES rank. Both live responses were inspected completely. XML confirms bacterial division, parent 2615210, code 11 and no alternate names. Dataset metadata confirm the full ten-ID root-inclusive lineage; the pinned ancestor labels and ranks exactly match the YAML.

The no-rank parent `unclassified Methylobacterium` remains below genus taxid 407. This carried NCBI grouping is not a named-species assignment. The sequence qualifier `strain C31` does not authorize replacing the taxon's SPECIES rank. EXACT is an identifier-grounding judgement, not a claim of valid publication of a species binomial.

The complete [LPSN Methylobacterium genus page](https://lpsn.dsmz.de/genus/methylobacterium), record 516060, was inspected in this turn and checked for C31. It identifies M. organophilum as type species; it does not identify C31 as a named species or type deposit. No genus nomenclature is inherited by this isolate.

Pinned backbone checks found no target children. Exact scans of type-material, merged-ID and dropped tables found no target rows. The legacy NCBI taxonomy browser URL was inaccessible; two successful structured responses supplied the identity evidence.

## Evidence

- `data/raw/ncbitaxon_taxa.tsv:221925` supplies the name, rank, parent, code, absence of synonyms and NCBI-only provenance.
- Complete native `data/catalog/ncbi_names-0005.jsonl.gz:31393` contains the exact scientific name and taxid, with an empty unique-name field.
- `data/taxa/PATHS.tsv:14416` resolves the slug. `curation/seed_scope.tsv:322200` adds it on 2026-09-13 using its one-source attested rule.
- The 2026-09-13T17:54:04Z seed event agrees with the scope reason and source list. The attestation counts one NAME, not a genome, culture deposit or experimental observation.

The initial numeric search returned two unrelated genome-source candidates. Both complete records were read:

- `data/catalog/gtdb_genomes-0017.jsonl.gz:41513` identifies `GB_GCA_964508205.1`, an archaeal metagenome-derived genome with taxid 2250275; 1035204 is its total and ungapped sequence length.
- `data/catalog/ncbi_genbank-0063.jsonl.gz:25333` identifies that same accession as Candidatus Hydrothermarchaeota archaeon, also taxid 2250275; 1035204 occurs in genome-size fields.

These are numeric coincidences, not C31 taxonomic or strain matches. They supply no target genome or GTDB mapping evidence. Their complete native fields are enough to reject the proposed identity; no review of that other genome was initiated.

Exact Entrez searches used `txid1035204[Organism:noexp]`. Assembly returned zero with phrases-not-found / no-items diagnostics, while Nuccore returned one UID, 347300701. The complete nucleotide ID list equals the reported count. The assembly no-hit is limited to this exact query, not proof that no genome exists anywhere.

Full [GenBank metadata for FR869800.1](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&rettype=gb&retmode=xml&id=FR869800.1) identify a 1,335-nt partial 16S rRNA sequence, strain C31 and exact taxon 1035204. Source qualifiers name host leaf surface and Cerastium holosteoides. The submission date is 18 May 2011, creation date 18 September 2011 and update date 6 December 2011. The inspected metadata contain no culture-collection qualifier, BioSample, BioProject or assembly. Every feature, source qualifier and reference was read; sequence bases were omitted. This is a marker, not a genome.

The sequence cites Wellner, Lodders and Kampfer, PMID 22000032 and DOI 10.1016/j.syapm.2011.08.005. The complete [PubMed citation and abstract](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=pubmed&id=22000032&retmode=xml), fetched during this turn and reread for the sequence's explicit citation, confirm that pairing. This is a phyllosphere-community study across hosts, sites and land-use regimes. The abstract does not identify C31 or establish an isolate-specific phenotype, sampling location or growth requirement. Full text and supplements were not inspected, and no community-level result is promoted into a C31 assertion.

## Completeness

Exact scans of the seven transformed tables found no target BacDive, LPSN, GTDB mapping, GOLD, MediaDive, Madin or BactoTraits row. Ignored-inclusive taxid/name/slug, expanded designation and accession searches found no eligible target culture deposit, genome-source link or explicit StrainInfo sequence-to-own-deposit assertion.

Zero listed strains matches the BacDive-subtree contract in `docs/HARMONIZATION.md:146` and `src/taxonmech/seed.py:488`: the target has neither an exact BacDive entry nor descendants to contribute one. This does not deny existence of the original cultured isolate. The existing culture normalizer rejects C31 and C-31 as unqualified designations.

The optional FR869800.1 marker and citation are not currently required representations. No supported existing strain entry or eligible SI-DP association was established to receive such a sequence link. Future enrichment needs explicit identity and a maintained import path, not a guessed deposit or equivalence from C31 alone.

The structured iModulonDB adapter returned 28 datasets before web follow-up, with no Methylobacterium or Methylorubrum coverage. It is not applicable and not negative biological evidence. Empty optional definition, phenotype and graph fields are acceptable.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found within the reviewed record and inspected evidence scope. The generated YAML supports its exact identity and provenance without conflating marker evidence, unrelated genome-size coincidences or genus nomenclature.

This pass does not certify corpus reproducibility or unasserted biological properties.

## Recommended Edits

None required for the current record.

Future enrichment, if supported by explicit identity evidence, belongs in maintained source extraction and seeding logic. Keep FR869800.1 typed as a non-genome marker and preserve the source attribution. Never turn bare C31 or a numeric text hit into a culture accession, genome link or species equivalence. Do not hand-edit generated YAML.

Do not promote SEEDED to REVIEWED or append curation history from this read-only report.

## Follow-up Checks

- On source refresh, repeat exact taxonomy, complete lineage, status and target schema/strict checks.
- After an authorized source/import change, run real full-corpus `just verify-corpus`, `just provenance-check`, `just render-check` and `just qc`; bounded manual comparisons do not replace these gates.
- Require eligible own-deposit evidence and explicit sequence attribution before adding a StrainInfo sequence link; keep the 16S marker outside genome counts.
- Match taxids by their source field, not by genome length or arbitrary numeric occurrence.
- Inspect full text and supplements of PMID 22000032 before making C31-specific ecological or phenotype claims.

## Additional Notes

Searches used `rg --no-ignore --hidden -n -z -i` across `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. The initial identity search returned five rows, including two unrelated genome-size matches. Expanded Methylobacterium/Methylorubrum C31/C-31 context searches returned the three target identity/scope rows, with no new candidates. All five distinct rows were read completely via structured pinned comparisons and lossless native JSONL decoding. Separate FR869800 / 347300701 searches returned no rows. Five SOURCE.json files were searched structurally; history filenames were checked independently. Absence findings include ignored files and remain bounded to the named sources.

Adapter command: `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache uv run --offline --no-sync --project /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw kg-microbe-sources imodulondb datasets`. Successful NCBI taxonomy and sequence APIs, full marker metadata, PubMed citation/abstract and LPSN genus text supplied the evidence. The already inspected same-paper response was reread against C31's reference. Failed browser output and search snippets were not used as evidence.

No YAML/code/generated-page changes, history events, review-status promotions, paid research, outbound contact or Git/GitHub mutations occurred. Eukaryota reviews were not reopened.

