'''
output: dis_log_vol
prediction score: 0.9424381311000124
Forward Pass
-----------------------------------------------------------------
iter  parent  var  knot  mse        terms  gcv     rsq    grsq
-----------------------------------------------------------------
0     -       -    -     29.347951  1      29.359  0.000  0.000
1     0       9    5286  9.443271   3      9.464   0.678  0.678
2     0       10   3403  4.736290   5      4.756   0.839  0.838
3     1       10   3634  3.201216   7      3.220   0.891  0.890
4     1       9    1150  2.779552   9      2.801   0.905  0.905
5     4       9    2793  2.554002   11     2.579   0.913  0.912
6     0       2    -1    2.343808   12     2.369   0.920  0.919
7     0       10   5094  2.269480   14     2.298   0.923  0.922
8     13      9    2637  2.212551   16     2.244   0.925  0.924
9     4       8    -1    2.166929   17     2.200   0.926  0.925
10    1       3    -1    2.133072   18     2.168   0.927  0.926
11    12      3    -1    2.092028   19     2.128   0.929  0.928
12    11      10   4907  2.068589   21     2.108   0.930  0.928
-----------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
------------------------------------------------
iter  bf  terms  mse    gcv     rsq     grsq
------------------------------------------------
0     -   21     2.07   2.108   0.930   0.928
1     3   20     2.07   2.106   0.930   0.928
2     6   19     2.07   2.104   0.930   0.928
3     8   18     2.07   2.105   0.929   0.928
4     19  17     2.08   2.109   0.929   0.928
5     2   16     2.08   2.113   0.929   0.928
6     15  15     2.10   2.127   0.928   0.928
7     12  14     2.12   2.143   0.928   0.927
8     13  13     2.13   2.155   0.927   0.927
9     4   12     2.13   2.157   0.927   0.927
10    20  11     2.16   2.185   0.926   0.926
11    16  10     2.23   2.246   0.924   0.923
12    17  9      2.36   2.375   0.920   0.919
13    14  8      2.58   2.593   0.912   0.912
14    9   7      2.81   2.827   0.904   0.904
15    11  6      3.08   3.099   0.895   0.894
16    7   5      3.62   3.638   0.877   0.876
17    5   4      4.53   4.545   0.846   0.845
18    10  3      7.27   7.286   0.752   0.752
19    18  2      12.87  12.889  0.561   0.561
20    1   1      29.35  29.359  -0.000  -0.000
------------------------------------------------
Selected iteration: 2

Earth Model
------------------------------------------------------------------------
Basis Function                                     Pruned  Coefficient
------------------------------------------------------------------------
(Intercept)                                        No      6.44823
h(log_co2_mass-0.4365)                             No      0.654318
h(0.4365-log_co2_mass)                             No      3.1223
h(log_brine_mass-15.4292)                          Yes     None
h(15.4292-log_brine_mass)                          No      0.528356
h(log_brine_mass-14.4835)*h(log_co2_mass-0.4365)   No      -0.0497112
h(14.4835-log_brine_mass)*h(log_co2_mass-0.4365)   Yes     None
h(log_co2_mass-11.6488)*h(log_co2_mass-0.4365)     No      0.0196476
h(11.6488-log_co2_mass)*h(log_co2_mass-0.4365)     No      -0.00645015
h(log_co2_mass-1.31549)*h(15.4292-log_brine_mass)  No      0.0348398
h(1.31549-log_co2_mass)*h(15.4292-log_brine_mass)  No      -1.06023
por                                                No      -7.47711
h(log_brine_mass-12.0897)                          No      0.541951
h(12.0897-log_brine_mass)                          No      -0.591384
h(log_co2_mass-1.48457)*h(12.0897-log_brine_mass)  No      -0.0356037
h(1.48457-log_co2_mass)*h(12.0897-log_brine_mass)  No      0.706465
time*h(15.4292-log_brine_mass)                     No      0.00135729
log_permh*h(log_co2_mass-0.4365)                   No      0.0307433
log_permh*h(log_brine_mass-12.0897)                No      -0.061007
h(log_brine_mass-0.0352522)*por                    No      -0.205353
h(0.0352522-log_brine_mass)*por                    No      217.597
------------------------------------------------------------------------
MSE: 2.0688, GCV: 2.1044, RSQ: 0.9295, GRSQ: 0.9283
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
        lambda x: 6.448228406211374,
        lambda x: 0.6543178750032425 * max(0, x[9] - 0.43650048324446167),
        lambda x: 3.1223039985681753 * max(0, 0.43650048324446167 - x[9]),
        lambda x: 0.5283555959477471 * max(0, 15.429210740532683 - x[10]),
        lambda x: -0.04971122070773737 * max(0, x[10] - 14.483511831085414) *\
            max(0, x[9] - 0.43650048324446167),
        lambda x: 0.019647599260843807 * max(0, x[9] - 11.648779188133467) *\
            max(0, x[9] - 0.43650048324446167),
        lambda x: -0.006450153490831025 * max(0, 11.648779188133467 - x[9]) *\
            max(0, x[9] - 0.43650048324446167),
        lambda x: 0.03483978022013376 * max(0, x[9] - 1.3154900858111318) *\
            max(0, 15.429210740532683 - x[10]),
        lambda x: -1.0602302316470946 * max(0, 1.3154900858111318 - x[9]) *\
            max(0, 15.429210740532683 - x[10]),
        lambda x: -7.47710516495177 * x[2],
        lambda x: 0.5419508282164403 * max(0, x[10] - 12.089722740605822),
        lambda x: -0.5913838992026265 * max(0, 12.089722740605822 - x[10]),
        lambda x: -0.03560373258388469 * max(0, x[9] - 1.4845650774705943) \
            * max(0, 12.089722740605822 - x[10]),
        lambda x: 0.7064653574259414 * max(0, 1.4845650774705943 - x[9]) *\
            max(0, 12.089722740605822 - x[10]),
        lambda x: 0.0013572851011875997 * x[8] * max(0, 15.429210740532683 - x[10]),
        lambda x: 0.03074334308766613 * x[3] * max(0, x[9] - 0.43650048324446167),
        lambda x: -0.06100697106502519 * x[3] * max(0, x[10] - 12.089722740605822),
        lambda x: -0.20535327723329735 * max(0, x[10] - 0.03525219629883897) * x[2],
        lambda x: 217.59732868333012 * max(0, 0.03525219629883897 - x[10]) * x[2]]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
