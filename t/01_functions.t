#!perl

# $Id: README 1103 2009-12-07 07:49:19Z corti $
# $Revision: 1103 $
# $HeadURL: https://svn.id.ethz.ch/nagios_plugins/check_updates/README $
# $Date: 2009-12-07 08:49:19 +0100 (Mon, 07 Dec 2009) $

use 5.00800;

use strict;
use warnings;

use Test::More tests => 17;

use File::Spec;

our $VERSION = '1.6.5';

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

is( get_updater('Fedora release 14 (Laughlin)'), 'yum', 'updater Fedora' );
is( get_updater('Fedora release 15 (Lovelock)'), 'yum', 'updater Fedora' );
is( get_updater('Red Hat Enterprise Linux Server release 6.1 (Santiago)'),
    'yum', 'updater FedorRHEL 6' );
is( get_updater('Scientific Linux release 6.0 (Carbon)'),
    'yum', 'updater Scientific Linux' );
is( get_updater('Red Hat Enterprise Linux AS release 4 (Nahant Update 9)'),
    'up2date', 'updater RHEL 4' );

1;
