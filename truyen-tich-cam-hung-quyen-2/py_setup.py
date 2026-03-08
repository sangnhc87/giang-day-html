import os

main_tex = r"""%============================================================
% TRUYỆN SONG NGỮ QUYỂN 2 - ĐẠO LÀM NGƯỜI
%============================================================
\documentclass[13pt,a4paper,twoside]{book}

\usepackage{extsizes}
\usepackage[utf8]{inputenc}
\usepackage[vietnamese]{babel}
\usepackage{amsmath,amssymb}
\usepackage{mathpazo} 
\usepackage{xcolor}
\usepackage{graphicx}
\usepackage{geometry}
\usepackage{fancyhdr}
\usepackage{titlesec}
\usepackage{tocloft}
\usepackage{microtype}
\usepackage{tcolorbox}
\tcbuselibrary{skins,breakable}
\usepackage{enumitem}
\usepackage{lettrine}
\usepackage{parskip}
\usepackage{afterpage}
\usepackage{tikz}
\usetikzlibrary{calc,shapes.geometric}

\geometry{
  a4paper,
  left=2.5cm,
  right=2.5cm,
  top=3cm,
  bottom=3cm,
  headheight=15pt
}

\definecolor{truyenblue}{RGB}{20, 60, 120}    
\definecolor{truyenred}{RGB}{160, 30, 30}     
\definecolor{truyengold}{RGB}{180, 130, 40}   
\definecolor{boxbg}{RGB}{250, 248, 240}       

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE,RO]{\color{truyenblue}\itshape\small Quyển II: Đạo Làm Người \& Đối Nhân Xử Thế}
\fancyhead[RE,LO]{\color{truyenred}\itshape\small \leftmark}
\fancyfoot[C]{\color{truyengold}\textbf{-- \thepage\ --}}
\renewcommand{\headrulewidth}{0.6pt}
\renewcommand{\headrule}{\hbox to\headwidth{\color{truyengold}\leaders\hrule height \headrulewidth\hfill}}
\renewcommand{\footrulewidth}{0pt}

\titleformat{\chapter}[display]
  {\normalfont\bfseries\color{truyenred}\centering}
  {\large\itshape Chương \thechapter}
  {1ex}
  {\Huge\scshape}[\vspace{1ex}{\color{truyengold}\rule{0.5\textwidth}{1pt}}]
\titlespacing*{\chapter}{0pt}{-20pt}{40pt}

\titleformat{\section}
  {\color{truyenblue}\Large\bfseries}
  {\thesection.}
  {1em}
  {}
\titlespacing*{\section}{0pt}{3ex plus 1ex minus .2ex}{2ex plus .2ex}

\newtcolorbox{truyen}[2]{
  colback=boxbg,
  colframe=truyenblue,
  coltitle=white,
  fonttitle=\bfseries\large,
  title={#1 \hfill \small\itshape #2},
  arc=5pt,
  boxrule=1.2pt,
  breakable,
  enhanced,
  drop shadow=black!15
}

\newtcolorbox{baihoc}{
  colback=truyenred!5,
  colframe=truyenred,
  title={\bfseries BÀI HỌC RÚT RA (Lesson Learned)},
  fonttitle=\bfseries,
  coltitle=white,
  arc=3pt,
  boxrule=1pt,
  left=10pt, right=10pt, top=10pt, bottom=10pt,
  breakable
}

\newcommand{\ngancach}{
  \vspace{0.4cm}
  \begin{center}
    {\color{truyengold}\rule{4cm}{0.5pt} \small $\diamond$ \rule{4cm}{0.5pt}}
  \end{center}
  \vspace{0.4cm}
}

\newcommand{\chuhoa}[2]{%
  \lettrine[lines=2, lhang=0.1, nindent=0em, findent=0.5em]%
  {\color{truyenred}\textbf{#1}}{#2}%
}

\newcommand{\ngayDay}{
  \begin{flushright}
  \small\itshape\color{gray} Ngày \dots\dots tháng \dots\dots năm \dots\dots
  \end{flushright}
  \vspace{-0.5cm}
}

\begin{document}

\include{cover}

\cleardoublepage
\begingroup
  \renewcommand{\contentsname}{\centering\color{truyenred}Mục Lục}
  \tableofcontents
\end{group}

\cleardoublepage

\include{chapters/ch01-dao-lam-con}

\end{document}
"""

