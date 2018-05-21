import requests

from operator import itemgetter

# 执行 API 调用并存储响应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print('status code:',r.status_code)

# 处理有关每篇文章的信息
submission_ids = r.json()
submission_dicts = []
for submission_id in subminssion_ids[:30]:
    # 对每篇文章执行一个 API 调用
    url = ('https://hacker-news.firebaseio.com/v0/item/' +
            str(submission_id) + '.json')
    submission_r = requests.get(url)
    print(submission_r.status_code)
    response_dict = submission_r.json()
    
    submission_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id=' + str(submission_id),
        # dict.get 不确定某键是否存在时
        'comments':response_dict.get('descendants',0)
        }        
    submisson_dicts.append(submission_dict)

submisson_dicts = sorted(submission_dicts,key=itemgetter('comments'),
                            reverse=True)

for submission_dict in submission_dicts:
    print('\nTitle:',submission_dict['title'])
    print('Discussion link:',submisson_dict['link'])
    print('comments:',submission_dict['comments'])
    
