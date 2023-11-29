import os
from PIL import Image
from glob import glob


def join(png1, png2, flag='horizontal'):
    """
    :param png1: path
    :param png2: path
    :param flag: horizontal or vertical
    :return:
    """

    img1, img2 = png1, png2
    # img1 = img1.resize((1024, 768), Image.ANTIALIAS)
    # img2 = img2.resize((1024, 768), Image.ANTIALIAS)
    size1, size2 = img1.size, img2.size
    if flag == 'horizontal':
        joint = Image.new('RGB', (size1[0] + size2[0], size1[1]))
        loc1, loc2 = (0, 0), (size1[0], 0)
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
    # joint.save('./results/multi_gpu/images/test_fake_imgs/showresults/{}.png'.format())
    elif flag == 'vertical':
        joint = Image.new('RGB', (size1[0], size1[1] + size2[1]))
        loc1, loc2 = (0, 0), (0, size1[1])
        joint.paste(img1, loc1)
        joint.paste(img2, loc2)
    # joint.save('./results/multi_gpu/images/test_fake_imgs/showresults/{}.png'.format())
    return joint


if __name__ == '__main__':
    # 两张图片地址：
    # png1 = r"./data/val/labels_H/163268_7618393749_b.png"
    # png2 = r"./results/multi_gpu/images/test_fake_imgs/epoch_180/163268_7618393749_b.jpg"
    # 横向拼接
    source_path1 = r'C:\Processing_classification\Processing_classification\Processing_classification\808APP-PIC\808APP-PIC-PSPT\03VOIP-buster.csv'
    filelist1 = os.listdir(source_path1)
    source_path2 = r'C:\Processing_classification\Processing_classification\Processing_classification\808APP-PIC\808APP-PIC-KZZD\0807VOIP_buster.csv'
    filelist2 = os.listdir(source_path2)
    # path1 = glob(filelist1 + '/*.*')
    # path1.sort()
    # path2 = glob(filelist2 + '/*.*')
    # path2.sort()
    target_path = r'C:\Processing_classification\Processing_classification\Processing_classification\808APP-PIC\808APP-PIC-KZZD\VOIP_buster.csv'
    if os.path.exists(target_path) == False:
        os.mkdir(target_path)

    # print(len(filelist1))
    # print(len(filelist2))
    for index in range(len(filelist1)):
        img_A = Image.open(os.path.join(source_path1, filelist1[index]))
        for index2 in range(len(filelist2)):

            if filelist1[index][:-3] == filelist2[index2][:-3]:
                print("index:{}index1:{}".format(filelist1[index], filelist2[index2]))
                img_B = Image.open(os.path.join(source_path2, filelist2[index2]))
                # joint = join(img_A, img_B, flag='horizontal')
                joint = join(img_A, img_B, flag='vertical')
                joint.save(r'C:\Processing_classification\Processing_classification\Processing_classification\808APP-PIC\808APP-PIC-KZZD\VOIP_buster.csv/{}'.format(filelist1[index]))

