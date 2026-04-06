#!/usr/bin/env python3
"""
Validate that a markdown analysis report properly cites URLs from an extraction JSON file.

This script checks:
1. Extraction JSON for all URLs across various report sections
2. Markdown report for markdown-style links [text](url)
3. Section-specific citation requirements
4. Coverage percentage of extraction URLs in the report

Usage:
    python validate-citations.py --report path/to/report.md --extraction path/to/extraction.json
"""

import json
import re
import sys
import argparse
from pathlib import Path
from typing import Set, Dict, List, Tuple, Any


def strip_jsonc_comments(content: str) -> str:
    """
    Strip // style line comments from JSONC content.

    Only strips comments that appear outside of JSON string values.
    A line comment starts with // when not inside a quoted string.

    Args:
        content: Raw JSONC file content

    Returns:
        JSON content with // comments removed
    """
    lines = []
    for line in content.split('\n'):
        stripped = line.lstrip()
        # Only strip lines that START with // (full-line comments)
        # This is safe because JSON values never start with //
        if stripped.startswith('//'):
            continue
        # For inline comments after JSON content, we'd need a full parser.
        # Since our extraction files only use full-line comments (if any),
        # this simple approach avoids corrupting URLs in string values.
        lines.append(line)
    return '\n'.join(lines)