ch1_tex = r"""%============================================================
% CHƯƠNG 1: ĐẠO LÀM CON
%============================================================
\chapter{Đạo Làm Con (Filial Piety)}

\begin{center}
  \textit{\color{truyenblue}``A father's goodness is higher than the mountain, a mother's goodness deeper than the sea.''}\\
  \textit{(Công cha như núi Thái Sơn, Nghĩa mẹ như nước trong nguồn chảy ra.)}\\[4pt]
  \small\color{truyengold}--- Tục ngữ Việt Nam ---
\end{center}

\ngancach

\begin{tcolorbox}[
  colback=truyenred!5, colframe=truyenred!40, arc=6pt,
  title={\bfseries Chữ Hiếu Vi Tiên (Filial Piety Comes First)},
  fonttitle=\bfseries\color{truyenred}
]
  \textbf{Of all virtues}, \textbf{filial piety is the most important}. We must always \textbf{respect and care for our parents} who gave us life and love.\\
  \textit{(Trong trăm cội nguồn đạo đức của con người, chữ Hiếu luôn được đặt lên hàng đầu. Chúng ta phải luôn tôn kính và phụng dưỡng mẹ cha, những người đã ban cho ta sinh mệnh và tình yêu thương vô bờ bến.)}
\end{tcolorbox}

\vspace{0.6cm}

%------------------------------------------------------------
\ngayDay{}
\section{Bát Mì Của Mẹ}
\begin{truyen}{Bát Mì Tình Thương}{Sự Biết Ơn}
\chuhoa{O}{ } \textbf{ne evening}, a young girl \textbf{argued fiercely with her mother} and \textbf{ran away from home}.\\
\textit{(Vào một buổi tối nọ, một cô gái trẻ đã cãi vã vô cùng gay gắt với mẹ mình và bỏ nhà bỏ cửa chạy trốn đi.)}

She \textbf{wandered the streets} feeling \textbf{exhausted and extremely hungry}.\\
\textit{(Cô cứ lang thang thất thểu dọc khắp mấy con phố trong trạng thái kiệt sức rã rời và đói cồn cào lả người đi.)}

She \textbf{arrived at a noodle stall}, but she \textbf{had no money} with her.\\
\textit{(Cô mò mẫm tới được một quầy bán mì nhỏ, ngặt nỗi lại chẳng còn một xu dính túi.)}

The kind stall owner \textbf{saw her crying} and \textbf{gave her a warm bowl of noodles} for free.\\
\textit{(Người chủ quán tốt bụng thấy cô đứng khóc rưng rức đành thương tình nấu tặng bát mì nóng bốc khói nghi ngút miễn phí.)}

The girl \textbf{thanked him profusely}, saying he was \textbf{kinder than her own mother}.\\
\textit{(Cô gái trẻ liền cảm ơn chú rối rít tuôn rơi nước mắt, và thốt lên rằng ông chú này còn tốt bụng tuyệt vời hơn cả chính người mẹ ruột rà mẹ đẻ của mình.)}

The owner \textbf{shook his head gently} and replied: \textit{"I only \textbf{gave you one bowl }, and you are \textbf{so grateful}."}\\
\textit{(Nhưng ông chủ quán khẽ từ từ lắc đầu và ôn tồn đáp lại: "Ta đây chỉ mớm cho cháu một tô mì còm, vậy mà cháu đã mừng rỡ biết ơn đến tận tâm can.")}

\textit{"Your mother has \textbf{cooked meals for you for twenty years}. Have you \textbf{ever thanked her}?"}\\
\textit{("Thế còn mẹ ruột của cháu đã miệt mài nấu nướng bao vây bữa cơm đút cho cháu ăn mòn ròng rã suốt hai mươi năm trời đằng đẵng. Cháu đã bao giờ thốt mở lời để nói tiếng cảm ơn bà ấy chưa?")}

The girl \textbf{burst into tears} and immediately \textbf{ran all the way back home}.\\
\textit{(Cô gái trẻ chết sững oà khóc nức nở như mưa và tức tốc quay cuồng cắm đầu cắm cổ cắm chạt cắm sải chạy vọt bay vút bay lượn miết về nhà.)}
\end{truyen}

\begin{baihoc}
  \textbf{We often take our parents' sacrifices for granted}.\\
  \textit{(Đôi khi chúng ta vô tâm và nghiễm nhiên coi sự hy sinh của cha mẹ là điều hiển nhiên phải thế.)}\\
  \textbf{Always be grateful} to the ones who \textbf{love you unconditionally}.\\
  \textit{(Hãy luôn học cách khắc cốt ghi tâm biết ơn sâu sắc đến những người đã và đang yêu thương bạn vô điều kiện.)}
\end{baihoc}

\vspace{0.8cm}
"""

with open("main.tex", "w") as f: f.write(main_tex)
with open("chapters/ch01-dao-lam-con.tex", "w") as f: f.write(ch1_tex)

with open("cover.tex", "r") as f: cover = f.read()
cover = cover.replace("QUYỂN I", "QUYỂN II")
cover = cover.replace("Tủ Sách Song Ngữ Việt - Anh", "Đạo Làm Người & Đối Nhân Xử Thế")
with open("cover.tex", "w") as f: f.write(cover)

