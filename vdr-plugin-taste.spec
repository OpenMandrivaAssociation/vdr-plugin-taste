
%define plugin	taste
%define name	vdr-plugin-%plugin
%define version	0.0.2d
%define snapshot 20070421
%define rel	4

Summary:	VDR plugin: Lock unwanted shows by keywords
Name:		%name
Version:	%version
Release:	%mkrel 1.%snapshot.%rel
Group:		Video
License:	GPL
URL:		http://linux.kompiliert.net/index.php?view=taste
Source:		vdr-%plugin-%snapshot.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	vdr-devel >= 1.4.1-6
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

%build
%vdr_plugin_build

%install
rm -rf %{buildroot}
%vdr_plugin_install

%clean
rm -rf %{buildroot}

%post
%vdr_plugin_post %plugin

%postun
%vdr_plugin_postun %plugin

%files -f %plugin.vdr
%defattr(-,root,root)
%doc README HISTORY
