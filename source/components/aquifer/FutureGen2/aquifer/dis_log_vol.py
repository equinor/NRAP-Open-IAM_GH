'''
output: dis_log_vol
prediction score: 0.930652576654232
Forward Pass
-----------------------------------------------------------------
iter  parent  var  knot  mse        terms  gcv     rsq    grsq
-----------------------------------------------------------------
0     -       -    -     31.026929  1      31.039  0.000  0.000
1     0       9    4973  9.508113   3      9.531   0.694  0.693
2     0       10   148   5.224519   5      5.248   0.832  0.831
3     1       10   1183  3.345477   7      3.367   0.892  0.892
4     1       9    4507  2.779360   9      2.803   0.910  0.910
5     4       9    3383  2.596840   11     2.624   0.916  0.915
6     0       2    -1    2.410966   12     2.439   0.922  0.921
7     1       3    -1    2.328917   13     2.358   0.925  0.924
8     4       10   848   2.290979   15     2.324   0.926  0.925
9     0       8    -1    2.248445   16     2.283   0.928  0.926
10    3       4    -1    2.223775   17     2.261   0.928  0.927
-----------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
------------------------------------------------
iter  bf  terms  mse    gcv     rsq     grsq
------------------------------------------------
0     -   17     2.22   2.261   0.928   0.927
1     8   16     2.23   2.260   0.928   0.927
2     4   15     2.23   2.263   0.928   0.927
3     2   14     2.25   2.276   0.928   0.927
4     16  13     2.27   2.299   0.927   0.926
5     13  12     2.30   2.330   0.926   0.925
6     14  11     2.32   2.347   0.925   0.924
7     9   10     2.35   2.374   0.924   0.924
8     6   9      2.36   2.376   0.924   0.923
9     15  8      2.40   2.414   0.923   0.922
10    12  7      2.48   2.491   0.920   0.920
11    11  6      2.66   2.679   0.914   0.914
12    7   5      3.33   3.343   0.893   0.892
13    5   4      4.85   4.872   0.844   0.843
14    10  3      7.75   7.767   0.750   0.750
15    3   2      12.84  12.862  0.586   0.586
16    1   1      31.03  31.039  -0.000  -0.000
------------------------------------------------
Selected iteration: 1

Earth Model
--------------------------------------------------------------------------
Basis Function                                       Pruned  Coefficient
--------------------------------------------------------------------------
(Intercept)                                          No      9.22457
h(log_co2_mass-0.189813)                             No      0.58933
h(0.189813-log_co2_mass)                             No      9.24033
h(log_brine_mass-14.6024)                            No      1.18229
h(14.6024-log_brine_mass)                            No      -0.0643847
h(log_brine_mass-14.0687)*h(log_co2_mass-0.189813)   No      -0.0521915
h(14.0687-log_brine_mass)*h(log_co2_mass-0.189813)   No      -0.15175
h(log_co2_mass-8.60268)*h(log_co2_mass-0.189813)     No      0.0207117
h(8.60268-log_co2_mass)*h(log_co2_mass-0.189813)     Yes     None
h(log_co2_mass-1.27872)*h(14.6024-log_brine_mass)    No      0.153689
h(1.27872-log_co2_mass)*h(14.6024-log_brine_mass)    No      -0.594912
por                                                  No      -8.35707
log_permh*h(log_co2_mass-0.189813)                   No      0.026922
h(log_brine_mass-8.68598)*h(14.6024-log_brine_mass)  No      -0.0812579
h(8.68598-log_brine_mass)*h(14.6024-log_brine_mass)  No      0.0154682
time                                                 No      0.0101684
log_aniso*h(log_brine_mass-14.6024)                  No      0.0549998
--------------------------------------------------------------------------
MSE: 2.2255, GCV: 2.2602, RSQ: 0.9283, GRSQ: 0.9272
parameters:
X[ 0 ] =  thick
X[ 1 ] =  depth
X[ 2 ] =  por
X[ 3 ] =  log_permh
X[ 4 ] =  log_aniso
X[ 5 ] =  rel_vol_frac_calcite
X[ 6 ] =  log_co2_rate
X[ 7 ] =  log_brine_rate
X[ 8 ] =  time
X[ 9 ] =  log_co2_mass
X[ 10 ] =  log_brine_mass
'''
def model(example_iterator):
    accessors = [
        lambda x: 9.2245729391476,
        lambda x: 0.5893304431315437 * max(0, x[9] - 0.18981344396428737),
        lambda x: 9.240329511152868 * max(0, 0.18981344396428737 - x[9]),
        lambda x: 1.1822894459353699 * max(0, x[10] - 14.602404871780717),
        lambda x: -0.06438465847756836 * max(0, 14.602404871780717 - x[10]),
        lambda x: -0.05219150926857284 * max(0, x[10] - 14.068749877366354) *\
            max(0, x[9] - 0.18981344396428737),
        lambda x: -0.15175025571070014 * max(0, 14.068749877366354 - x[10]) *\
            max(0, x[9] - 0.18981344396428737),
        lambda x: 0.0207117245316992 * max(0, x[9] - 8.602675723493846) *\
            max(0, x[9] - 0.18981344396428737),
        lambda x: 0.1536889873960273 * max(0, x[9] - 1.2787222498572224) *\
            max(0, 14.602404871780717 - x[10]),
        lambda x: -0.5949118242221657 * max(0, 1.2787222498572224 - x[9]) *\
            max(0, 14.602404871780717 - x[10]),
        lambda x: -8.357073108005922 * x[2],
        lambda x: 0.02692199727215311 * x[3] * max(0, x[9] - 0.18981344396428737),
        lambda x: -0.08125789676363811 * max(0, x[10] - 8.685976173003596) *\
            max(0, 14.602404871780717 - x[10]),
        lambda x: 0.015468201084986824 * max(0, 8.685976173003596 - x[10]) *\
            max(0, 14.602404871780717 - x[10]),
        lambda x: 0.010168356287131461 * x[8],
        lambda x: 0.05499979288714904 * x[4] * max(0, x[10] - 14.602404871780717)]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
