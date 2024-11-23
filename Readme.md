## 项目简介

本项目是使用Python开发的，基于FFmpeg音视频流处理、OpenAI-Whisper语音识别模型和googletrans翻译库的字幕生成和翻译程序。



### 1 环境配置

1. FFmpeg安装：[FFmpeg官网](https://ffmpeg.org/download.html)，可以按照网络上的教程安装对应版本，并加入环境变量。

2. Whisper安装：
   
   ```shell
   pip install openai-whisper
   ```

3. googletrans安装：（安装版本不对可能会报错）
   
   ```shell
   pip install googletrans==4.0.0-rc1
   ```

### 2 软件使用

将待处理的视频放在mp4目录下，更名为`video.mp4`

在src目录下打开cmd，执行01audio.py：

```shell
python 01audio.py
```

按照提示输入视频的地址（必须是绝对地址！下同）和mp3音频文件地址。mp3的地址选择audio文件夹下即可，例如：

```shell
....../Subtitle-Generate-and-Translate/audio/audio.mp3
```

同理输入wav文件地址



执行完成后，就得到了视频的音频流。



执行02text.py：

```shell
python 02text.py
```

按照提示输入wav音频地址和原始字幕地址，建议字幕与视频在同一地址下，如：

```shell
....../Subtitle-Generate-and-Translate/mp4/video_ori.srt
```

等待执行完成后即可得到原始字幕，如果源视频为中文，执行到这一步即可完成。



执行03translate.py，这里请求了`google.com.hk`的接口，需要在代理环境下运行。

```shell
python 03translate.py
```

按照提示输入原始字幕和翻译字幕地址，运行完成后即可得到翻译后的字幕。



### 3 后续开发

若star超过50则开始更新图形化/WEB界面。
