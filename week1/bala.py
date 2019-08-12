import ybc_trans as t
import ybc_box as b
while True:
    ch = b.choicebox('您想将中文成翻译英文，还是将英文翻译成中文。请选择：',['中译英','英译中','退出'])
    if ch == '中译英':
        zho = b.enterbox('请输入中文文本：')
        x = len(zho)
        if x !=0:
            zho = t.zh2en(zho)
            print('翻译完成：'+zho)
    if ch == '英译中':
        yin = b.enterbox('请输入英文文本：')
        y = len(yin)
        if y != 0:
            yin = t.en2zh(yin)
            print('翻译完成：'+yin)
    if ch == '退出':
        break