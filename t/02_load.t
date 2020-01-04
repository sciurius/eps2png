#! perl

use strict;
use warnings;
use Test::More tests => 1;

if ( -d "t" ) {
    chdir "t";
}

@ARGV = qw( --test );
require_ok("../script/eps2png");

diag( "Testing eps2png $::VERSION, Perl $], $^X" );

