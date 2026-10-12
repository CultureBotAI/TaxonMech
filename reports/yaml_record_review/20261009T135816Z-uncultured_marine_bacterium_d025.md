# YAML Record Review: uncultured marine bacterium D025

- Repository: CultureBotAI/TaxonMech
- Record: `data/taxa/bacteria/uncultured_marine_bacterium_d025.yaml`
- Started UTC: 2026-10-09T13:55:36Z
- Finished UTC: 2026-10-09T13:58:16Z
- Verdict: pass

## Target

The complete 39-line generated `TaxonRecord` for `NCBITaxon:103674`, uncultured marine bacterium D025, was reviewed. NCBI assigns rank `SPECIES` within `BACTERIA`, under `NCBITaxon:150608`, marine bacteria D ensemble. The record contains five root-first ancestors, genetic code 11, `EXACT` grounding, `SEEDED` mapping status, zero BacDive strain entries, one NCBI name attestation and one seed event. It does not assert a cultured isolate, formally named species, genome assembly or phenotype.

Its SHA-256 remained `1a2b3099b88d9c77309a1e3a60b685d8dffa25bc8027623fb5eec12ef0111553`. Only this new review report was written for the target; the YAML was not changed.

## Validation

The following commands ran with `UV_CACHE_DIR=/private/tmp/taxonmech-review-uv-cache` and `UV_OFFLINE=1` and exited zero:

```bash
just validate data/taxa/bacteria/uncultured_marine_bacterium_d025.yaml
just validate-strict data/taxa/bacteria/uncultured_marine_bacterium_d025.yaml --out /private/tmp/taxonmech-d025-review-strict.tsv
```

LinkML reported no issues. Strict validation scanned one file with zero errors; its entire TSV contained only the header. Full backbone-chain, source-row, PATHS, scope and seed-reason comparisons passed. The deposited sequence's declared length, actual length, nucleotide alphabet and annotated rRNA transcription were also checked, separately from schema validation.

Not checked: full-corpus `just verify-corpus`, `just qc`, `just test`, provenance, generated-page, documentation-statistics and history gates. The corpus verifier has no per-record selector, and bounded comparisons were not represented as a reproduction run. No target causal nodes or external history records require a focused term/history check. No generator, curation writer or status promotion was run.

## Identity and Grounding

`data/raw/ncbitaxon_taxa.tsv:18539` and complete native name record `data/catalog/ncbi_names-0000.jsonl.gz:38555` agree on the exact target identity. The native name is a scientific-name entry, not an exact-synonym candidate for another D025-labelled organism.

