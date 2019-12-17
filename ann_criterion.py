import numpy as np

training_data = [
 {'x': np.array([0.5819, 0.3683, 0.4413]), 'y': 0.3675},
 {'x': np.array([0.5257, 0.8034, 0.3369]), 'y': 0.4502},
 {'x': np.array([0.5464, 0.5087, 0.2151]), 'y': 0.323},
 {'x': np.array([0.0368, 0.4483, 0.1082]), 'y': 0.0932},
 {'x': np.array([0.3923, 0.8577, 0.844 ]), 'y': 0.554},
 {'x': np.array([0.2598, 0.8384, 0.4308]), 'y': 0.3847},
 {'x': np.array([0.2948, 0.7698, 0.8535]), 'y': 0.4811},
 {'x': np.array([0.3932, 0.6851, 0.5644]), 'y': 0.4076},
 {'x': np.array([0.3504, 0.1667, 0.0203]), 'y': 0.1258},
 {'x': np.array([0.5699, 0.083 , 0.2821]), 'y': 0.2843},
 {'x': np.array([0.5214, 0.3075, 0.7003]), 'y': 0.3978},
 {'x': np.array([0.5106, 0.3842, 0.2181]), 'y': 0.2775},
 {'x': np.array([0.9681, 0.3554, 0.6043]), 'y': 0.6357},
 {'x': np.array([0.0159, 0.516 , 0.7315]), 'y': 0.2727},
 {'x': np.array([0.202 , 0.4277, 0.1312]), 'y': 0.1447},
 {'x': np.array([0.4517, 0.6635, 0.0862]), 'y': 0.2951},
 {'x': np.array([0.5695, 0.4303, 0.7988]), 'y': 0.471},
 {'x': np.array([0.1438, 0.4769, 0.561 ]), 'y': 0.2537},
 {'x': np.array([0.8781, 0.005 , 0.5077]), 'y': 0.5148},
 {'x': np.array([0.2462, 0.9468, 0.6733]), 'y': 0.4972},
 {'x': np.array([0.5648, 0.7944, 0.5051]), 'y': 0.5097},
 {'x': np.array([0.0151, 0.5057, 0.9673]), 'y': 0.333},
 {'x': np.array([0.9351, 0.3965, 0.8533]), 'y': 0.6879},
 {'x': np.array([0.1393, 0.442 , 0.567 ]), 'y': 0.2452},
 {'x': np.array([0.5434, 0.1117, 0.0418]), 'y': 0.2087},
 {'x': np.array([0.5808, 0.4009, 0.4434]), 'y': 0.3743},
 {'x': np.array([0.0573, 0.6268, 0.9303]), 'y': 0.3717},
 {'x': np.array([0.0879, 0.2472, 0.5177]), 'y': 0.1804},
 {'x': np.array([0.8892, 0.4163, 0.7102]), 'y': 0.6231},
 {'x': np.array([0.9976, 0.0016, 0.8722]), 'y': 0.695},
 {'x': np.array([0.075 , 0.5708, 0.9446]), 'y': 0.3626},
 {'x': np.array([0.9911, 0.4114, 0.1397]), 'y': 0.5387},
 {'x': np.array([0.5167, 0.6452, 0.3098]), 'y': 0.3772},
 {'x': np.array([0.5823, 0.1991, 0.9728]), 'y': 0.4848},
 {'x': np.array([0.3766, 0.5462, 0.0057]), 'y': 0.2047},
 {'x': np.array([0.2625, 0.2555, 0.7608]), 'y': 0.3029},
 {'x': np.array([0.5443, 0.6129, 0.6856]), 'y': 0.4799},
 {'x': np.array([0.1287, 0.5737, 0.4872]), 'y': 0.2565},
 {'x': np.array([0.5684, 0.9465, 0.4019]), 'y': 0.5549},
 {'x': np.array([0.2328, 0.7245, 0.1978]), 'y': 0.2648},
 {'x': np.array([0.914 , 0.9175, 0.4937]), 'y': 0.7611},
 {'x': np.array([0.2271, 0.4644, 0.8575]), 'y': 0.3572},
 {'x': np.array([0.0864, 0.0804, 0.3205]), 'y': 0.1122},
 {'x': np.array([0.1798, 0.0815, 0.8586]), 'y': 0.2857},
 {'x': np.array([0.5004, 0.8261, 0.6381]), 'y': 0.5298},
 {'x': np.array([0.7573, 0.8823, 0.1121]), 'y': 0.5441},
 {'x': np.array([0.8791, 0.2571, 0.9163]), 'y': 0.6431},
 {'x': np.array([0.0732, 0.4323, 0.7305]), 'y': 0.2672},
 {'x': np.array([0.0034, 0.1835, 0.2874]), 'y': 0.0873},
 {'x': np.array([0.7829, 0.2822, 0.6289]), 'y': 0.51},
 {'x': np.array([0.9289, 0.8584, 0.9859]), 'y': 0.8752},
 {'x': np.array([0.2879, 0.3621, 0.4345]), 'y': 0.2419},
 {'x': np.array([0.859 , 0.468 , 0.3035]), 'y': 0.5065},
 {'x': np.array([0.3386, 0.3234, 0.891 ]), 'y': 0.3761},
 {'x': np.array([0.4942, 0.9679, 0.5773]), 'y': 0.5791},
 {'x': np.array([0.3298, 0.2964, 0.3284]), 'y': 0.217},
 {'x': np.array([0.9949, 0.9716, 0.5551]), 'y': 0.8616},
 {'x': np.array([0.6914, 0.9031, 0.5679]), 'y': 0.6401},
 {'x': np.array([0.5477, 0.9153, 0.9674]), 'y': 0.6816},
 {'x': np.array([0.7822, 0.5467, 0.7356]), 'y': 0.5972},
 {'x': np.array([0.0617, 0.8124, 0.2402]), 'y': 0.2593},
 {'x': np.array([0.0033, 0.6644, 0.7327]), 'y': 0.3167},
 {'x': np.array([0.1184, 0.7044, 0.3024]), 'y': 0.2486},
 {'x': np.array([0.012 , 0.2953, 0.3404]), 'y': 0.1182},
 {'x': np.array([0.5689, 0.5353, 0.2987]), 'y': 0.3635},
 {'x': np.array([0.5426, 0.2256, 0.7156]), 'y': 0.3999},
 {'x': np.array([0.9523, 0.5509, 0.7318]), 'y': 0.7065},
 {'x': np.array([0.5466, 0.3827, 0.5994]), 'y': 0.3962},
 {'x': np.array([0.8549, 0.3651, 0.0881]), 'y': 0.4229},
 {'x': np.array([0.6769, 0.1411, 0.9955]), 'y': 0.5334},
 {'x': np.array([0.3948, 0.8252, 0.464 ]), 'y': 0.4381},
 {'x': np.array([0.6073, 0.6924, 0.4008]), 'y': 0.4614},
 {'x': np.array([0.136 , 0.4414, 0.7052]), 'y': 0.2813},
 {'x': np.array([0.9094, 0.7285, 0.5405]), 'y': 0.6869},
 {'x': np.array([0.8051, 0.8431, 0.7533]), 'y': 0.7264},
 {'x': np.array([0.4946, 0.2798, 0.3238]), 'y': 0.2802},
 {'x': np.array([0.7026, 0.448 , 0.1602]), 'y': 0.3711},
 {'x': np.array([0.5262, 0.2316, 0.5341]), 'y': 0.3443},
 {'x': np.array([0.6447, 0.0107, 0.423 ]), 'y': 0.3573},
 {'x': np.array([0.9458, 0.7168, 0.0561]), 'y': 0.5768},
 {'x': np.array([0.2762, 0.0242, 0.6527]), 'y': 0.2612},
 {'x': np.array([0.8588, 0.579 , 0.9023]), 'y': 0.6987},
 {'x': np.array([0.4085, 0.9815, 0.6949]), 'y': 0.5817},
 {'x': np.array([0.274 , 0.4376, 0.6946]), 'y': 0.3231},
 {'x': np.array([0.3026, 0.4449, 0.5889]), 'y': 0.3067},
 {'x': np.array([0.3634, 0.4367, 0.3362]), 'y': 0.2596},
 {'x': np.array([0.8218, 0.4028, 0.0488]), 'y': 0.3996},
 {'x': np.array([0.6126, 0.9342, 0.0632]), 'y': 0.479},
 {'x': np.array([0.4159, 0.4047, 0.5318]), 'y': 0.3258},
 {'x': np.array([0.2581, 0.3702, 0.865 ]), 'y': 0.3487},
 {'x': np.array([0.9556, 0.4297, 0.3273]), 'y': 0.5681},
 {'x': np.array([0.6467, 0.3666, 0.432 ]), 'y': 0.3969},
 {'x': np.array([0.1882, 0.1628, 0.5189]), 'y': 0.2024},
 {'x': np.array([0.2447, 0.6555, 0.0429]), 'y': 0.2017},
 {'x': np.array([0.9605, 0.5576, 0.7954]), 'y': 0.7313},
 {'x': np.array([0.2844, 0.131 , 0.8107]), 'y': 0.3111},
 {'x': np.array([0.6513, 0.8081, 0.455 ]), 'y': 0.5449},
 {'x': np.array([0.3039, 0.0487, 0.2701]), 'y': 0.1688},
 {'x': np.array([0.7149, 0.6344, 0.4245]), 'y': 0.5032},
 {'x': np.array([0.1934, 0.9614, 0.6691]), 'y': 0.4859},
 {'x': np.array([0.9782, 0.9374, 0.7458]), 'y': 0.8832},
 {'x': np.array([0.6589, 0.3404, 0.8188]), 'y': 0.5022},
 {'x': np.array([0.9996, 0.0406, 0.3657]), 'y': 0.5606},
 {'x': np.array([0.5866, 0.7489, 0.223 ]), 'y': 0.4254},
 {'x': np.array([0.8548, 0.0654, 0.236 ]), 'y': 0.4279},
 {'x': np.array([0.0599, 0.2245, 0.3526]), 'y': 0.125},
 {'x': np.array([0.5582, 0.8149, 0.572 ]), 'y': 0.5334},
 {'x': np.array([0.5848, 0.7718, 0.4005]), 'y': 0.4816},
 {'x': np.array([0.7732, 0.555 , 0.8219]), 'y': 0.6177},
 {'x': np.array([0.7937, 0.3883, 0.6229]), 'y': 0.5339},
 {'x': np.array([0.8657, 0.6768, 0.9154]), 'y': 0.7396},
 {'x': np.array([0.9966, 0.4677, 0.9739]), 'y': 0.7804},
 {'x': np.array([0.7549, 0.5367, 0.7743]), 'y': 0.5889},
 {'x': np.array([0.9174, 0.4121, 0.7512]), 'y': 0.6519},
 {'x': np.array([0.2975, 0.727 , 0.1467]), 'y': 0.2748},
 {'x': np.array([0.5051, 0.7208, 0.6813]), 'y': 0.4997},
 {'x': np.array([0.9716, 0.7796, 0.033 ]), 'y': 0.614},
 {'x': np.array([0.2522, 0.1755, 0.3215]), 'y': 0.1719},
 {'x': np.array([0.6301, 0.8266, 0.5715]), 'y': 0.5735},
 {'x': np.array([0.9852, 0.7718, 0.6734]), 'y': 0.7927},
 {'x': np.array([0.5307, 0.7507, 0.7803]), 'y': 0.5497},
 {'x': np.array([0.4445, 0.5047, 0.9589]), 'y': 0.4769},
 {'x': np.array([0.2088, 0.9341, 0.5953]), 'y': 0.4572},
 {'x': np.array([0.2311, 0.458 , 0.6427]), 'y': 0.2992},
 {'x': np.array([0.2855, 0.9732, 0.7678]), 'y': 0.5501},
 {'x': np.array([0.4491, 0.7721, 0.3696]), 'y': 0.4122},
 {'x': np.array([0.1781, 0.1101, 0.5302]), 'y': 0.1983},
 {'x': np.array([0.3195, 0.9199, 0.6077]), 'y': 0.4923},
 {'x': np.array([0.9729, 0.4863, 0.5731]), 'y': 0.6603},
 {'x': np.array([0.0357, 0.431 , 0.686 ]), 'y': 0.2442},
 {'x': np.array([0.5236, 0.9087, 0.1052]), 'y': 0.4354},
 {'x': np.array([0.5903, 0.0541, 0.0645]), 'y': 0.2345},
 {'x': np.array([0.5923, 0.95  , 0.1293]), 'y': 0.4949},
 {'x': np.array([0.1322, 0.7993, 0.0558]), 'y': 0.2249},
 {'x': np.array([0.5932, 0.4393, 0.8538]), 'y': 0.4993},
 {'x': np.array([0.1457, 0.4702, 0.4327]), 'y': 0.218},
 {'x': np.array([0.0233, 0.1034, 0.8285]), 'y': 0.232},
 {'x': np.array([0.5399, 0.5836, 0.1108]), 'y': 0.3139},
 {'x': np.array([0.9516, 0.132 , 0.9272]), 'y': 0.6816},
 {'x': np.array([0.1914, 0.1213, 0.4745]), 'y': 0.1883},
 {'x': np.array([0.1454, 0.1993, 0.1493]), 'y': 0.0929},
 {'x': np.array([0.6884, 0.9215, 0.9839]), 'y': 0.7594},
 {'x': np.array([0.6092, 0.4763, 0.457 ]), 'y': 0.4096},
 {'x': np.array([0.7892, 0.7555, 0.7776]), 'y': 0.6858},
 {'x': np.array([0.9588, 0.9468, 0.2841]), 'y': 0.7501},
 {'x': np.array([0.3179, 0.7266, 0.875 ]), 'y': 0.478},
 {'x': np.array([0.9489, 0.2208, 0.501 ]), 'y': 0.5735},
 {'x': np.array([0.0244, 0.0186, 0.3675]), 'y': 0.1055},
 {'x': np.array([0.1991, 0.0501, 0.2796]), 'y': 0.1351},
 {'x': np.array([0.0936, 0.7135, 0.5127]), 'y': 0.3012},
 {'x': np.array([0.8106, 0.0617, 0.2445]), 'y': 0.4027},
 {'x': np.array([0.8878, 0.0998, 0.4681]), 'y': 0.5131},
 {'x': np.array([0.3699, 0.1302, 0.6161]), 'y': 0.2906},
 {'x': np.array([0.6821, 0.6284, 0.4862]), 'y': 0.5},
 {'x': np.array([0.7141, 0.601 , 0.6361]), 'y': 0.5485},
 {'x': np.array([0.1059, 0.7988, 0.7961]), 'y': 0.4158},
 {'x': np.array([0.1281, 0.35  , 0.9682]), 'y': 0.3301},
 {'x': np.array([0.7738, 0.8266, 0.3006]), 'y': 0.5787},
 {'x': np.array([0.1618, 0.0357, 0.0508]), 'y': 0.0612},
 {'x': np.array([0.4577, 0.9039, 0.9986]), 'y': 0.6444},
 {'x': np.array([0.8169, 0.4082, 0.3095]), 'y': 0.4679},
 {'x': np.array([0.8513, 0.8316, 0.5623]), 'y': 0.6983},
 {'x': np.array([0.4186, 0.435 , 0.8749]), 'y': 0.426},
 {'x': np.array([0.6257, 0.1205, 0.2263]), 'y': 0.2986},
 {'x': np.array([0.8743, 0.0652, 0.7711]), 'y': 0.5843},
 {'x': np.array([0.9807, 0.366 , 0.1296]), 'y': 0.519},
 {'x': np.array([0.1278, 0.8862, 0.3248]), 'y': 0.3352},
 {'x': np.array([0.7414, 0.8919, 0.2336]), 'y': 0.5723},
 {'x': np.array([0.5928, 0.5806, 0.0589]), 'y': 0.3241},
 {'x': np.array([0.2462, 0.5868, 0.9128]), 'y': 0.4132},
 {'x': np.array([0.9876, 0.332 , 0.1174]), 'y': 0.5143},
 {'x': np.array([0.7624, 0.2374, 0.4741]), 'y': 0.4502},
 {'x': np.array([0.4867, 0.721 , 0.7881]), 'y': 0.5204},
 {'x': np.array([0.7606, 0.4946, 0.9815]), 'y': 0.6363},
 {'x': np.array([0.519 , 0.6686, 0.4023]), 'y': 0.4114},
 {'x': np.array([0.5335, 0.0999, 0.8845]), 'y': 0.4301},
 {'x': np.array([0.0289, 0.5249, 0.9725]), 'y': 0.3435},
 {'x': np.array([0.3011, 0.9584, 0.5181]), 'y': 0.4809},
 {'x': np.array([0.7612, 0.2042, 0.7191]), 'y': 0.5114},
 {'x': np.array([0.6749, 0.1267, 0.7709]), 'y': 0.4709},
 {'x': np.array([0.9404, 0.6902, 0.165 ]), 'y': 0.5923},
 {'x': np.array([0.6358, 0.0942, 0.0994]), 'y': 0.2681},
 {'x': np.array([0.7963, 0.4894, 0.7742]), 'y': 0.6},
 {'x': np.array([0.9131, 0.6293, 0.8581]), 'y': 0.7386},
 {'x': np.array([0.1971, 0.9761, 0.0116]), 'y': 0.3179},
 {'x': np.array([0.5491, 0.3627, 0.8619]), 'y': 0.464},
 {'x': np.array([0.267 , 0.1507, 0.4202]), 'y': 0.2014},
 {'x': np.array([0.9454, 0.3033, 0.9736]), 'y': 0.7098},
 {'x': np.array([0.5493, 0.2459, 0.6606]), 'y': 0.3908},
 {'x': np.array([0.9072, 0.8009, 0.409 ]), 'y': 0.6799},
 {'x': np.array([0.3976, 0.7768, 0.43  ]), 'y': 0.4092},
 {'x': np.array([0.8998, 0.0438, 0.0899]), 'y': 0.4171},
 {'x': np.array([0.3786, 0.6542, 0.0111]), 'y': 0.2419},
 {'x': np.array([0.0042, 0.0136, 0.6059]), 'y': 0.1641},
 {'x': np.array([0.7018, 0.8646, 0.7105]), 'y': 0.6657},
 {'x': np.array([0.0596, 0.815 , 0.8551]), 'y': 0.4251},
 {'x': np.array([0.5984, 0.3564, 0.1988]), 'y': 0.3079},
 {'x': np.array([0.7262, 0.0778, 0.6177]), 'y': 0.4548},
 {'x': np.array([0.4452, 0.0654, 0.3031]), 'y': 0.2335},
 {'x': np.array([0.6386, 0.0948, 0.1771]), 'y': 0.2904},
 {'x': np.array([0.9059, 0.2154, 0.5579]), 'y': 0.559},
 {'x': np.array([0.1341, 0.0113, 0.8648]), 'y': 0.2712},
 {'x': np.array([0.279 , 0.1534, 0.3301]), 'y': 0.1816},
 {'x': np.array([0.1319, 0.066 , 0.5924]), 'y': 0.1984},
 {'x': np.array([0.9516, 0.5803, 0.799 ]), 'y': 0.733},
 {'x': np.array([0.5595, 0.4506, 0.9721]), 'y': 0.5177},
 {'x': np.array([0.2926, 0.0503, 0.4904]), 'y': 0.224},
 {'x': np.array([0.0166, 0.1502, 0.2493]), 'y': 0.0776},
 {'x': np.array([0.9002, 0.1189, 0.5406]), 'y': 0.5419}
]

