from typing import Dict, List, Optional
import pandas as pd


def search_documents(documents: List[Dict], keyword: str, max_results: int) -> Dict:
    if not keyword:
        return {"results": documents[:max_results], "total": len(documents)}

    results = list(
        filter(
            lambda doc: keyword.lower()
            in (
                doc["title"].lower() or doc["journal"].lower() or doc["authors"].lower()
            ),
            documents,
        )
    )
    total = len(results)
    return {"results": results[:max_results], "total": total}


def add_bookmark(documents: List[Dict], doc_id: int) -> Optional[Dict]:
    if len(documents) - 1 >= doc_id:
        documents[doc_id]["bookmarked"] = True

        return documents[doc_id]


def remove_bookmark(documents: List[Dict], doc_id: int) -> Optional[Dict]:
    if len(documents) - 1 >= doc_id:
        documents[doc_id]["bookmarked"] = False

        return documents[doc_id]


def list_bookmarks(documents: List[Dict]):
    bookmarked: List = []
    for doc in documents:
        if doc["bookmarked"]:
            bookmarked.append(doc)

    return {"results": bookmarked, "total": len(bookmarked)}


def store_data():
    url = "https://ai2-semanticscholar-cord-19.s3-us-west-2.amazonaws.com/2020-04-03/metadata.csv"
    documents: List[Dict] = []
    dtype = {
        "cord_uid": "string",
        "sha": "string",
        "source_x": "string",
        "title": "string",
        "doi": "string",
        "pmcid": "string",
        "pubmed_id": "string",
        "license": "string",
        "abstract": "string",
        "publish_time": "string",
        "authors": "string",
        "journal": "string",
        "Microsoft Academic Paper": "string",
        "WHO #Covidence": "string",
        "has_pdf_parse": "string",
        "has_pmc_xml_parse": "string",
        "full_text_file": "string",
        "url": "string",
    }
    data = pd.read_csv(url, dtype=dtype)
    for i, row in enumerate(data.to_dict("records")):
        doc = {
            "id": i,
            "title": str(row["title"]),
            "journal": str(row["journal"]),
            "date": str(row["publish_time"]),
            "authors": str(row["authors"]),
            "url": str(row["url"]),
            "bookmarked": False,
        }
        documents.append(doc)

    return documents
