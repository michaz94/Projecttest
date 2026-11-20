import re,json,subprocess,sys
URLS={1:"https://www.goodreads.com/book/show/18191523-radiant-tome-1",2:"https://www.goodreads.com/book/show/21991318-radiant-tome-2",3:"https://www.goodreads.com/book/show/25117448-radiant-tome-3"}
out=[]
for t,u in URLS.items():
    h=subprocess.run(['curl','-s','-m','30','-A','Mozilla/5.0',u],capture_output=True,text=True).stdout
    m=re.search(r'<script id="__NEXT_DATA__"[^>]*>(.*?)</script>',h,re.S)
    d=json.loads(m.group(1)); st=d['props']['pageProps']['apolloState']
    # livre principal
    bk=[v for k,v in st.items() if k.startswith('Book:') and v.get('webUrl','') and v['webUrl'].startswith(u)]
    b=bk[0]
    work=st[b['work']['__ref']] if b.get('work') else {}
    stats=work.get('stats',{})
    revs=[]
    for k,v in st.items():
        if k.startswith('Review:'):
            ref=v.get('creator',{}).get('__ref'); cr=st.get(ref,{}) if ref else {}
            revs.append(dict(review_id=v['id'].split(':')[-1],author=cr.get('name'),rating=v.get('rating'),created_at=v.get('createdAt'),updated_at=v.get('updatedAt'),like_count=v.get('likeCount'),comment_count=v.get('commentCount'),text=v.get('text')))
    print(t,b.get('title'),stats.get('averageRating'),stats.get('ratingsCount'),stats.get('textReviewsCount'),len(revs))
    out.append(dict(tome=t,url=u,book_title=b.get('title'),average_rating=stats.get('averageRating'),ratings_count=stats.get('ratingsCount'),text_reviews_count=stats.get('textReviewsCount'),extracted_reviews_count=len(revs),reviews=revs))
json.dump(out,open('goodreads_radiant_t1_t3_raw.json','w'),ensure_ascii=False,indent=1)
