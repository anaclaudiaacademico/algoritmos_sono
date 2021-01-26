#!/bin/bash

saida="log_sem_sono.csv"

if [ -e $saida ]; then 
	echo "Arquivo de saída já existe. Não executado!"
#	exit
fi

echo "alpha;epsilon;total_epoch;seed;dataset;loss;acc;val_loss;val_acc;epoch" > $saida

for i in `ls *.txt`; do 
	arq=`echo $i|cut -d"_" -f4-7|sed "s/_/\;/g" | cut -d"." -f1`
       	data=`grep "/step" $i | tail -n1|awk {'print $8 ";" $11 ";" $14 ";" $17'}`
	dataset="cifar"

	# Escrevendo o arquivo
	grep "Epoch 999/999" $i && tail -n1 $i|grep "500/500" && echo "$arq;$dataset;$data" >> $saida
#        echo "$arq;$dataset;$data" >> $saida

done
