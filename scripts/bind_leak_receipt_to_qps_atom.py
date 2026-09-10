#!/usr/bin/env python3
"""Bind a leak-physics receipt to an explicit current-QPS engineering atom.

This is evidence binding, not compliance closure. The QPS atom owns the conditions and
source identity; the satellite receipt must match those conditions exactly.
"""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path

SHA256 = re.compile(r"^[a-f0-9]{64}$")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    p=argparse.ArgumentParser()
    p.add_argument('--atom', type=Path, required=True)
    p.add_argument('--receipt', type=Path, required=True)
    p.add_argument('--output', type=Path, required=True)
    a=p.parse_args()
    atom=json.loads(a.atom.read_text(encoding='utf-8'))
    receipt=json.loads(a.receipt.read_text(encoding='utf-8'))

    required_atom=['atom_id','source_ref','source_sha256','leak_mbar_l_s','temperature_k','pressure_bar_abs','reference_pressure_bar']
    missing=[k for k in required_atom if k not in atom]
    if missing:
        raise SystemExit(f'FAIL missing QPS atom fields: {missing}')
    if atom.get('authority_class') not in {'CANONICAL_SOURCE_AUTHORITY','SSOT_BOUND_ENGINEERING_ATOM'}:
        raise SystemExit('FAIL QPS atom is not current governed authority-bound input')
    if not SHA256.fullmatch(str(atom['source_sha256'])):
        raise SystemExit('FAIL QPS atom source_sha256 must be lowercase 64-hex')

    required_receipt=['leak_mbar_l_s','temperature_k','pressure_bar_abs','reference_pressure_bar','interpretation']
    missing_receipt=[k for k in required_receipt if k not in receipt]
    if missing_receipt:
        raise SystemExit(f'FAIL missing satellite receipt fields: {missing_receipt}')

    pairs=[
        ('leak_mbar_l_s','leak_mbar_l_s'),
        ('temperature_k','temperature_k'),
        ('pressure_bar_abs','pressure_bar_abs'),
        ('reference_pressure_bar','reference_pressure_bar'),
    ]
    mismatches=[]
    for ak,rk in pairs:
        if float(atom[ak]) != float(receipt[rk]):
            mismatches.append({'atom_field':ak,'receipt_field':rk,'atom':atom[ak],'receipt':receipt[rk]})
    if mismatches:
        raise SystemExit(f'FAIL condition mismatch: {mismatches}')

    expected='REFERENCE_THROUGHPUT_CONVERSION' if float(atom['pressure_bar_abs']) == float(atom['reference_pressure_bar']) else 'COMPARATIVE_PRESSURE_SENSITIVITY'
    if receipt.get('interpretation') != expected:
        raise SystemExit(f"FAIL interpretation mismatch: expected {expected}, got {receipt.get('interpretation')}")

    out={
        'schema':'qps-leak-evidence-binding/v0.2',
        'classification':'BOUND_ENGINEERING_EVIDENCE_NOT_COMPLIANCE',
        'qps_atom_id':atom['atom_id'],
        'qps_source_ref':atom['source_ref'],
        'qps_source_sha256':atom['source_sha256'],
        'atom_file_sha256':sha(a.atom),
        'satellite_receipt_sha256':sha(a.receipt),
        'interpretation':expected,
        'conditions_match':True,
        'authority_effect':'NONE',
        'compliance_credit':False,
        'release_credit':False,
    }
    a.output.parent.mkdir(parents=True, exist_ok=True)
    a.output.write_text(json.dumps(out,indent=2,sort_keys=True)+'\n',encoding='utf-8')
    print(json.dumps(out,sort_keys=True))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
