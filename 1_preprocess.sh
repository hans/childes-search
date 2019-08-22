#!/bin/bash
set -e

# find . -name "*.cha" | \
#   xargs -I {} bash -c 'fn=`dirname {} | sed 's/[/]/_/g' | sed 's/^\._//g'`; fn2=`basename {}`; fn3="${fn}_${fn2}"; echo $fn3; java -cp chatter.jar org.talkbank.chatter.App {} > $fn3.xml'
find . -name "*.xml" | xargs -I {} -n 1 bash -c "bn=\$(basename {}); echo \$bn && cp {} \$bn && python convert_conllu.py {} --speaker MOT > \$bn.conllu"
