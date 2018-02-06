# Copyright 2017 Division of Medical Image Computing, German Cancer Research Center (DKFZ)
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from batchgenerators.augmentations.noise_augmentations import augment_blank_square_noise, augment_gaussian_blur, \
    augment_gaussian_noise, augment_rician_noise
from batchgenerators.transforms.abstract_transforms import AbstractTransform


class RicianNoiseTransform(AbstractTransform):
    """Adds rician noise with the given variance.
    The Noise of MRI data tends to have a rician distribution: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2254141/

    Args:
        noise_variance (tuple of float): samples variance of Gaussian distribution used to calculate
        the rician distribution from this interval

    CAREFUL: This transform will modify the value range of your data!
    """

    def __init__(self, noise_variance=(0, 0.1)):
        self.noise_variance = noise_variance

    def __call__(self, **data_dict):
        data_dict["data"] = augment_rician_noise(data_dict['data'], noise_variance=self.noise_variance)
        return data_dict


class GaussianNoiseTransform(AbstractTransform):
    """Adds additive Gaussian Noise

    Args:
        noise_variance (tuple of float): samples variance of Gaussian distribution from this interval

    CAREFUL: This transform will modify the value range of your data!
    """

    def __init__(self, noise_variance=(0, 0.1)):
        self.noise_variance = noise_variance

    def __call__(self, **data_dict):
        data_dict["data"] = augment_gaussian_noise(data_dict["data"], self.noise_variance)
        return data_dict


class GaussianBlurTransform(AbstractTransform):
    def __init__(self, blur_sigma=(1, 5)):
        self.blur_sigma = blur_sigma

    def __call__(self, **data_dict):
        data_dict['data'] = augment_gaussian_blur(data_dict['data'], self.blur_sigma)
        return data_dict


class BlankSquareNoiseTransform(AbstractTransform):
    def __init__(self, squre_size=20, n_squres=1, noise_val=(0, 0)):
        self.noise_val = noise_val
        self.n_squres = n_squres
        self.squre_size = squre_size

    def __call__(self, **data_dict):
        data_dict['data'] = augment_blank_square_noise(data_dict['data'], self.squre_size, self.n_squres,
                                                       self.noise_val)
        return data_dict
