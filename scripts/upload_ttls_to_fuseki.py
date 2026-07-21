#!/usr/bin/env python3
"""Upload generated Turtle files to an Apache Jena Fuseki dataset.

Defaults target the APL-O dataset shown in the Fuseki UI:
  http://arsenal.cs.wright.edu:3030/#/dataset/aplo/info

The Graph Store Protocol endpoint for that dataset is:
  http://arsenal.cs.wright.edu:3030/aplo/data

Examples:
  python3 scripts/upload_ttls_to_fuseki.py
  python3 scripts/upload_ttls_to_fuseki.py foundry/output/synthetic_sample_20260720-115511
  python3 scripts/upload_ttls_to_fuseki.py --clear-first
  python3 scripts/upload_ttls_to_fuseki.py --graph-uri https://w3id.org/aplo/graph/synthetic-sample
  python3 scripts/upload_ttls_to_fuseki.py --user admin --password 'your-password'
"""

from __future__ import annotations

import argparse
import base64
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path


DEFAULT_BASE_URL = "http://arsenal.cs.wright.edu:3030"
DEFAULT_DATASET = "aplo"


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def default_ttl_root(root: Path) -> Path | None:
    materialization_root = root / "materialization"
    if list(materialization_root.rglob("*.ttl")):
        return materialization_root

    output_root = root / "foundry" / "output"
    if not output_root.exists():
        return None

    candidates = sorted(
        path for path in output_root.iterdir()
        if path.is_dir() and path.name.startswith("synthetic_sample_")
    )
    return candidates[-1] if candidates else None


def request_headers(user: str | None, password: str | None) -> dict[str, str]:
    headers = {
        "User-Agent": "aplo-ttl-uploader/1.0",
    }
    if user is not None or password is not None:
        raw = f"{user or ''}:{password or ''}".encode("utf-8")
        headers["Authorization"] = "Basic " + base64.b64encode(raw).decode("ascii")
    return headers


def post_form(url: str, form: dict[str, str], headers: dict[str, str], timeout: float) -> None:
    body = urllib.parse.urlencode(form).encode("utf-8")
    req = urllib.request.Request(
        url,
        data=body,
        headers={
            **headers,
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        response.read()


def post_turtle(url: str, ttl_file: Path, headers: dict[str, str], timeout: float) -> None:
    req = urllib.request.Request(
        url,
        data=ttl_file.read_bytes(),
        headers={
            **headers,
            "Content-Type": "text/turtle; charset=utf-8",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=timeout) as response:
        response.read()


def upload_url(data_endpoint: str, graph_uri: str | None) -> str:
    if graph_uri:
        return data_endpoint + "?" + urllib.parse.urlencode({"graph": graph_uri})
    return data_endpoint + "?default"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Upload Turtle files to the APL-O Fuseki dataset."
    )
    parser.add_argument(
        "ttl_root",
        nargs="?",
        help="Directory containing generated .ttl files. Defaults to materialization/, then latest foundry/output/synthetic_sample_*.",
    )
    parser.add_argument(
        "--base-url",
        default=DEFAULT_BASE_URL,
        help=f"Fuseki base URL. Default: {DEFAULT_BASE_URL}",
    )
    parser.add_argument(
        "--dataset",
        default=DEFAULT_DATASET,
        help=f"Fuseki dataset name. Default: {DEFAULT_DATASET}",
    )
    parser.add_argument(
        "--graph-uri",
        default=None,
        help="Named graph URI. If omitted, uploads to the default graph.",
    )
    parser.add_argument(
        "--clear-first",
        action="store_true",
        help="Clear the target graph before uploading.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be uploaded without changing Fuseki.",
    )
    parser.add_argument("--user", default=None, help="Fuseki username, if auth is enabled.")
    parser.add_argument("--password", default=None, help="Fuseki password, if auth is enabled.")
    parser.add_argument(
        "--timeout",
        type=float,
        default=60.0,
        help="HTTP timeout per request, in seconds. Default: 60.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()

    if args.ttl_root:
        ttl_root = Path(args.ttl_root)
        if not ttl_root.is_absolute():
            ttl_root = root / ttl_root
    else:
        ttl_root = default_ttl_root(root)

    if ttl_root is None or not ttl_root.is_dir():
        print(
            "No TTL root directory found. Pass one explicitly or generate TTLs first.",
            file=sys.stderr,
        )
        return 1

    ttl_files = sorted(ttl_root.rglob("*.ttl"))
    if not ttl_files:
        print(f"No .ttl files found under: {ttl_root}", file=sys.stderr)
        return 1

    base_url = args.base_url.rstrip("/")
    dataset_url = f"{base_url}/{args.dataset}"
    data_endpoint = f"{dataset_url}/data"
    update_endpoint = f"{dataset_url}/update"
    target_label = f"named graph {args.graph_uri}" if args.graph_uri else "default graph"
    target_upload_url = upload_url(data_endpoint, args.graph_uri)
    headers = request_headers(args.user, args.password)

    print(f"Fuseki dataset: {dataset_url}")
    print(f"Upload endpoint: {data_endpoint}")
    print(f"Target: {target_label}")
    print(f"TTL root: {ttl_root}")
    print(f"TTL files: {len(ttl_files)}")

    if args.dry_run:
        print("Dry run only. No Fuseki changes will be made.")
        return 0

    try:
        if args.clear_first:
            clear_update = (
                f"CLEAR GRAPH <{args.graph_uri}>"
                if args.graph_uri
                else "CLEAR DEFAULT"
            )
            print(f"Clearing {target_label} before upload...")
            post_form(
                update_endpoint,
                {"update": clear_update},
                headers,
                args.timeout,
            )

        for index, ttl_file in enumerate(ttl_files, start=1):
            try:
                rel_path = ttl_file.relative_to(root)
            except ValueError:
                rel_path = ttl_file
            print(f"Uploading [{index}/{len(ttl_files)}] {rel_path}")
            post_turtle(target_upload_url, ttl_file, headers, args.timeout)

    except urllib.error.HTTPError as exc:
        body = exc.read().decode("utf-8", errors="replace")
        print(f"Fuseki returned HTTP {exc.code}: {exc.reason}", file=sys.stderr)
        if body:
            print(body, file=sys.stderr)
        return 1
    except urllib.error.URLError as exc:
        print(f"Could not reach Fuseki: {exc.reason}", file=sys.stderr)
        return 1

    print(f"Uploaded {len(ttl_files)} Turtle files to {target_label}.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
