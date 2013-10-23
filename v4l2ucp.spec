Summary:	A universal control panel for all Video for Linux Two devices
Name:		v4l2ucp
Version:	2.0.2
Release:	7
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://v4l2ucp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/v4l2ucp/v4l2ucp/2.0/%{name}-%{version}.tar.bz2
Patch0:		v4l2ucp-2.0.2-kernel-2.6.38.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(libv4l1)
BuildRequires:	qt4-devel

%description
It reads a description of the controls that the V4L2 device 
supports from the device, and presents the user with a graphical 
means for adjusting those controls. It allows for controlling 
multiple devices. Controls can be updated with the device status 
either manually, or periodically. There is an easy way to reset 
one or all the controls to their default state

%prep
%setup -q %{name}-%{version}
%patch0 -p0 -b .kernel

%build
%cmake
%make

%install
%makeinstall_std -C build

%files
%doc README TODO
%{_bindir}/v4l2*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*.png
