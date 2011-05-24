# Load the Module::Install bundled in ./inc/
use inc::Module::Install;

################################################################################
# Version information:
#
# $Id$
# $Revision$
# $HeadURL$
# $Date$
#

##############################################################################
# Define metadata (we read it from the binary)

name              'check_updates';
version_from      'check_updates';
perl_version_from 'check_updates';
all_from          'check_updates.pod';

##############################################################################
# Specific dependencies

include 'version';

requires 'Carp'                      => 0;
requires 'English'                   => 0;
requires 'Nagios::Plugin'            => 0;
requires 'Nagios::Plugin::Getopt'    => 0;
requires 'Nagios::Plugin::Threshold' => 0;
requires 'POSIX'                     => 0;
requires 'Sort::Versions'            => 0;

install_script  'check_updates';

tests 't/*.t';
test_requires 'Test::More'       => 0;

WriteMakefile(
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_updates.pod' => 'blib/man1/check_updates.1', },
    MAN3PODS             => { },
);