The live [NCBI Taxonomy XML](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=103674&retmode=xml) confirms species rank, parent 150608, genetic code 11, and no other-name block. The [NCBI Datasets taxonomy response](https://api.ncbi.nlm.nih.gov/datasets/v2/taxonomy/taxon/103674) confirms the five-ancestor chain including root: 1, 131567, 2, 48479 and 150608. The labels/ranks are root/no rank, cellular organisms/cellular root, Bacteria/domain, environmental samples/no rank and marine bacteria D ensemble/no rank. All are reproduced correctly in the YAML.

The environmental-sample division is consistent with the bacterial domain. `SPECIES` is NCBI's rank for this sequence-associated taxon; it does not imply a validly published binomial or an independently delimited cultured species. Exact target scans of the complete type-material, merged-ID and dropped inventories found no target rows. NCBI grounding is sound within those semantics.

## Evidence

An exact, non-descendant-expanded NCBI nuccore query for taxon 103674 returned one UID, 5882276. The complete [GenBank AF177561.1 record](https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=nuccore&id=5882276&rettype=gb&retmode=xml) explicitly names D025, gives `taxon:103674`, identifies clone D025 as an environmental sample and describes a surface-associated uncultured marine bacterium. It is a partial 16S rRNA gene, not an assembly.

The sequence has exactly 559 bases, all A/C/G/T; its submitted 559-base transcription matches the DNA sequence after case normalization. The feature table contains source and rRNA entries, with the rRNA partial at both ends. This establishes annotation consistency, not independent phylogenetic placement, full-length 16S coverage or genome equivalence.

The sequence directly cites Dang and Lovell's [primary study, DOI 10.1128/AEM.66.2.467-475.2000](https://journals.asm.org/doi/10.1128/aem.66.2.467-475.2000), PMID 10653705 / PMC91850; PubMed identifiers and abstract were independently fetched. The publisher's methods, accession statement, Table 1 and relevant results/discussion were inspected. This was a cultivation-independent study of surfaces incubated in a salt-marsh creek. D025's Table 1 frequencies are PVA-72 1.8%, BR-24 1.2%, PEG-S-72 1.2%, PEG-M-72 5.4% and PU-24 4.0%. These percentages describe clone-library ARDRA frequencies, not direct organism abundance. The paper's phylogenetic and methodological discussion does not authorize replacing the carried NCBI lineage, declaring a cultured strain, assigning polymer degradation, or transferring an assay of the cloning host to D025. The deposited accession falls within the paper's stated sequence series.

The one `NAME` attestation matches the target's backbone entry and the 2026-09-13 NCBI snapshot. There are no additional source attestations or source-count units to sum. No phenotype, assembly, causal edge or literature citation is asserted by the YAML itself.

Complete candidate records establish why superficially matching source hits are unrelated:

| Candidate | Inspected source identity | Exclusion from D025 |
| --- | --- | --- |
| BacDive 103674 | `data/bacdive/records.jsonl.gz:27795`: Rhodococcus sp. ST007459, taxon 194249 | The same number is a BacDive identifier, not NCBI taxon 103674. |
| CIP 103674 | BacDive 12683 (`data/bacdive/records.jsonl.gz:12525`), Pseudoalteromonas carrageenovora, taxa 1314868/227; StrainInfo 264316, deposit 154038 (`data/straininfo/records.jsonl.gz:206260`) | A qualified collection accession for another organism. Its LPSN/type-material, strain-link, culture-list and related-record rows retain that identity. |
| NBRC 103674 | `data/bacdive/records.jsonl.gz:17902`: Thermosulfidibacter takaii ABI70S6, taxon 412593, with sequence/assembly evidence under 1298851 | Neither the culture accession nor its genome describes this environmental clone. |
| StrainInfo deposit 103674 | `data/straininfo/records.jsonl.gz:26767`: ATCC 25132, Mycobacterium intracellulare, taxon 1767; strain 38371 | Independent deposit namespace, not a taxon match. |
| Rickettsia sp. D025 | `data/raw/ncbitaxon_taxa.tsv:56516`, own scope row and `data/catalog/ncbi_names-0001.jsonl.gz:36904`: taxon 274849 | A shared short designation is not shared identity. |
| Escherichia coli D025 | BV-BRC 562.108443 (`data/bvbrc/bvbrc-0022.jsonl.gz:3226`), GCA_024496645.1, SAMN29884162, taxon 562; matching complete GTDB and GenBank rows | Distinct strain, sample and assembly, not a genome for marine D025. |
| Staphylococcus pseudintermedius H8-D025 | GCA/GCF_056839125.1, SAMN48001391, taxon 283734; complete native GenBank/RefSeq rows | A substring in another strain designation. |
| Numeric GTDB/GenBank matches | GCF_001377095.1, GCF_002484185.1 and GCF_046552455.1 have a scaffold statistic 103674; GCA_047370395.1 has genome size 5882276 | Assembly metrics are not identifiers; the last value merely equals D025's nuccore UID. |

For CIP 103674, the complete StrainInfo record also identifies which other deposits own each sequence. A record's shared grouping would not transfer those sequences even among deposits, much less to this taxon. No foreign genome, synonym, collection or type-strain assertion was imported.

## Completeness

Searches included hidden and ignored files through `rg --no-ignore --hidden`, with decompression for native catalogs, under `data/raw`, `data/catalog`, `data/bacdive`, `data/bvbrc`, `data/gold`, `data/seqcode`, `data/straininfo`, `data/atb`, `curation` and `history`. Initial searches covered 103674, the full label, slug and D025 token, yielding 31 rows, all read in full. Expansion to AF177561/AF177561.1 and UID 5882276 yielded one additional row, the Klebsiella pneumoniae genome-size collision described above; that complete native record was read too.

Separate complete structured reads covered the five source metadata JSON files. The sole metadata match was the BacDive request ID 103674 in its own namespace. Ignored-independent filename searches covered records, prior reports and history. Full exact-taxonomy scans covered the seven source-count/mapping inventories and the entire backbone parent column.

Within those scopes, no target-supported BacDive deposit/strain, GTDB mapping/genome, LPSN name, GOLD organism/analysis, BV-BRC assembly, ATB/StrainInfo link, MediaDive/Madin/BactoTraits attestation, immediate child or separate history record was found. These are bounded local findings, not proof of absence from every external source. The search results above were rejected only after reading their identity and source context.

Zero emitted strains and absent optional mappings, synonyms, nomenclature, xrefs and genome lists are appropriate. The known partial rRNA accession would need a typed marker-sequence representation in any future enrichment; it cannot populate an assembly/genome field. iModulonDB was not applicable because the YAML has no gene, regulator, expression-module or transcriptomic assertion.

## Findings

Counts: 0 blocker, 0 major, 0 minor.

None found. The NCBI identity, carried lineage, rank, code, sole attestation and seeded provenance agree with the inspected record-specific evidence. No mandatory strain/genome representation was established by the unrelated source hits.

## Recommended Edits

None required. Do not hand-edit the generated YAML, substitute a cultured taxon based on D025 or 103674 string matches, promote status, or treat AF177561.1 as a genome assembly.

If separate marker-sequence enrichment is authorized later, implement it through the maintained schema/source/seeder surfaces with evidence-aware typing and focused tests, preserving the NCBI clone identity. The current maintained owners are `src/taxonmech/ncbi_taxdump.py`, `src/taxonmech/extract.py` and `src/taxonmech/seed.py`; the generated taxon file is not the correction surface.

## Follow-up Checks

No corrective check is pending for a finding. A future source refresh should recheck exact NCBI identity and accession version, require explicit ownership for every deposit/genome link, and retain marker sequence versus assembly distinctions. Re-run the focused validators and then corpus reproduction and repository quality gates for any authorized maintained-input change.

## Additional Notes

`data/taxa/PATHS.tsv:15140` resolves this identifier to the reviewed slug. `curation/seed_scope.tsv:144183` records the 2026-09-13 one-source admission reason. The event at 2026-09-13T17:54:04Z matches that reason and source and is a seed event, not evidence of prior human review.

All 32 initial/expanded content candidates were inspected independently for this record. No neighboring clone verdict was reused. Existing reports, all taxon YAMLs including Eukaryota, history, generated products, branches and worktrees were left unchanged; no GitHub or paid-provider action was taken.
