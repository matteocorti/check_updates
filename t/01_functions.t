#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More;
use File::Spec;

our $VERSION = '1.4.12';

my $check_updates = File::Spec->catfile( qw(blib script check_updates) );

require($check_updates);

# any user is OK
like(whoami(), '/[\w]/mxs', 'whoami');

is( clean_kernel_version( 'kernel-2.6.35.13-91.fc14.i686'), 'kernel-2.6.35.13-91');
is( clean_kernel_version( 'kernel-2.6.18-194.3.1.el5'), 'kernel-2.6.18-194.3.1');

#is( check_running_kernel(), 'uu');

done_testing();

1;
