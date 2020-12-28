#!/bin/bash
count=$(find /root/pictures/ -name *mov | wc -l)
for ((i=1; i<=$count; i+=1)); do
	file=$(find /root/pictures/ -name *mov | head -n $i | tail -n 1)
	if [ $(ls -l ${file/mov/mp4} | wc -l) == 0 ]; then
		echo make ${file/mov/mp4} from $file
		ffmpeg -i $file ${file/mov/mp4}
	else
		echo file already exists ${file/mov/mp4}
	fi
done
