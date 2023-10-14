# Screenshot_OCR_to_clipboard
在Ubuntu环境下，使用gnome-screenshot截屏，然后对截屏内容使用paddleOCR进行识别，将识别的内容复制到剪切板
take a Screenshot, then using paddleOCR to read the words, then to clipboard in Ubuntu

如果您真的要使用，请注意路径问题
If you want to use, please pay attention to the path problem

首先应该按照[paddleOCR文档](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/quickstart.md#1)安装paddleOCR
First you should install paddleOCR according to [paddleOCR documentation](https://github.com/PaddlePaddle/PaddleOCR/blob/release/2.7/doc/doc_ch/quickstart.md#1)

然后把该文件放在已知文件夹下，在设置中的定制快捷键中设置快捷键，命令应该是`python3 ocr.py`
Then put the file in a known folder and set the shortcut key in the custom shortcut key in the settings. The command should be `python3 ocr.py`

当然还有更好的方法，我也一直在精进自己的编程技能，只是觉得不是只有完美的作品才可以被分享出来，因此把它上传到Github
Of course there is a better way.I have been improving my programming skills.I just feel that not only perfect works can be shared, so I uploaded it to Github.
