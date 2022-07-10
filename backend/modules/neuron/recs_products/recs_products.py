from random import randint
import numpy as np
import pandas as pd
from sklearn.neighbors import NearestNeighbors
from scipy.sparse import csr_matrix
# from app.extenstion import db
import ast
# print(db)

ids = [2217, 635, 551, 2852, 2365, 1602, 2125, 371, 2840, 259, 1275, 1685, 1884, 1600, 2543, 1486, 626, 2518, 1810, 2431, 2569, 2416, 1431, 1478, 2701, 1727, 1697, 2560, 1995, 961, 2145, 1570, 399, 2824, 173, 1072, 1068, 2436, 1321, 425, 621, 1328, 1086, 2748, 2811, 2345, 2530, 1558, 1315, 1896, 1838, 244, 1903, 148, 1440, 1304, 2950, 294, 2120, 1955, 2147, 1107, 413, 2653, 2065, 1593, 165, 856, 237, 1490, 2222, 1698, 2007, 1917, 516, 989, 2258, 2500, 1243, 206, 2901, 709, 192, 153, 1492, 2951, 712, 2428, 488, 186, 2746, 1552, 2647, 193, 655, 829, 1229, 2871, 811, 1230, 507, 1728, 450, 1318, 1415, 1713, 2625, 1526, 2915, 2240, 2285, 2253, 394, 1619, 2011, 863, 2762, 564, 1005, 2478, 2035, 1191, 2837, 48, 300, 2421, 171, 2009, 348, 428, 625, 801, 599, 1135, 562, 2681, 1131, 1575, 366, 390, 476, 1973, 1609, 1730, 796, 1023, 2517, 1358, 1032, 2599, 1228, 453, 15, 1958, 254, 1114, 33, 509, 1540, 2301, 864, 2803, 2270, 2480, 392, 253, 221, 217, 1250, 1226, 2481, 2576, 1012, 2971, 2822, 1434, 2896, 1147, 2512, 2933, 2889, 2251, 1538, 979, 1957, 537, 1374, 2589, 2287, 2078, 1467, 2316, 224, 1477, 344, 2973, 2296, 1717, 1732, 2220, 2373, 880, 1081, 729, 435, 1162, 1949, 892, 2069, 2974, 2594, 1868, 1741, 1900, 1607, 2353, 1174, 2341, 2498, 706, 545, 1748, 2290, 549, 1171, 2562, 1937, 2340, 622, 2447, 2348, 2858, 1372, 418, 1753, 57, 2052, 1411, 1366, 296, 2213, 647, 2199, 501, 761, 1752, 1664, 2225, 2910, 168, 2883, 1217, 2387, 2276, 2673, 1952, 1256, 2494, 386, 1971, 996, 2282, 1290, 2218, 1747, 898, 2612, 2080, 2677, 1356, 2514, 1603, 569, 1187, 968, 1360, 658, 268, 169, 55, 374, 2202, 1817, 2657, 309, 698, 465, 717, 2396, 2826, 2163, 674, 64, 1303, 2223, 5, 1423, 1660, 2206, 821, 2877, 138, 1028, 651, 1213, 1935, 1874, 2618, 17, 1829, 2839, 895, 2730, 2563, 1120, 114, 1568, 1631, 1587, 2374, 1537, 1002, 2801, 1494, 1792, 20, 1982, 1683, 668, 849, 873, 876, 1872, 1531, 416, 1322, 2948, 524, 1495, 1596, 2031, 2475, 362, 283, 29, 1849, 1554, 436, 1534, 112, 2779, 544, 27, 2226, 871, 144, 248, 2571, 1990, 2501, 2417, 1416, 2401, 25, 1926, 868, 1977, 2821, 481, 1264, 2994, 2770, 2875, 2516, 454, 2885, 1945, 1694, 1938, 2247, 1767, 587, 632, 2583, 1371, 850, 1887, 2912, 1373, 2936, 2597, 827, 2281, 694, 1891, 2469, 2150, 2902, 583, 1117, 1008, 449, 1483, 2391, 340, 1281, 1143, 580, 2135, 1826, 1796, 578, 1544, 2142, 1251, 2390, 279, 1185, 1255, 2842, 2680, 2878, 2023, 2969, 2362, 1177, 2978, 2627, 172, 575, 630, 1192, 2356, 1744, 543, 1890, 1, 2020, 2568, 805, 2208, 970, 2016, 1768, 2227, 1999, 907, 1297, 2884, 1850, 841, 2060, 1276, 214, 908, 2849, 2556, 2977, 2164, 718, 1652, 2131, 46, 1820, 735, 2047, 2372, 2094, 1613, 2479, 955, 2768, 1639, 1573, 285, 644, 911, 2161, 1203, 2655, 1765, 2013, 1905, 785, 522, 2355, 1209, 2892, 822, 542, 1102, 317, 89, 1122, 1274, 2058, 789, 2893, 1103, 2174, 2395, 2916, 1655, 2577, 563, 2818, 314, 1653, 2759, 2507, 327, 1336, 669, 397, 1476, 1405, 1812, 2838, 1436, 584, 1711, 1794, 2610, 1123, 692, 0, 2946, 2927, 157, 1170, 1519, 1293, 287, 2753, 612, 858, 916, 517, 1403, 1301, 1632, 2001, 1974, 1067, 265, 852, 643, 1867, 2170, 1923, 2375, 714, 2652, 1962, 1058, 833, 1404, 2260, 1421, 2134, 1888, 106, 2141, 803, 557, 574, 512, 2763, 2804, 1967, 1816, 2800, 2557, 2720, 2696, 2440, 140, 1582, 235, 489, 311, 1172, 1484, 2867, 361, 1465, 884, 430, 2288, 737, 2054, 1599, 1581, 1249, 2688, 2650, 897, 19, 2212, 2370, 1362, 2128, 1333, 663, 2731, 444, 2700, 234, 1621, 2622, 1089, 901, 2790, 2452, 2196, 469, 2361, 2796, 2019, 1119, 904, 1848, 1383, 1860, 117, 1000, 1222, 1125, 1577, 725, 592, 683, 2369, 1590, 2477, 1722, 680, 2283, 2399, 2810, 1474, 1846, 1085, 1347, 795, 550, 56, 1025, 1501, 116, 2468, 1482, 2900, 2198, 297, 2694, 565, 2794, 736, 2465, 156, 1271, 798, 2344, 262, 2138, 2648, 560, 2708, 299, 1453, 2311, 1022, 1044, 1433, 2789, 2537, 2660, 1535, 2833, 2386, 1528, 770, 1710, 1062, 75, 2953, 593, 589, 2347, 2299, 2986, 754, 2876, 2542, 978, 2176, 1313, 836, 1782, 702, 1443, 2438, 1133, 499, 2797, 510, 2033, 2939, 2112, 164, 2351, 2064, 732, 7, 2126, 2624, 442, 2116, 990, 963, 66, 1875, 459, 521, 180, 2423, 1108, 2609, 2350, 2630, 1200, 686, 2685, 1771, 763, 8, 398, 1257, 2868, 2942, 1173, 2586, 746, 2904, 277, 616, 132, 947, 338, 576, 984, 581, 1584, 1442, 1389, 2343, 2041, 2405, 1546, 2148, 929, 603, 52, 1118, 54, 1605, 2947, 924, 2068, 1427, 869, 195, 2000, 2574, 2829, 2831, 786, 1344, 402, 1370, 2706, 1975, 308, 2747, 2377, 1798, 665, 2613, 1986, 1156, 2037, 2957, 1630, 2565, 1284, 1547, 2937, 2646, 2044, 2324, 2313, 1244, 2119, 685, 1198, 815, 1232, 1272, 909, 1690, 1506, 2940, 1858, 588, 2845, 2558, 2663, 2959, 2529, 2211, 2197, 2898, 2393, 2289, 196, 2584, 2711, 2129, 2553, 1985, 645, 447, 2237, 1220, 2967, 1626, 697, 1233, 44, 166, 2482, 846, 667, 1522, 1950, 2413, 762, 130, 2224, 1861, 1906, 2189, 1970, 2785, 2872, 758, 982, 532, 40, 410, 2769, 1168, 2143, 1296, 210, 843, 1097, 865, 1835, 1312, 2592, 1438, 662, 2626, 331, 1992, 890, 216, 1742, 2645, 2082, 649, 1787, 1703, 699, 1132, 260, 190, 2972, 1153, 47, 2980, 1093, 170, 354, 162, 2999, 629, 2021, 657, 721, 696, 1316, 2736, 1936, 743, 2911, 2703, 229, 2825, 198, 1314, 2906, 2427, 1645, 3, 363, 22, 461, 1919, 2327, 1622, 2813, 2207, 2860, 1723, 986, 633, 498, 2691, 376, 1541, 734, 506, 1654, 1580, 2408, 2250, 2855, 2739, 2882, 1020, 2970, 1381, 185, 952, 2046, 125, 2774, 1407, 1327, 950, 1948, 16, 903, 713, 1979, 2067, 97, 861, 503, 2814, 2451, 809, 2245, 2203, 2303, 2113, 611, 502, 831, 2913, 1578, 2672, 1410, 339, 1882, 566, 272, 456, 2309, 1920, 1150, 1912, 1662, 1598, 703, 1843, 1199, 1345, 2767, 2777, 324, 1808, 1707, 1432, 2328, 343, 2359, 2441, 985, 199, 2081, 776, 2775, 2108, 2397, 1764, 263, 1193, 2062, 1038, 464, 1648, 932, 108, 2415, 2090, 751, 2029, 1994, 828, 538, 2462, 1472, 936, 1831, 752, 2028, 2954, 999, 2835, 1993, 1306, 634, 1651, 92, 2894, 211, 1907, 1289, 1349, 2661, 330, 2961, 1545, 2684, 2346, 1669, 2658, 351, 274, 1561, 1414, 838, 159, 727, 2149, 2520, 872, 2601, 212, 1287, 1574, 2513, 1195, 2843, 2996, 1240, 2689, 1115, 919, 1634, 2817, 163, 1583, 1780, 1245, 2602, 356, 2367, 1402, 407, 1803, 1733, 2133, 1305, 944, 2232, 595, 2414, 1444, 437, 479, 411, 1261, 2238, 1136, 2799, 1597, 1624, 1090, 2793, 2378, 2593, 641, 2881, 1094, 1088, 2823, 806, 2925, 1238, 1332, 1847, 1268, 1684, 99, 61, 128, 1987, 2888, 1687, 2670, 95, 866, 1726, 2616, 2002, 2710, 1151, 2279, 2442, 2718, 606, 1536, 1859, 215, 2721, 2366, 2983, 600, 415, 2798, 675, 2890, 528, 2200, 155, 9, 2975, 207, 98, 1997, 2083, 1060, 191, 2964, 556, 2528, 2765, 2615, 383, 276, 2642, 1212, 1285, 1834, 2474, 1947, 113, 2298, 158, 103, 2830, 141, 2667, 1902, 1052, 2989, 2314, 2519, 547, 257, 2807, 1130, 2834, 2219, 1035, 2400, 648, 2526, 1516, 1408, 637, 1104, 37, 1715, 389, 536, 2628, 491, 607, 2547, 2144, 2235, 147, 2582, 899, 1034, 2992, 1326, 1197, 906, 980, 1617, 966, 2450, 2231, 2339, 705, 203, 2572, 2982, 1241, 2908, 358, 2781, 1386, 925, 2160, 1448, 2319, 457, 2511, 1837, 2806, 991, 2272, 2329, 881, 812, 921, 1291, 1202, 2573, 1827, 2443, 2177, 63, 1751, 956, 930, 1671, 32, 318, 1828, 2943, 1702, 1569, 1036, 21, 508, 375, 2515, 620, 2205, 2307, 1562, 448, 627, 1461, 1140, 1398, 2741, 2570, 2077, 923, 1365, 1548, 2891, 1382, 2269, 2075, 2772, 2403, 2714, 1754, 2115, 1758, 414, 1841, 2275, 1761, 2847, 94, 352, 2985, 1159, 1364, 1635, 2991, 504, 231, 2965, 1481, 2546, 13, 2752, 1065, 315, 1330, 1339, 2805, 1650, 1825, 2758, 1946, 1914, 604, 2243, 1295, 62, 1940, 82, 2495, 653, 1842, 1464, 2053, 586, 1704, 1505, 1031, 1893, 1298, 369, 2398, 41, 839, 1390, 889, 650, 28, 2490, 51, 808, 2905, 2363, 2304, 2935, 1049, 2153, 360, 1968, 365, 767, 1503, 202, 965, 1311, 784, 10, 1101, 2550, 230, 1310, 1623, 4, 654, 2228, 2284, 1027, 1604, 1040, 2127, 367, 2034, 255, 240, 1533, 310, 2317, 2816, 2619, 757, 298, 745, 400, 93, 2315, 1208, 1564, 2406, 690, 1725, 2585, 2310, 2114, 472, 1934, 143, 659, 2342, 1797, 548, 949, 1880, 167, 513, 2600, 933, 2215, 2432, 1280, 1235, 514, 891, 1450, 1064, 467, 823, 1428, 76, 1814, 958, 726, 151, 2146, 2808, 922, 1161, 1148, 976, 2828, 2879, 1943, 1791, 1457, 832, 490, 939, 150, 1324, 1513, 85, 2856, 2687, 701, 245, 323, 1509, 232, 1869, 2750, 1901, 642, 2679, 1343, 1959, 2419, 2788, 2306, 322, 1659, 2579, 1647, 1779, 2742, 1928, 1309, 1387, 704, 619, 977, 1437, 728, 1393, 2692, 1925, 2, 2832, 526, 486, 957, 530, 1412, 1406, 1178, 2488, 1105, 1059, 1627, 154, 826, 1385, 1424, 2312, 2559, 1743, 2864, 1876, 1057, 2554, 2210, 1259, 2026, 409, 1700, 1873, 1805, 1015, 1507, 2334, 2499, 988, 73, 388, 525, 2644, 2084, 760, 636, 594, 1278, 2737, 2778, 1078, 1854, 2383, 1989, 1864, 2087, 182, 1699, 1674, 111, 818, 791, 2277, 676, 2384, 2743, 2722, 441, 1166, 2158, 741, 1334, 1137, 1586, 2335, 2552, 2073, 2458, 1430, 305, 2914, 2489, 475, 1643, 912, 1376, 1395, 1247, 1216, 2209, 817, 937, 209, 2330, 887, 246, 2259, 53, 1693, 511, 445, 781, 495, 30, 1517, 2815, 738, 1167, 1439, 1418, 1549, 1070, 1007, 2422, 2675, 2733, 1749, 474, 1037, 382, 2292, 554, 2015, 1391, 412, 2085, 1571, 1466, 797, 2850, 2066, 1633, 1014, 577, 1978, 1099, 2887, 910, 2103, 2322, 905, 1594, 2676, 2050, 1323, 2598, 1215, 1550, 1863, 2662, 2104, 700, 270, 1793, 2632, 948, 1363, 2792, 1511, 2273, 2605, 2107, 2690, 860, 1201, 1612, 1368, 243, 711, 1307, 671, 940, 883, 2836, 688, 2492, 45, 1163, 2564, 1894, 1112, 1214, 960, 2239, 810, 672, 1157, 68, 60, 1806, 1098, 1657, 2402, 1456, 183, 715, 377, 888, 1972, 1325, 2098, 825, 118, 2533, 975, 2561, 1724, 1576, 142, 2666, 1083, 2265, 2751, 2846, 2820, 275, 1419, 2092, 304, 2596, 1029, 687, 2926, 1553, 1966, 326, 2704, 1832, 1479, 1426, 1789, 1512, 602, 2923, 1246, 610, 2640, 423, 1485, 1489, 920, 391, 1092, 1463, 859, 772, 792, 152, 1981, 434, 1681, 1716, 1144, 716, 2566, 1113, 2523, 2635, 902, 1004, 2483, 2463, 1016, 2783, 1152, 1737, 1508, 677, 24, 1785, 2723, 452, 608, 973, 2715, 1870, 2506, 2639, 2749, 1591, 2157, 775, 1933, 1019, 1369, 2444, 2221, 451, 1018, 1944, 2617, 303, 2349, 707, 1675, 1865, 1514, 1399, 1441, 2167, 252, 1740, 1158, 1618, 71, 1530, 631, 2032, 1821, 2261, 1677, 1111, 1939, 628, 337, 2229, 1051, 90, 1824, 1942, 1889, 2155, 2076, 2172, 419, 1862, 188, 765, 136, 1224, 1128, 1736, 281, 2175, 1260, 1629, 161, 2124, 2262, 689, 2870, 2719, 938, 2433, 855, 1013, 2297, 1471, 972, 2844, 783, 1043, 1340, 992, 2934, 1637, 478, 664, 2074, 2105, 179, 2429, 1788, 2055, 800, 65, 2010, 1352, 529, 2549, 518, 1223, 1056, 1109, 1895, 615, 2111, 1644, 1179, 1682, 213, 2745, 2984, 2184, 1712, 1783, 2509, 1470, 1830, 596, 2771, 2140, 2392, 900, 1446, 1916, 1211, 2641, 2252, 1459, 336, 39, 2738, 558, 2376, 443, 236, 1984, 282, 1066, 1818, 11, 618, 722, 2995, 807, 2861, 1299, 614, 1800, 579, 1833, 1786, 764, 733, 2955, 1237, 854, 2457, 470, 1351, 582, 2536, 2637, 2091, 995, 284, 477, 1050, 913, 1017, 2102, 749, 2030, 2607, 2709, 1608, 69, 1346, 2960, 1572, 2186, 484, 2267, 773, 2928, 267, 316, 2388, 1219, 1646, 885, 742, 101, 2776, 2248, 830, 1649, 2352, 2089, 1913, 2389, 2354, 1729, 1961, 1397, 1910, 1010, 1965, 1227, 1615, 455, 2014, 1718, 571, 187, 2551, 2326, 840, 1696, 2979, 981, 1638, 2664, 492, 184, 1269, 2863, 1445, 2993, 882, 546, 1927, 494, 223, 1184, 2152, 896, 353, 1253, 540, 2654, 403, 1745, 2587, 935, 1679, 2854, 617, 2476, 2271, 2473, 1777, 100, 1196, 2764, 204, 2555, 2424, 1755, 1375, 1359, 2043, 2280, 2088, 422, 1350, 934, 1763, 242, 247, 2987, 1518, 319, 1100, 2263, 290, 2486, 2531, 468, 2990, 2487, 2121, 886, 2274, 1204, 2190, 994, 1769, 1695, 473, 1401, 2181, 2857, 427, 639, 2101, 1592, 2246, 205, 1866, 2255, 1270, 914, 1666, 2693, 460, 1480, 2727, 1266, 834, 2183, 2917, 36, 2903, 2716, 80, 131, 432, 2325, 2521, 1819, 2357, 842, 373, 2323, 1839, 1262, 433, 58, 485, 837, 2455, 2472, 967, 2360, 424, 638, 2188, 527, 249, 104, 2782, 2459, 387, 2944, 1954, 851, 682, 2780, 2945, 1011, 2809, 1804, 1462, 2651, 226, 273, 1878, 1770, 2734, 1836, 1095, 1236, 666, 1784, 115, 1852, 1845, 286, 2678, 107, 2539, 1258, 334, 2525, 1239, 1286, 355, 2886, 1160, 2865, 2268, 1378, 18, 983, 971, 96, 1757, 1396, 2381, 2154, 1772, 500, 1046, 1776, 2656, 1556, 601, 1555, 1420, 598, 1813, 1367, 1668, 1931, 2057, 768, 26, 1460, 1918, 271, 2005, 946, 1960, 1799, 1379, 2122, 289, 1263, 127, 790, 175, 2256, 345, 964, 2194, 1924, 568, 1908, 2508, 2623, 1853, 723, 1279, 1823, 1055, 201, 2242, 149, 1640, 2051, 2668, 2109, 181, 1705, 780, 408, 2717, 1273, 1567, 2611, 2705, 535, 1735, 799, 878, 2674, 2244, 1134, 1983, 439, 2581, 2006, 519, 1155, 1879, 1980, 1265, 1969, 1520, 462, 160, 269, 79, 731, 2439, 2873, 2042, 77, 225, 1182, 1493, 987, 241, 570, 2532, 1292, 2236, 539, 1932, 197, 2862, 2132, 1468, 1815, 2454, 357, 137, 78, 1248, 605, 590, 1377, 691, 2766, 2682, 1692, 2171, 1206, 1077, 320, 1543, 2812, 302, 1840, 673, 2924, 2504, 2446, 1525, 421, 2874, 1110, 1189, 1388, 23, 1082, 2757, 349, 1294, 2629, 845, 50, 2761, 2302, 1738, 2869, 1620, 2099, 1021, 1342, 974, 848, 123, 740, 2048, 2453, 2118, 341, 1106, 1425, 385, 384, 2802, 1026, 1091, 804, 2538, 1497, 2931, 656, 378, 1422, 1807, 105, 372, 1075, 2695, 31, 480, 684, 2308, 2958, 1455, 875, 2241, 505, 646, 1361, 640, 1680, 1142, 2008, 38, 1686, 515, 347, 993, 1491, 1892, 81, 553, 405, 74, 2725, 2760, 2300, 14, 2056, 1857, 2097, 2697, 1409, 2497, 894, 2180, 2254, 523, 6, 1658, 440, 2952, 2921, 139, 1071, 2061, 2510, 561, 2293, 2337, 2897, 1127, 1911, 2496, 278, 1951, 2929, 280, 1542, 84, 2162, 2434, 1354, 49, 227, 2466, 2631, 918, 1053, 853, 2754, 954, 2435, 1811, 102, 2535, 1778, 2169, 2724, 2591, 2880, 59, 1129, 1039, 1750, 1392, 998, 328, 1566, 2938, 962, 325, 200, 1417, 678, 471, 2580, 420, 1688, 1357, 555, 2321, 1435, 2038, 395, 2139, 660, 2827, 1559, 1033, 1721, 1451, 228, 333, 942, 1331, 2418, 1585, 1636, 2022, 497, 2437, 1380, 2291, 1691, 1504, 613, 1355, 1524, 1734, 2412, 2257, 295, 2049, 794, 2079, 1469, 2712, 1394, 2168, 1183, 862, 814, 1126, 1400, 1175, 219, 1475, 1899, 1384, 941, 2214, 1308, 2036, 359, 2578, 2305, 177, 134, 126, 1413, 559, 1042, 1054, 2467, 429, 1883, 483, 1775, 755, 292, 1616, 1487, 2382, 1625, 426, 124, 695, 2665, 2320, 2204, 541, 2385, 2920, 482, 1234, 43, 2636, 1061, 2411, 1498, 239, 2669, 2683, 1663, 1963, 1610, 2851, 2787, 893, 782, 307, 2567, 1579, 624, 368, 759, 251, 926, 2332, 1527, 346, 1964, 401, 2988, 1510, 2756, 312, 2545, 1205, 2404, 238, 2364, 2394, 1886, 1242, 306, 1154, 1003, 2070, 2527, 2949, 393, 2932, 661, 2503, 2866, 1001, 2853, 747, 1337, 1190, 1074, 2726, 2588, 1746, 222, 1588, 431, 2491, 1500, 1164, 2505, 2795, 2117, 1739, 2368, 2643, 1176, 879, 1353, 931, 1909, 1488, 2230, 1560, 857, 1338, 591, 86, 1079, 1922, 597, 2018, 2740, 2430, 1502, 552, 1976, 1521, 1452, 2426, 1447, 917, 487, 1706, 2735, 2024, 119, 2962, 533, 178, 1877, 438, 1915, 813, 1921, 122, 261, 1084, 1283, 1188, 34, 2173, 2976, 1676, 1614, 2072, 1822, 1628, 2286, 1589, 959, 2621, 293, 788, 2981, 719, 1087, 2575, 463, 2702, 779, 2786, 1194, 2930, 1941, 567, 679, 753, 2649, 446, 2100, 2407, 1991, 1169, 1719, 1998, 145, 1009, 1186, 1254, 1557, 332, 769, 819, 2728, 1656, 877, 2638, 1076, 1267, 1165, 2159, 874, 381, 1551, 2841, 417, 1539, 220, 1563, 2110, 2968, 379, 329, 2729, 1210, 2027, 835, 1454, 915, 2784, 2266, 2318, 1146, 1773, 2464, 2484, 2918, 87, 1080, 2380, 121, 2686, 2178, 1048, 120, 208, 1181, 2460, 2040, 301, 1139, 787, 1499, 2216, 1929, 2185, 2755, 520, 1898, 670, 1601, 1667, 1006, 1762, 793, 1565, 2192, 2233, 1218, 969, 2201, 258, 174, 1897, 802, 1069, 1611, 1045, 1855, 2445, 1790, 2017, 572, 1781, 1988, 928, 844, 1180, 2732, 1515, 1063, 2379, 573, 2295, 2187, 652, 1047, 1121, 1606, 945, 748, 609, 2522, 1844, 2165, 1124, 2907, 927, 2336, 1041, 2179, 1096, 1641, 2025, 2106, 2096, 774, 2608, 1496, 766, 1642, 2606, 2699, 1277, 2707, 2461, 1024, 1532, 2590, 2744, 1348, 1288, 264, 2848, 1801, 1709, 2166, 2249, 2922, 2448, 2633, 2151, 335, 870, 2471, 2130, 35, 1252, 997, 1665, 1116, 2039, 83, 493, 396, 2895, 739, 2614, 1319, 623, 2195, 1871, 380, 2773, 1904, 2410, 681, 2859, 2819, 1885, 2331, 847, 12, 2063, 2012, 2713, 1149, 2548, 2338, 756, 2095, 1661, 1708, 1956, 2003, 1300, 953, 233, 2071, 1802, 710, 1523, 1073, 109, 2278, 1302, 1329, 777, 42, 1138, 531, 2541, 2634, 288, 2093, 2956, 2264, 744, 1225, 1856, 88, 2659, 2485, 720, 2524, 1930, 771, 176, 1714, 1731, 2449, 1809, 1760, 2698, 2004, 72, 951, 1953, 2470, 291, 364, 585, 1756, 2294, 1317, 2534, 2371, 2493, 693, 1795, 135, 2998, 321, 370, 2456, 2425, 2909, 2123, 1774, 129, 2059, 2193, 2603, 1473, 2997, 730, 2620, 1720, 2156, 1766, 708, 1207, 2966, 820, 2919, 2409, 1282, 2191, 2234, 1030, 2963, 458, 1141, 1595, 2595, 133, 750, 867, 313, 67, 342, 350, 2358, 110, 2941, 2137, 2502, 250, 194, 778, 1689, 1673, 1458, 824, 2604, 2045, 1429, 2086, 2899, 2136, 1335, 146, 496, 1759, 256, 2333, 1701, 1996, 406, 266, 2671, 2544, 1320, 1449, 1341, 2420, 1529, 189, 70, 1231, 91, 218, 1678, 1221, 1881, 2182, 816, 1145, 2540, 724, 1672, 404, 1670, 2791, 466, 1851, 534, 943]

