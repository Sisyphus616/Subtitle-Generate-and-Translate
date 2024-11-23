import subprocess

def extract_audio(video_file, audio_file):
    """
    从MP4视频文件中提取音频。

    参数:
    video_file (str): 视频文件的路径。
    audio_file (str): 提取的音频文件的路径。
    """
    # 构建ffmpeg命令
    command = [
        'ffmpeg',
        '-i', video_file,  # 输入文件
        '-vn',  # 禁用视频
        '-c:a', 'mp3',  # 复制音频流
        audio_file  # 输出文件
    ]

    # 调用ffmpeg命令
    subprocess.run(command, check=True)

# 使用示例


video_path = input("请输入视频文件路径：")
audio_path = input("请输入mp3音频文件路径：")
extract_audio(video_path, audio_path)

# 修改音频格式
def convert_to_wav(input_file, output_file):
    command = [
        'ffmpeg',
        '-i', input_file,
        output_file
    ]
    subprocess.run(command, check=True)

# 使用示例
input_path = audio_path
output_path = input("请输入wav音频文件路径：")
convert_to_wav(input_path, output_path)