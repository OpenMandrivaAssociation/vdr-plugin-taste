%define plugin	taste
%define snapshot 20080425

Summary:	VDR plugin: Lock unwanted shows by keywords
Name:		vdr-plugin-%plugin
Version:	0.0.2d
Release:	1.%snapshot.7
Group:		Video
License:	GPL
URL:		https://linux.kompiliert.net/index.php?view=taste
Patch0:		91_taste-0.0.2d+cvs20061111-1.5.0.dpatch
Patch1:		taste-i18n-1.6.patch
Source:		vdr-%plugin-%snapshot.tar.bz2
BuildRequires:	vdr-devel >= 1.6.0
Requires:	vdr-abi = %vdr_abi

%description
With this plugin, VDR will skip every channel that doesn't match
your "taste", which means that the current programme (if available)
is checked against a blacklist, and if it matches, a message will be
displayed and the channel is being skipped. You can either wait for
the plugin to change the channel for you after a configurable amount
of time, or simply zap again.

%prep
%setup -q -n %plugin
%patch0 -p1
%patch1 -p1
%vdr_plugin_prep

%build
%vdr_plugin_build

%install
%vdr_plugin_install

%files -f %plugin.vdr
%doc README HISTORY