def recs_by_products(data,user):
    # print(db)
    # # working with DB
    # # creating database cursor
    # cursor = db.connection.cursor()
    # # selecting userid, shopname, ProductName and Product cost
    # cursor.execute('''SELECT * FROM user''')
    # data = cursor.fetchall()

    # as output we get python dict called data
    
    # datas = pd.read_csv("src/data/sales.csv",encoding = "utf-16le")
    # converting into dataframe
    datas = pd.DataFrame(data)
    table1 = datas.groupby(['UserId','ProductName']).mean()['ProductCost']
    table1 = table1.to_frame()
    # new_data = datas.drop(['ProductName',"MCC"], axis = 1, inplace = False)
    new_data = pd.crosstab(datas['UserId'],datas['ProductName'],values = datas['ProductCost'],aggfunc='mean')
    new_data.fillna(0, inplace = True)
    csr_data = csr_matrix(new_data.values)
    knn = NearestNeighbors(metric = 'cosine', algorithm = 'brute', n_neighbors = 20, n_jobs = -1)
    knn.fit(csr_data)
    recommendations = 20
    distances, indices = knn.kneighbors(csr_data[user],n_neighbors = recommendations + 1)
    distances = distances[0][1:]
    indices = indices[0][1:]
    returnDict = {'distances': list(distances), 'indices': list(indices)}
    return returnDict

def test_insert(data):
    merchants = ["Булка","Банан","Тапки","Пакет","Стул","Диван","Лодка","Энергос","Кофе",]
    for i in range(0,100):
        data['UserId'].append(i)
        data['ProductCost'].append(randint(100,5000))
        data['MCC'].append(merchants[randint(0,8)])
    return data


def genCache():
    with open('modules/neuron/recs_products/products.txt', 'r') as textDict:
        dict = textDict.read()
        dict = ast.literal_eval(dict)
        print(type(dict))
    print(len(ids))
    for id in ids:
        path = f'modules/neuron/recs_products/cache/{id}.txt'
        writeDict = recs_by_products(dict, id)
        with open(path, 'w') as output:
            output.write(str(writeDict))

genCache()