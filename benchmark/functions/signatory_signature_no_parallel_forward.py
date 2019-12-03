# Copyright 2019 Patrick Kidger. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# =========================================================================
import signatory
import torch


def setup(obj):
    obj.torch_num_threads = torch.get_num_threads()
    torch.set_num_threads(1)
    obj.path = torch.rand(obj.size, dtype=torch.float)


def run(obj):
    return signatory.signature(obj.path, obj.depth)


def teardown(obj):
    torch.set_num_threads(obj.torch_num_threads)
