"""Custom vector db."""

import hashlib
import json
from typing import Any

from langchain_chroma import Chroma
from langchain_core.documents import Document


def get_document_id(document: Document) -> str:
    """Get document id, as an hash of the document content and metadata."""
    # get the page content and metadata from the document
    pc = document.page_content
    md = document.metadata
    # create a hash object
    hash_object = hashlib.sha256()
    # set the chunk size for hashing the document content
    chunk_size = 4096
    # update the hash object with the document content in chunks
    for i in range(0, len(pc), chunk_size):
        chunk = pc[i : i + chunk_size]
        hash_object.update(chunk.encode("utf-8"))
    # update the hash object with the serialized metadata
    hash_object.update(json.dumps(md, sort_keys=True).encode("utf-8"))
    # get the hexadecimal representation of the hash
    document_id = hash_object.hexdigest()
    return document_id


class VectorDB(Chroma):
    """Custom vector db."""

    def __init__(self, *args, **kwargs) -> None:
        """Initialize."""
        super().__init__(*args, **kwargs)

    def add_documents(
        self,
        documents: list[Document],
        id_in_metadata: str = "",
        **kwargs: Any,
    ) -> list[str]:
        """Add documents, computing unique ids, unless provided in the metadata."""
        if id_in_metadata == "":
            ids = [get_document_id(doc) for doc in documents]
        else:
            ids = [doc.metadata[id_in_metadata] for doc in documents]
        # MAYBE use self.get to check if the document already exists
        return super().add_documents(documents=documents, ids=ids, **kwargs)
