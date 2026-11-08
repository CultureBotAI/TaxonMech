# Extend exact native evidence and projection coverage for EdgeMech

The initial native adapter for CLAW #767 exports the complete pinned
`data/raw/gtdb_mappings.tsv` surface, with explicit manifest exclusions.

The complete extracted GTDB-to-NCBI mapping inventory has no exact assertion-level native approval proof in this surface. All exported rows remain unassessed. Strain/deposit identity, genome assembly links and nomenclature need distinct native adapters and evidence, rather than inheritance from a generated record status.

Follow-up work must establish source-row identities, evidence ancestry,
reviewed payload scope and safe projection rules before admitting additional
assertions to eligible reuse. Keep counts/units, taxonomy/strain versions,
conditions and polarity where present. Never promote a record-level status
or native cohort review into approval of every exported assertion.

The current PR preserves these limitations and native statuses rather than
fabricating scientific RecordReview objects. This issue remains open for the
additional native evidence and projection work.
