from numpy.core.fromnumeric import shape
import pywt
import cv2
import numpy as np


'''
将获取的图片进行小波分解：
work 1：将不同level的小波分解，剔除掉A部分
work 2：进行ndarray转化
work 3:
'''


'''
:method definition：
-------------------
:param img_path
-------------------
:return nodedata_list ndarray (0:type,1:channel,2:level,3:node order)
'''


def nodedatalist_gen(img_path, maxlevel, mode='symmetric',):

    # Initialize return list
    nodedata_list = []

    # loading img
    img = cv2.imread(img_path)

    # Seperate its channel
    img_0 = img[:, :, 0]
    img_1 = img[:, :, 1]
    img_2 = img[:, :, 2]

    # Apply WaveletPacketDescomposition
    # After this step we gain node imformation,we only need its data
#     wavelet_list = ['haar', 'db', 'sym', 'coif', 'bior', 'rbio', 'dmey', 'gaus',
# 'mexh', 'morl', 'cgau', 'shan', 'fbsp', 'cmor']
    list_wavelet_all = [item for item in pywt.wavelist() if item[0] != 'c']
    list_wavelet_5 = ['db1', 'haar', 'coif1', 'sym2', 'coif1']

    for wavelet_type in list_wavelet_5:
        # for index_type, wavelet_type in enumerate(['haar', 'db1']):
        # dim 0 wavelet type
        # dim 1 channel
        wp_0 = pywt.WaveletPacket2D(data=img_0, wavelet=wavelet_type,
                                    mode=mode, maxlevel=maxlevel)
        wp_1 = pywt.WaveletPacket2D(data=img_1, wavelet=wavelet_type,
                                    mode=mode, maxlevel=maxlevel)
        wp_2 = pywt.WaveletPacket2D(data=img_2, wavelet=wavelet_type,
                                    mode=mode, maxlevel=maxlevel)
        wps = [wp_0, wp_1, wp_2]
        # dim 2
        list_tmp_type = []
        for wp_currentChannel in wps:
            list_tmp_channel = []
            for level in range(1, maxlevel):
                # Get current level node list
                nodes_currentL = wp_currentChannel.get_level(level=level)
                list_tmp_level = []
                for node in nodes_currentL:
                    list_tmp_level.append(node.data)
                list_tmp_channel.append(list_tmp_level)
            list_tmp_type.append(list_tmp_channel)
        nodedata_list.append(list_tmp_type)

    print('hi')
    return np.array(nodedata_list)

    # Extract data from node imformation
    for index, wp in enumerate(wps):
        wp_data_tmp = []

        # Collect all node data from one level
        datalist_tmp = []
        for node in wp.get_level(0):
            datalist_tmp.append(node.data)
        wp_data_tmp.append(datalist_tmp)
    return nodedata_list


if __name__ == '__main__':
    img = cv2.imread("Tuck.jpg")
    print(pywt.wavelist())
    nodedatalist_gen("Tuck.jpg", 4)
    pywt.dwt
    print(img.shape)

    img_0 = img[:, :, 0]
    img_1 = img[:, :, 1]
    img_2 = img[:, :, 2]
    wp_0 = pywt.WaveletPacket2D(data=img_0, wavelet='db1',
                                mode='symmetric', maxlevel=4)
    wp_1 = pywt.WaveletPacket2D(data=img_1, wavelet='db1',
                                mode='symmetric', maxlevel=4)
    wp_2 = pywt.WaveletPacket2D(data=img_2, wavelet='db1',
                                mode='symmetric', maxlevel=4)
    wps = [wp_0, wp_1, wp_2]

    nodedata_list = []
    for index, wp in enumerate(wps):
        nodes_1 = wp.get_level(1)
        len_1 = len(nodes_1)
        nodes_2 = wp.get_level(2)
        len_2 = len(nodes_2)
        nodes_3 = wp.get_level(3)
        len_3 = len(nodes_3)
        nodes_4 = wp.get_level(4)
        len_4 = len(nodes_4)
        nodedata_list[index].append()

    for item in nodes_1:
        nodedata_list1.append(item.data)
    print(nodes_1)
    # print(np.shape(nodes_1[0].data))
    # print(np.shape(nodes_2[0].data))
    # print(np.shape(nodes_3[0].data))
    # print(np.shape(nodes_4[0].data))
    # len = len(nodes)
    # for item in nodes[int(len/4):len]:
    #     print(item.path)

    # print(wp['ada'])
