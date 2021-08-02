#!perl

use 5.00800;

use strict;
use warnings;

use Test::More tests => 40;

use File::Spec;

our $VERSION = '1.6.19';

my $check_updates = File::Spec->catfile(qw(blib script check_updates));

require_ok($check_updates);

# any user is OK
like( whoami(), '/[\w]/mxs', 'whoami' );

is( clean_kernel_version('kernel-2.6.35.13-91.fc14.i686'),
    'kernel-2.6.35.13-91', 'kernel version Fedora' );
is( clean_kernel_version('kernel-2.6.18-194.3.1.el5'),
    'kernel-2.6.18-194.3.1', 'kernel version RHEL' );

# TODO: should be extended with mock files
is(
    get_os_name_and_version('t/examples/fedora_14'),
    'Fedora release 14 (Laughlin)',
    '/etc/redhat-release Fedora 14'
);
is(
    get_os_name_and_version('t/examples/fedora_15'),
    'Fedora release 15 (Lovelock)',
    '/etc/redhat-release Fedora 15'
);
is(
    get_os_name_and_version('t/examples/fedora_17'),
    'Fedora release 17 (Beefy Miracle)',
    '/etc/system-release Fedora 17'
);
is(
    get_os_name_and_version('t/examples/rhel_4'),
    'Red Hat Enterprise Linux AS release 4 (Nahant Update 9)',
    '/etc/redhat-release RHEL 4'
);
is(
    get_os_name_and_version('t/examples/rhel_6'),
    'Red Hat Enterprise Linux Server release 6.1 (Santiago)',
    '/etc/redhat-release RHEL 6'
);
is(
    get_os_name_and_version('t/examples/scientific_linux_6'),
    'Scientific Linux release 6.0 (Carbon)',
    '/etc/redhat-release Scientific Linux'
);
is(
    get_os_name_and_version('t/examples/scientific_linux_6'),
    'Scientific Linux release 6.0 (Carbon)',
    '/etc/redhat-release Scientific Linux'
);
is(
    get_os_name_and_version('t/examples/puias_6.2'),
    'PUIAS Linux  release 6.2 (Pisa)',
    '/etc/system-release PUIAS Linux 6.2'
);
is(
    get_os_name_and_version('t/examples/rocky_linux_8'),
    'Rocky Linux release 8.4 (Green Obsidian)',
    '/etc/system-release Rocky Linux 8.4'
);

is( get_updater('Fedora release 14 (Laughlin)'), 'yum', 'updater Fedora' );
is( get_updater('Fedora release 15 (Lovelock)'), 'yum', 'updater Fedora' );
is( get_updater('Red Hat Enterprise Linux Server release 6.1 (Santiago)'),
    'yum', 'updater FedorRHEL 6' );
is( get_updater('Scientific Linux release 6.0 (Carbon)'),
    'yum', 'updater Scientific Linux' );
is( get_updater('Red Hat Enterprise Linux AS release 4 (Nahant Update 9)'),
    'up2date', 'updater RHEL 4' );
is( get_updater('Rocky Linux release 8.4 (Green Obsidian)'),
    'yum', 'updater Rocky Linux' );

# versioncmp

sub test_versioncmp {

    my ( $left_operand, $right_operand, $res ) = @_;

    local $a = $left_operand;
    local $b = $right_operand;

    is( versioncmp(), $res, "versioncmp('$left_operand','$right_operand')" );

    return;

}

## no critic (ProhibitMagicNumbers)
test_versioncmp( '1.1', '1.2', -1 );

test_versioncmp( '1.2', '1.1', 1 );
test_versioncmp( '1.1', '1.1', 0 );

test_versioncmp( '1.1a', '1.2',  -1 );
test_versioncmp( '1.2',  '1.1a', 1 );

test_versioncmp( '1.1',   '1.1.1', -1 );
test_versioncmp( '1.1.1', '1.1',   1 );

test_versioncmp( '1.1',  '1.1a', -1 );
test_versioncmp( '1.1a', '1.1',  1 );

test_versioncmp( '1.1.a', '1.1a',  -1 );
test_versioncmp( '1.1a',  '1.1.a', 1 );

test_versioncmp( '1', 'a', -1 );
test_versioncmp( 'a', '1', 1 );

test_versioncmp( 'a', 'b', -1 );
test_versioncmp( 'b', 'a', 1 );

test_versioncmp( '1', '2', -1 );
test_versioncmp( '2', '1', 1 );

test_versioncmp( '1.1-3', '1.1-4', -1 );
test_versioncmp( '1.1-4', '1.1-3', 1 );

test_versioncmp( '1.1-5', '1.1.6', -1 );
test_versioncmp( '1.1.6', '1.1.5', 1 );
## use critic (ProhibitMagicNumbers)

1;

