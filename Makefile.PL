# Load the Module::Install bundled in ./inc/
use lib '.'; # added since from Perl 5.26 '.' is no more in @INC
use inc::Module::Install;

##############################################################################
# Define metadata (we read it from the binary)

name              'check_updates';
version_from      'check_updates';
perl_version_from 'check_updates';
all_from          'check_updates.pod';

##############################################################################
# Specific dependencies

include 'version';

my %prereqs = (
    'Carp'     => 0,
    'English'  => 0,
    'POSIX'    => 0,
    'Readonly' => 0,
    'Monitoring::Plugin' => 0,
    'Monitoring::Plugin::Threshold' => 0,
    'Monitoring::Plugin::Getopt' => 0,
);

install_script  'check_updates';

auto_install;

tests 't/*.t';
test_requires 'Test::More'       => 0;
test_requires 'File::Spec'       => 0;

WriteMakefile(
    PREREQ_PM            => \%prereqs,
    INSTALLSCRIPT        => '/usr/lib/nagios/plugins/contrib',
    INSTALLSITESCRIPT    => '/usr/lib/nagios/plugins/contrib',
    MAN1PODS             => { 'check_updates.pod' => 'blib/man1/check_updates.1', },
    MAN3PODS             => { },
);
