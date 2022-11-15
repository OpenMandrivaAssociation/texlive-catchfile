Name:		texlive-catchfile
Version:	53084
Release:	1
Summary:	Catch an external file into a macro
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/catchfile
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfile.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfile.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/catchfile.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package catches the contents of a file and puts it in a
macro. It requires e-TeX. Both LaTeX and plain TeX are
supported.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/catchfile
%{_texmfdistdir}/tex/generic/catchfile
%doc %{_texmfdistdir}/doc/latex/catchfile

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
