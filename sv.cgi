#!/usr/bin/perl


$addr  = $ENV{'REMOTE_ADDR'};
$buffer = $ENV{'QUERY_STRING'};

$localtime=localtime;
$time=time;

open (FILE,">>logs/sv_c.txt");
	print (FILE "$localtime#$addr#$time\n");
close(FILE);

open (FILE,">logs/sv.txt");
	print (FILE "$localtime#$addr#$time\n");
close(FILE);

print "Content-type: text/html\n\n";

print "$addr\n";
exit;

