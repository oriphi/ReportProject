import matplotlib.pyplot  as plt
import numpy as np
import matplotlib


MIN = 0.5

#matplotlib.use("pgf")
#matplotlib.rcParams.update({
#    "pgf.texsystem": "pdflatex",
#    'font.family': 'serif',
#    'text.usetex': True,
#    'pgf.rcfonts': False,
#    'figure.figsize': [8,4]
#})

Bench15 = [ 40628 , 6950  ,  4339,   39820, 12079,12985,13036]
Bench20 = [ 93818 , 15585 ,  8358,   92650, 24750,23318,25596]
Bench25 = [180686 , 30413 , 15585,  179030, 38090,39568,39415]

Bench30 = [309426 , 42659  , 18776,  307210, 59887,61701,61635]
Bench35 = [488316 , 71279  , 32295,  485440, 89283,91754,61682]
Bench40 = [725606 , 92536  , 36487 ,721970,126523,129668,129413]

Items = [0,1,2]

LegendLabels = [
    "Halide: No Schedule"          ,
    "Halide: Parallel"             ,
    "Halide: Parallel + Vectorize" ,
    "OpenMp: Single Thread"        ,
    "OpenMp: Parallel No DMA "     ,
    "OpenMp: Parallel DMA "        ,
    "OpenMp: Parallel DMA SVM "
    ]
LegendColors = [
    'salmon',
    'darkorange',
    'royalblue' ,
    'purple' ,
    'mediumseagreen',
    'turquoise',
    'lightblue',]

### Benchmarks

BenchList = [Bench15,Bench20,Bench25,Bench30,Bench35,Bench40]
MarkerList = ["x","x","x","1","1","1","1"]
Factors = [15,20,25,30,35,40]

def genTable(b,e):
    header = """
\\begin{table}[ht]
\\begin{center}
\\begin{tabular}{|c||""" + len(BenchList[b:e]) *"c|" +  "}\n\\hline\n"
    footer="""
\end{tabular}
\end{center}
\end{table}
"""
    res = header
    l = "Schedule"
    for f in Factors[b:e]:
        l += "& {}x{}".format(f,f)
    hl = "\\hline"
    endline= "\\\\ \n"  +hl + "\n"
    res += l
    res += endline + hl+"\n"
    for s in Items:
        l = LegendLabels[s]
        for k,be in enumerate(BenchList[b:e]):
            F = 2 * Factors[b + k] ** 3
            l += "& {} ({})".format(be[s], round(F / be[s],3))
        l += endline
        res += l
    res += footer
    print(res)


def plotFunctions():
    FIG1 = 'RooflineHalideOpenMp.pgf'
    FIG2 = 'BarplotHalideOpenMp.pgf'
    # Bandwidth limitation
    plt.figure(figsize=(8,4))
    X1 = np.array([MIN / 4,2, 20])
    Y1 = np.array([MIN,8,8])
    plt.loglog(X1,Y1,color='tab:blue',zorder=10)
    plt.grid(zorder=0,linestyle="dashed",color="lightgrey")


    X3 =np.array([0, 2])
    Y3 =np.array([8, 8])
    plt.loglog(X3,Y3,color='tab:blue',linestyle='dotted',zorder=10)
    plt.yscale('log',basey=2)
    plt.xscale('log',basex=2)



    firstPlot = True
    for j,B in enumerate(BenchList):
        F = Factors[j]
        N = 2 * F ** 3
        X4 = np.array([F/6,F/6])
        Y4 = np.array([MIN,8])

        # Select the Items in the benchmark list
        for i in Items:
            b = B[i]
            X = np.array([F / 6])
            tmp = N / b
            Y = np.array([tmp])
            if firstPlot:
                plt.loglog(X,Y, MarkerList[i],label=LegendLabels[i],color = LegendColors[i],zorder=3,mfc= None)
            else:
                plt.loglog(X,Y, MarkerList[i],color = LegendColors[i],zorder=3, mfc=None)
        firstPlot = False

    plt.xlabel("Computing Intensity (Operations / Byte)")
    plt.ylabel("Performance (Operations / Cycle)")

    xLabels = np.array(["$\\frac{1}{4}$",
        "$2$",
        "$\\frac{15}{6}$",
        "$\\frac{20}{6}$",
        "$\\frac{25}{6}$",
        "$\\frac{30}{6}$",
        "$\\frac{35}{6}$",
        "$\\frac{40}{6}$",
        ])
    xLabelsCoord = np.array([1 / 4, 2, 15 / 6, 20 / 6, 25 / 6,30 / 6,35/6,40/6])
    plt.xticks(xLabelsCoord,xLabels)

    yLabels = np.array(["$0.1$",
        "$1$",
        "$2$",
        "$4$",
        "$8$"])
    yLabelsCoord = np.array([0.1,1, 2, 4,8])
    plt.yticks(yLabelsCoord,yLabels)
    plt.legend()
    plt.tight_layout()


    plt.show()
    #plt.savefig(FIG1)
    plt.figure(figsize=(8,6))

    firstplot = True
    for b in range(len(BenchList)):
        plt.subplot(3,3,1 + b)
        plt.grid(linestyle='dashed', color='lightgrey',axis='y',zorder=0)
        F = Factors[b]
        N = 2 * F ** 3
        B = N / np.array(BenchList[b])
        B = B / B[Items[0]]
        for i in Items:
            plt.bar([i],[B[i]],label = LegendLabels[i],color = LegendColors[i],zorder=3)
        plt.xlabel("Matrix Size {}".format(F))
        plt.yticks([1] + [4 *i for i in range(1,6)])
        plt.tick_params(
            axis='x',          # changes apply to the x-axis
            which='both',      # both major and minor ticks are affected
            bottom=False,      # ticks along the bottom edge are off
            top=False,         # ticks along the top edge are off
            labelbottom=False) # labels along the bottom edge are off

    ax = plt.subplot(335)
    ax.legend(loc='center', bbox_to_anchor=(.5,-1))
    #plt.legend(LegendLabels)

    #plt.savefig(FIG2)
    plt.show()

#genTable(0,3)
#genTable(3,6)
plotFunctions()
