# coding:utf-8
import requests
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

# 指向API调用并存储响应
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
rep = requests.get(url)
# print("pesponse status code:",rep.status_code)
# 200
# 将Api响应存储在一个变量中
rep_dict = rep.json()
# 处理结果
# print(rep_dict.keys())
#-- dict_keys(['total_count', 'incomplete_results', 'items'])
repo_dicts = rep_dict["items"]
# 研究第一个仓库
# repo_dict = repo_dicts[0]
# for key in sorted(repo_dict.keys()):
# 	print(key)
names , stars = [] , []
for repo_dict in repo_dicts:
	names.append(repo_dict["name"])
	# stars.append(repo_dict['stargazers_count'])
	# 添加自定义工具提示 可单击的链接
	stars.append({'value':repo_dict['stargazers_count'],'label':repo_dict['description'],'xlink':repo_dict['html_url']})
# 可视化
my_style = LS('#333366', base_style=LCS)
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000
# chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart = pygal.Bar(my_config,style=my_style)
chart.title = '在GitHub上更受关注的Python项目'
chart.x_labels = names
chart.add('',stars)
chart.render_to_file('python_repos.svg')
