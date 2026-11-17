# YAML Record Review: Bifidobacterium breve CECT 7263

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/bifidobacterium_breve_cect_7263.yaml`
- Started UTC: 2026-10-09T13:38:54Z
- Finished UTC: 2026-10-09T13:47:40Z
- Verdict: needs curation

## Target

This review concerns one generated `TaxonRecord`, `NCBITaxon:1036735`, labelled Bifidobacterium breve CECT 7263, rank `STRAIN`, domain `BACTERIA`, parent `NCBITaxon:1685`. All 89 YAML lines were read. It is not a review of the entire B. breve species or its type strain.

The record is `EXACT` / `SEEDED`, has genetic code 11, ten root-first ancestors, one GTDB mapping, three synonyms, one GTDB xref, four source attestations, zero emitted BacDive strains, and one seed event. Generated YAML is not the maintained correction surface.

The target SHA-256 before and after investigation was `87af6afb71eec61c955ada2268f1e28fb8ab901ad36c3448d6d18dcf38ebbdbf`. No record, source inventory, scope, history, or generated page was changed.

## Validation

Commands were run with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1`:

```bash
just validate data/taxa/bacteria/bifidobacterium_breve_cect_7263.yaml
just validate-strict data/taxa/bacteria/bifidobacterium_breve_cect_7263.yaml --out /private/tmp/taxonmech-bbreve7263-review-strict.tsv
```

Both exited zero. LinkML reported no issues. Strict validation scanned one file and reported zero error rows; its complete TSV was header-only. These gates accept the syntax of the mapping but do not prove its biological scope.

