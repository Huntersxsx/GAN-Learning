## <font face="楷体">说明</font>
李宏毅老师的GAN课程作业 HW3-1：使用GAN实现动漫人物头像的生成  
详细说明见[PPT](https://github.com/Huntersxsx/GAN-Learning/tree/master/HW3-1/HW3-1.pdf)  
数据集 [Anime Dataset](https://drive.google.com/drive/folders/1mCsY5LEsgCnc0Txv0rpAUhKVPWVkbw5I)  
数据集 [Extra Data](https://drive.google.com/file/d/1tpW7ZVNosXsIAWu8-f5EpwtF3ls3pb79/view)  

## 使用线性全连接的GAN  
代码见gan.py，原代码见[PyTorch-GAN](https://github.com/eriklindernoren/PyTorch-GAN/blob/master/implementations/gan/gan.py)  
batch_size为64，在Anime Dataset中共33431张动漫头像上训练了200个epochs，共104400个steps
line18、line101、line163处需要修改路径

```
python gan.py
```

效果很不理想，见下图：  

![](https://github.com/Huntersxsx/GAN-Learning/blob/master/HW3-1/imgs/GAN-step104400.png)

## 使用CNN的DCGAN 
代码见dcgan.py，原代码见[PyTorch-DCGAN](https://github.com/pytorch/examples/tree/master/dcgan) 
batch_size为64，在Anime Dataset中共33431张动漫头像上训练了200个epochs，共104400个steps

```
dataset参数这里选择folder，dataroot是用来训练的动漫头像存放路径，cuda是使用GPU，outf是存放生成的图像以及模型的路径
样例：
python dcgan.py --dataset folder --dataroot /workspace/GAN-Learning/Anime_data/ --cuda --outf /workspace/GAN-Learning/HW3-1/dcgan
```

效果相对于只使用全连接的GAN有了很大的改进，但是有些生成的头像看起来仍然比较奇怪，见下图：  

![](https://github.com/Huntersxsx/GAN-Learning/blob/master/HW3-1/imgs/DCGAN-step104400.png)
