Name:		texlive-glossaries-extra
Version:	64973
Release:	1
Summary:	An extension to the glossaries package
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-extra
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-extra.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-extra.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-extra.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package provides improvements and extra features to the
glossaries package. Some of the default glossaries.sty
behaviour is changed by glossaries-extra.sty. See the user
manual glossaries-extra-manual.pdf for further details.
glossaries-extra.sty requires the glossaries package and,
naturally, all packages required by glossaries.sty.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/glossaries-extra
%{_texmfdistdir}/tex/latex/glossaries-extra
%{_texmfdistdir}/bibtex/bib/glossaries-extra
%doc %{_texmfdistdir}/doc/latex/glossaries-extra

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
