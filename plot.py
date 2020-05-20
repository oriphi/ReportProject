import matplotlib.pyplot  as plt
import numpy as np


MIN = 0.1


# Application intensity
for i in 1/6 * np.array([15,20,25]):
    X4 = np.array([i,i])
    Y4 = np.array([MIN,8])
    plt.loglog(X4,Y4,color='lightgrey',linestyle='dashed')

# Bandwidth limitation
X1 = np.array([MIN / 4,2, 100])
Y1 = np.array([MIN,8,8])
plt.loglog(X1,Y1,color='tab:blue')


X3 =np.array([0, 2])
Y3 =np.array([8, 8])
plt.loglog(X3,Y3,color='tab:blue',linestyle='dotted')


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
    'palegreen' ,
    'mediumseagreen',
    'turquoise',
    'lightblue',]

### Benchmarks
Bench15 = [ 40628 , 6950  ,  4339,   39820, 12079,12985,13036]
Bench20 = [ 93818 , 15585 ,  8358,   92650, 24750,23318,25596]
Bench25 = [180686 , 30413 , 15585,  179030, 38090,39568,39415]

Bench30 = [309426 , 42659  , 18776,  307210, 59887,61701,61635]
Bench35 = [488316 , 71279  , 32295,  485440, 89283,91754,61682]
Bench40 = [725606 , 92536  , 36487 ,721970,126523,129668,129413]

BenchList = [Bench15,Bench20,Bench25,Bench30,Bench35,Bench40]
Factors = [15,20,25,30,35,40]
firstPlot = True
for j,B in enumerate(BenchList):
    F = Factors[j]
    N = 2 * F ** 3
    X4 = np.array([F/6,F/6])
    Y4 = np.array([MIN,8])
    plt.loglog(X4,Y4,color='lightgrey',linestyle='dashed')

    for i,b in enumerate(B):
        X = np.array([F / 6])
        tmp = N / b
        Y = np.array([tmp])
        if firstPlot:
            plt.loglog(X,Y, marker = 'x',label=LegendLabels[i],color = LegendColors[i])
        else:
            plt.loglog(X,Y, marker = 'x',color = LegendColors[i])
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
#plt.grid()

#plt.show()

plt.figure()
firstplot = True
for b in range(len(BenchList)):
    plt.subplot(2,4,1 + b)
    plt.grid(linestyle='dashed', color='lightgrey',axis='y')
    F = Factors[b]
    N = 2 * F ** 3
    B = N / np.array(BenchList[b])
    B = B / B[0]
    for i in range(len(B)):
        plt.bar([i],[B[i]],label = LegendLabels[i],color = LegendColors[i])
    plt.xlabel("Matrix Size {}".format(F))
    plt.yticks([1] + [2 *i for i in range(1,11)])

ax = plt.subplot(246)
ax.legend(loc='center left', bbox_to_anchor = (2, 0.5))
#plt.legend(LegendLabels)
plt.show()