def sigmoid(x):
    """
        Calculate standard logistic sigmoid function.
    """

    y = 1 / (1 + np.exp(-x))
    return y


def get_ann_output(x, w):
    """
        Calculate ANN output for given input x, using neuron synapse weights w.
    """

    first_weights, second_weights = reshape_weights(w)
    hidden_layer_count = second_weights.size

    hidden_neuron_ins = np.dot(x, first_weights)
    hidden_neuron_outs = np.empty([hidden_layer_count])
    for i in range(hidden_layer_count):
        hidden_neuron_outs[i] = sigmoid(hidden_neuron_ins[i])

    ann_output = sigmoid(np.dot(hidden_neuron_outs, second_weights))

    return ann_output


def reshape_weights(w):
    """
        Reshape given vector of weights into weight matrices expected by the
        artificial neural network.
    """

    input_layer_count = 3
    hidden_layer_count = 15
    
    first_weights_shape = (input_layer_count, hidden_layer_count)
    second_weights_shape = hidden_layer_count

    first_weights_count = input_layer_count * hidden_layer_count
    seconds_weights_count = hidden_layer_count
    total_weights_count = first_weights_count + seconds_weights_count

    if len(w) != total_weights_count:
        raise Exception("Invalid vector size; expected {0}, got {1}".format(
            total_weights_count, len(w)))

    first_weights = np.reshape(w[0:first_weights_count], first_weights_shape)
    second_weights = np.reshape(w[first_weights_count:], second_weights_shape)

    return (first_weights, second_weights)


def get_mean_absolute_error(w):
    """
        Evaluate mean absolute error of artificial neural network performance
        for the loaded training set.
    """

    total_absolute_error = 0

    for point in training_data:
        estimated_y = get_ann_output(point['x'], w)
        absolute_error = np.abs(estimated_y - point['y'])

        total_absolute_error += absolute_error

    mean_absolute_error =  total_absolute_error / len(training_data)
    return mean_absolute_error


def optimality_criterion(w):
    """
        Evaluate optimality criterion for given input vector w. Represents
        evaluation of artificial neural network performance for the given set of
        weights. 
    """

    return get_mean_absolute_error(w)


if __name__ == "__main__":
    w = list(np.random.uniform(-10, 10, 60))
    optimality_criterion(w)