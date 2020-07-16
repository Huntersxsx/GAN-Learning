## <font face="楷体">说明</font>
李宏毅老师的GAN课程作业 HW3-3：风格迁移  
详细说明见[PPT](https://github.com/Huntersxsx/GAN-Learning/tree/master/HW3-3/HW3-3.pdf)   

## CycleGAN  
原代码见[pytorch-CycleGAN-and-pix2pix](https://github.com/junyanz/pytorch-CycleGAN-and-pix2pix)  
在该实验中我使用了photo to Van Gogh的风格迁移  
首先下载数据集
```
cd CycleGAN
bash ./datasets/download_cyclegan_dataset.sh vangogh2photo
```
然后训练模型
```
python train.py --dataroot ./datasets/vangogh2photo --name vangogh2photo_cyclegan --model cycle_gan --checkpoints_dir ./checkpoints
```
测试模型
```
python ./test.py --dataroot ./datasets/vangogh2photo --name vangogh2photo_cyclegan --model cycle_gan --checkpoints_dir ./checkpoints --results_dir ./results
```
可以得到效果如图所示：  

![](https://github.com/Huntersxsx/GAN-Learning/blob/master/HW3-3/imgs/result1.jpg)

我还利用训练得到的模型对[黑人抬棺](https://www.bilibili.com/video/BV1NZ4y1j7nw?from=search&seid=17026038389325936880)视频进行了实验  
首先使用SplitCombine.py对视频进行拆帧  
```
cd ..
python SplitCombine.py --frame_dir ./frames --input_video ./demo.avi --v2i True
```
然后利用训练得到的模型对所有帧进行风格迁移
```
python CycleGAN/test.py --dataroot ./test --name vangogh2photo_cyclegan --model cycle_gan --checkpoints_dir ./checkpoints --results_dir ./results
```
**需要注意的是  
1、要像原实验中数据存放的方式一样，在test文件夹中创建testA和testB两个文件夹，将刚刚拆分得到的帧放入testB文件夹中，testA文件夹中也可以放入拆得的帧  
2、将CycleGAN/options/base_options.py中的--crop_size修改为实验图像的宽，--load_size修改为合适的大小，将CycleGAN/options/test_options.py文件中的--num_test修改为需要风格迁移的图片数目，将--aspect_ratio修改为实验图像的宽高比。**  
下图是某一帧经过风格迁移后的效果：  

![](https://github.com/Huntersxsx/GAN-Learning/blob/master/HW3-3/imgs/result2.jpg)

使用onlyfake.py代码将经过风格迁移的图片保存至fakeimages文件夹中，并使用SplitCombine.py将所有帧图像合并成视频  
```
python onlyfake.py
python SplitCombine.py --frame_dir ./fakeimages --output_video ./demo_output.avi --i2v True
``` 