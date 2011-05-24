#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More;

use lib '..';

use check_updates;

our $VERSION = '1.4.12';

like( check_updates::whoami(), '/IIII/mxs', 'TEXT');

done_testing();

1;
