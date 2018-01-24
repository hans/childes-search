#!/bin/bash

find . -name "*.cha" | \
  xargs -I {} bash -c 'fn=`dirname {} | sed 's/[/]/_/g' | sed 's/^\._//g'`; fn2=`basename {}`; fn3="${fn}_${fn2}"; echo $fn3; java -cp ~/Downloads/chatter.jar org.talkbank.chatter.App {} > $fn3.xml'
for x in *.xml; do python ../convert_conllu.py . $x > $x.conllu; done
