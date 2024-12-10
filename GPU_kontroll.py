"""

 https://pytorch.org/
 
valida CUDA versiooniga variant, näiteks:
pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu124
 
sisestada käsurida terminali Condas või PyCharmis

"""


import torch

print(torch.cuda.is_available())

print(torch.cuda.device_count())

print(torch.cuda.current_device())

print(torch.cuda.device(0))

print(torch.cuda.get_device_name(0))
