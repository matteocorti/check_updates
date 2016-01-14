#!perl

use 5.00800;

use strict;
use warnings;

use Test::More tests => 17;

our $VERSION = '1.6.14';

use_ok('Carp');

use_ok('English');

my $plugin_name;
if ( eval { require Monitoring::Plugin } ) {
    $plugin_name = 'Monitoring::Plugin';
}
else {
    $plugin_name = 'Nagios::Plugin';
}

use_ok($plugin_name);
can_ok( $plugin_name, 'new' );
can_ok( $plugin_name, 'nagios_exit' );
can_ok( $plugin_name, 'add_perfdata' );
can_ok( $plugin_name, 'perfdata' );

use_ok( $plugin_name . '::Getopt' );
can_ok( $plugin_name . '::Getopt', 'new' );
can_ok( $plugin_name . '::Getopt', 'arg' );
can_ok( $plugin_name . '::Getopt', 'getopts' );
can_ok( $plugin_name . '::Getopt', 'get' );

use_ok( $plugin_name . '::Threshold' );
can_ok( $plugin_name . '::Threshold', 'new' );
can_ok( $plugin_name . '::Threshold', 'set_thresholds' );

use_ok('POSIX');
can_ok( 'POSIX', 'uname' );

1;
