#!/usr/bin/perl
# $Id$

use Test::More;
plan tests => 5;

require_ok "t/basic.pl";

SKIP: {
    skip "GhostScript (gs) not available", 4
      unless findbin("gs");
    testit("jpg");
}
