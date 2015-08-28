#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 1;
use File::Spec;

our $VERSION = '1.6.12';

my $check_updates = File::Spec->catfile(qw(blib script check_updates));

require_ok($check_updates);

## no critic (ProhibitPackageVars)
our $yum_executable = 't/mocks/yum_errors.1.sh';
## use critic
run_yum(q{});

1;
