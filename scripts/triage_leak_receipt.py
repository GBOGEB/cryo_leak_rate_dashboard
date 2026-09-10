#!/usr/bin/env python3
import argparse, json
from src.calc_leak_rate import dimensional_proof

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--leak', type=float, required=True)
    p.add_argument('--temperature-k', type=float, required=True)
    p.add_argument('--pressure-bar-abs', type=float, default=1.0)
    p.add_argument('--reference-pressure-bar', type=float, default=1.0)
    a=p.parse_args()
    result=dimensional_proof(a.leak,a.temperature_k,a.pressure_bar_abs)
    # Preserve the worked dimensional proof while making the receipt contract explicit.
    result['leak_mbar_l_s']=a.leak
    result['temperature_k']=a.temperature_k
    result['pressure_bar_abs']=a.pressure_bar_abs
    result['reference_pressure_bar']=a.reference_pressure_bar
    result['interpretation']='COMPARATIVE_PRESSURE_SENSITIVITY' if a.pressure_bar_abs != a.reference_pressure_bar else 'REFERENCE_THROUGHPUT_CONVERSION'
    result['release_credit']=False
    print(json.dumps(result, sort_keys=True))
if __name__=='__main__': main()
