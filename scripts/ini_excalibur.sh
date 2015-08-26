#!/bin/bash

# get path of Excalibur relative to location of this script
export EXCALIBURPATH=$(dirname $(dirname $(readlink -mf ${BASH_SOURCE[0]})))
export ARTUSPATH=$EXCALIBURPATH/../Artus

# source Artus ini script
source $ARTUSPATH/Configuration/scripts/ini_ArtusAnalysis.sh
export PATH=$ARTUSPATH/Utility/scripts:$PATH

# set the environment
export BOOSTPATH=$(ls ${VO_CMS_SW_DIR}/${SCRAM_ARCH}/external/boost/* -d | tail -n 1)
BOOSTVER=${BOOSTPATH%-*}
export BOOSTLIB=${BOOSTPATH}/lib/libboost_regex.so.${BOOSTVER/*\//}
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:$ARTUSPATH:$BOOSTPATH/lib
export PATH=$PATH:$EXCALIBURPATH/scripts
export PYTHONPATH=$PYTHONPATH:$EXCALIBURPATH/cfg/python:$EXCALIBURPATH/cfg/excalibur
export USERPC=`who am i | sed 's/.*(\([^]]*\)).*/\1/g'`

# excalibur.py auto-completion
function _artuscomplete_()
{
    local names
    for i in `ls ${EXCALIBURPATH}/cfg/excalibur/*.py`
        do names="${names} `basename $i .py`"
    done
    COMPREPLY=($(compgen -W "${names}" -- ${COMP_WORDS[COMP_CWORD]}))
}
complete -F _artuscomplete_ excalibur.py

if [ -d "/storage/a/$USER/zjet" ]; then
    export EXCALIBUR_WORK=/storage/a/$USER/zjet
fi
# Set some user specific variables
if [ $USER = "dhaitz" ]; then
    if [[ $HOSTNAME == *"naf"* ]]; then
        export EXCALIBUR_WORK=/afs/desy.de/user/d/dhaitz/nfs/zjet
    fi
elif [ $USER = "berger" ]; then
    export PATH=$PATH:$EXCALIBURPATH/../grid-control:$EXCALIBURPATH/../grid-control/scripts
    alias merlin='merlin.py'
    alias excalibur='excalibur.py'
    alias merlinp='merlin.py --python'
    alias merlinw='merlin.py --www'
    alias merlinl='merlin.py --live evince'
    alias merlinlp='merlin.py --live evince --python'
    alias merlinlx='merlin.py --live evince -x'
fi
