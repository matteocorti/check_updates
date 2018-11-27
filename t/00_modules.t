#!perl

use 5.00800;

use strict;
use warnings;

use Test::More tests => 17;
use Monitoring::Plugin;

our $VERSION = '1.6.19';

use_ok('Carp');

use_ok('English');

use_ok('Monitoring::Plugin');
can_ok( 'Monitoring::Plugin', 'new' );
can_ok( 'Monitoring::Plugin', 'nagios_exit' );
can_ok( 'Monitoring::Plugin', 'add_perfdata' );
can_ok( 'Monitoring::Plugin', 'perfdata' );

use_ok( 'Monitoring::Plugin' . '::Getopt' );
can_ok( 'Monitoring::Plugin' . '::Getopt', 'new' );
can_ok( 'Monitoring::Plugin' . '::Getopt', 'arg' );
can_ok( 'Monitoring::Plugin' . '::Getopt', 'getopts' );
can_ok( 'Monitoring::Plugin' . '::Getopt', 'get' );

use_ok( 'Monitoring::Plugin' . '::Threshold' );
can_ok( 'Monitoring::Plugin' . '::Threshold', 'new' );
can_ok( 'Monitoring::Plugin' . '::Threshold', 'set_thresholds' );

use_ok('POSIX');
can_ok( 'POSIX', 'uname' );

1;
