'''
格式：[自定义内容,不含'[]'][-_?](可选)[数字]
递增值：n
'''
import re,os,sys
reg = '(\[[^\[\]]+\][\-\_]?)?([0-9]+)(\..*)' #正则
inc = 1  # 递增值

'''
核心逻辑
参数
    @fstr: 第一个文件的名字
    @path：重命名路径
    @inc： 增长量
'''
def renameDir(path,fstr,inc=1):
    try:
        mchObj = re.match(reg,fstr)
    except:
        print('重命名格式不规范!')
        return
    else:
        content, firstNum, format = mchObj.group(1), mchObj.group(2), mchObj.group(3)
        if content==None:
            content=''
        wrong=0
        flag = False
        curNumber = firstNum
        if not os.path.exists(path):
            print('选择路径不存在！')
            return 
        for file in os.listdir(path):
            fpath = path+os.path.sep+file
            if os.path.isdir(fpath):
                wrong+=1
                flag=True
                continue
            
            newName = content+curNumber+format
            newPath = path+os.path.sep+newName
            os.rename(fpath,newPath)
            
            # 前导零处理
            newNumber = str(int(curNumber)+inc)
            for i in range(0,len(curNumber)-len(newNumber)):
                newNumber = '0'+newNumber
            curNumber = newNumber
            
        if flag:
            print('选择目录存在子目录。共略过%d个子目录'%wrong)
if __name__=='__main__':
    if len(sys.argv)==3:
        renameDir(sys.argv[1],sys.argv[2])
    else:
        renameDir(sys.argv[1],sys.argv[2],int(sys.argv[3]))
    