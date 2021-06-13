from typing import List
import re


class Solution:
    def maximumRemovals(self, s: str, p: str, removable: List[int]) -> int:
        positions = [set() for _ in range(len(p))]
        for i, char in enumerate(p):
            for result in re.finditer(char, s):
                positions[i].add(result.start())

        i = 0
        for pos in removable:
            min_pos = -1
            for position in positions:
                if pos in position:
                    position.remove(pos)
                # find a position that is just greater than min_pos
                found = False
                for p in sorted(position):
                    if p > min_pos:
                        min_pos = p
                        found = True
                        break
                if not found:
                    return i
            i += 1

        return i

# TLE
# "ywevzxpsminwessjhyeiyztnnpahjmojsgwecwfeulyosdyeshhaukhjwjxlgalaepmyklltpffljcafcbyynysznhyzsyvupqqibvlmzculsmjojxtjhmunhczybsjgpwssmgctpmhaulzagnzaoicyxnvuiqcktkenxlhruyndiglyfpnauxnppjkpqdcntcwbirhkcrpzlvggcgbiaalhbknlmhltjleufxuzhbxupxdagkqksswmarjdytzoaodrjojlttpwzlpxqfekqafqkkzwbraidagxncovknbbjwvtnftopoiwoynezvrgdvvjnbxrgrurlwvfybghrndhzebhszshzeoudlzoncwijhujndztnpyhwnibnfkibcfczwrudxldqzjxfowscxxikcysyppdutgxfvjzkjlqwlwokmsanfhifbkanbexpnqxmkkbugibtwinwicnolpvljfurjnaxriyiotciuynwmoybyjgxzekjgtmkudlhctvaokeqhmjiwvzjgaoiuwulagxedglclzqfdiwndpgewexnngpyacctdfokmfecxpwymlvfagpcnjgvfackkobcvhslkgnltevnvlmanbvzhhlnvsmnnqltsguwxyfqiwfgekprghixpbburlbcfzcqytnabymvjayiakwdaiyucoeeixlpoadmtntpyfyvgimzsbffudhyfshgdzfjzhllintxnmgfrfhxbzfrmobxqkfturlykhrjgtmrfpnewrulbnqbzhkrcaddxccjdarguocnbqaazwucnnzvimsdyahxynkaqhmkorsgamqdtccaxnnudywsdzjddpyrfzvpichuvdlooigdzcvxlbckaafscetivonsrihcgnzjgyidmqegfrgiepvsfmfyilrpeqdkbcurdxaxziicxgnuthzciyzjhjbucszowocvmtwajghwnakvfzenjihniqmbzmotdprrsqctrvmxzpkezgdfbttrgtbucuoazruegyeelspmzrogbhmpwcqcerxgyrsdvfjvprbpfccghkxdkehchlqcalqosuwubmjjpubhipnjprbupzgfjdyhxemlyquzenfrgwcgcnoxxzeaqoswraonouwlabfyirilptztmrojumujteihkdajesalrhjdcrhcwabrskbxkjjstdrtbydqwhxkxdjszzggpwfsmkgqtexfvmuugilpcsermjnngopgkxwmksmffzseesyuqbhbwcxhhogysrxesnlysztuironwblycxtudaqvhcbxukuoyetgvddkjcxqgojsvnosxmtfzvxsupygxgowcuvmadaugdohwvudaurculgnzzobhdisnzdopylpkderizdqvapukcynavolwggviyfzgchlrfkztkjonfyvcffwwcrtefikvmnitlqfrrmqwtwspvwbkxcjssjjmwzembcxyaljxjvfyrrzdwhmnvqxtjwbbmztbnlogfduwbamavkntlbafztjhnjvjeyomessajwyjijkhvrcxzvdvqaxrflcvvelrxldoafkwcumllturzgodialdtekhjgnphdevuxwnigpfreoaouuqspyoyclwgsuvwjqmyixiwfiugehvmlvdfsxieonwfnihguhhbkxozjzbnlajkoqthuwdadjuiggpidpuioultjwyxgkpbzpuibxigrsepdmyxbelrknqtwyerxseswbjxvernkarzotkpqzkjbchqljsobumjhynqiemwovuqnvipkjewtnnpcqzsqadwkebdogltwmywyeneohgitqjjzxrafszaijrzaqxnoxqvwngwljheiomfinlrtwnoctcixaanfpdtoqmqpvtsiqniegdgcccdpzhswebaeligfgfnfoxwjrhvlqjqrbznuypvagmwptgfygbvactqgcqblrmnjlqqtoiywrdffoifxepxygzlhcovivrzxaraeqdhothdizibnzkrxgdbscjkzunqadwcbcfidwhwvvwqjryreaxwyvsgrfaxjmeyezriufjkhzcykmcklveuemmftsrpwilfoxjlcqpscuiaowixbsbcpeblfpdgikcrhymvmforcqrjnhhlkzmtvmzusbgvodisunoygaidnzlwcfdbqrcdgfpmboklckxneqitqgsggzkbpgnobmluarhawqwufezidzuhtwmcqqtwlfzttqikzprftlipkbdswsogfxfazolkmtrhbvkddmbottuxhtpcszugvqstvdwsazdkysnhpeuwqkpbzhdgllgjnoharortphvwovyppyjrycjcbusdxxkyyuhcttujfezjlrhjkxctmiuwfussvocuecmiqmhwctiypbbgwiihhijuclcpqduafqcwvczpkkxarrtejmitfhiggcthnjcfsccjgdyktycjfjpugqrckupkeoubtitvjegvpblfsavjrcnbpocwupsiunipbivozfcumefnxjbijrtqxksvozvckfsrccufqnwdkpongytgrtuzhxktveelxxcrwlxhpovlvgmxiafqbttzysgjuswqtwuummkwmpzbfbvfqrxdmcccibqvpvwiqyuwpemtclgvoawawnmfxnwwtkovsjtyaxgbfjfigreejkcmikmnekbwwutoearbrbybwmiiwcjfqkfnhcffmcyhygyzmjntsmiakfazhcpoebpvflplsuqdedrjyacniwnmsbndlwscspbddhdhujzaygsvhdxfzafpcjxhswihcgwxmsvuoiofqbhpiwgodahuidhjvzvbcyfzdvoldkvnegaudjaqgxbqydiilboxwpzsnpjaahgldtygjnclgdrgqsnfewxnoszlacsapmanjjsyeobqlixesdchhurwnfdaulfxzxmvjyelkbwhcujtkehwzfimrmgjywqbcqhkbljmdlkmaojpopinzcftehyymdlhtagsjniraizteztvfgsjqrtpqqaodpcdziyndhkstqwmbbpwieopquvwngssrceyblrujvnfakrgewespqcyfwhimvkkzylzmpjbpqathvwdsawyezwdpaugapfzphrpttkgkovvgkcfsutkwafkcanjvewbcactwpmabwvqwfqjtjqftftdtyujdrbzinpflrwtdkqoowhykdvsamqpskjmlcrfwlyagplfkyruklmefobdipouunqyampoyscswxyajcoscsohuyynvwlmjmfzkefhtpgsylbhksmdumkfcnjuzfcqoorxqxntykcygwacrigmqurhfehklptxaqdzxnbecpxbcloamwzkfidjpiyxvqmkzgazqsbxubjvvtafekdhevvdtjusgmtahqyxofnzwysrczysnirraetzqpvikufrlqkvtdcqzczrywpcyngakwjtybmgsbjntkikbchpnobzvkgiemztkfuitxuqnvowivotavpvrhewxaqzueqveedjanrqmaunvsflsqodabkxpimlguuxbrgjwabulmccwnquikhtesuamwqdwlelambfppcvnvnjprhnfvoccgvfhfgfkgaegotluwsbeevibyxjoqvyyltyprbieexsxaczqsvkptqidtbskwddeayxnwhdlrrvyeplemrnhoquwvoexzjbtcapqpsncvsgrebzyxeahugdfvalrnthqamijjyoaxazaltgfilfnijwfckbaxaqvvfxvadxzfhjwefubhmajkozpjmphqkkdgsawvlhrhpbknfaerojjcuylnexaoxvupcvpxiojdaerjjyfhpmhfhofyklbmdccqcfajabdqwnmofytxdtqebkrhfcmjjbeoszcmhjqiwqdusnxbgrwbxqsbeeaqwcghejnpxzsuttwziyvrhczoghxqkyofqvhlgtecprwmpweblssaskxpyfctztfesdwfmonkiaggemytvuiimbwiyzvkvqrwqeiiwualkbvlmlzm"
# "zmnwsjyenpasgweuyoauhwlaktfjafynysysyvpqvuxubsmmazaaynqcexlunilyauxkptwklgabnhljeufxubxudaqksryodltlfakbxnconjwtftpiergjrruybrndzehshuzhujzpywnbizrqfocxypputgfvzklofibmkbgbtnwcnopjurjniyoiyxegtkuhokqwzjaoiwulaglzqfdiwpgexngyccdfmcxpwlvfapnjackkovhsgltennvzhlnnltswyqwekphubytnaymauoeldpvzsfdygdjzlxnrzfmbkfuhrlbnzxdauocnazwcnzvmdyhnkqhrqtcausdyrzphvdodvaseivocgjfrgpmfipedkbcrxainujhjbcowmtwjgkvejqbzmodrsqvpggtazreyelpmzrmccgrsfpfkxkhqcqbipnjbgdmnfrgxeaqoaoupzujkdjslrbxkjsdtbdkzgfkuugipsjggmkfeuqbhbwhxenlsionwbxdavcxketgdcxovnxzxsugxwumduwuurulzodszdlpdrzqucvwggviychlftjonyfteirmqwwswzembxxfrdwmqxtfukbjhnjeoesswjjhrcdqaxlfwculzgaldtehgnuxwipreoaouyoysvwqixwdinijnlaohudjpdyxgkpbibxsemelyexeswekrzotpjchqjumhyemnpkjnpqdwebdglywyeitqjxrfsrzaqxnoxvwgwjhiolrwoianfompncdpzhsealigffoxwvqzupvfbtqlrmntiwrdfixgvivxreqtiznzkrbzqcbidwwvvwqrwyvsmeyezjzkvummfpwipiixcpblfdgirhfoqrjnzzgdiunyidcfdgpmbokckneitgsgpnobahafizwqlfqprtwogfzolkmtrhvdtucvstazkyuqhdglgohvwvpjycbsduhtjfezjrjfuvoucmibwijcpwkaehgtnjccjtcjfjgrcubitvgaocwuscmbijrqkokrcdtelcrovgafbzsgswtwumkvmbqvimcganmfwwtjxfjfeejcnkeabrbywchmcygnahcoebpvflpsjninmdspdhdhshxfzfpshcvuifbhwaujvcdvlegayiozaaclgqsnwxozacaaeqednaufxxmhuthwfmybcblmjpinzhmhrtvfsjpqqodinbbpwipuvsseufrgespcwkkmqhezpgpfztgvgksutkvawpwvwfftyujblwdqowdvaqslcrllfefbdmpsxoscsoljmzetpgylkdukzfcrqtrgurhfkxbclmwzfidjmkaqsjvafdeusmtayonwrcsnrefqkdqzzwynakmntkpnobkgiuituqiovvrhewxzedjarnfsakxrgnquiktsalvnrhhfggeousbevioybesczvpttsweanhdlrrelemuoxzjbaqcgrbeahugantmagfnjwkxaqvahwujkojkdgavlbfjjynxpjyhfmqcfadwtqerhfcmjeozmhqxeacghnpxstwzyvrcgxyqvlgecwwlfdytibwvqikvlml"
# [4047,2765,2735,3409,3246,2305,87,2037,1993,1332,522,3374,2896,3044,2968,2650,1505,285,991,3356,387,981,378,1325,952,1177,3429,3846,765,2381,1742,407,1438,324,2585,3821,3861,287,1709,3420,3716,2991,2057,3740,1634,1417,1080,2270,3412,2975,357,1189,12,3865,261,3150,2089,385,1171,1223,3757,3444,1288,2318,3906,1675,1038,3857,1168,1224,3380,936,1822,2531,580,2171,1001,1609,909,2890,511,1838,3730,2844,3866,256,1641,2220,2251,3988,599,3428,694,409,394,788,2320,2359,2888,3485,2433,825,1926,1221,3381,3239,2040,498,1890,1127,712,2143,1991,1879,41,3293,128,2545,3611,568,494,2476,3871,1297,2645,1624,140,586,2940,1860,2664,3162,2675,1899,690,405,558,2893,1743,2674,627,2634,544,2454,2452,581,1735,398,996,1900,873,3802,57,902,1154,1648,3480,1343,116,335,2628,3334,461,4009,2132,1451,3191,1218,2526,960,3930,816,3919,3826,312,2360,1466,2677,2830,3187,1919,3926,510,1462,3053,1613,83,2439,3174,333,1019,874,3685,901,1760,2169,3189,1796,1009,2014,458,2980,4025,3129,2084,3915,1571,2081,3651,4026,2712,3782,2463,1958,456,3314,3574,3306,2973,2574,117,911,1815,846,1347,1959,3415,1108,1000,3108,1182,1037,2892,1335,2073,2698,2758,3941,1353,1397,863,1398,3572,1669,1898,3738,279,1065,3395,1136,3607,3,3342,3905,2315,3508,3667,3855,1812,834,3911,738,2056,1606,2700,3823,2096,3645,879,2138,2807,2501,3476,2929,2795,3140,2626,2885,3249,2798,4024,3064,1699,593,2992,2304,3295,1084,912,811,1068,1349,2633,265,2431,1286,1389,2571,2200,3780,516,2254,3271,1974,542,2895,2553,3850,3096,1964,1486,88,289,1712,3893,349,3668,1077,111,1424,3285,1801,1166,3856,1183,2382,471,2777,1452,2337,114,2720,353,1922,718,1902,1358,3473,3083,973,1779,2502,3369,1321,2619,3102,2967,3595,1949,4042,1824,2659,2063,2912,3656,1015,1565,1257,2314,523,3182,2726,1300,2524,3868,2598,3020,682,1086,371,817,1794,604,178,3792,614,1909,1113,1698,1495,4031,1515,883,250,3748,276,1184,2684,2499,1615,2212,63,3949,2690,1230,3771,197,2128,3081,2234,2209,3946,274,2186,3577,1122,2901,1785,2354,3847,1063,3643,2403,1109,2259,3142,3266,616,1557,2705,3499,2683,2029,1708,169,3071,771,3047,430,1939,2928,2107,3472,496,1658,624,1546,1520,2603,1471,3099,1576,2548,203,3268,2580,2954,432,3121,3888,890,2835,36,3204,2484,1260,2389,2779,2256,4011,3534,1797,2657,3708,848,3171,3474,3115,983,2594,3781,2560,3159,3652,1845,1665,929,2121,3263,1180,314,1097,3463,2956,3462,3035,3514,2483,1863,1467,3358,900,2544,938,14,1473,955,1091,685,1758,2868,2426,4029,2725,3343,1568,978,3533,3403,3688,3501,3178,545,2218,384,3194,2505,3875,648,1373,489,1664,3049,2328,997,2148,1362,3920,1056,3245,3936,4005,703,3015,3007,1463,3101,1710,1829,4001,1987,2810,877,2951,2481,2635,1663,1793,2593,1213,3219,3617,3451,1202,1251,3543,2366,1573,3110,3798,248,484,3364,136,3168,1872,1518,2564,1453,2353,3701,2306,729,3532,719,3774,769,692,1194,613,1978,1007,3238,1677,316,3833,1953,3240,600,2618,3754,2861,1647,1228,1522,2693,2932,2764,3519,3324,1229,3859,2119,1167,2833,3664,3797,138,3351,3576,338,934,3161,395,3326,3873,803,1653,615,2827,1433,943,2482,1569,2933,3489,1426,1995,217,727,1434,3139,1704,858,30,1058,3756,533,1721,144,2749,3028,1524,1408,842,1529,67,897,2520,3634,2492,2647,2710,2418,1165,1823,1004,3126,1915,2402,1110,2529,2208,3260,3360,1313,701,3897,2819,2639,1881,359,3564,55,3370,1513,360,3399,3724,1491,2027,208,1299,146,1123,3009,462,1145,2670,3828,2496,2303,855,2300,824,3076,115,3753,185,3925,3550,1536,2339,1498,2158,3184,1083,875,1659,976,3210,3107,3998,4012,299,1384,2917,3615,362,3478,1324,47,1011,2937,933,3674,2600,332,240,1312,3547,2398,2630,2298,480,283,741,1738,2400,990,3237,898,3986,1421,1357,591,1748,1519,705,2863,3869,3120,2941,127,3553,739,2894,1112,513,2641,1839,1983,441,2443,843,402,657,1650,309,2717,786,3218,945,1639,3715,2449,2350,2965,436,223,887,2891,2082,3803,2507,2654,479,2404,3675,196,1833,2497,3109,2622,995,3621,3147,3702,2537,3357,2721,2767,2375,3323,499,177,3832,3091,232,150,715,3552,1217,3148,3589,903,1220,1733,1399,515,2401,2910,3021,1680,399,2377,1320,1073,3761,3604,159,1947,763,3153,3974,1334,2876,2959,2792,553,3353,830,1631,1765,3455,2961,1281,847,3849,3092,3585,2856,69,1460,3993,2714,1711,1782,1676,1889,1719,1135,783,3996,4004,1600,3365,1847,77,3599,1502,2718,3023,2078,20,3695,2848,722,1175,31,1809,3475,3922,0,2528,66,215,1757,1064,2264,2733,408,2395,2522,2494,2579,4032,1965,1948,4028,2926,3318,2816,823,749,3610,1564,2878,3765,386,869,2269,1512,3058,3570,381,888,1393,1274,3328,980,2503,918,166,1107,148,3012,3309,3820,1944,2067,2345,3469,49,3004,540,3842,1258,2781,699,2384,3202,184,552,3355,3561,3622,3732,3027,1816,3332,1139,2151,3143,2425,3879,970,1197,937,1633,364,1162,1988,1950,3457,3592,3224,2237,2438,2867,735,2938,1778,2925,3446,3195,1559,3019,3491,3511,3980,27,2153,2703,927,1561,1936,270,3686,3618,1739,673,2575,2364,278,2697,3235,913,1379,2678,1121,2457,80,4007,3670,575,3554,2995,346,1137,4017,3275,3400,2346,609,560,319,1016,669,3962,2570,1537,2908,3494,787,979,799,2882,630,1215,3282,1577,731,1731,1523,2869,1517,3796,4019,3288,2210,2506,707,3117,2408,744,2741,1725,3591,3338,1662,3658,3845,3335,1509,173,22,3999,2451,3078,2001,3931,740,108,2668,3886,3965,3928,3337,2939,2656,2332,3312,268,1018,3495,698,3605,129,3971,2083,3914,2410,3488,2429,3513,3722,191,271,3384,123,3682,207,2569,2223,2041,3835,1098,95,512,2669,1407,420,1255,1830,1906,1972,3598,3036,1259,3870,4003,1692,352,3567,3848,464,3854,3606,2963,605,2864,2931,3542,2981,313,2335,3297,3244,649,2567,3228,1290,968,2466,1580,3302,2740,1102,311,1377,1351,3154,2566,100,1012,2085,3273,2120,391,1156,2546,3917,1385,1753,1605,2338,1105,3614,296,210,1483,447,297,3710,1593,152,1237,885,3016,625,171,1114,3203,1144,2498,427,3984,2769,2392,4038,2923,3894,1842,1686,3880,2316,2184,481,3298,3578,2033,120,1917,2133,1811,3287,1572,2284,3806,2587,3408,1153,2197,2203,2914,1005,2919,182,2796,3199,322,2552,336,3010,493,2006,1869,198,755,155,2837,3481,2055,3697,1805,3041,3267,3521,2606,1734,3887,3329,3751,565,3594,1903,3432,1607,3043,410,3932,2699,3205,3960,977,2183,3445,3383,419,761,2156,4000,2104,3815,3208,3644,2058,1249,1225,2074,188,2182,3775,2233,2309,688,3531,1740,193,487,2573,2845,35,1464,564,3426,368,3597,1895,2235,3141,220,1673,3752,3406,1566,2076,259,2177,3661,73,2590,1226,2142,2112,1531,1880,3995,102,2644,1636,3226,3795,641,2688,2226,1702,105,2172,2900,866,2363,3882,3484,2702,895,1700,3257,1792,999,2032,2459,2261,3179,2746,3000,3924,236,3433,1525,1489,3758,141,104,3788,34,75,2023,2010,2839,167,1205,3069,1654,881,1331,2800,3600,3810,1832,1211,1989,1210,2420,2087,2948,1625,3404,3284,1481,1508,112,1446,1149,176,1528,2045,792,3362,2035,2155,334,752,2176,3487,62,2323,946,1907,1541,3563,1905,3565,2095,2178,2115,1342,3948,3837,622,2866,2787,2406,776,3853,1670,2516,768,2379,2030,3177,328,1307,1492,2419,3571,3544,2621,2245,2518,3747,1587,3648,3864,504,661,403,422,3200,290,1678,89,1689,662,1278,1017,1997,1034,2385,713,3640,746,3991,588,1152,2331,1923,3079,1479,2009,3005,1656,3125,2194,2772,2434,3018,3248,2444,2879,563,639,3862,3085,2399,2601,3410,3786,1602,3843,3170,2512,1626,453,1181,650,819,1401,1775,3535,760,1896,4036,1617,3450,58,3983,1971,764,2722,526,1672,2510,3559,2730,2607,919,1552,2441,3160,2229,766,2734,3959,4008,1955,964,2285,7,1371,1671,1450,133,1807,1706,1963,1338,969,2231,1589,1354,3135,2738,1365,3677,3653,97,680,3026,826,3968,3055,1726,3921,2175,1894,655,2809,791,2853,2713,3331,1666,706,1101,1391,2114,1328,1539,2423,1157,2561,2584,1470,2673,4033,654,325,3650,3261,2539,260,2075,736,689,2250,375,3113,1053,190,1771,415,2825,3503,1305,2768,3562,1960,497,126,503,211,2996,1405,1695,3130,1503,1870,3062,759,3243,798,557,678,219,2671,3742,1484,806,19,3890,3454,635,2054,1207,1772,572,762,651,2474,2620,944,1386,3024,2002,1984,904,1116,4010,3336,3438,134,44,3169,3229,1372,2743,3133,267,1632,663,1652,4021,2297,3375,2159,1246,574,2154,1730,4,302,282,125,2079,1222,2188,2413,1803,1062,3025,3923,3276,519,2473,3548,1179,1023,1442,2062,448,231,1707,3927,3166,3746,3560,491,1506,2834,2642,3255,2736,2097,3793,922,671,828,3145,3933,2648,3419,2691,2103,1720,683,1036,3863,3286,1104,2623,81,2106,2854,1477,3705,1937,1956,434,2111,307,988,3441,3528,3006,853,3659,3889,1754,2616,24,4037,2108,393,974,3084,2850,1178,343,3502,723,143,46,21,2238,3636,1008,2435,1130,3037,1309,2614,779,1848,3104,3382,122,1088,2260,1437,3165,2480,3838,90,163,1507,200,2217,1932,839,1768,275,3813,3259,1078,212,2105,2958,1567,2884,3393,3193,2873,2855,160,3230,2291,3633,50,1487,3442,1346,214,1043,2004,1570,9,2692,435,2972,3655,372,1046,1150,2817,2804,2013,1263,2295,2292,2445,1151,1935,3274,1010,3629,3051,876,209,674,942,2437,2139,2549,658,2322,3707,2447,860,433,3032,2568,3056,107,2343,3500,3987,3080,932,2427,2562,2228,3977,495,3013,3779,916,1186,1986,1275,3556,1360,1052,1444,3704,2556,1277,354,3683,2532,3361,1082,3892,272,3198,2051,3602,99,954,894,1148,1227,1060,3827,1185,3516,3186,653,2239,2412,2682,2572,726,3439,2137,1040,4018,3470,3290,3173,1820,4040,2268,1250,103,1904,748,3070,829,1885,697,2638,1319,3348,1705,2875,2162,1254,2025,444,3990,967,3720,1143,2504,870,3222,2663,1247,1311,3785,3308,857,2367,295,225,1381,3772,389,3033,109,1649,1741,251,3807,3739,1295,756,507,3536,3916,2793,1049,3874,3448,2440,3052,1448,3087,3763,3504,1415,2775,2386,1206,2288,3760,2160,304,1548,3824,2053,1846,3725,832,1642,2701,201,4048,2257,1117,1584,3349,2333,2632,2216,2036,1875,380,1819,2761,1241,2348,1674,1504,189,1423,48,1888,579,2902,1465,814,1942,2889,2986,443,2334,363,2977,369,3247,45,1482,2222,3957,472,3118,3631,3185,1409,2745,1436,660,2595,2841,757,3411,637,317,767,2776,1087,1966,2629,3540,1243,2610,592,2424,320,2858,411,3819,131,2907,3942,3029,3840,3593,539,1364,1526,3978,3646,2446,425,3269,469,1045,2521,1239,1284,626,3394,3352,2185,4039,2731,611,2246,2390,546,2999,1432,1199,850,652,1931,1204,2695,1059,3387,3354,1163,2820,1968,710,1235,2163,3681,2541,1041,3910,809,2583,1416,2362,1303,440,3132,681,2563,2840,778,339,1047,70,3443,634,1588,1655,536,1089,1190,2870,521,827,3214,2627,2017,2586,672,1777,1857,3045,2206,135,298,65,2955,2906,1439,1270,2290,941,3460,1027,844,1368,3057,1271,2380,2283,693,3512,3964,1209,1030,3103,1808,2763,397,2655,3363,244,959,3088,2491,3579,1787,2296,734,958,1128,514,2330,2762,3603,1681,2432,3479,1594,3317,1511,3379,3768,2312,867,1688,607,2791,2724,3649,1140,442,3759,2760,3787,3620,4014,3465,3601,1585,1072,1472,1403,2024,2279,3164,1660,1376,1578,1592,1100,2971,3545,1327,3496,1790,2519,3234,3188,2957,3163,53,2739,2110,3898,1458,2136,2922,2293,2924,2487,1173,2589,1147,1897,1314,72,1933,2517,1070,1025,872,326,1831,2554,3663,382,1892,3424,1187,2993,2465,775,2091,1871,3937,644,205,1755,6,1521,1608,3731,3114,2428,1287,2831,2782,2065,3805,348,797,1727,679,1877,2313,1447,3575,1645,4034,3989,424,647,3258,2247,2883,1323,2102,1996,2461,449,1035,2942,451,2794,2555,2542,3852,1550,3627,541,2849,474,2530,1003,286,241,5,429,524,361,3122,1767,1422,331,3583,119,253,3992,91,1810,2101,3333,428,1126,3953,3619,1752,2281,2149,2,1074,2018,465,3808,2150,2576,3703,3466,1994,3072,110,730,1160,2985,643,486,255,1685,183,837,2166]
