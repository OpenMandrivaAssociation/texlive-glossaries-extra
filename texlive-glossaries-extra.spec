%global tl_name glossaries-extra
%global tl_revision 78801

Name:		texlive-%{tl_name}
Epoch:		1
Version:	2.1
Release:	%{tl_revision}.1
Summary:	An extension to the glossaries package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/glossaries-extra
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-extra.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-extra.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/glossaries-extra.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(glossaries)
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides improvements and extra features to the glossaries
package. Some of the default glossaries.sty behaviour is changed by
glossaries-extra.sty. See the user manual glossaries-extra-manual.pdf
for further details. glossaries-extra.sty requires the glossaries
package and, naturally, all packages required by glossaries.sty.

