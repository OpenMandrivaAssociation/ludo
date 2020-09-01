
Name:		ludo
Version:	0.11.2
Release:	1
License:	GPLv3+
Group:		Emulators
Summary:	A libretro frontend written in golang 
Url:		https://ludo.libretro.com/
Source0:	https://github.com/libretro/ludo/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires: golang
BuildRequires: pkgconfig(openal)
BuildRequires: pkgconfig(glfw3)
BuildRequires: pkgconfig(dri)
BuildRequires: pkgconfig(opengl)
BuildRequires: pkgconfig(libdrm)

%description
Ludo is a work in progress libretro frontend written in go.
It is able to launch most non GL libretro cores.
It works on OSX, Linux, Linux ARM and Windows. 

%prep
%autosetup -p1

%build
go build

#make_build

%install
%make_install

%files
