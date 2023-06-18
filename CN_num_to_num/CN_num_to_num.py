# This is a lib for NovelContent module,enabling it to convert
# date:2023.06.18

def space_process(target):
    # 对于区内容的处理
    haveQian = "千" in target  # 是否有千字
    haveBai = "百" in target  # 是否有百字
    haveShi = "十" in target  # 是否有十字
    print("对于以下对象的spaceConvert:", target, ",",
          "haveQian:%s,haveBai:%s,haveShi:%s" % (haveQian, haveBai, haveShi))
    if haveQian:
        qian = target.split("千")[0]
        afterQian = target.split("千")[1]
        if haveBai:
            bai = afterQian.split("百")[0]
            afterBai = afterQian.split("百")[1]
            if haveShi:
                shi = afterBai.split("十")[0]
                afterShi = afterBai.split("十")[1]
                if afterShi:  # 等同于haveGe.在”十“字后面有内容，说明有个位
                    ge = afterShi
                else:
                    ge = ""
            else:
                shi = ""
                if afterBai:  # 如果没有”十“字，但是百字后面有内容，则百字后面的那是个位的
                    ge = afterBai
                else:
                    ge = ""
        else:  # 有千无百
            bai = ""
            if haveShi:  # 有千无百有十
                shi = afterQian.split("十")[0]
                afterShi = afterQian.split("十")[1]
                if afterShi:  # 等同于haveGe.在”十“字后面有内容，说明有个位
                    ge = afterShi
                else:
                    ge = ""
            else:  # 有千无百无十
                shi = ""
                if afterQian:  # 有千无百无十,如果千以后有内容，则都是个位
                    ge = afterQian
                else:  # 千以后就无内容了，个也是空的
                    ge = ""
    else:  # 无千，开始检测是否有百
        qian = ""
        if haveBai:
            bai = target.split("百")[0]
            afterBai = target.split("百")[1]
            if haveShi:
                shi = afterBai.split("十")[0]
                afterShi = afterBai.split("十")[1]
                if afterShi:
                    ge = afterShi
                else:
                    ge = ""
            else:
                shi = ""
                if afterBai:
                    ge = afterBai
                else:
                    ge = ""
        else:  # 无千无百
            bai = ""
            if haveShi:
                shi = target.split("十")[0]
                afterShi = target.split("十")[1]
                if afterShi:
                    ge = afterShi
                else:
                    ge = ""
            else:  # 无千无百无十
                shi = ""
                ge = target

    if qian == "":
        qian = 0
    else:
        qian = int(qian)

    if bai == "":
        bai = 0
    else:
        bai = int(bai)

    if shi == "":
        shi = 0
    else:
        shi = int(shi)

    if ge == "":
        ge = 0
    else:
        ge = int(ge)

    result = qian * 1000
    result += bai * 100
    result += shi * 10
    result += ge

    print("spaceConvert结果:%s,qian%s,bai%s,shi%s,ge%s" % (result, qian, bai, shi, ge))
    return result


def cn_num2num(text):
    text = text.replace("仟", "千")
    text = text.replace("佰", "百")
    text = text.replace("拾", "十")

    text = text.replace("零", "0")
    text = text.replace("〇", "0")

    text = text.replace("一", "1")
    text = text.replace("壹", "1")

    text = text.replace("二", "2")
    text = text.replace("贰", "2")
    text = text.replace("两", "2")

    text = text.replace("三", "3")
    text = text.replace("叁", "3")
    text = text.replace("四", "4")
    text = text.replace("肆", "4")

    text = text.replace("五", "5")
    text = text.replace("伍", "5")

    text = text.replace("六", "6")
    text = text.replace("陆", "6")
    text = text.replace("七", "7")
    text = text.replace("柒", "7")

    text = text.replace("八", "8")
    text = text.replace("捌", "8")
    text = text.replace("九", "9")
    text = text.replace("玖", "9")

    print("替换处理后的text:", text, type(text))

    haveWan = "万" in text  # 输入的中文数字是否有“万”字（10^4）
    haveYi = "亿" in text  # 输入的中文数字是否有“亿”字（10^8）
    print("haveYi & haveWan", haveYi, haveYi)
    #
    # 分别是亿区（称为xxx亿的部分）万区（称为xxx万的部分）  个区（10^3 到1）
    # 例如一千五百五十亿六千三百五十五万四千六百零一（1550 6355 4601）
    # 则亿区yiSpace=1550,万区wanSpace=6355,个区geSpace=4601
    wanSpace = ""
    yiSpace = ""
    geSpace = ""

    afterYi = ""
    afterWan = ""

    if haveYi:
        yiSpace = text.split("亿")[0]
        afterYi = text.split("亿")[1]

        if haveWan:  # 若有亿也有万，则对以亿拆分的亿后面的内容分析万
            wanSpace = afterYi.split("万")[0]
            afterWan = afterYi.split("万")[1]
            print(wanSpace)
            print(afterWan)
            if afterWan:  # 万字之后有内容(因为一个数里没有“个”，不能像亿区万区用亿、万字来识别)，即个区有内容,
                geSpace = afterWan
            else:
                geSpace = "0"

        else:  # 无万字，无万区
            wanSpace = "0"
            if afterYi:  # 看亿字以后有没有内容，因为没有万区，有内容则说明有个区
                geSpace = afterYi
            else:  # 亿字之后无内容，说明也无个区
                geSpace = "0"
    else:  # 没有亿字
        yiSpace = "0"
        print("当前无亿字，yiSpace=0")
        if haveWan:  # 若有万，则对输入文本分析万
            wanSpace = text.split("万")[0]
            afterWan = text.split("万")[1]
            print("wanSpace:%s,afterWan:%s" % (wanSpace, afterWan))
            if afterWan:  # 万字之后有内容(因为一个数里没有“个”，不能像亿区万区用亿、万字来识别)，即个区有内容,
                geSpace = afterWan
            else:
                geSpace = "0"

        else:  # 无万字，无万区
            wanSpace = "0"
            print("当前无万字，wanSpace=0")
            if text:  # 没有亿区也没有万区，看看输入处理的文本是否为空
                geSpace = text
                print("输入文本text不为空，geSpace=text=", geSpace)
            else:  # 输入处理的文本为空，个也为0
                geSpace = "0"
                print("输入文本text为空，geSpace=0")
    processResult = 0
    print("准备生成processResult,此时yiSpace为%s，wanSpace为%s,geSpace为%s" % (yiSpace, wanSpace, geSpace))
    if haveYi:
        processResult += space_process(yiSpace) * 100000000
    if haveWan:
        processResult += space_process(wanSpace) * 10000
    processResult += space_process(geSpace)
    return processResult



