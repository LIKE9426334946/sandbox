from PIL import Image

# 打开图片
img1 = Image.open("1.jpg")
img2 = Image.open("2.jpg")
img3 = Image.open("3.jpg")
img4 = Image.open("4.jpg")


# 创建画布（1行4列）
new_img = Image.new("RGB", (width * 4, height))

# 依次粘贴（横向排列）
new_img.paste(img1, (0, 0))
new_img.paste(img2, (width, 0))
new_img.paste(img3, (width * 2, 0))
new_img.paste(img4, (width * 3, 0))

# 保存
new_img.save("merged_1x4.jpg")
