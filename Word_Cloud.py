import openpyxl
from wordcloud import WordCloud

# 读取数据
wb = openpyxl.load_workbook('data.xlsx')
# 获取工作表
ws = wb['国内疫情']
frequency_in = {}
for row in ws.values:
    if row[1] == "累计确诊":
        pass
    else:
        frequency_in[row[0]] = float(row[1])

frequency_out = {}
sheet_names = wb.sheetnames

for each in sheet_names:
    if '洲' in each:
        ws = wb[each]
        for row in ws.values:
            if row[1] == "累计确诊":
                pass
            else:
                frequency_out[row[0]] = float(row[1])
    else:
        pass


def generate_pic(frequency, name):
    wordcloud = WordCloud(font_path="C:/Windows/Fonts/SIMLI.TTF",
                          background_color="white",
                          width=1920, height=1080,
                          max_words=100,
                          max_font_size=500,
                          min_word_length=10,
                          relative_scaling=0.2
                          )
    # 按照确诊病例数目生成词云
    wordcloud.generate_from_frequencies(frequency)
    # 保存词云
    wordcloud.to_file('%s.png' % name)

# 调用函数
generate_pic(frequency_in, '国内疫情词云图')
# generate_pic(frequency_out, '国外疫情词云图')
