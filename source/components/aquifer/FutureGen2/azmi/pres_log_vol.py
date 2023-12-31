'''
output: pres_log_vol
prediction score: 0.897645930466075
Forward Pass
-------------------------------------------------------------------
iter  parent  var  knot  mse         terms  gcv      rsq    grsq
-------------------------------------------------------------------
0     -       -    -     140.865274  1      140.917  0.000  0.000
1     0       10   5232  76.375774   3      76.545   0.458  0.457
2     0       9    1496  37.536298   5      37.689   0.734  0.733
3     3       10   3341  25.950260   7      26.104   0.816  0.815
4     0       3    -1    21.193083   8      21.339   0.850  0.849
5     7       9    4595  19.816068   10     19.989   0.859  0.858
6     7       8    -1    18.494933   11     18.674   0.869  0.867
7     4       10   1490  17.511489   13     17.714   0.876  0.874
8     7       10   1608  16.696468   15     16.921   0.881  0.880
9     3       9    440   15.985440   17     16.230   0.887  0.885
10    7       9    1117  15.367823   19     15.632   0.891  0.889
11    2       9    5402  14.906787   21     15.192   0.894  0.892
12    7       10   3738  14.411969   23     14.715   0.898  0.896
13    3       1    -1    14.154899   24     14.466   0.900  0.897
14    0       10   4005  13.914582   26     14.247   0.901  0.899
15    0       9    4283  13.735295   28     14.090   0.902  0.900
16    4       8    -1    13.569728   29     13.933   0.904  0.901
17    7       9    3664  13.451528   31     13.837   0.905  0.902
-------------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
--------------------------------------------------
iter  bf  terms  mse     gcv      rsq     grsq
--------------------------------------------------
0     -   31     13.46   13.843   0.904   0.902
1     25  30     13.46   13.830   0.904   0.902
2     22  29     13.46   13.817   0.904   0.902
3     7   28     13.46   13.804   0.904   0.902
4     18  27     13.45   13.783   0.905   0.902
5     12  26     13.45   13.770   0.905   0.902
6     4   25     13.46   13.765   0.904   0.902
7     13  24     13.46   13.752   0.904   0.902
8     15  23     13.50   13.781   0.904   0.902
9     3   22     13.55   13.823   0.904   0.902
10    11  21     13.64   13.903   0.903   0.901
11    20  20     13.72   13.971   0.903   0.901
12    23  19     13.89   14.130   0.901   0.900
13    28  18     14.18   14.411   0.899   0.898
14    24  17     14.56   14.786   0.897   0.895
15    2   16     14.95   15.165   0.894   0.892
16    14  15     15.13   15.336   0.893   0.891
17    16  14     15.62   15.811   0.889   0.888
18    26  13     16.58   16.773   0.882   0.881
19    27  12     17.24   17.423   0.878   0.876
20    17  11     17.75   17.924   0.874   0.873
21    19  10     18.83   18.998   0.866   0.865
22    21  9      19.62   19.769   0.861   0.860
23    6   8      20.51   20.651   0.854   0.853
24    10  7      21.69   21.822   0.846   0.845
25    29  6      23.86   23.980   0.831   0.830
26    9   5      24.90   25.003   0.823   0.823
27    30  4      25.50   25.580   0.819   0.818
28    5   3      35.89   35.966   0.745   0.745
29    8   2      76.94   77.039   0.454   0.453
30    1   1      140.87  140.917  -0.000  -0.000
--------------------------------------------------
Selected iteration: 7

Earth Model
------------------------------------------------------------------------
Basis Function                                     Pruned  Coefficient
------------------------------------------------------------------------
(Intercept)                                        No      -72.6101
h(log_brine_mass-15.1684)                          No      4.238
h(15.1684-log_brine_mass)                          No      2.26003
h(log_co2_mass-13.0076)                            No      2.27825
h(13.0076-log_co2_mass)                            Yes     None
h(log_brine_mass-17.1572)*h(log_co2_mass-13.0076)  No      -0.297849
h(17.1572-log_brine_mass)*h(log_co2_mass-13.0076)  No      0.608334
log_permh                                          Yes     None
h(log_co2_mass-12.6919)*log_permh                  No      -1.63326
h(12.6919-log_co2_mass)*log_permh                  No      1.44917
time*log_permh                                     No      0.00558957
h(log_brine_mass-22.5364)*h(13.0076-log_co2_mass)  No      -0.270774
h(22.5364-log_brine_mass)*h(13.0076-log_co2_mass)  Yes     None
h(log_brine_mass-15.0858)*log_permh                Yes     None
h(15.0858-log_brine_mass)*log_permh                No      0.177705
h(log_co2_mass-21.0521)*h(log_co2_mass-13.0076)    No      0.908362
h(21.0521-log_co2_mass)*h(log_co2_mass-13.0076)    No      -0.572974
h(log_co2_mass-21.2116)*log_permh                  No      3.30045
h(21.2116-log_co2_mass)*log_permh                  Yes     None
h(log_co2_mass-13.2453)*h(15.1684-log_brine_mass)  No      -0.625258
h(13.2453-log_co2_mass)*h(15.1684-log_brine_mass)  No      -0.015745
h(log_brine_mass-21.2709)*log_permh                No      1.7215
h(21.2709-log_brine_mass)*log_permh                Yes     None
depth*h(log_co2_mass-13.0076)                      No      0.000557177
h(log_brine_mass-21.2134)                          No      18.5832
h(21.2134-log_brine_mass)                          Yes     None
h(log_co2_mass-21.2605)                            No      28.1978
h(21.2605-log_co2_mass)                            No      2.2067
time*h(13.0076-log_co2_mass)                       No      0.0043999
h(log_co2_mass-16.1567)*log_permh                  No      1.50506
h(16.1567-log_co2_mass)*log_permh                  No      -1.27634
------------------------------------------------------------------------
MSE: 13.4567, GCV: 13.7523, RSQ: 0.9045, GRSQ: 0.9024
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
        lambda x: -72.61012938688043,
        lambda x: 4.238000729844602 * max(0, x[10] - 15.168375533662203),
        lambda x: 2.2600264092983395 * max(0, 15.168375533662203 - x[10]),
        lambda x: 2.278247234241819 * max(0, x[9] - 13.007550699130583),
        lambda x: -0.29784886172270014 * max(0, x[10] - 17.15717894035357) *\
            max(0, x[9] - 13.007550699130583),
        lambda x: 0.6083340352975181 * max(0, 17.15717894035357 - x[10]) *\
            max(0, x[9] - 13.007550699130583),
        lambda x: -1.6332636281400623 * max(0, x[9] - 12.691906359778656) * x[3],
        lambda x: 1.4491688274537848 * max(0, 12.691906359778656 - x[9]) * x[3],
        lambda x: 0.005589566034760907 * x[8] * x[3],
        lambda x: -0.2707736915361451 * max(0, x[10] - 22.536443700926455) *\
            max(0, 13.007550699130583 - x[9]),
        lambda x: 0.1777052227129866 * max(0, 15.085799178984193 - x[10]) * x[3],
        lambda x: 0.9083618980278267 * max(0, x[9] - 21.05214080475075) *\
            max(0, x[9] - 13.007550699130583),
        lambda x: -0.5729738881612549 * max(0, 21.05214080475075 - x[9]) *\
            max(0, x[9] - 13.007550699130583),
        lambda x: 3.300454490968858 * max(0, x[9] - 21.211587298965615) * x[3],
        lambda x: -0.625257641967234 * max(0, x[9] - 13.245319764297824) *\
            max(0, 15.168375533662203 - x[10]),
        lambda x: -0.01574501347890333 * max(0, 13.245319764297824 - x[9]) *\
            max(0, 15.168375533662203 - x[10]),
        lambda x: 1.7215028323566686 * max(0, x[10] - 21.270903560153858) * x[3],
        lambda x: 0.0005571768577103953 * x[1] * max(0, x[9] - 13.007550699130583),
        lambda x: 18.583186018984453 * max(0, x[10] - 21.21344866686797),
        lambda x: 28.19775062179327 * max(0, x[9] - 21.260457953970647),
        lambda x: 2.2066956124128994 * max(0, 21.260457953970647 - x[9]),
        lambda x: 0.004399902463826988 * x[8] * max(0, 13.007550699130583 - x[9]),
        lambda x: 1.505057899312627 * max(0, x[9] - 16.15665687299809) * x[3],
        lambda x: -1.2763447599041995 * max(0, 16.15665687299809 - x[9]) * x[3]]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
