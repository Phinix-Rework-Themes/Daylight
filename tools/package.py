#!/usr/bin/env python3
"""Build and validate with the trusted Phinix theme package tool."""
import argparse
import json
from pathlib import Path
import subprocess
p=argparse.ArgumentParser(description=__doc__)
p.add_argument('--tool',type=Path,required=True)
p.add_argument('--output',type=Path,required=True)
a=p.parse_args();root=Path(__file__).resolve().parents[1]
config=root/'theme/package.json';data=json.loads(config.read_text())
if not a.tool.is_file() or a.output.exists():p.error('Use a trusted tool DLL and a fresh output directory.')
a.output.mkdir(parents=True)
archive=a.output/(data['packageId'].split('.')[-1]+'-'+data['version']+'.zip')
subprocess.run(['dotnet',str(a.tool.resolve()),'--pack-theme',str(config),str(archive)],check=True)
subprocess.run(['dotnet',str(a.tool.resolve()),'--validate-theme',str(archive)],check=True)
