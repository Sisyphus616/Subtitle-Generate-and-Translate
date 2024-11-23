import whisper
# from translate import Translator

# def translate(subtitle, dest_lang="zh-cn"):
#     translator = Translator(to_lang=dest_lang)
#     translated_text = translator.translate(subtitle)
#     return translated_text

def transcribe_audio_whisper(audio_path):
    # 加载Whisper模型
    model = whisper.load_model("medium")
    
    # 转录音频文件
    result = model.transcribe(audio_path)
    
    # 返回转录的文本
    return result

# 使用示例
audio_path = input("请输入wav音频地址：")
srt_ori_path = input("请输入原始srt文件地址：")
transcribed_text = transcribe_audio_whisper(audio_path)

'''
返回内容：
    - text: 转录的文本，不分句
    - segments: 一个包含转录文本的列表。
        - id: 段落的ID
        - start: 段落的开始时间
        - end: 段落的结束时间
        - text: 段落的文本
    - language: 语言
'''

def second_to_time(s):
    hour = s // 3600
    minute = s % 3600 // 60
    second = s % 60
    str = "%02d:%02d:%02d,000" % (hour, minute, second)
    return str

# print(transcribed_text)

for item in transcribed_text["segments"]:
    st = item["start"]
    ed = item["end"]
    timestamp = f"{second_to_time(st)} --> {second_to_time(ed)}"
    with open(srt_ori_path, "a", encoding='utf-8') as f:
        f.write(str(item["id"]+1) + "\n")
        f.write(timestamp + "\n")
        # f.write(translate(item["text"]) + "\n")
        f.write(item["text"] + "\n")
        f.write("\n")
    print(item["id"]+1)
    # # print(item["text"])
    # print(timestamp)
    # print(translate(item["text"]))