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
   pacote = substr($1, index($1, ": ")+1)
   tamanho = substr($5, index($5, ": ")+1)

   tamanho = tamanho*1

   for (x=1024^2; x>=1024; x/=1024) {
      if ( tamanho>=x ) {
        printf "%.2d %s",tamanho/x,hum[x]
        break
      }
   }

   if ( tamanho < 1024 ){
      printf "%s","<~1Mb"
      #print "<~1Mb"
   }

   print pacote

}
