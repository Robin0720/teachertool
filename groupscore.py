import logging
import pandas as pd


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
def getgroupaverage(group,socre):
  for key in group.keys():
    for i in range(len(group[key])):
      print(socre[group[key][i]])

groupinf = getgroupinfo(r"E:\code\teamscore\高一9班小组名单-0510.xlsx")
scoreinf = getscore(r"E:\code\teamscore\2022-2023学年下学期高一期中测试-高一年级9班.xls")

getgroupaverage(groupinf,scoreinf)