The full backbone ancestor chain, source counts, native names, PATHS entry, scope row and seed-event reason were compared independently. Exact-ID scans of the complete type-material, merged-ID and dropped inventories found no target rows. This is not a corpus-reproduction result.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, provenance, rendering, documentation-statistics and history gates. `verify_corpus.py` exposes no single-record selector; no synthetic focused equivalent was substituted. There are no curator-added graph nodes or external history records for this target requiring a focused term/history check. No refresh, generator or history writer was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:222615` and complete native name rows `data/catalog/ncbi_names-0005.jsonl.gz:32171`, `:32172` and `:32173` support the scientific name and the two NCBI equivalent names containing `str. CECT 7263` and `strain CECT 7263`.

The live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1036735&retmode=xml) independently confirms the strain rank, parent 1685, genetic code 11 and equivalent-name classes. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/1036735) confirms all ten ancestor identifiers, including root. The lineage runs through Bacteria, Bacillati, Actinomycetota, Actinomycetes, Bifidobacteriales, Bifidobacteriaceae, Bifidobacterium and B. breve. GTDB's different order placement is not a reason to replace the carried NCBI lineage.

Live NCBI also retains Bifidobacterium breve 26M2 as a `misspelling`. That source-qualified name helps explain the older GOLD chain below; it must not be promoted to another exact synonym. Its absence from the pinned native name rows is a bounded snapshot difference, not evidence that the two existing NCBI synonyms are wrong.

The GTDB species mapping does not have the same scope as this strain. That issue is distinct from the correctly resolved NCBI identity and is the single major finding below.

## Evidence

The target's source projections were read in full: `data/raw/gtdb_mappings.tsv:1463`, `data/raw/gold_organisms.tsv:504` and `data/raw/madin_taxa.tsv:696`. They reproduce the emitted counts and predicates, but reproduction alone does not validate an identity interpretation.

GTDB cluster evidence:

- `data/raw/gtdb_species.tsv:17200` gives 402 genomes for `GTDB:s__Bifidobacterium_breve`. An ignored-inclusive decompressed search followed by exact JSON taxonomy-segment comparison across `data/catalog/gtdb_genomes-*.jsonl.gz` found 402 members and 402 unique assembly accessions. Only one has `ncbi_taxid` 1036735; 353 use species taxon 1685. Two entries explicitly carry CECT 7263/CECT7263 strain designations.
- Those two complete native records are `data/catalog/gtdb_genomes-0009.jsonl.gz:44524` (`RS_GCF_000247755.1`) and `data/catalog/gtdb_genomes-0012.jsonl.gz:15985` (`RS_GCF_002027265.1`). They support classification of the sequenced strain in that species, not equivalence between a strain and the whole species.
- The complete representative record `data/catalog/gtdb_genomes-0004.jsonl.gz:38538` identifies `RS_GCF_001025175.1`, DSM 20213 = JCM 1192, taxon 518634, not CECT 7263. Complete contrasts `data/catalog/gtdb_genomes-0011.jsonl.gz:1870` and `:2376` concern strain Bg155.S08_4F7 and a distinct metagenome-derived isolate. These independently demonstrate broader cluster membership.
- The live GTDB tree page could not be retrieved by the web reader. The cluster finding rests on inspected pinned native metadata, not on a claimed successful live GTDB query.

The 402 count is correct for the source species. `TaxonomyMapping.genome_count` explicitly means assemblies classified under the source taxon (`src/taxonmech/schema/taxonmech.yaml:435`). It must not be interpreted as 402 CECT 7263 genomes or replaced with one or two merely to hide the mapping-scope problem. The GTDB attestation likewise identifies the source species; its `closeMatch` is the unsupported part.

Assembly evidence was read as complete native records and independently checked against live [NCBI assembly GCA_000247755.2](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_000247755.2/dataset_report) and [NCBI assembly GCA_002027265.1](https://api.ncbi.nlm.nih.gov/datasets/v2/genome/accession/GCA_002027265.1/dataset_report):

| Sequence chain | Explicit strain and classification | Distinct source identity |
| --- | --- | --- |
| GCA_000247755.2 / GCF_000247755.1 | CECT 7263; taxon 1036735 | SAMN02471362; PRJNA67403; AFVV00000000.1; 2,314,396 bp; 34 contigs |
| GCA_002027265.1 / GCF_002027265.1 | CECT7263; taxon 1685 | SAMN06473336; PRJNA377846; MWVR00000000.1; 2,330,408 bp; 25 contigs |

Native GenBank addresses are `data/catalog/ncbi_genbank-0000.jsonl.gz:4883` and `data/catalog/ncbi_genbank-0001.jsonl.gz:29652`; corresponding RefSeq rows are `data/catalog/ncbi_refseq-0000.jsonl.gz:4158` and `data/catalog/ncbi_refseq-0001.jsonl.gz:14864`. The paired comparisons are identical within each pair, not across both sequencing efforts. `data/catalog/ncbi_genbank_historical-0000.jsonl.gz:2069` marks GCA_000247755.1 as suppressed; it is not an additional current assembly. BV-BRC native rows `data/bvbrc/bvbrc-0000.jsonl.gz:3396` and `data/bvbrc/bvbrc-0005.jsonl.gz:14748` explicitly link genome IDs 1036735.3 and 1685.59 to the respective assembly/sample/project chains.

Two independently inspected primary announcements support those distinctions. The [2012 genome announcement, DOI 10.1128/JB.00691-12](https://journals.asm.org/doi/10.1128/jb.00691-12), linked by native PMID 22740680, describes the AFVV draft with 34 contigs, despite its title using "Complete Genome Sequence". It identifies a human-milk isolate; some functional discussion invokes unpublished measurements or predicted machinery. The [2017 resequencing announcement, DOI 10.1128/genomea.00299-17](https://journals.asm.org/doi/10.1128/genomea.00299-17), explicitly contrasts the earlier assembly with its new 25-contig MWVR sequence and gives PRJNA377846. Neither paper turns the species cluster into a strain identity, and no clinical-benefit, resistance-mechanism or phenotype assertions were added to this record.

The complete GOLD source chains were inspected, including newly found analysis/project rows:

- Older chain: `data/gold/organisms.jsonl.gz:9898`, Go0011271, is named B. breve 26M2 and explicitly classified as taxon 1036735. `data/gold/projects.jsonl.gz:9762`, Gp0011271, links that organism to PRJNA67403 and SAMN02471362. `data/gold/analyses.jsonl.gz:9294`, Ga0015740, links the project to IMG 2534682293 and AFVV00000000/GCA_000247755. The analysis has no direct organism ID; the explicit project link supplies the inspected chain. The supplied assembly accession is unversioned and was not rewritten.
- Resequencing chain: `data/gold/organisms.jsonl.gz:346081`, Go0496658, explicitly gives CECT7263 and taxon 1685. `data/gold/projects.jsonl.gz:268300`, Gp0380721, links that organism to PRJNA377846 and SAMN06473336. `data/gold/analyses.jsonl.gz:213222`, Ga0353376, links that project to IMG 3005006590 and MWVR00000000/GCA_002027265.1. Again, the project chain, not name co-occurrence, resolves the organism.
- The one-organism GOLD attestation is supported by the exact target taxon classification of Go0011271. The species-classified second organism is not another exact-ID count row. GOLD Go/Gp/Ga identifiers and BioSample/BioProject identifiers are not themselves genomes.
- Shared PRJNA377846 also retrieves Gp0380722 / Go0496659, Limosilactobacillus reuteri CECT 8605, SAMN06473517 and GCA_002027295.1. Complete source rows were read. That distinct organism cannot be attached to CECT 7263 simply because the project is shared.

NCBI's one-`NAME` attestation is a source identity attestation, not a count of all name strings. Madin's five-`TRAIT_ASSERTION` count matches the committed inventory exactly. Its five underlying transformed edges were not reverified: the configured kg-microbe `data/transformed/madin_etal/edges.tsv` was unavailable, and a gitignore-independent `find` under that configured checkout found no such path. The manifest retains its pinned SHA-256 `3fbe08ab2502458a515f2efc036d4d7004e2ae992521fe25426554126dcdf77f`. No five specific traits, experiments or mechanisms were inferred from this count.

## Completeness

Gitignore-independent searches included hidden/ignored files and compressed native content under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Identifier 1036735, the label, slug, CECT token variants and the NCBI equivalent names yielded 22 candidate rows, all read in full. Separate full structured reads covered the five `SOURCE.json` files, and an ignored-independent filename inventory covered target records, reports and history.

Expansion to both assembly families, BioSamples, specific BioProjects, WGS prefixes, 26M2 and the initially found GOLD/IMG IDs yielded 50 rows, including 37 new candidates; all 59 distinct initial/expanded candidate rows were read in full. The expanded search was deliberately broad: WGS-prefix substrings also matched unrelated AFVV/MWVR-containing accessions from Salmonella, Escherichia, Staphylococcus, Xanthobacter, Helicobacter, Vibrio and metagenomic Clostridia records. Their complete identities were checked rather than accepted as strain matches. The separate exact GTDB cluster scan and representative/contrast reads are described above.

Within those bounded searches and full exact-taxonomy inventory scans, no own BacDive strain/deposit row, LPSN name row, MediaDive/BactoTraits attestation, type-material row, immediate NCBI child or external history record was found. This is not a claim of absence from every external database. A live collection-catalog deposit was not independently resolved. `strain_count: 0` correctly reflects emitted BacDive entries under the current admission model, not the nonexistence of CECT 7263 or its genomes.

The assembly and source chains above are actionable enrichment evidence, but not permission to invent a BacDive strain identifier, merge assemblies, transfer a species-wide culture list, or bypass the documented CAFI/full-deposit ownership rules. Missing optional genome listings on a record without an admitted strain entry are not counted here as a second defect. Future enrichment would need an explicit maintained strain-admission decision and source-preserving links.

There are no cited DOIs/PMIDs, genes, protein identifiers, expression modules or causal edges in the YAML itself. Literature was investigated for identity/assembly context, not imposed as required phenotype content. iModulonDB was not applicable to this identity/count record; no absence claim about its database is made.

## Findings

Counts: 0 blocker, 1 major, 0 minor.

1. **Major: a species-wide GTDB concept is promoted to strain equivalence.** YAML line 43 maps `GTDB:s__Bifidobacterium_breve` by `skos:closeMatch`; lines 46-49 call Bifidobacterium breve an `EXACT_SYNONYM` of CECT 7263; line 57 adds the species as an identity-derived xref; line 70 repeats the predicate in the attestation. The complete cluster, representative and two explicit CECT assembly records establish species membership, not equal scope. The NCBI strain and parent species are explicitly different taxa. This is one connected mapping/identity-promotion defect, not four independently counted errors.

   Maintained owners: the upstream kg-microbe GTDB mapping semantics propagated by `src/taxonmech/extract.py:501`, and local identity promotion in `src/taxonmech/seed.py:451` through the synonym/xref block and the attestation block at line 578. The extractor copies each whole species count into mapping rows at line 755. The seeder treats every `closeMatch` as identity without a rank/scope guard. `scripts/seed_from_sources.py` is only the compatibility entry point. Correct the maintained logic and source relation, not this generated YAML.

No blocker was found: the target's NCBI identity, parent, lineage, seed provenance and schema shape remain sound. No separate minor finding was established. Failure to retrieve a live GTDB page and the unavailable Madin edge file remain verification limitations, not invented biological failures.

## Recommended Edits

1. Add rank/scope-aware identity admission in `src/taxonmech/seed.py` so this strain does not acquire a species-wide exact synonym or identity xref solely from an upstream `closeMatch`. Preserve its legitimate NCBI equivalent names, parent, lineage and `EXACT` NCBI grounding.
2. Correct the maintained upstream relation and its handling in `src/taxonmech/extract.py` / `src/taxonmech/seed.py`. Retain provenance and supported species classification without asserting equality. Predicate direction is from the GTDB source taxon to the record: blindly substituting `broadMatch` would also be wrong here, because the strain is narrower, not broader, than the species. Choose a supported non-equivalence representation and document its scope before regenerating the inventories and record.
3. Preserve 402 only as the source species' genome count, with clear notes if the relation is retained. Do not relabel it as a CECT-specific total, sum incompatible source units, or replace it with the count of matching assembly rows. Any future per-strain assembly count needs its own explicit semantics and version-aware source links.
4. Extend `tests/test_seed.py` with a strain-level `closeMatch` fixture that cannot yield a species exact synonym or identity xref. Cover the corresponding attestation, explicit source-wide count semantics, species-level valid identity cases and existing pooled-mapping behavior. If enrichment is separately authorized, preserve both assembly chains and the distinct GOLD project/organism paths; never join the CECT 8605 project sibling to CECT 7263.

These are future curation recommendations only. No upstream mutation, test edit, regenerated record, status promotion or history entry was made by this review.

## Follow-up Checks

After an authorized correction, run the focused seeder regressions, dry-run the seeder and inspect a CECT 7263 canary before any bulk regeneration. Verify that the two NCBI exact names survive, the species-only synonym/xref disappear, mapping and attestation predicates agree with their declared direction, and 402 is not represented as the number of this strain's genomes.

Re-run both focused validators above against the generated canary, then `just verify-corpus` and the documented repository quality gates after the complete source/generator change. Recheck the current authoritative GTDB view when accessible and recover/hash the pinned Madin input if individual trait evidence is later required. An enrichment change additionally needs independent eligible-deposit ownership and tests keeping the two samples/assemblies and the shared-project L. reuteri sibling separate.

## Additional Notes

`data/taxa/PATHS.tsv:15138` resolves this identifier to the reviewed slug; `curation/legacy_page_paths.tsv:899` is a page-path mapping, not another taxon. `curation/seed_scope.tsv:26091` has added date 2026-09-12 and the four-source admission reason. The YAML seed event at 2026-09-13T17:54:04Z carries that reason and the four named sources; it does not claim a completed scientific review.

This report was authored for this single record after its own full source investigation. No neighboring verdict was inherited. Eukaryota and all other taxon YAMLs were left untouched. Existing reports were not overwritten, and no branch/worktree, GitHub object, external message or paid research action was created.
