import module.get_urlList as get_urlList

caomin = get_urlList.Reques('https://www.cmdy5.com/')
urlList = caomin.get_content(".nav-down-1[id^='topnav'] a::attr('href')")


def nextPage(doc):
    a_button_text = doc.get_content(".page.mb a::text")
    try:
        next_page_index = a_button_text.index('下一页')
    except Exception:
        return False

    next_button_url = 'https://www.cmdy5.com/' + doc.get_content(".page.mb a::attr('href')")[next_page_index]
    return next_button_url


def saveMovie(movie_urlList, movie_nameList):
    for i in range(len(movie_urlList)):
        name = movie_nameList[i]
        url = movie_urlList[i]
        print(name, '-->', url)

        with open('movie.txt', 'a') as f:
            try:
                f.write('%s --> %s\n' % (name, url))
            except Exception:
                continue


for url in urlList:
    while url:
        movie_classify = get_urlList.Reques(url)
        movie_urlList = movie_classify.get_content(".link-hover::attr('href')")
        movie_nameList = movie_classify.get_content(".link-hover .name::text")
        url = nextPage(movie_classify)

        saveMovie(movie_urlList, movie_nameList)
