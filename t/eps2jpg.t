#!/usr/bin/perl
# $Id$

print "1..5\n";

eval { require "t/basic.pl"; };
print "$@\nnot ok 1\n" if $@;

testit ("jpg");
