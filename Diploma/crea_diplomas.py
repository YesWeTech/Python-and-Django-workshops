from subprocess import run

with open('asistentes.txt','r') as f:
    asistentes = [line[:-1] for line in f.readlines()]

for asistente in asistentes:
    file = 'diploma_{}.tex'.format(asistente)
    with open(file, 'w') as f:
        f.write("\\documentclass[landscape]{article}\n")
        f.write("\\usepackage{wallpaper}\n")
        f.write("\\usepackage{niceframe}\n")
        f.write("\\usepackage{xcolor}\n")
        f.write("\\usepackage{ulem}\n")
        f.write("\\usepackage{graphicx}\n")
        f.write("\\usepackage{geometry}\n")
        f.write("\\geometry{tmargin=.5cm,bmargin=.5cm,\n")
        f.write("lmargin=.5cm,rmargin=.5cm}\n")
        f.write("\\usepackage{multicol}\n")
        f.write("\\setlength{\\columnseprule}{0.4pt}\n")
        f.write("\\columnwidth=0.3\\textwidth\n\n")

        f.write("\\begin{document}\n\n")

        f.write("\\centering\n")
        f.write("\\scalebox{3}{\\color{blue!30!black!60}\n")
        f.write("\\begin{minipage}{.33\\textwidth}\n")
        f.write("\\font\\border=umrandb\n")
        f.write("\\generalframe\n")
        f.write("{\\border \\char113} % up left\n")
        f.write("{\\border \\char109} % up\n")
        f.write("{\\border \\char112} % up right\n")
        f.write("{\\border \\char108} % left \n")
        f.write("{\\border \\char110} % right\n")
        f.write("{\\border \\char114} % lower left\n")
        f.write("{\\border \\char111} % bottom\n")
        f.write("{\\border \\char115} % lower right\n")
        f.write("{\\centering\n\n")

        f.write("\\vspace{3mm}\n\n")

        f.write("\\curlyframe[.9\\columnwidth]{\n\n")

        f.write("\\textcolor{red!10!black!90}\n")
        f.write("{\\small Geek \\& Tech Girls}\\\\ \n")
        f.write("\\textcolor{blue!10!black!90}{\n")
        f.write("\\tiny Granada}\n\n")

        f.write("\\smallskip\n\n")

        f.write("\\textcolor{purple!30!black!90}\n")
        f.write("{\\textit{Diploma de}}\n\n")

        f.write("\\textcolor{black}{\\large \\textsc{Asistencia al taller \"Women in Django\"}}\n\n")

        f.write("\\vspace{2mm}\n\n")

        f.write("\\tiny\n")
        f.write("Para: \\uline{\\textcolor{black}\n")
        f.write("{")
        f.write(asistente)
        f.write("}}\n\n")
        f.write("\\vspace{10mm}\n\n")

        f.write("\\textcolor{black}{17 de Febrero de 2017}\n\n")

        f.write("}}\n")
        f.write("\\end{minipage}\n")
        f.write("}\n\n")

        f.write("\\end{document}\n")

    run(["pdflatex", file])
