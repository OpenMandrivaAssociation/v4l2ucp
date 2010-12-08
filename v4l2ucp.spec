Summary:	A universal control panel for all Video for Linux Two devices
Name:		v4l2ucp
Version:	2.0.2
Release:	%mkrel 2
License:	GPLv2+
Group:		System/Kernel and hardware
Url:		http://v4l2ucp.sourceforge.net/
Source0:	http://downloads.sourceforge.net/project/v4l2ucp/v4l2ucp/2.0/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	libv4l-devel
BuildRequires:	qt4-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
It reads a description of the controls that the V4L2 device 
supports from the device, and presents the user with a graphical 
means for adjusting those controls. It allows for controlling 
multiple devices. Controls can be updated with the device status 
either manually, or periodically. There is an easy way to reset 
one or all the controls to their default state

%prep
%setup -q %{name}-%{version}

%build
%cmake

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

pushd build
%makeinstall_std
popd

%find_lang %{name}

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%doc README TODO
%{_bindir}/v4l2*
%{_datadir}/applications/*.desktop
%{_datadir}/icons/*.png
