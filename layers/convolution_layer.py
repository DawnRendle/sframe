# coding=UTF-8

import numpy as np


class ConvolutionLayer(object):
    def __init__(self, filter_size, filter_num, stride, padding=0):
        self.filter_size = filter_size
        self.filter_num = filter_num
        self.stride = stride
        self.padding = padding

        # 使用均值为0、标准差为1的高斯分布初始化卷积核
        # 组织成[filter_num, filter_size, filter_size]的形式
        self.weights = np.random.normal(0, 0.01, self.filter_num * self.filter_size ** 2) \
            .reshape((self.filter_num, self.filter_size, self.filter_size))

        self.outputs = []

    def setup(self, inputs_shape):
        # 根据输入数据计算当前层次输出结果的大小
        #
        # 输入数据以4维数组的形式组织，具体格式为：
        #     [batch, width, height, channel]
        outputs_size = (inputs_shape[1] + 2 * self.padding - self.filter_size) / self.stride + 1
        self.outputs = np.zeros((inputs_shape[0], outputs_size, outputs_size, self.filter_num))
        return self.outputs.shape

    # 计算卷积层的前向传播结果
    def forward(self, inputs):
        pass