def extract_urls_from_json(extraction_file: Path) -> Tuple[Set[str], int]:
    """
    Parse extraction JSON and collect all URLs from relevant sections.

    Walks through:
    - reports[0].tier1.reddit (list of objects with 'url')
    - reports[0].tier1.hacker_news (list of objects with 'url')
    - reports[0].tier1.blogs_publications (list of objects with 'url')
    - reports[0].tier1_5.youtube (list of objects with optional 'url')
    - reports[0].tier2 (list of objects with 'url')
    - reports[0].incidents (list of objects with 'url')
    - reports[0].emerging_patterns (list of objects with 'sources' list)
    - reports[0].deduplication_references (list of objects with 'canonical_url')

    Args:
        extraction_file: Path to extraction JSON/JSONC file

    Returns:
        Tuple of (set of unique URLs, total count of URL occurrences)
    """
    urls = set()
    url_count = 0

    try:
        with open(extraction_file, 'r', encoding='utf-8') as f:
            content = f.read()

        # Strip JSONC comments
        content = strip_jsonc_comments(content)
        data = json.loads(content)

        if not data.get('reports') or len(data['reports']) == 0:
            return urls, url_count

        report = data['reports'][0]

        # tier1.reddit
        tier1 = report.get('tier1', {})
        for item in tier1.get('reddit', []):
            if isinstance(item, dict) and 'url' in item:
                url = item['url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

        # tier1.hacker_news
        for item in tier1.get('hacker_news', []):
            if isinstance(item, dict) and 'url' in item:
                url = item['url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

        # tier1.blogs_publications
        for item in tier1.get('blogs_publications', []):
            if isinstance(item, dict) and 'url' in item:
                url = item['url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

        # tier1_5.youtube
        tier1_5 = report.get('tier1_5', {})
        for item in tier1_5.get('youtube', []):
            if isinstance(item, dict) and 'url' in item:
                url = item['url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

        # tier2
        for item in report.get('tier2', []):
            if isinstance(item, dict) and 'url' in item:
                url = item['url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

        # incidents
        for item in report.get('incidents', []):
            if isinstance(item, dict) and 'url' in item:
                url = item['url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

        # emerging_patterns
        for item in report.get('emerging_patterns', []):
            if isinstance(item, dict) and 'sources' in item:
                sources = item['sources']
                if isinstance(sources, list):
                    for source in sources:
                        if isinstance(source, str) and source.startswith('http'):
                            urls.add(source)
                            url_count += 1

        # deduplication_references
        for item in report.get('deduplication_references', []):
            if isinstance(item, dict) and 'canonical_url' in item:
                url = item['canonical_url']
                if url.startswith('http'):
                    urls.add(url)
                    url_count += 1

    except FileNotFoundError:
        print(f"Error: Extraction file not found: {extraction_file}", file=sys.stderr)
        sys.exit(2)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse extraction JSON: {e}", file=sys.stderr)
        sys.exit(2)

    return urls, url_count


def extract_urls_from_markdown(report_file: Path) -> Tuple[Set[str], int]:
    """
    Parse markdown report and extract all URLs from markdown links.

    Looks for markdown link syntax: [text](url)
    Only captures http/https URLs.

    Args:
        report_file: Path to markdown report file

    Returns:
        Tuple of (set of unique URLs, total count of link occurrences)
    """
    urls = set()
    link_count = 0

    try:
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Error: Report file not found: {report_file}", file=sys.stderr)
        sys.exit(2)

    # Regex for markdown links: [text](url)
    pattern = r'\[([^\]]+)\]\((https?://[^)]+)\)'
    matches = re.findall(pattern, content)

    for text, url in matches:
        if url.startswith('http'):
            urls.add(url)
            link_count += 1

    return urls, link_count


def check_section_links(markdown_content: str, section_name: str) -> Dict[str, Any]:
    """
    Check if a specific section exists and contains links.

    Finds section by header (## Section Name), then counts links until next ## header.

    Args:
        markdown_content: Full markdown report content
        section_name: Section name to search for (e.g., "Deep Analysis by Cluster")

    Returns:
        Dict with 'has_links' (bool) and 'link_count' (int)
    """
    # Search for the section header (case-insensitive)
    header_pattern = rf'^## \s*{re.escape(section_name)}\s*$'
    match = re.search(header_pattern, markdown_content, re.MULTILINE | re.IGNORECASE)

    if not match:
        return {'has_links': False, 'link_count': 0, 'found': False}

    # Find the start of this section
    section_start = match.start()

    # Find the next ## header after this section
    next_header_pattern = r'^## '
    next_match = re.search(next_header_pattern, markdown_content[match.end():], re.MULTILINE)

    if next_match:
        section_end = match.end() + next_match.start()
    else:
        section_end = len(markdown_content)

    section_content = markdown_content[section_start:section_end]

    # Count links in this section
    link_pattern = r'\[([^\]]+)\]\((https?://[^)]+)\)'
    links = re.findall(link_pattern, section_content)
    link_count = len(links)

    return {
        'has_links': link_count > 0,
        'link_count': link_count,
        'found': True
    }


def validate_report(report_file: Path, extraction_file: Path) -> Dict[str, Any]:
    """
    Validate a markdown report against extraction URLs.

    Args:
        report_file: Path to markdown report
        extraction_file: Path to extraction JSON/JSONC

    Returns:
        Dict with validation results and status
    """
    errors = []

    # Extract URLs from both sources
    extraction_urls, extraction_url_count = extract_urls_from_json(extraction_file)
    report_urls, report_link_count = extract_urls_from_markdown(report_file)
    report_unique_urls = len(report_urls)

    # Read markdown for section checks
    with open(report_file, 'r', encoding='utf-8') as f:
        markdown_content = f.read()

    # Check required sections
    # Section names must match the Output Format (LOCKED) headers from the analysis prompt.
    # The prompt specifies: "Emerging Patterns & Weak Signals" and "Contradictions & Contested Claims"
    sections_to_check = [
        'Deep Analysis by Cluster',
        'Emerging Patterns & Weak Signals',
        'Incidents Log',
        'Contradictions & Contested Claims'
    ]

    section_checks = {}
    for section in sections_to_check:
        section_result = check_section_links(markdown_content, section)
        section_checks[section] = {
            'has_links': section_result['has_links'],
            'link_count': section_result['link_count']
        }
        if not section_result.get('found'):
            errors.append(f"Section not found: {section}")
        elif not section_result['has_links']:
            errors.append(f"Section has no links: {section}")

    # Calculate coverage
    coverage_pct = 0.0
    missing_urls = list(extraction_urls - report_urls)

    if extraction_urls:
        coverage_pct = (len(extraction_urls & report_urls) / len(extraction_urls)) * 100

    # Determine status
    status = 'PASS'

    if report_link_count == 0:
        status = 'FAIL'
        errors.insert(0, "No links found in report")
    elif coverage_pct < 50:
        status = 'FAIL'
        errors.insert(0, f"Coverage below 50%: {coverage_pct:.1f}%")
    elif any(not section_checks[s]['has_links'] for s in sections_to_check):
        status = 'FAIL'
    elif coverage_pct < 75:
        status = 'WARN'
        errors.insert(0, f"Coverage below 75%: {coverage_pct:.1f}%")

    return {
        'status': status,
        'extraction_url_count': len(extraction_urls),
        'report_link_count': report_link_count,
        'report_unique_urls': report_unique_urls,
        'coverage_pct': round(coverage_pct, 1),
        'section_checks': section_checks,
        'missing_urls': sorted(missing_urls),
        'errors': errors
    }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate markdown report citations against extraction JSON'
    )
    parser.add_argument(
        '--report',
        required=True,
        type=Path,
        help='Path to markdown analysis report file'
    )
    parser.add_argument(
        '--extraction',
        required=True,
        type=Path,
        help='Path to extraction JSON/JSONC file'
    )

    args = parser.parse_args()

    # Validate report
    result = validate_report(args.report, args.extraction)

    # Output JSON result
    print(json.dumps(result, indent=2))

    # Exit with appropriate code
    if result['status'] == 'PASS':
        sys.exit(0)
    elif result['status'] == 'WARN':
        sys.exit(1)
    else:  # FAIL
        sys.exit(2)


if __name__ == '__main__':
    main()
