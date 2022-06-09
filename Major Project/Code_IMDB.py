import bs4
import urllib.request as url
stopwords=["A truly honest police officer is transferred to a town controlled by a gangster he has humiliated. The gangster believes he can use good power to bring down this officer who made him look foolish and weak."
           ,"{}","Based on an incredible true story of the Battle of Saragarhi in which an army of 21 Sikhs fought against 10,000 Afghans in 1897.",
           "After the devastating events of Avengers: Infinity War (2018), the universe is in ruins. With the help of remaining allies, the Avengers assemble once more in order to reverse Thanos' actions and restore balance to the universe.",
           "","Director","Writers","Stars"]
moviename = input("Enter movie name :")
path="https://www.imdb.com/find?ref_=nv_sr_fn&q="+moviename
http=url.urlopen(path)
page=bs4.BeautifulSoup(http,'lxml')
td=page.find('td',class_='result_text')
a_tag=td.find('a')
href=a_tag["href"]
newurl="https://www.imdb.com/"+href
http_2=url.urlopen(newurl)
page_2=bs4.BeautifulSoup(http_2,'lxml')



'''
path_m="https://www.imdb.com/find?ref_=nv_sr_fn&q="+moviename
http_m=url.urlopen(path_m)
page_m=bs4.BeautifulSoup(http_m,'lxml')
td_m=page_m.find('td',class_='result_text')
a_tag_m=td_m.find('a')
href_m=a_tag_m["href"]
newurl_m="https://www.imdb.com/"+href_m
http_2m=url.urlopen(newurl_m)
page_2m=bs4.BeautifulSoup(http_2m,'lxml')
'''


'''Title'''
def details_():
    title=page_2.find('h1',class_='TitleHeader__TitleText-sc-1wu6n3d-0 dxSWFG').text.strip()
    return title

'''Sub title'''
def details_2():
    sub_title=page_2.find('span', class_="GenresAndPlot__TextContainerBreakpointXS_TO_M-cum89p-0 dcFkRD").text.strip()
    return sub_title

'''Cast'''
def details_3():
    cast = page_2.find('li', class_="ipc-metadata-list__item").text.strip() +"\n" + page_2.find('li',attrs={'data-testid':'title-pc-principal-credit','class':"ipc-metadata-list__item ipc-metadata-list-item--link"}).text.strip()
    '''
    for word in stopwords:
        if word in cast:
            cast=cast.replace("Director","Director:")
            cast=cast.replace("Writers","Writers:")
            cast=cast.replace("Stars","Stars:")
    '''
    return cast.strip()

'''Storyline'''
def details_4():
     storyline = page_2.find('div',attrs={'class':'ipc-html-content ipc-html-content--base'}).text.strip()
     return storyline

'''Rating'''
def details_5():
    rating = page_2.find('span',class_='AggregateRatingButton__RatingScore-sc-1ll29m0-1 iTLWoV').text.strip()
    return rating

'''User Reviews'''
def details_7():
    review=page_2.find('span',attrs={'class':'UserReviewSummary__Summary-kfza1v-1 bA-dHai'}).text + page_2.find('div',attrs={'class':'ipc-overflowText ipc-overflowText--listCard ipc-overflowText--height-long ipc-overflowText--long ipc-overflowText--base'}).text
    return review.strip()

