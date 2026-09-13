"""Read published taxon evidence independently of the renderer's implementation."""

import gzip
import json


def rendered_taxon(output, identifier):
    bucket = int(identifier.split(":")[1]) // 1000
    record = json.loads(gzip.decompress((output / f"taxon-details/{bucket:04}.json.gz").read_bytes()))[
        identifier
    ]
    return record["html"] + "".join(page["html"] for page in record["strain_pages"])
