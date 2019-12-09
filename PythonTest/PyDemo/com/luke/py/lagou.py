import requests
import time
import json
from urllib.parse import quote


def get_page(url_start, url_parse, params, job):
    # 创建一个session对象
    s = requests.Session()
    # 用session对象发出get请求，请求首页获取cookies
    s.get(url_start, headers=headers, timeout=3)
    cookie = s.cookies
    # 获取此次的文本
    respons = s.post(url_parse, data=params, headers=headers, cookies=cookie)

    # 设置每次请求间隔5秒钟
    time.sleep(5)
    # 从json数据钟获取到数据的总数
    json_data=json.loads(respons.text)
    total_Count = json_data['content']['positionResult']['totalCount']
    print("搜索结果一共又" + str(total_Count) + "条")
    '''
          拉勾网每页是15条数据,默认只有30页的信息,如果抓取信息的总数/15>30,就取30页
    '''
    if int(total_Count / 15) < 30:
        page_number = int(total_Count / 15)
    else:
        page_number = 30

    # 根据页数决定方法调用的次数
    for pn in range(1, page_number + 1):
        get_info(url_start, url_parse, pn, job)
        print("```````````````````````````````````````````")


def get_info(url_start, url_parse, page_number, job):
    print("正在爬取第" + str(page_number) + "页数据")
    data = {
        'first':'false',
        'pn':page_number,#页数
        'kd':job #搜索关键字
    }

    #创建一个session对象
    s=requests.Session()
    #用session对象发出get请求，请求首页获取cookies
    s.get(url_start,headers=headers,timeout=3)
    #获取此处的cookie
    cookie=s.cookies
    #获取此次的文本
    response=s.post(url_parse,data=data,headers=headers,cookies=cookie,timeout=3)
    time.sleep(5)
    text=json.loads(response.text)
    info=text['content']['positionResult']['result']
    for i in info:
        # 获取公司id
        print('公司id', i['companyId'])
        # 获取公司全名
        print('公司全名', i['companyFullName'])
        # 获取位置
        print('位置', i['city'])
        # 获取薪资
        print('薪资', i['salary'])
        # 获取公司规模
        print('公司所在人数', i['companySize'])
        # 获取要求技能
        print('所需技能', i['skillLables'])
        # 招聘信息发布时间
        print('信息发布时间', i['createTime'])
        # 区域
        print('所在区域', i['district'])
        # 要求学历
        print('要求学历', i['education'])
        #  车站名称
        print('车站名称', i['stationname'])
        print("===========================================================")


if __name__=='__main__':
    job=input("欢迎来到拉勾网,请输入您想咨询的职位:")
    job_transcode=quote(job)
    print("job",job_transcode)
    url_start="https://www.lagou.com/jobs/list_"+job_transcode+"/p-city_0?&cl=false&fromSearch=true&labelWords=&suginput="
    url_parse="https://www.lagou.com/jobs/positionAjax.json?needAddtionalResult=false"
    print(url_start)
    params={
        'first':'true',
        'pn':'1',
        'kd':job
    }
    # 加入请求头,伪装成浏览器
    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        'Referer': 'https://www.lagou.com/jobs/list_' + job_transcode + '/p-city_undefined?&cl=false&fromSearch=true&labelWords=&suginput=',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'
    }

    get_page(url_start,url_parse,params,job)

