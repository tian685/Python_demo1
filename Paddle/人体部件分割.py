#   ---*- coding: utf-8 -*-
#  ￥- *--- author---祥彪--￥
import paddlehub as hub
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
module = hub.Module(name="ace2p")
res = module.segmentation(paths=["./test02.jpg"],visualization=True,
output_dir='ace2p_output')

test_img_path= ["./test02.jpg"]
img = mpimg.imread(test_img_path[0])

input_dict = {"image": test_img_path}
results = module.segmentation(data=input_dict, visualization=True)
for result in results:
    print(result)
# 展示待预测图片
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()