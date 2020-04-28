#!/usr/bin/perl -w
##############################################################################
# COPYLEFT NOTICE  JPL   ver.cgi                                                                                                         #
##############################################################################

print "Content-type: text/html\n\n";
print "<html><head><META HTTP-EQUIV=\"REFRESH\" CONTENT=\"900;URL=http://ip.gnu.works/ddns.cgi\"><title>Controle de IP's</title></head>\n";
print "<body bgcolor=\"#000000\" text=\"#FFFFFF\">\n";

%hosts=(	"01","cv:Cabo Verde:#00FF00",
			"02","ge:Geral:#FF0080",
			"03","ip:IP:#FF8373",
			#"04","ro:Ross:#008080",
			"05","sv:São Vicente:#FFFFFF",
			#"06","st:Tilápia:#80A8FF",
			#"07","ca:Carpa:#ffbd71",
                        #"08","st2:Cara:#8EFFAC",
			#"09","el:Orsi:#FF8373",
			#3"10","ci:Bene:#FF7F00",
			#"11","pa:Papagaio:#C043FF",
			#"12","eq:Embaquim:#8EFFAC",
			#"13","dw:DWG:#008080",
			#"14","ex:Calex:#FF8373",
			#"15","ih:Ihm:#CO43FF",
			#"16","ch:Chassi:#FF8373",
			#"17","ad:Aglaw:#8EFFAC",
			#"18","ce:Ceramic:#008080",
			#"19","pi:Pipe:#C043FF",

			);

$on  = "<img src=\"imagens/on.png\" width=\"32\" height=\"32\" alt=\"On\" />";
$off = "<img src=\"imagens/off.png\" width=\"32\" height=\"32\" alt=\"Off\" />";
$agora = time;
$localtime = localtime;

print "<table border=\"1\" cellpadding=\"0\" cellspacing=\"0\">\n";

print "<tr>";
print "<td colspan=\"5\"><font color=\"#FFFFFF\">Controle de servidores: [$localtime]</font></td>";
print "</tr>\n";

print "<tr>";
print "<th>Estado</th>";
print "<th>&nbsp;Diferença</th>";
print "<th width=\"130\"><font color=\"$dados[2]\">&nbsp;Servidor</font></th>";
print "<th width=\"170\"><font color=\"$dados[2]\">&nbsp;IP</font></th>";
print "<th width=\"250\"><font color=\"$dados[2]\">&nbsp;Horário</font></th>";
print "</tr>\n";


foreach $host (sort keys %hosts) {

	@dados = split(":",$hosts{$host});

	open (FILE,"logs/$dados[0].txt");
		$linha = <FILE>;
	close(FILE);

	@info = split("#",$linha);
	$hora = $info[0];

        $hora_epoch = $info[2];

	$diferenca = $agora - $hora_epoch;
	if ( $diferenca < 1200 ) {
		$status = "<font color=\"#00FF00\">On</font>";
	}	else {
		$status = "<font color=\"#FF0000\">Off</font>";
	}

	print "<tr>";
	print "<td>$status&nbsp;</td>";
	print "<td>&nbsp;$diferenca</td>";
	print "<td width=\"130\"><font color=\"$dados[2]\">&nbsp;$dados[1]</font></td>";
	print "<td width=\"170\"><font color=\"$dados[2]\">&nbsp;$info[1]</font></td>";
	print "<td width=\"250\"><font color=\"$dados[2]\">&nbsp;$hora</font></td>";
	print "</tr>\n";

}

#print "<font color=\"#ffbd71\" >";
#print "<font color=\"#0000FF\" >";
#print "<font color=\"#FF7F00\" >";



print "</table>";
print "</body></html>";
exit;
