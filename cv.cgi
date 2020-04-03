#!/usr/bin/perl


$addr  = $ENV{'REMOTE_ADDR'};
$buffer = $ENV{'QUERY_STRING'};

open (FILE,">>logs/cv_c.txt");
print (FILE "[",scalar(localtime(time+21600)),"] $addr<br>\n");
close(FILE);

open (FILE,">logs/cv.txt");
#print (FILE time,"| $addr | $buffer ");
print (FILE "[",time+21600,"] $addr");

close(FILE);

print "Content-type: text/html\n\n";

print "$addr\n";
exit;

