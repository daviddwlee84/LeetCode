from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:

        time = 0
        left_ants = {index: index for index in left}
        right_ants = {index: index for index in right}
        if left == [0] and (not right or right == [n]):
            return 0
        if right == [n] and (not left or left == [0]):
            return 0

        while left_ants or right_ants:
            left_index = {}
            next_left_ants = {}
            next_right_ants = {}

            for ant, pos in left_ants.items():
                if pos - 1 > 0:
                    next_left_ants[ant] = pos - 1
                    left_index[pos - 1] = ant

            for ant, pos in right_ants.items():
                if pos + 1 < n:
                    next_right_ants[ant] = pos + 1
                    if pos + 1 in left_index:
                        ant_left = left_index[pos + 1]
                        next_left_ants[ant] = pos + 1
                        next_right_ants[ant_left] = pos + 1

            # prevent from: RuntimeError: dictionary changed size during iteration
            right_ants = next_right_ants
            left_ants = next_left_ants
            time += 1

        return time

# WA
#
# 1000
# [0]
# []
#
# 0

# TLE
# 4220
# [2,4,7,9,11,14,16,18,20,22,24,26,28,33,36,38,41,43,46,48,50,53,55,57,59,61,64,66,69,71,73,75,80,82,84,88,90,92,95,97,99,101,103,106,108,110,114,117,121,124,126,128,131,133,135,137,139,141,144,146,148,151,153,156,159,161,163,166,170,174,177,180,182,186,189,192,194,196,199,201,203,206,208,210,212,214,217,219,222,225,227,229,231,236,238,241,243,245,248,251,254,259,262,265,267,270,272,275,277,279,283,285,287,289,296,299,302,304,307,309,312,314,316,318,322,324,327,329,332,334,336,339,341,343,345,348,350,352,357,359,361,363,365,367,369,371,373,376,380,383,386,389,391,394,397,399,404,409,411,414,417,422,424,426,428,430,432,434,436,438,441,444,447,449,451,453,455,457,459,462,464,466,468,470,474,477,479,482,484,487,489,492,495,497,500,503,505,508,512,514,518,523,525,527,529,531,533,535,537,539,541,543,546,549,552,556,559,561,563,565,567,570,572,575,577,579,581,583,586,588,591,594,596,598,600,602,605,607,609,611,613,615,617,620,622,624,626,628,630,632,634,636,638,640,643,645,648,650,652,655,657,659,661,663,665,667,669,671,673,676,679,681,684,686,688,690,692,694,697,699,702,704,707,709,711,715,719,721,725,727,729,732,735,737,740,742,745,747,749,751,753,755,757,759,762,765,768,771,774,778,780,783,786,790,793,796,799,801,806,808,810,813,815,817,819,821,823,827,829,831,833,835,837,841,844,846,848,854,856,858,860,862,865,868,871,873,876,878,880,883,885,887,889,891,893,896,900,902,904,907,909,912,914,916,919,921,924,930,932,935,937,939,943,945,947,950,952,954,957,960,963,965,967,972,975,977,980,983,985,987,989,992,994,996,999,1003,1006,1008,1011,1015,1017,1019,1021,1026,1029,1031,1033,1036,1039,1041,1044,1046,1048,1050,1052,1054,1056,1058,1060,1063,1066,1070,1073,1075,1078,1080,1083,1088,1090,1092,1094,1097,1099,1102,1104,1108,1110,1113,1118,1120,1122,1125,1128,1130,1132,1134,1136,1138,1140,1142,1144,1147,1150,1152,1154,1157,1160,1162,1164,1167,1169,1171,1173,1177,1179,1182,1184,1187,1190,1192,1194,1196,1198,1201,1203,1205,1209,1211,1213,1215,1220,1222,1224,1228,1231,1234,1238,1240,1242,1244,1246,1248,1250,1252,1255,1257,1260,1263,1265,1268,1270,1272,1274,1276,1279,1281,1285,1288,1290,1292,1294,1296,1299,1302,1305,1307,1310,1313,1316,1318,1320,1322,1324,1327,1330,1332,1334,1336,1338,1340,1343,1347,1349,1352,1354,1357,1359,1361,1363,1365,1367,1370,1372,1375,1378,1380,1382,1386,1388,1390,1393,1395,1397,1399,1402,1404,1406,1409,1414,1417,1420,1422,1426,1428,1430,1432,1434,1439,1441,1444,1447,1449,1451,1453,1458,1461,1465,1467,1469,1473,1476,1478,1480,1482,1484,1486,1488,1490,1492,1494,1497,1501,1503,1505,1507,1509,1511,1515,1517,1519,1521,1524,1526,1528,1532,1534,1539,1542,1544,1546,1548,1551,1553,1556,1558,1562,1564,1566,1568,1570,1573,1575,1577,1579,1581,1583,1585,1587,1591,1593,1595,1597,1599,1602,1604,1606,1609,1611,1613,1616,1619,1621,1625,1627,1630,1634,1637,1640,1642,1646,1648,1650,1652,1654,1658,1661,1668,1671,1673,1675,1677,1679,1681,1683,1685,1691,1694,1696,1698,1700,1703,1705,1707,1710,1714,1716,1718,1720,1722,1725,1728,1731,1733,1735,1738,1740,1742,1745,1749,1751,1755,1759,1762,1764,1766,1769,1771,1773,1775,1777,1782,1785,1788,1793,1795,1797,1801,1805,1807,1809,1811,1813,1818,1821,1823,1825,1828,1830,1832,1834,1839,1842,1844,1850,1852,1855,1857,1860,1862,1864,1866,1868,1870,1872,1874,1877,1880,1883,1885,1887,1891,1893,1895,1897,1899,1901,1904,1906,1908,1910,1916,1919,1921,1923,1927,1929,1931,1933,1935,1937,1939,1941,1943,1947,1949,1951,1953,1955,1959,1961,1964,1966,1968,1970,1972,1975,1978,1980,1984,1986,1988,1990,1992,1994,1997,2000,2003,2005,2007,2009,2011,2013,2015,2017,2022,2025,2027,2031,2033,2035,2038,2040,2044,2046,2048,2050,2053,2055,2058,2060,2063,2066,2069,2072,2075,2077,2080,2082,2084,2086,2088,2090,2093,2096,2098,2100,2102,2104,2106,2108,2113,2115,2117,2119,2121,2123,2125,2128,2131,2134,2137,2140,2143,2145,2148,2152,2154,2157,2159,2161,2164,2166,2173,2175,2178,2180,2185,2187,2190,2192,2194,2196,2198,2201,2203,2205,2209,2211,2214,2218,2220,2222,2224,2226,2228,2230,2233,2236,2238,2241,2243,2245,2248,2250,2252,2254,2258,2261,2264,2267,2270,2272,2274,2277,2279,2281,2283,2285,2287,2289,2291,2293,2296,2298,2303,2305,2307,2310,2312,2314,2317,2320,2323,2325,2327,2329,2331,2333,2335,2337,2339,2341,2343,2346,2349,2351,2353,2358,2360,2362,2364,2366,2369,2372,2374,2376,2379,2382,2385,2387,2390,2392,2395,2398,2400,2402,2404,2406,2408,2410,2412,2414,2416,2421,2423,2427,2430,2432,2434,2436,2439,2441,2443,2445,2447,2452,2454,2457,2459,2462,2466,2468,2470,2472,2477,2479,2485,2489,2491,2493,2495,2497,2499,2502,2506,2511,2513,2516,2518,2521,2523,2525,2527,2530,2533,2535,2537,2539,2541,2543,2545,2547,2550,2552,2555,2557,2559,2561,2563,2565,2568,2570,2573,2576,2579,2581,2585,2589,2591,2593,2596,2598,2600,2602,2604,2606,2609,2611,2613,2615,2617,2619,2621,2626,2628,2630,2633,2635,2638,2640,2642,2644,2646,2649,2651,2653,2655,2657,2659,2665,2667,2669,2671,2675,2677,2679,2682,2686,2691,2693,2696,2698,2702,2704,2707,2711,2713,2715,2719,2723,2725,2727,2729,2734,2736,2740,2743,2746,2748,2750,2753,2757,2759,2761,2763,2766,2771,2773,2775,2777,2779,2782,2784,2787,2789,2791,2793,2795,2798,2800,2802,2804,2806,2808,2810,2813,2815,2817,2820,2822,2824,2827,2830,2832,2834,2836,2839,2842,2844,2846,2848,2851,2853,2856,2858,2861,2863,2865,2868,2870,2873,2875,2877,2879,2881,2883,2886,2888,2892,2896,2898,2900,2902,2904,2907,2910,2913,2915,2918,2921,2924,2926,2931,2934,2936,2938,2941,2943,2946,2949,2951,2954,2956,2958,2960,2962,2964,2966,2968,2971,2973,2975,2980,2982,2984,2987,2990,2993,2995,2998,3000,3003,3005,3008,3010,3013,3016,3019,3021,3023,3026,3028,3030,3032,3034,3036,3038,3041,3043,3045,3047,3049,3051,3055,3057,3059,3062,3066,3068,3070,3074,3076,3078,3082,3085,3088,3090,3092,3095,3098,3100,3103,3107,3109,3112,3115,3117,3119,3121,3124,3126,3128,3130,3132,3135,3138,3140,3142,3145,3147,3149,3151,3153,3157,3159,3161,3163,3165,3167,3169,3172,3174,3177,3179,3181,3184,3187,3190,3194,3197,3199,3202,3205,3208,3210,3212,3214,3216,3218,3220,3223,3225,3228,3230,3232,3234,3236,3238,3240,3244,3247,3252,3254,3256,3259,3261,3263,3265,3268,3270,3274,3277,3279,3281,3285,3289,3292,3294,3296,3299,3301,3305,3307,3309,3311,3313,3317,3320,3322,3325,3327,3329,3331,3334,3337,3339,3341,3345,3347,3349,3354,3358,3361,3363,3367,3369,3371,3374,3376,3378,3380,3382,3386,3389,3391,3394,3396,3398,3400,3402,3404,3406,3410,3413,3415,3418,3422,3425,3427,3429,3431,3433,3435,3437,3439,3442,3444,3447,3449,3451,3453,3455,3457,3459,3461,3464,3467,3470,3473,3476,3478,3480,3482,3485,3487,3490,3492,3494,3497,3499,3502,3504,3507,3509,3512,3514,3516,3518,3520,3522,3525,3527,3530,3534,3536,3538,3540,3542,3544,3546,3549,3553,3556,3559,3561,3563,3566,3569,3571,3574,3576,3578,3581,3584,3587,3592,3595,3597,3599,3601,3604,3606,3608,3610,3615,3617,3619,3623,3626,3628,3632,3634,3636,3639,3641,3645,3647,3650,3653,3656,3658,3660,3664,3666,3671,3673,3675,3677,3680,3682,3685,3687,3689,3691,3693,3695,3697,3700,3702,3707,3709,3711,3713,3715,3718,3722,3724,3726,3728,3731,3736,3738,3743,3746,3748,3751,3753,3755,3758,3760,3763,3765,3768,3770,3773,3775,3777,3781,3784,3787,3790,3792,3794,3798,3800,3803,3806,3808,3810,3813,3815,3817,3820,3822,3826,3829,3832,3834,3837,3839,3841,3843,3846,3848,3850,3853,3855,3857,3860,3865,3867,3869,3871,3873,3876,3878,3882,3884,3886,3888,3890,3892,3894,3896,3898,3900,3903,3905,3907,3909,3911,3914,3916,3918,3920,3922,3924,3927,3930,3932,3934,3936,3938,3940,3942,3944,3946,3950,3952,3955,3957,3960,3962,3965,3967,3970,3973,3976,3979,3981,3983,3985,3988,3990,3992,3994,3996,3999,4002,4005,4007,4010,4012,4014,4016,4018,4020,4022,4024,4026,4028,4030,4032,4034,4037,4039,4041,4043,4045,4048,4050,4052,4054,4057,4060,4063,4066,4068,4070,4073,4077,4079,4081,4084,4087,4089,4091,4095,4097,4100,4103,4106,4108,4110,4112,4115,4117,4119,4121,4123,4125,4127,4131,4135,4137,4139,4141,4143,4146,4148,4151,4153,4155,4159,4162,4164,4167,4170,4173,4176,4178,4181,4183,4186,4190,4193,4196,4198,4200,4202,4204,4206,4210,4212,4214,4216,4219]
# [1,3,5,8,10,12,15,17,19,21,23,25,27,29,35,37,40,42,45,47,49,51,54,56,58,60,63,65,67,70,72,74,79,81,83,86,89,91,93,96,98,100,102,105,107,109,112,116,120,123,125,127,129,132,134,136,138,140,142,145,147,149,152,154,157,160,162,164,168,172,175,179,181,185,187,190,193,195,198,200,202,204,207,209,211,213,215,218,221,224,226,228,230,233,237,240,242,244,247,250,253,255,261,264,266,269,271,274,276,278,281,284,286,288,291,298,300,303,305,308,311,313,315,317,319,323,325,328,331,333,335,337,340,342,344,347,349,351,356,358,360,362,364,366,368,370,372,375,377,381,385,387,390,393,396,398,402,408,410,412,416,419,423,425,427,429,431,433,435,437,439,443,446,448,450,452,454,456,458,460,463,465,467,469,472,476,478,480,483,485,488,491,493,496,499,502,504,506,511,513,515,520,524,526,528,530,532,534,536,538,540,542,544,547,550,553,558,560,562,564,566,569,571,574,576,578,580,582,584,587,590,592,595,597,599,601,604,606,608,610,612,614,616,618,621,623,625,627,629,631,633,635,637,639,641,644,647,649,651,654,656,658,660,662,664,666,668,670,672,675,678,680,683,685,687,689,691,693,695,698,700,703,705,708,710,713,718,720,722,726,728,730,734,736,739,741,743,746,748,750,752,754,756,758,760,764,766,769,773,777,779,781,785,789,792,795,797,800,802,807,809,811,814,816,818,820,822,826,828,830,832,834,836,840,843,845,847,850,855,857,859,861,863,867,870,872,874,877,879,881,884,886,888,890,892,895,899,901,903,905,908,911,913,915,918,920,922,927,931,934,936,938,941,944,946,948,951,953,955,959,961,964,966,970,973,976,979,982,984,986,988,991,993,995,997,1002,1005,1007,1010,1014,1016,1018,1020,1023,1027,1030,1032,1035,1037,1040,1043,1045,1047,1049,1051,1053,1055,1057,1059,1061,1065,1067,1072,1074,1077,1079,1082,1084,1089,1091,1093,1095,1098,1100,1103,1106,1109,1112,1115,1119,1121,1123,1127,1129,1131,1133,1135,1137,1139,1141,1143,1146,1148,1151,1153,1156,1159,1161,1163,1165,1168,1170,1172,1175,1178,1180,1183,1186,1188,1191,1193,1195,1197,1200,1202,1204,1208,1210,1212,1214,1216,1221,1223,1225,1230,1232,1236,1239,1241,1243,1245,1247,1249,1251,1254,1256,1259,1261,1264,1267,1269,1271,1273,1275,1278,1280,1284,1286,1289,1291,1293,1295,1297,1300,1304,1306,1309,1312,1314,1317,1319,1321,1323,1326,1328,1331,1333,1335,1337,1339,1341,1344,1348,1351,1353,1356,1358,1360,1362,1364,1366,1369,1371,1373,1376,1379,1381,1385,1387,1389,1391,1394,1396,1398,1400,1403,1405,1407,1411,1416,1419,1421,1424,1427,1429,1431,1433,1437,1440,1443,1445,1448,1450,1452,1456,1459,1462,1466,1468,1471,1474,1477,1479,1481,1483,1485,1487,1489,1491,1493,1496,1500,1502,1504,1506,1508,1510,1514,1516,1518,1520,1523,1525,1527,1530,1533,1536,1541,1543,1545,1547,1550,1552,1554,1557,1560,1563,1565,1567,1569,1572,1574,1576,1578,1580,1582,1584,1586,1588,1592,1594,1596,1598,1601,1603,1605,1607,1610,1612,1614,1617,1620,1622,1626,1629,1633,1635,1638,1641,1643,1647,1649,1651,1653,1657,1659,1665,1669,1672,1674,1676,1678,1680,1682,1684,1689,1693,1695,1697,1699,1702,1704,1706,1709,1713,1715,1717,1719,1721,1724,1726,1730,1732,1734,1737,1739,1741,1743,1748,1750,1754,1758,1760,1763,1765,1768,1770,1772,1774,1776,1778,1784,1786,1792,1794,1796,1800,1804,1806,1808,1810,1812,1814,1819,1822,1824,1827,1829,1831,1833,1836,1840,1843,1849,1851,1853,1856,1859,1861,1863,1865,1867,1869,1871,1873,1875,1878,1881,1884,1886,1888,1892,1894,1896,1898,1900,1902,1905,1907,1909,1913,1917,1920,1922,1925,1928,1930,1932,1934,1936,1938,1940,1942,1945,1948,1950,1952,1954,1957,1960,1963,1965,1967,1969,1971,1974,1977,1979,1983,1985,1987,1989,1991,1993,1995,1998,2002,2004,2006,2008,2010,2012,2014,2016,2018,2024,2026,2030,2032,2034,2036,2039,2041,2045,2047,2049,2052,2054,2056,2059,2061,2065,2067,2071,2073,2076,2078,2081,2083,2085,2087,2089,2091,2094,2097,2099,2101,2103,2105,2107,2110,2114,2116,2118,2120,2122,2124,2126,2130,2132,2136,2138,2141,2144,2147,2149,2153,2155,2158,2160,2162,2165,2168,2174,2177,2179,2182,2186,2189,2191,2193,2195,2197,2199,2202,2204,2208,2210,2213,2216,2219,2221,2223,2225,2227,2229,2232,2234,2237,2240,2242,2244,2246,2249,2251,2253,2257,2260,2262,2265,2268,2271,2273,2276,2278,2280,2282,2284,2286,2288,2290,2292,2295,2297,2301,2304,2306,2309,2311,2313,2316,2319,2321,2324,2326,2328,2330,2332,2334,2336,2338,2340,2342,2345,2348,2350,2352,2356,2359,2361,2363,2365,2368,2371,2373,2375,2377,2381,2384,2386,2389,2391,2393,2396,2399,2401,2403,2405,2407,2409,2411,2413,2415,2418,2422,2424,2428,2431,2433,2435,2438,2440,2442,2444,2446,2449,2453,2455,2458,2460,2465,2467,2469,2471,2475,2478,2481,2487,2490,2492,2494,2496,2498,2501,2504,2507,2512,2514,2517,2520,2522,2524,2526,2528,2531,2534,2536,2538,2540,2542,2544,2546,2549,2551,2554,2556,2558,2560,2562,2564,2566,2569,2571,2575,2578,2580,2582,2587,2590,2592,2595,2597,2599,2601,2603,2605,2608,2610,2612,2614,2616,2618,2620,2622,2627,2629,2631,2634,2637,2639,2641,2643,2645,2648,2650,2652,2654,2656,2658,2661,2666,2668,2670,2672,2676,2678,2680,2683,2687,2692,2694,2697,2701,2703,2705,2708,2712,2714,2717,2720,2724,2726,2728,2732,2735,2738,2741,2745,2747,2749,2751,2755,2758,2760,2762,2765,2769,2772,2774,2776,2778,2781,2783,2786,2788,2790,2792,2794,2796,2799,2801,2803,2805,2807,2809,2812,2814,2816,2818,2821,2823,2825,2829,2831,2833,2835,2837,2840,2843,2845,2847,2850,2852,2854,2857,2860,2862,2864,2867,2869,2872,2874,2876,2878,2880,2882,2885,2887,2889,2893,2897,2899,2901,2903,2906,2909,2912,2914,2916,2920,2922,2925,2927,2932,2935,2937,2940,2942,2944,2948,2950,2952,2955,2957,2959,2961,2963,2965,2967,2969,2972,2974,2976,2981,2983,2985,2989,2992,2994,2996,2999,3001,3004,3007,3009,3012,3015,3018,3020,3022,3024,3027,3029,3031,3033,3035,3037,3039,3042,3044,3046,3048,3050,3052,3056,3058,3060,3064,3067,3069,3071,3075,3077,3079,3083,3086,3089,3091,3093,3097,3099,3102,3105,3108,3111,3114,3116,3118,3120,3122,3125,3127,3129,3131,3134,3136,3139,3141,3144,3146,3148,3150,3152,3155,3158,3160,3162,3164,3166,3168,3170,3173,3176,3178,3180,3183,3186,3188,3192,3195,3198,3200,3203,3206,3209,3211,3213,3215,3217,3219,3222,3224,3227,3229,3231,3233,3235,3237,3239,3243,3246,3248,3253,3255,3257,3260,3262,3264,3267,3269,3272,3275,3278,3280,3283,3287,3291,3293,3295,3298,3300,3304,3306,3308,3310,3312,3314,3319,3321,3323,3326,3328,3330,3332,3335,3338,3340,3344,3346,3348,3350,3356,3360,3362,3366,3368,3370,3373,3375,3377,3379,3381,3385,3387,3390,3393,3395,3397,3399,3401,3403,3405,3408,3411,3414,3416,3419,3423,3426,3428,3430,3432,3434,3436,3438,3441,3443,3446,3448,3450,3452,3454,3456,3458,3460,3463,3465,3469,3471,3475,3477,3479,3481,3483,3486,3488,3491,3493,3495,3498,3500,3503,3505,3508,3511,3513,3515,3517,3519,3521,3523,3526,3529,3533,3535,3537,3539,3541,3543,3545,3548,3551,3555,3558,3560,3562,3564,3568,3570,3573,3575,3577,3579,3583,3586,3591,3593,3596,3598,3600,3602,3605,3607,3609,3612,3616,3618,3621,3624,3627,3631,3633,3635,3638,3640,3644,3646,3649,3652,3655,3657,3659,3662,3665,3667,3672,3674,3676,3678,3681,3683,3686,3688,3690,3692,3694,3696,3698,3701,3705,3708,3710,3712,3714,3717,3721,3723,3725,3727,3730,3732,3737,3742,3745,3747,3749,3752,3754,3757,3759,3761,3764,3767,3769,3772,3774,3776,3779,3783,3786,3788,3791,3793,3797,3799,3802,3805,3807,3809,3812,3814,3816,3819,3821,3824,3827,3830,3833,3835,3838,3840,3842,3845,3847,3849,3851,3854,3856,3859,3863,3866,3868,3870,3872,3875,3877,3879,3883,3885,3887,3889,3891,3893,3895,3897,3899,3901,3904,3906,3908,3910,3913,3915,3917,3919,3921,3923,3926,3929,3931,3933,3935,3937,3939,3941,3943,3945,3948,3951,3954,3956,3959,3961,3964,3966,3969,3972,3974,3978,3980,3982,3984,3987,3989,3991,3993,3995,3998,4001,4004,4006,4009,4011,4013,4015,4017,4019,4021,4023,4025,4027,4029,4031,4033,4035,4038,4040,4042,4044,4046,4049,4051,4053,4056,4059,4062,4064,4067,4069,4072,4074,4078,4080,4083,4085,4088,4090,4094,4096,4098,4102,4105,4107,4109,4111,4113,4116,4118,4120,4122,4124,4126,4129,4134,4136,4138,4140,4142,4144,4147,4150,4152,4154,4156,4160,4163,4166,4169,4172,4174,4177,4179,4182,4185,4189,4192,4194,4197,4199,4201,4203,4205,4207,4211,4213,4215,4218,4220]