# encoding: utf-8
import os

def init_box(imgfolder):
  """
    给原始图片预先只生成一个box框，方便标注的时候copy paste
  """
  files = [m for m in os.listdir(imgfolder) if m.endswith('jpg')]
  for f in files:
    txt_name = f.replace('.jpg','.txt')
    txt_file = os.path.join(imgfolder,txt_name)
    if not os.path.exists(txt_file):
      with open(txt_file,'w') as f:
        f.write('0 0.5 0.5 0.206395 0.179688')

if __name__ == '__main__':
  imgfolder = '../images'    # 也可以放到trining文件夹中
  init_box(imgfolder)
