#!/bin/bash

saida="todos_sem_sono.out"

if [ -e $saida ]; then 
	echo "Arquivo de saída já existe. Não executado!"
#	exit
fi

echo "experimento;alpha;epsilon;esparso;acuracia;seed;dataset;peso" > $saida
for i in `ls *.csv | grep log`; do 

linha=`tail -n 1 $i`
experimento=`echo $linha |cut -d";" -f1`
alpha=`echo $linha | cut -d";" -f2`
epsilon=`echo $linha | cut -d";" -f3`
acuracia=`echo $linha | cut -d";" -f16`
seed=`echo $linha | cut -d";" -f17`
neur_cam_2=`echo $linha | cut -d";" -f12`
neur_cam_3=`echo $linha | cut -d";" -f13`
peso_total=`echo $linha | cut -d";" -f15`
dataset="cifar"
#esparso=`echo "100 - (($neur_cam_2 + $neur_cam_3)*100/(2*(1000 * $alpha / 100) * ( 1000 * $alpha / 100)))" | bc -l`

#esparso=`echo "100 - (($neur_cam_2 + $neur_cam_3)*100/(2*(1000 * $alpha / 100) * ( 1000 * $alpha / 100)))" | bc -l`
#echo "100 - (($neur_cam_2 + $neur_cam_3)*100/(2*(1000 * $alpha / 100) * ( 1000 * $alpha / 100)))"  >> $saida

echo "$experimento;$alpha;$epsilon;$esparso;$acuracia;$seed;$dataset;$peso_total" >> $saida
done
