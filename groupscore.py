import logging
import pandas as pd
import tkinter as tk
from ttkbootstrap import Style


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


#获取小组名称及小组成员
def getgroupinfo(path):
  #用于存放小组信息
  groupinfo = {}
  #获取表格原始数据，提取表头为组员和组名的两列
  group = pd.read_excel(io = path)
  groupmember = list(group['组员'])
  groupname = list(group['组名'])

  #通过组名，获取成员名单
  for i in range(len(groupname)-1):
    if type(groupname[i]) == str:
      groupinfo[groupname[i]] = []
      #组长
      groupinfo[groupname[i]].append(groupmember[i])
      j = 1
      #得到组名后，循环添加组员
      while type(groupname[i+j]) != str:
          groupinfo[groupname[i]].append(groupmember[i+j])
          #防止越界
          if i+j >=53:
            break
          else:
            j+=1
    else:
      continue
  
  return groupinfo

#获取总分成绩
def getscore(path):
  scoreinfo = {}
  score = pd.read_excel(io=path)
  #名字为键，总分为值
  for i in range(score.shape[0]):
    scoreinfo[score['姓名'][i]] = [score['总分'][i]]
  
  return scoreinfo

#获取各组平均分
def getgroupaverage(group,score):
  #遍历各小组
  for key in group.keys():
    #记录总成绩
    totalscore = 0.0
    #分母
    denominator = len(group[key])
    #遍历小组成员
    for i in range(len(group[key])):
      #小组成员
      member = group[key][i]
      if type(member) == float:
        #跳过空白小组成员
        continue
      #没找到
      elif member not in score.keys():
        logger.warning("未找到{0}小组的成员{1}的成绩，请确认名称是否正确".format(key,member))
      
      #计算能找到的
      elif member in score.keys():
        #计算总分
        if type(score[member][0]) == str:
          logger.warning("{0}的成绩内容是{1}，无法计入总分，将不计算此人".format(member,score[member][0]))
          denominator -=1
          continue
        else:        
          totalscore += score[member][0]

    averagescore = totalscore/denominator

    logger.info("{0}的总分为{1}，平均分为{2}".format(key,totalscore,averagescore))

def getentry():
  grouppath= e1.get()
  scorepath = e2.get()
  
  groupinf = getgroupinfo(grouppath)
  scoreinf = getscore(scorepath)
  
  getgroupaverage(groupinf,scoreinf)

def clear():
  e1.delete(0,"end")
  e2.delete(0,"end")

if __name__ == "__main__" :
  # groupinf = getgroupinfo(r"E:\code\teamscore\高一9班小组名单-0510.xlsx")
  # scoreinf = getscore(r"E:\code\teamscore\2022-2023学年下学期高一期中测试-高一年级9班.xls")
    
  #主窗口
  window = tk.Tk()
  #导入主题库
  style = Style(theme='darkly')
  window = style.master

  #设置标题
  window.title('teachertool fo momoka')

  window.geometry("1000x700")

  #文本标签
  tk.Label(window,text="请输入小组消息表格存放位置").grid(row=0,column=0)
  tk.Label(window,text="请输入全班成绩表格存放位置").grid(row=1,column=0)
  #定义
  v1 = tk.StringVar()
  v2 = tk.StringVar()

  e1 = tk.Entry(window,textvariable=v1)
  e1.grid(row=0,column=1,padx=30,pady=10)

  e2 = tk.Entry(window,textvariable=v2)
  e2.grid(row=1,column=1,padx=30,pady=10)
  
  tk.Button(window,text ="开始计算",width=10,command=getentry).grid(row=2,column=0,stick="w",padx=30,pady=10)
  tk.Button(window,text ="清空",width=10,command=clear).grid(row=2,column=1,stick="w",padx=30,pady=10)

  window.mainloop()
