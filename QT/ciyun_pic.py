
# 关于生成词云图的测试文件
import jieba
from wordcloud import WordCloud

# 将输入特定文本内容生成词云图
def getciyuntu(textcontent):
    # 把歌词剪开
    cut_text = jieba.cut(textcontent)
    # 以空格拼接起来
    result = " ".join(cut_text)
    # 生成词云图
    wc = WordCloud(
        font_path='simhei.ttf',  # 设置字体路劲
        background_color='white',  # 设置背景颜色
        # 设置生成图片的宽和高
        width=512,
        height=384,
        max_font_size=60,  # 设置字体大小
        min_font_size=10,
        # mask=plt.imread('background.jpg'),  # 设置背景图片
        max_words=1000
    )
    wc.generate(result)
    wc.to_file('ciyuntu.png')  # 图片保存

if __name__ == '__main__':
    textcontent='针对中美就经贸问题进行磋商，外交部发言人耿爽在今天（7日）的例行记者会上表示，中方始终认为，相互尊重、平等互利是达成协议的前提和基础，加征关税解决不了任何问题。谈判本身就是一个讨论的过程，双方存在分歧很正常，中方不回避矛盾，对继续磋商具有诚意。'
    getciyuntu(textcontent)