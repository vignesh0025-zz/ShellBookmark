#!/usr/bin/env bash

cdb () {
	output="$(python $HOME/cdb.py $*)"
	case $output in
   	cd*)
		eval $output
   	;;	
   	*)
   		echo $output
   	;;
	esac
}