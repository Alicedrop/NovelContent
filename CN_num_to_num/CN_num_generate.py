def character_process(character, level):
    if character == "0":
        character = "零"

    elif character == "1":
        character = "一" + level

    elif character == "2":
        character = "二" + level
    elif character == "3":
        character = "三" + level
    elif character == "4":
        character = "四" + level
    elif character == "5":
        character = "五" + level
    elif character == "6":
        character = "六" + level
    elif character == "7":
        character = "七" + level
    elif character == "8":
        character = "八" + level
    elif character == "9":
        character = "九" + level

    return character


def space_process(space):
    # space为int
    str_space = str(space)
    space_len = len(str_space)
    result = ""  # 返回的十汉字，那自然是str
    zero_list = []
    if space_len == 4:
        # 有千
        for i, level in zip(range(0, space_len), ["千", "百", "十", ""]):
            item = str_space[i]

            if i == 0:
                # 读到千位
                if not item == 0:
                    result = character_process(item,level)
            elif i == 1:
                # 百位
                if item == 0:
                    result += "零"
                    zero_list.append(i)
                else:
                    result += character_process(item,level)
            elif i == 2:
                # 十位
                if item == 0:  # 注意，需要判断上一位是否是是零，所以可以建立一个列表，记录是0的位
                    zero_list.append(i)
                    if i - 1 in zero_list:  # 上一位是0
                        pass
                    else:
                        result += "零"
                else:
                    result += character_process(item,level)
            elif i == 3:
                # 个位
                if item == 0:
                    zero_list.append(i)
                else:
                    result += character_process(item,level)

    elif space_len == 3:
        # 最高位是百
        for i, level in zip(range(0, space_len), ["百", "十", ""]):
            item = str_space[i]
            if i == 0:
                # 读到百位
                if not item == 0:
                    result = character_process(item,level)
            elif i == 1:
                # 十位
                if item == 0:
                    result += "零"
                    zero_list.append(i)
                else:
                    result += character_process(item,level)
            elif i == 2:
                # 个位
                if item == 0:
                    zero_list.append(i)
                else:
                    result += character_process(item,level)
    elif space_len == 2:
        # 最高位为十位
        for i, level in zip(range(0, space_len), ["十", ""]):
            item = str_space[i]
            if i == 1:
                # 十位
                if item == 0:
                    result += "零"
                    zero_list.append(i)
                else:
                    result += character_process(item,level)
            elif i == 2:
                # 个位
                if item == 0:
                    zero_list.append(i)
                else:
                    result += character_process(item,level)
    elif space_len == 1:
        if str_space == "0":
            result = ""
        else:
            result = str_space
    return result


def num2cn_num(target):
    # 把数字转换为中文数字
    # 警告！未加入自动除去开头的零的判定，不能乱玩！请输入正常的阿拉伯数字！(范围0~9999 9999 9999)
    target = int(target)  # 保证target是数
    str_target = str(target)  # 只有str才有lne()、a[]等方法
    length = len(str_target)
    geSpace = 0
    wanSpace = 0
    yiSpace = 0
    if target > 999999999999:
        return "Over range"
    else:
        if length <= 4:  # 千及以下
            # 此时只有geSpace
            geSpace = target
            wanSpace = 0
            yiSpace = 0
            # OK,之后实现确认这是在哪个位，通过

            # 注意！！length是长度，而range以及顺序都是从零开始，值会减一！！

        elif 4 < length <= 8:
            # 若a="1 2345",易知length=5,geSpace=2345，即索引1起到结尾
            # 若a="12 3456",易知length=6,geSpace=3456,即从索引2到结尾
            # 对于一个长度为n的数，其geSpce = target[n-4,n]
            # 注意由于索引从0开始，长度为n的数结尾的索引是n-1，由于[：]取前不取后，所以到 n就可以取到n-1
            wanSpace = str_target[0:length - 4]
            wanSpace = int(wanSpace)

            geSpace = str_target[length - 4:length]
            geSpace = int(geSpace)

            yiSpace = 0

        elif 8 < length <= 12:
            yiSpace = str_target[0:length - 8]
            yiSpace = int(yiSpace)

            wanSpace = str_target[length - 8:length - 4]
            wanSpace = int(wanSpace)

            geSpace = str_target[length - 4:length]
            geSpace = int(geSpace)

        geSpace = space_process(geSpace)

        wanSpace = space_process(wanSpace)
        yiSpace = space_process(yiSpace)
        if not yiSpace == "":
            yiSpace += "亿"
        if not wanSpace == "":
            wanSpace += "万"  # 不应该在这里补
        result = yiSpace + wanSpace + geSpace

    return result


'''当前存在问题：
12340456 即某个space个位的零

'''
