import json
import random


data_indices = [2145, 358, 49, 2316, 1878, 1958, 3492, 625, 4250, 3682, 2083, 2993, 2843, 1143, 3946, 2529, 3153, 117, 994, 2030, 2295, 1220, 4436, 3981, 3804, 2601, 2248, 2593, 1457, 3655, 3284, 4140, 2695, 17, 2337, 3899, 3957, 2605, 4182, 1631, 3360, 703, 3195, 4665, 2996, 1427, 2092, 429, 228, 4117, 4568, 3354, 2673, 1327, 3626, 3812, 1549, 941, 1343, 2742, 1062, 3513, 1837, 1827, 1074, 2451, 4492, 2060, 1606, 146, 2351, 3684, 2437, 4287, 2582, 3201, 3042, 4543, 2119, 1814, 453, 1307, 4460, 3955, 3424, 2040, 4324, 2780, 3629, 3934, 4136, 1446, 3127, 777, 4486, 1698, 2685, 2356, 3614, 2820, 2817, 2152, 887, 3983, 153, 4611, 847, 4210, 3300, 4632, 374, 1752, 1956, 4206, 1863, 2190, 950, 1856, 1476, 2046, 1455, 3810, 1965, 574, 4245, 1871, 1975, 1713, 1786, 3061, 517, 4351, 2211, 1110, 1104, 1313, 3829, 62, 3949, 1425, 2, 2048, 2475, 3664, 2433, 3940, 2602, 1782, 3206, 3463, 353, 3496, 4389, 2979, 1392, 2341, 3833, 21, 701, 2731, 2775, 1212, 3792, 4349, 1758, 1703, 2572, 4166, 1816, 412, 602, 2541, 1660, 1919, 1086, 873, 4132, 4313, 2354, 3250, 1094, 4152, 1000, 3678, 3960, 2393, 3572, 750, 4645, 2320, 4605, 4017, 2336, 4383, 2568, 1572, 1691, 1154, 4413, 2323, 3609, 3318, 2450, 3847, 1471, 2851, 4190, 3896, 87, 1105, 2772, 565, 1469, 1093, 4503, 3760, 1409, 3590, 1697, 3975, 3260, 4455, 476, 2767, 3004, 237, 2540, 3730, 1, 38, 2954, 4364, 42, 4400, 4262, 1078, 4471, 1418, 3627, 760, 2859, 319, 469, 438, 3035, 2314, 3644, 2807, 2255, 3453, 2471, 2712, 687, 250, 1072, 3525, 3820, 3895, 2548, 1031, 2266, 662, 1852, 2587, 1491, 3569, 3567, 2782, 4207, 1035, 4588, 4016, 3608, 2353, 4164, 3431, 583, 3231, 2428, 670, 1386, 200, 3665, 344, 787, 3502, 3139, 1492, 77, 1254, 354, 890, 1120, 3757, 4036, 118, 3531, 875, 3107, 1567, 433, 3008, 2798, 4675, 2328, 4567, 4458, 2058, 410, 3024, 2376, 396, 2434, 4359, 1669, 724, 1992, 3692, 1770, 3490, 1228, 1353, 536, 1199, 4302, 4508, 209, 1748, 2172, 2481, 1116, 618, 1590, 1046, 437, 4619, 573, 660, 1140, 3880, 732, 1990, 1732, 2394, 2607, 4631, 2216, 876, 3418, 3037, 987, 60, 3673, 1800, 4340, 2137, 2332, 4204, 3403, 176, 3725, 3685, 1968, 1103, 4087, 3752, 4552, 2011, 2297, 2932, 684, 712, 989, 397, 1331, 1006, 2298, 4406, 2617, 4066, 2423, 845, 3738, 1519, 3854, 856, 2254, 4023, 2944, 3454, 521, 1367, 4275, 3500, 308, 2821, 1974, 2436, 1309, 3251, 2480, 3402, 4058, 2982, 2279, 1715, 2818, 2167, 3676, 3843, 3228, 2884, 375, 246, 789, 124, 3670, 2559, 2709, 1215, 2345, 1487, 4040, 1937, 80, 1596, 1850, 2532, 3142, 3953, 3462, 4143, 2223, 3469, 804, 3751, 2018, 4189, 3118, 2468, 3415, 1407, 1047, 623, 2796, 3705, 2306, 2203, 2521, 3237, 1623, 1501, 4542, 4575, 1767, 2787, 3514, 4476, 3272, 867, 178, 2007, 1041, 2109, 3119, 1139, 1442, 1040, 2688, 3674, 1257, 1643, 2286, 3509, 3746, 3086, 1192, 2839, 1690, 1946, 3068, 3202, 1007, 3693, 2710, 624, 300, 307, 1336, 4646, 2096, 219, 1280, 1601, 3552, 2756, 306, 120, 1915, 284, 447, 3010, 1942, 3022, 2570, 4091, 4371, 2084, 3508, 1737, 3882, 3387, 4412, 1423, 4196, 1119, 652, 2469, 4157, 3800, 825, 1573, 214, 4128, 4625, 3410, 1063, 1002, 1400, 1186, 2378, 1674, 3565, 1500, 2907, 4283, 999, 4477, 1997, 444, 4082, 3324, 3065, 1486, 4379, 1429, 1920, 4215, 1872, 2647, 1559, 2725, 571, 360, 3947, 3170, 3832, 2313, 244, 3566, 1657, 970, 4343, 791, 3958, 4459, 819, 365, 3129, 2484, 2962, 1535, 2362, 4541, 2666, 1930, 3707, 3219, 4440, 4168, 4518, 2645, 2186, 4427, 2757, 3936, 1222, 1092, 1719, 2633, 2952, 718, 1568, 489, 1087, 4511, 4022, 1756, 3944, 3580, 427, 907, 4504, 1973, 1865, 4081, 3131, 3980, 2684, 2382, 2192, 3828, 3603, 4019, 4073, 1557, 3568, 3717, 3504, 379, 3625, 1249, 3329, 116, 3467, 3266, 1929, 3034, 3063, 3330, 2182, 2322, 627, 1563, 2034, 2883, 1299, 4222, 4185, 2166, 371, 835, 4257, 2523, 3437, 3522, 1434, 2464, 3236, 2591, 3649, 2029, 3870, 1586, 1906, 2500, 2150, 3841, 838, 2514, 3776, 1761, 3731, 899, 2261, 4138, 3207, 4108, 1351, 4191, 2537, 2727, 515, 3166, 4228, 4661, 2704, 2151, 4327]
batch_indices = data_indices[:300]
results = {}

