from django.test import TestCase
from collections import defaultdict

posts = [
    {
        'id': 1,
        'title': 'a'
    },
    {
        'id': 2,
        'title': 'b'
    },
    {
        'id': 3,
        'title': 'c'
    }
]

comments = [
    {
        'id': 1,
        'post': 2,
        'message': 'b2'
    },
    {
        'id': 2,
        'post': 3,
        'message': 'c2'
    },
    {
        'id': 3,
        'post': 2,
        'message': 'b2'
    },
    {
        'id': 4,
        'post': 1,
        'message': 'a2'
    },
    {
        'id': 5,
        'post': 1,
        'message': 'a2'
    }
]

...

print(posts)

result = [
    {
        'id': 3,
        'title': 'a',
        'comments': [
            {
                'id': 4,
                'post': 1,
                'message': 'a2'
            },
            {
                'id': 5,
                'post': 1,
                'message': 'a2'
            }
        ]
    },
    {
        'id': 2,
        'title': 'b',
        'comments': [
            {
                'id': 1,
                'post': 2,
                'message': 'b2'
            },
            {
                'id': 3,
                'post': 2,
                'message': 'b2'
            }
        ]
    },
    {
        'id': 1,
        'title': 'c',
        'comments': [
            {
                'id': 2,
                'post': 3,
                'message': 'c2'
            }
        ]
    },
]

post_comments = defaultdict(list)
for comment in comments:
    post_comments[comment['post']].append(comment)

res = []
for post in posts:
    post_data = {
        'id': post['id'],
        'title': post['title'],
        'comments': post_comments.get(post['id'], [])
    }
    res.append(post_data)

print(res)

posts = [
    {
        'id': 1,
        'author': 23,
        'title': 'a'
    },
    {
        'id': 2,
        'author': 24,
        'title': 'b'
    },
    {
        'id': 3,
        'author': 23,
        'title': 'c'
    },
    {
        'id': 4,
        'author': 25,
        'title': 'c'
    }
]
followings = [23, 24]
