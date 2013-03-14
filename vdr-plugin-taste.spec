
%define plugin	taste
%define name	vdr-plugin-%plugin
%define version	0.0.2d
%define snapshot 20080425
%define rel	6

Summary:	VDR plugin: Lock unwanted shows by keywords
Name:		%name
Version:	%version
Release:	%mkrel 1.%snapshot.%rel
Group:		Video
License:	GPL
URL:		http://linux.kompiliert.net/index.php?view=taste
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
%defattr(-,root,root)
%doc README HISTORY


%changelog
* Thu Jul 30 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20080425.5mdv2011.0
+ Revision: 404573
- rebuild due to BS building the previous release against wrong VDR on x86_64

* Tue Jul 28 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20080425.4mdv2010.0
+ Revision: 401088
- rebuild for new VDR

* Fri Mar 20 2009 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20080425.3mdv2009.1
+ Revision: 359374
- rebuild for new vdr

* Mon Apr 28 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20080425.2mdv2009.0
+ Revision: 197986
- rebuild for new vdr

* Sat Apr 26 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20080425.1mdv2009.0
+ Revision: 197731
- new snapshot
- add vdr_plugin_prep
- bump buildrequires on vdr-devel
- adapt to gettext i18n of VDR 1.6 (semi-automatic patch)
- adapt for api changes of VDR 1.5.0 (P0 from e-tobi)

* Fri Jan 04 2008 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20070421.6mdv2008.1
+ Revision: 145217
- rebuild for new vdr

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20070421.5mdv2008.1
+ Revision: 103221
- rebuild for new vdr

* Sun Jul 08 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20070421.4mdv2008.0
+ Revision: 50055
- rebuild for new vdr

* Thu Jun 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20070421.3mdv2008.0
+ Revision: 42138
- rebuild for new vdr

* Sat May 05 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20070421.2mdv2008.0
+ Revision: 22710
- rebuild for new vdr

* Sat Apr 21 2007 Anssi Hannula <anssi@mandriva.org> 0.0.2d-1.20070421.1mdv2008.0
+ Revision: 16472
- initial Mandriva release

