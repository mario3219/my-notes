```
\documentclass[12pt]{article}
\usepackage[english]{babel}
\usepackage{amsmath}
\usepackage{array}
\usepackage{caption}
\usepackage{comment}
\usepackage{commath}
\usepackage{eufrak}
\usepackage{floatrow}
\usepackage{amsmath, amssymb}
\floatsetup[figure]{capposition=bottom}
\floatsetup[table]{capposition=top}
\usepackage{fullpage}
\usepackage{geometry}
\usepackage{graphicx}
\usepackage{hyperref}
\usepackage{layout}
\usepackage{mwe}
\usepackage{physics}
\usepackage{subcaption}
\usepackage[table]{xcolor}
\usepackage{upgreek}
\setcounter{secnumdepth}{3}
\usepackage{array}

\geometry{
    a4paper,
    left=20mm,
    right=20mm,
    top =20mm,
}

\setlength\parindent{0em}
\setlength\parskip{0em}

\begin{document}

\begin{titlepage}
\newcommand{\HRule}{\rule{\linewidth}{0.5mm}}
\newcommand{\un}[1]{\ensuremath{\ \mathrm{#1}}}
\newcommand{\ex}[1]{\ensuremath{\times10^{#1}}}
\center
\textsc{\LARGE BMEN01 - Biomedical Signal Processing}\\[2cm]
\HRule\\[1.0cm]
{\huge\bfseries AF Detector Project}\\[0.4cm]
\HRule\\[1.5cm]
\begin{minipage}{0.4\textwidth}
\begin{flushleft}
\large
\textit{Authors}\\
\textsc{Jonathan Olsson}\\
\textsc{Ossian Erixon}\\
\end{flushleft}
\end{minipage}
\begin{minipage}{0.4\textwidth}
\begin{flushright}
\large
\textit{Supervisor}\\
\textsc{Martin Stridh}\\
\end{flushright}
\end{minipage}
 \vfill\vfill\vfill\vfill
\includegraphics[width=0.8\textwidth]{Lund.png}
\vfill\vfill\vfill
{Turned in: 20/5-25}
\vfill
\end{titlepage}

\renewcommand{\contentsname}{Table of contents}
\tableofcontents
\newpage

\end{document}
```