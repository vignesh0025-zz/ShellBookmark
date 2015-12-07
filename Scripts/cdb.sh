#!/usr/bin/env bash

cdb () {
	output="$(python /usr/local/cdb.py $*)"
	case $output in
   	cd*)
		eval $output
   	;;	
   	*)
   		echo $output
   	;;
	esac
}