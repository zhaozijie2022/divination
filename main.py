import random
# 蓍草占卜法
if __name__ == '__main__':
    yaos = []
    for i in range(6):  # 六爻, 先得初爻在下
        n = 50 - 1
        for j in range(3):  # 三次变卦为1爻
            n_right = int(n * random.random())
            n_left = n - n_right
            n_right -= 1  # 左手为天, 右手为地, 从右手取出1枝代表"人"
            # 4个分成一组, 取出最后一组
            mod_left = n_left % 4
            if mod_left == 0:
                mod_left += 4
            mod_right = n_right % 4
            if mod_right == 0:
                mod_right += 4
            # 将剩余木策合并
            n = n_left + n_right - mod_left - mod_right
        yaos.append(int(n / 4))
    ben_gua = ""
    for i in range(6):
        ben_gua += "0" if yaos[i] % 2 == 0 else "1"
    bian_gua = ben_gua * 1
    for i in range(6):
        if yaos[i] == 6:
            bian_gua = bian_gua[:i] + "1" + bian_gua[i + 1:]
        elif yaos[i] == 9:
            bian_gua = bian_gua[:i] + "0" + bian_gua[i + 1:]
    tips = ["以本卦动爻之爻辞为占", "以本卦二动爻爻辞为占，上位为主", "以本卦、变卦的卦辞、彖辞为占",
            "以变卦二不动爻爻辞为占，下位为主", "以变卦不变爻之爻辞为占", "以变卦的卦辞为占，并参考彖辞"]
    tip = ""
    for i in range(6):
        if ben_gua[i] != bian_gua[i]:
            tip += tips[i] + ";"
    if tip == "":
        tip = "以本卦卦辞、彖辞为占;"
    print("占卜结果: ")
    print("爻数: ", yaos)
    print("本卦: ", ben_gua)
    print("变卦: ", bian_gua)
    print("占卜建议: ", tip)














