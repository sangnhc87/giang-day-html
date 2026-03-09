#!/usr/bin/env bash
set -euo pipefail

export DEBIAN_FRONTEND=noninteractive

sudo apt-get update
sudo apt-get install -y \
  latexmk \
  lmodern \
  texlive-fonts-recommended \
  texlive-lang-other \
  texlive-latex-base \
  texlive-latex-extra \
  texlive-latex-recommended \
  texlive-pictures \
  texlive-xetex

echo "Installed LaTeX toolchain:"
command -v pdflatex
command -v xelatex
command -v latexmk
kpsewhich extbook.cls || true