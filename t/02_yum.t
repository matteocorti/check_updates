#!perl

use 5.00800;

use strict;
use warnings;

use Test::More tests => 1;
use File::Spec;

our $VERSION = '1.6.13';

my $check_updates = File::Spec->catfile(qw(blib script check_updates));

require_ok($check_updates);

## no critic (ProhibitPackageVars)
our $yum_executable = 't/mocks/yum_errors.1.sh';
## use critic
run_yum(q{});

1;
