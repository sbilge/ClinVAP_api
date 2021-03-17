#!/bin/bash
 
if [ ! -e /mnt/homo_sapiens ]; then
    cp -r /opt/vep/src/ensembl-vep/offline_cache/homo_sapiens /mnt
fi

if  [ ! -f /mnt/LoFtool_scores.txt ]; then
    cp LoFtool_scores.txt /mnt
fi

wait
echo "Dependency files are now in the volume." >> /mnt/completeness.flag
