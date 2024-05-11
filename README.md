# PDF 页面合并排版工具

---

## Introduction 介绍:	

​	这个项目是基于 `PyMuPDF` 制作的用于打印 PDF 文件时将两页合为一页来打印的文件转化工具

​	原理很简单: 通过一个 `page_sort()` 函数来确定页数的顺序, 然后将原文件里的对应页转化为图片旋转然后放置在新文件的对应位置罢了

​	这里贴张图来说明工作原理

<img src=".\对比.png" alt="https://github.com/Koji-Huang/PDF_Mixer/blob/master/%E5%AF%B9%E6%AF%94.png" style="zoom:50%;" />

​	它可以将两页的数据压缩至一页(节约用纸嘛), 对于缺纸或者希望节约点打印费的人来说非常实用(不过打印完的需要对折, 你可以自己更改 page_sort 函数来实现不同的排列方式, 比如直接叠加或者隔几页纸可以叠加的版本), 我之前预留有这个想法但是懒得开发了, GUI 也懒得搞 (我社团的人说不需要, 未来看我什么时候想加就加吧)

---

## 安装:

1. 通过 Python

> pip 安装 `PyMuPDF` 命令
>
> ```
> pip install PyMuPDF
> ```
>
> 运行 main.py

 2. 用 Release

    > 下载后直接运行

---

## 使用方法:

​	这个项目是通过命令行使用的, 下面是对命令行的解释

### Stage1. 转换文件路径

> ```
> Please input file's path: 
> >>>
> ```
>
> 这里是要你输入需要转换文件的位置

### Stage 2. 确认文件信息

> ```
>  Now reading parameter...
> |  format ->  PDF 1.4
> |  title ->  MiniLab mkII FL Studio User Manual V.1
> |  author ->  
> |  subject ->  
> |  keywords ->  
> |  creator ->  
> |  producer ->  Skia/PDF m95 Google Docs Renderer
> |  creationDate ->  
> |  modDate ->  
> |  trapped ->  
> |  encryption ->  None
> Confirm ? Y(1) or N(0): 
> ```
>
> 这里会打印 PDF 的一些基础信息, 确认的话输入1, 不确认输入 0 _(虽然我感觉这一步可有可无, 但是有时候PDF版本确实会导致错误, 所以我决定保留这段)_
>
> 没报错的话会显示:
>
> ```
> File Load Success
> ```

### Stage 3. 转换信息自定义

> ```
> Convert Parameter:
> Customize Output Parameter: ( Yes = 1 | No = 0)
> >>> 
> ```
>
> 这里的意思是是否自定义转换格式, 确认的话会开启自定义参数选择, 否的话就会使用默认参数并开始转换了. 1 为是, 0 为否

### Stage4. 转换参数显示

> ```
> Parameter Input Complete.
> 
> --------------------------------
> Output File: 
> 	Document('.pdf')
> 
> Scale mode: 
> 	Default
> 
> Build mode: 
> 	Default
> 
> Page resolution: 
> 	(21, 29.7)
> 
> Margins: 
> 	(2.54, 2.8)
> 
> Tmp file path: 
> 	./tmp
> 
> Output file path: 
> 	./output.pdf
> ```
>
> `Parameter Input Complete`. 指的是参数设定完成
>
> `Output File` 指的是输出文件的位置 (后缀必须要为 pdf 哦)
>
> `Build mode` 指的是分页规律, 这会影响到页的排布规律, 目前仅支持 Default 选项(也就是打印出来的纸张需要对折)
>
> `Page resolution` 指的是页的长宽(单位: cm)
>
> `Margins` 指的是页边距 (单位: cm)
>
> `Tmp file path` 指的是临时文件存放路径, 默认为 `./tmp`
>
> `Output file path` 指的是输出文件路径, 默认为 `./output.pdf`

### 	Stage 5. 提取图片

> ```
> Extracting Picture: 92%:  ▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋ page: 12 - 13
> Extract Picture Finished
> ```
>
> 从PDF中提取并生成图片, 进度条代表提取进度, 提取出来的图片并不会自动删除, 他会一直保存在临时文件夹里(很抱歉)

### 	Stage 6. 生成PDF

> ```
> Convert progress: 100%:  ▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋▋
> Convert Complete, Now saving file...
> Done (Push any key to continue)
> ```
>
> 合成新文件, 进度条代表输入进度
>
> `Convert Complete, Now saving file... ` 表示生成完毕, 正在保存文件
>
> `Done (Push any key to continue)` 表示完成, 按任意键继续 (再生成一次)

### 	Stage Extre. 自定义转化格式:

> _注意: 所有选项都有默认值, 可以用回车输入_
>
> 1. #### 分页规律:
>
> > ```
> > Rebuild Mod
> > For the details
> > you can go to the folder of this software
> > then you can find the docs
> > Default: Default
> > >>>
> > ```
> >
> > 这是用来指定不同的分页函数 `page_sort` 的输入, 供使用者自行编写拓展, 默认为 Default
>
> 2. #### 页分辨率
>
> > ```
> > Big Page page_resolution
> > 1 for A4 (Vertical)
> > 2 for A4 (horizontal)
> > 3 for A5 (Vertical)
> > 4 for A5 (horizontal)
> > Other for Custom Setting
> > Default x = 21, y = 29.7 (A4 Vertical)
> > >>>
> > ```
> >
> > 指定输出文件的页分辨率 1 = A4纵向, 2 = A4 横向, 3 = A5纵向, 4 = A5横向, 默认为 A4 纵向
>
> 3. #### 页边距
>
> > ```
> > Page Margins
> > 0 for No margins
> > 1 for Standard margins
> > 2 for low margins
> > 3 for large margins
> > Other for custom margins
> > Default x = 2.54, y = 2.8
> > >>>
> > ```
> >
> > 设置页边距, 0 是没有页边距, 1 是标准页边距, 2 是小页边距, 3是大页边距, 默认为标准缩放
>
> 4. #### 缩放模式
>
> > ```
> > Scale Mode
> > 0 for Force Zoom
> > 1 for Keep to theCentered and Adaptive scaling
> > Default 0
> > >>>
> > ```
> >
> > 设置原画面在新文件中的缩放模式, 0 是强制缩放, 1 是保持长宽比缩放, 默认为强制缩放
>
> 5. #### 临时文件存放
>
> > ```
> > TMP file folder:
> > No Input will put on ./tmp
> > >>>
> > ```
> >
> > 设置临时文件存放路径, 默认为 `./tmp`
>
> 6. #### 输出文件路径
>
> > ```
> > Output file folder
> > No Input will put on output.pdf
> >  >? 
> > ```
> >
> > 设置输出文件路径, 默认为 `./output.pdf`

---

## 写在最后:

​	这个项目是当时为了节约社团用纸想出来的东西, 也没怎么想就写出来了, 结果用着还算不错. 加上 GUI 应该会很好的吧~

​	欢迎大家使用或者重构这个项目, 如果对你有帮助的话可以V我50喵, 孩子想买哈迪斯惹o((>ω< ))o, 谢谢支持~

<img src="https://github.com/Koji-Huang/PDF_Mixer/blob/master/zfb.jpg" style="zoom:25%;" />