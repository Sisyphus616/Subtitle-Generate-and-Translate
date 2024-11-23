from translate import Translator

def translate(subtitle, dest_lang="ZH"):
    translator = Translator(from_lang="JA",to_lang=dest_lang)
    translated_text = translator.translate(subtitle)
    return translated_text


srt_ori_path = input("请输入原始srt文件地址：")
srt_path = input("请输入翻译后srt文件地址：")
with open(srt_ori_path, "r", encoding='utf-8') as f:
    lines = f.readlines()
    for i in range(0, len(lines), 4):
        translate_text = translate(lines[i+2])
        with open(srt_path, "a", encoding='utf-8') as f:
            f.write(lines[i])
            f.write(lines[i+1])
            f.write(translate_text + "\n")
            f.write("\n")
        print(i)
        print(translate_text)
        # time.sleep(1)