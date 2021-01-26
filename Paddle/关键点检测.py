#   ---*- coding: utf-8 -*-
#  ￥- *--- author---祥彪--￥
import paddlehub as hub
import matplotlib; matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
module = hub.Module(name="human_pose_estimation_resnet50_mpii")
res = module.keypoint_detection(paths=["./test01.jpg"],visualization=True,
output_dir='keypoint_output')
test_img_path= ["./test01.jpg"]
img = mpimg.imread(test_img_path[0])

input_dict = {"image": test_img_path}
results = module.keypoint_detection(data=input_dict, visualization=True)
for result in results:
    print(result)
# 展示待预测图片
plt.figure(figsize=(10,10))
plt.imshow(img)
plt.axis('off')
plt.show()