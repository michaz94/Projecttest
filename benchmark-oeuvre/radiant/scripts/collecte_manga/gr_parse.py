import re,json
URL={1:"https://www.goodreads.com/book/show/18191523-radiant-tome-1",2:"https://www.goodreads.com/book/show/21991318-radiant-tome-2",3:"https://www.goodreads.com/book/show/25117448-radiant-tome-3"}
out=[]
for t in (1,2,3):
    h=open(f'gr_t{t}.html',encoding='utf8').read()
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
    st=json.loads(m.group(1))['props']['pageProps']['apolloState']
    b=[v for k,v in st.items() if k.startswith('Book:') and (v.get('webUrl') or '').startswith(URL[t])][0]
    work=st[b['work']['__ref']]; stats=work.get('stats',{})
    revs=[]
    for k,v in st.items():
        if k.startswith('Review:'):
            cr=st.get(v.get('creator',{}).get('__ref'),{})
            revs.append(dict(review_id=v['id'].split(':')[-1],author=cr.get('name'),rating=v.get('rating'),created_at=v.get('createdAt'),updated_at=v.get('updatedAt'),like_count=v.get('likeCount'),comment_count=v.get('commentCount'),spoiler=v.get('spoilerStatus'),text=v.get('text')))
    revs.sort(key=lambda r:-(r['like_count'] or 0))
    print(t,b['title'],stats.get('averageRating'),stats.get('ratingsCount'),stats.get('textReviewsCount'),len(revs),sum(1 for r in revs if r['text']),sum(len((r['text'] or '').split()) for r in revs))
    out.append(dict(tome=t,url=URL[t],book_title=b['title'],average_rating=stats.get('averageRating'),ratings_count=stats.get('ratingsCount'),text_reviews_count=stats.get('textReviewsCount'),extracted_reviews_count=len(revs),reviews=revs))
json.dump(out,open('goodreads_radiant_t1_t3_raw.json','w'),ensure_ascii=False,indent=1)
import collections
for o in out: print(o['tome'],collections.Counter(r['rating'] for r in o['reviews']))
