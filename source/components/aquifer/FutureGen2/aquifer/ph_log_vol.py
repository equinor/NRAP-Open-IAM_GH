'''
output: ph_log_vol
prediction score: 0.8601408129588759
Forward Pass
-----------------------------------------------------------------
iter  parent  var  knot  mse        terms  gcv     rsq    grsq
-----------------------------------------------------------------
0     -       -    -     50.019210  1      50.039  0.000  0.000
1     0       9    2497  10.899107  3      10.925  0.782  0.782
2     0       10   2115  9.651443   5      9.694   0.807  0.806
3     3       9    1122  7.878422   7      7.929   0.842  0.842
4     3       9    3986  7.513113   9      7.577   0.850  0.849
5     3       9    4733  7.270763   11     7.347   0.855  0.853
6     1       9    3888  7.073272   13     7.162   0.859  0.857
7     3       10   571   6.930395   15     7.031   0.861  0.859
8     1       10   571   6.776560   17     6.889   0.865  0.862
9     0       2    3729  6.635968   19     6.760   0.867  0.865
10    18      10   4716  6.291806   21     6.422   0.874  0.872
11    18      10   4071  6.225808   23     6.368   0.876  0.873
12    18      9    2623  6.169091   25     6.322   0.877  0.874
13    1       1    -1    6.111281   26     6.270   0.878  0.875
14    3       9    4337  6.064289   28     6.234   0.879  0.875
-----------------------------------------------------------------
Stopping Condition 2: Improvement below threshold

Pruning Pass
----------------------------------------------
iter  bf  terms  mse    gcv     rsq    grsq
----------------------------------------------
0     -   28     6.07   6.235   0.879  0.875
1     27  27     6.07   6.229   0.879  0.876
2     19  26     6.07   6.223   0.879  0.876
3     8   25     6.07   6.216   0.879  0.876
4     3   24     6.07   6.210   0.879  0.876
5     14  23     6.07   6.204   0.879  0.876
6     16  22     6.07   6.199   0.879  0.876
7     4   21     6.07   6.194   0.879  0.876
8     13  20     6.07   6.193   0.879  0.876
9     17  19     6.09   6.205   0.878  0.876
10    11  18     6.12   6.232   0.878  0.875
11    7   17     6.15   6.252   0.877  0.875
12    25  16     6.21   6.310   0.876  0.874
13    24  15     6.29   6.382   0.874  0.872
14    12  14     6.33   6.418   0.873  0.872
15    23  13     6.37   6.449   0.873  0.871
16    6   12     6.68   6.761   0.866  0.865
17    15  11     6.97   7.038   0.861  0.859
18    21  10     7.25   7.316   0.855  0.854
19    18  9      7.25   7.310   0.855  0.854
20    22  8      7.32   7.379   0.854  0.853
21    20  7      7.46   7.505   0.851  0.850
22    26  6      8.26   8.304   0.835  0.834
23    5   5      8.91   8.947   0.822  0.821
24    9   4      9.03   9.059   0.819  0.819
25    2   3      9.99   10.018  0.800  0.800
26    10  2      11.41  11.426  0.772  0.772
27    1   1      50.02  50.039  0.000  0.000
----------------------------------------------
Selected iteration: 8

Earth Model
--------------------------------------------------------------------------
Basis Function                                       Pruned  Coefficient
--------------------------------------------------------------------------
(Intercept)                                          No      4.40966
h(log_co2_mass-1.37674)                              No      0.66947
h(1.37674-log_co2_mass)                              No      -4.15876
h(log_brine_mass-9.54838)                            Yes     None
h(9.54838-log_brine_mass)                            Yes     None
h(log_co2_mass-2.03811)*h(log_brine_mass-9.54838)    No      -0.0541566
h(2.03811-log_co2_mass)*h(log_brine_mass-9.54838)    No      0.404268
h(log_co2_mass-15.7589)*h(log_brine_mass-9.54838)    No      -0.106989
h(15.7589-log_co2_mass)*h(log_brine_mass-9.54838)    Yes     None
h(log_co2_mass-10.0819)*h(log_brine_mass-9.54838)    No      0.250196
h(10.0819-log_co2_mass)*h(log_brine_mass-9.54838)    No      -0.077753
h(log_co2_mass-15.7389)*h(log_co2_mass-1.37674)      No      0.0118211
h(15.7389-log_co2_mass)*h(log_co2_mass-1.37674)      No      0.0338684
h(log_brine_mass-22.5564)*h(log_brine_mass-9.54838)  Yes     None
h(22.5564-log_brine_mass)*h(log_brine_mass-9.54838)  Yes     None
h(log_brine_mass-22.5564)*h(log_co2_mass-1.37674)    No      -0.280536
h(22.5564-log_brine_mass)*h(log_co2_mass-1.37674)    Yes     None
h(por-0.199086)                                      No      -4107.32
h(0.199086-por)                                      No      -467.467
h(log_brine_mass-22.6663)*h(0.199086-por)            Yes     None
h(22.6663-log_brine_mass)*h(0.199086-por)            No      59.6115
h(log_brine_mass-14.7789)*h(0.199086-por)            No      56.4076
h(14.7789-log_brine_mass)*h(0.199086-por)            No      -59.6951
h(log_co2_mass-11.2643)*h(0.199086-por)              No      1.57894
h(11.2643-log_co2_mass)*h(0.199086-por)              No      1.00777
depth*h(log_co2_mass-1.37674)                        No      0.000124311
h(log_co2_mass-13.7137)*h(log_brine_mass-9.54838)    No      -0.127234
h(13.7137-log_co2_mass)*h(log_brine_mass-9.54838)    Yes     None
--------------------------------------------------------------------------
MSE: 6.0730, GCV: 6.1926, RSQ: 0.8786, GRSQ: 0.8762
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
        lambda x: 4.409659363417846,
        lambda x: 0.6694701873021016 * max(0, x[9] - 1.3767380705598726),
        lambda x: -4.1587593950760295 * max(0, 1.3767380705598726 - x[9]),
        lambda x: -0.0541566332383474 * max(0, x[9] - 2.0381123140850694) *\
             max(0, x[10] - 9.548379711602534),
        lambda x: 0.4042683377514592 * max(0, 2.0381123140850694 - x[9]) *\
            max(0, x[10] - 9.548379711602534),
        lambda x: -0.10698897374800655 * max(0, x[9] - 15.758850586168437) *\
            max(0, x[10] - 9.548379711602534),
        lambda x: 0.25019643454367596 * max(0, x[9] - 10.081930981217656) *\
            max(0, x[10] - 9.548379711602534),
        lambda x: -0.07775295810593373 * max(0, 10.081930981217656 - x[9]) *\
            max(0, x[10] - 9.548379711602534),
        lambda x: 0.011821066139669139 * max(0, x[9] - 15.738887291319937) *\
            max(0, x[9] - 1.3767380705598726),
        lambda x: 0.03386836669128046 * max(0, 15.738887291319937 - x[9]) *\
            max(0, x[9] - 1.3767380705598726),
        lambda x: -0.2805355510841816 * max(0, x[10] - 22.556428366292643) *\
            max(0, x[9] - 1.3767380705598726),
        lambda x: -4107.315976905821 * max(0, x[2] - 0.19908597940829562),
        lambda x: -467.4668560036563 * max(0, 0.19908597940829562 - x[2]),
        lambda x: 59.61151177998592 * max(0, 22.66632172651078 - x[10]) *\
            max(0, 0.19908597940829562 - x[2]),
        lambda x: 56.40758622599693 * max(0, x[10] - 14.778920464156723) *\
            max(0, 0.19908597940829562 - x[2]),
        lambda x: -59.69506825145658 * max(0, 14.778920464156723 - x[10]) *\
            max(0, 0.19908597940829562 - x[2]),
        lambda x: 1.5789414605320136 * max(0, x[9] - 11.264302469194485) *\
            max(0, 0.19908597940829562 - x[2]),
        lambda x: 1.0077726015413293 * max(0, 11.264302469194485 - x[9]) *\
            max(0, 0.19908597940829562 - x[2]),
        lambda x: 0.00012431071573248964 * x[1] * max(0, x[9] - 1.3767380705598726),
        lambda x: -0.1272337646998225 * max(0, x[9] - 13.713739577627104) *\
            max(0, x[10] - 9.548379711602534)]
    for x in example_iterator:
        yield sum(accessor(x) for accessor in accessors)
