#-*- coding:utf-8 -*-

import requests,pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# 执行 API 调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
r = requests.get(url)
print('status code:',r.status_code)

# 将API响应存储在一个变量中
response_dict = r.json()
#print(response_dict.keys())
print('Total repositories:',response_dict['total_count'])

# 探索有关仓库的信息
repo_dicts = response_dict['items']
print('repositories returned:',len(repo_dicts))

# 研究第一个仓库
'''
repo_dict = repo_dicts[0]
print('\nkeys:',len(repo_dict))
for key in sorted(repo_dict.keys()):
    print(key)
'''
names, plot_dicts = [], []
#print('\nSelected information about first repository:')
for repo_dict in repo_dicts:
    '''('name:',repo_dict['name'])
    print('Owner:',repo_dict['owner']['login'])
    print('Stars:',repo_dict['stargazers_count'])
    print('Repository:',repo_dict['html_url'])
    #print('Created:',repo_dict['created_at'])
    #print('updated:',repo_dict['updated_at'])
    print('Description:',repo_dict['description'])''' 
    names.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    plot_dict = {
        'value':repo_dict['stargazers_count'],
        'label':repo_dict['description'],
        'xlink':repo_dict['html_url'],
        }
    plot_dicts.append(plot_dict)
# 可视化
my_style = LS('#333366',base_style=LCS)

# 创建配置对象
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.lable_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
chart = pygal.Bar(my_config,style=my_style)
# show_legend 隐藏图例
#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Python Projects on Github'
chart.x_labels = names

chart.add('',plot_dicts)
chart.render_to_file('python_repos_5.svg')
