#!/usr/bin/env -S awk -f

# coding: utf-8

# Copyright 2020 Paulo Kretcheu <https://github.com/kretcheu/devel/>

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Lesser General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Lesser General Public License for more details.

#    You should have received a copy of the GNU Lesser General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


BEGIN {
   RS=""
   FS="\n"

   hum[1024^2]="Gb"
   hum[1024]="Mb"

   ARGV[1] = "/var/lib/dpkg/status"
   ARGC = 2
}


NR {
   pacote = substr($1, index($1, ": ")+2)
   tamanho = substr($5, index($5, ": ")+1)

   tamanho = tamanho*1
   array [pacote]=tamanho
}

END {

   for (i in array) {

      for (x=1024^2; x>=1024; x/=1024) {
         if ( array[i]>=x ) {
           registro = sprintf("%.2f %s %s",array[i]/x,hum[x],i)
           break
         }
      }


     if ( array[i] < 1024 ){
        registro = sprintf("%s %s","<~1Mb",i)
     }

     print registro | "sort -h -k1 -k2"
  }

}