def get_examples(model, data_type, batch, ids):
    filename = f'predictions/{model}-{data_type}-{batch}.json'
    with open(filename, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    wanted = [d for d in data if d['id'] in ids]
    for i in range(len(wanted)):
        wanted[i]['model'] = model
        wanted[i]['data_type'] = data_type
        wanted[i]['batch'] = batch
        
    return [d for d in data if d['id'] in ids]

def test(data,task):
    input_s = ""
    output = ""
    if task == "emoji-gpt-to-chinese":
        input_s = "emoji-gpt"
        output = "emoji-gpt-to-chinese"
    elif task == "emoji-algo-to-chinese":
        input_s = "emoji-algo"
        output = "emoji-algo-to-chinese"
    elif task == "chinese-to-emoji":
        input_s = "chinese"
        output = "chinese-to-emoji"
    else:
        print("error")
        return
    dd = data.copy()
    random.shuffle(dd)
    result = []
    n = len(dd)
    for i,d in enumerate(dd):
        print(f"{i+1}/{n}")
        print(f"input: {d[input_s]}")
        print(f"output: {d[output]}")
        score = 0
        while True:
            try:
                s = input("score(a float from 0~10): ")
                score = float(s)
                if score > 10 or score < 0:
                    print("fuck u")
                    continue
                break
            except ValueError:
                print("fuck u")
                continue
        r = {
            'score': score,
            'model': d['model'],
            'data_type': d['data_type'],
            'batch': d['batch']
        }
        result.append(r)
    results[task] = result
    return        
    

def main():
    test_ids = random.choices(batch_indices, k=5)
    models = ['llama', 'mt5']
    random.shuffle(models)
    
    name = input("input your name: ")
    results['name'] = name
    data = []
    for m in models:
        # get data
        data += get_examples(m, 'mix', 2, test_ids)
        data += get_examples(m, 'mix', 4, test_ids)
        data += get_examples(m, 'mix', 8, test_ids)
        data += get_examples(m, 'algo', 4, test_ids)
        data += get_examples(m, 'gpt', 4, test_ids)
        random.shuffle(data)
    for task in ["emoji-gpt-to-chinese", "emoji-algo-to-chinese", "chinese-to-emoji"]:
        print(f"starting {task}")
        test(data,task)
    
    with open(f'{name}.json', 'w', encoding='utf-8') as f:
        json.dump(results, f, ensure_ascii=False, indent=4)
        
        
if __name__ == '__main__':
    main()
        
        
        