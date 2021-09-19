
import requests
from bs4 import BeautifulSoup
import csv


def getdata():
  try:
        # URL = "https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches"

        # r = requests.get(URL)
        r = requests.get(
                "https://www.cricbuzz.com/cricket-series/3472/indian-premier-league-2021/matches").text
        soup = BeautifulSoup(r, 'lxml')
        val = 1
        team1=0
        nteam1=0
        nteam2=0
        datatocompare=getdatetimedata()
        matchesm = {}
        matchesm["data"] = []
        matchesm["next"] = []
        nextmatchlink1 = ''
        table = soup.find('div', attrs={
                'class': 'cb-bg-white cb-col-100 cb-col cb-hm-rght cb-series-filters'})

        for row in table.findAll('div',
                                attrs={'class': 'cb-col-60 cb-col cb-srs-mtchs-tm'}):
                try:
                        matchm = {}
                        link='www.cricbuzz.com'+row.a['href']
                        matchm['link'] = link
                        matchm['matchteam'] = row.span.text
                        matchm['vanue'] = row.div.text
                        team1=getteam(row.span.text,team1)                       
                        team2=getteam(row.span.text,team1)
                        matchm['team1']=team1
                        matchm['team2']=team2
                        matchm['matchst']=0
                        

                        
                        
                        if(val == 1):
                                nextmatchlink1 = link
                                nteam1=team1
                                nteam2=team2
                        #else:
                            #matchm['date'] = search(datatocompare,row.span.text)

                        team1=0
                        team2=0
                        
                        try:
                                matchm['data'] = row.find( 'a', attrs={'class': 'cb-text-complete'}).text
                                matchm['matchst'] = 1

                        except Exception as e:
                                val = 0
                                pass
                        matchesm["data"].append(matchm)
                except Exception as e:
                          pass
        matchnext = {}
        matchnext['nextmatchlink'] = nextmatchlink1
        matchnext['nteam1'] = nteam1
        matchnext['nteam2'] = nteam2
        try:
                matchesm["next"].append(matchnext)
        except Exception as e:
                pass
        return matchesm
        #print(search(datatocompare,nextmatchlink1))

  except Exception as e:
                 print(e)
        # return {"status": False, "error": e}

def search(values, searchFor):
    for k in values:
        for v in values[k]:
            if v['string'] in searchFor: 
                 return v['date']
            

def getteam(stringcomp,team1):
        if "Rajasthan" in stringcomp: 
                if(team1!=1):
                        return 1
        if "Bangalore" in stringcomp: 
           if(team1!=2):
                return 2
        if "Punjab" in stringcomp: 
           if(team1!=3):
                return 3
        if "Mumbai" in stringcomp: 
           if(team1!=4):
                return 4
        if "Chennai" in stringcomp: 
           if(team1!=5):
                return 5
        if "Capitals" in stringcomp: 
           if(team1!=6):
                return 6
        if "Hyderabad" in stringcomp: 
           if(team1!=7):
                return 7
        if "Kolkata" in stringcomp: 
           if(team1!=8):
                return 8
def getdatetimedata():
    try:
            
        getdatetimeurl = requests.get(
                    "https://www.espncricinfo.com/series/ipl-2021-1249214/match-schedule-fixtures").text
        getdatetimesoup = BeautifulSoup(getdatetimeurl, "lxml")
        getdatetimetable = getdatetimesoup.find('div', attrs={
                    'class': 'card content-block league-scores-container'})
        getdatetimematchm = {}
        getdatetimematchm['data'] = []

        for getdatetimerow in getdatetimetable.findAll('div',
                                    attrs={'class': 'col-md-8 col-16'}):
                #print(row.find('div',attrs={'class':'status'}).text)
            #    for rr in row.findAll('div',attrs={'class':'team'}):
            #      print(rr.text)

                    getdatetimett=getdatetimerow.find('a',attrs={'class':'match-info-link-FIXTURES'})
                    getdatetimenh=getdatetimett.find('div',attrs={'class':'description'}).text
                    getdatematchm = {}
                    getdatematchm['string'] = getdatetimenh[:10]
                    getdatematchm['date'] = getdatetimerow.find('div',attrs={'class':'status'}).text
                    getdatetimematchm['data'].append(getdatematchm)
                

        
        return getdatetimematchm
    
    except Exception as e:
                    pass
            
