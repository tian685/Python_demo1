#   ---*- coding: utf-8 -*-
#  ￥- *--- author---祥彪--￥

import paddlehub as hub
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
module = hub.Module(name="ultra_light_fast_generic_face_detector_1mb_640")
res = module.face_detection(paths=["./test1.jpg"],visualization=True,
output_dir='face_detection_output')

test_img_path= ["./test1.jpg"]
img = mpimg.imread(test_img_path[0])

input_dict = {"image": test_img_path}
results = module.face_detection(data=input_dict, visualization=True)
for result in results:
    print(result)
#展示待预测图片
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()