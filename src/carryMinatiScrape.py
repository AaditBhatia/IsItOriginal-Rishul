import json
from lib2to3.pgen2.token import NEWLINE
from sqlalchemy import null
from youtube_transcript_api import YouTubeTranscriptApi
import scrapetube


postingList={}
def generateListOfChannelTranscript(): #this method will return a list of video id's
    video_id='lZC45nxzH7Q' 
    idList=[]
    idList.append(video_id)
    #UCj22tfcQrWG7EMEKS0qLeEg
    allVideos=scrapetube.get_channel("UCj22tfcQrWG7EMEKS0qLeEg")
    for channel in allVideos:
        idList.append(channel['videoId'])
    print(len(idList))
    channelVideos = scrapetube.get_channel("UC0IWRLai-BAwci_e9MylNGw")
    for channel in channelVideos:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])

    channelProductionOfficials=scrapetube.get_channel('UCUF6oiWricAnO0WYEHZWEaQ')
    for channel in channelProductionOfficials:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    
    playListQuarantineAndChill=scrapetube.get_playlist('PLObNowOPccbukgcAXAjzBnuLobtcjXit0')
    for channel in playListQuarantineAndChill:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    playListYouWantAPartner=scrapetube.get_playlist('PLObNowOPccbtrlq0cJgQJxngTsrCITCGY')
    for channel in playListYouWantAPartner:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    playListWrongWithIndianSchools=scrapetube.get_playlist('PLObNowOPccbsD0FeNlfx_-424AgTV1nPA')
    for channel in playListWrongWithIndianSchools:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    playListIndianWrapper=scrapetube.get_playlist('PLObNowOPccbtESonQJ_jlGHLw0ghFdY7-')
    for channel in playListIndianWrapper:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    playListIndianMusic=scrapetube.get_playlist('PLObNowOPccburE_FYVnxr4zFf3Pb8foKa')
    for channel in playListIndianMusic:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    playListGujjarSweg=scrapetube.get_playlist('PLObNowOPccbuYUP8MfsrnvHu0hgX23rCx')
    for channel in playListGujjarSweg:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])
    playListAnswerQuestions=scrapetube.get_playlist('PLObNowOPccbtYbBNOmIlz0zb8OeoQlNlUs')
    for channel in playListAnswerQuestions:
        if channel in idList: print('present')
        else:
            idList.append(channel['videoId'])

    return idList



def writeInFile():
    countErr=0
    countPos=0
    with open('transcriptT.txt', 'w') as fp:
        pass
    with open('errorFilesT.txt', 'w') as fp:
        pass

    for video_id  in generateListOfChannelTranscript():
        #transcripts = YouTubeTranscriptApi.list_transcripts
        try:
            transcripts=YouTubeTranscriptApi.list_transcripts((video_id));
        except:
            with open('errorFilesT.txt','a') as f:
                j=video_id
                f.write('%s\n'%j)
        else:
            
            with open('transcriptT.txt', 'a') as f:
                
                for i in transcripts:
                    s=i.fetch()
                    for list in s:
                        str=list['text']
                        f.write(str+'\n')
                        s=str.split()
                        for word in s:
                            index(word, video_id )
                    
         
def index(term, videoId):
    videoIds=postingList.get(term)
    if videoIds:
        videoIds.append(term)
    else:
        videoIds=[]
        videoIds.append(term)

    postingList.update({term:videoIds})

def readFile():
    with open("transcriptT.txt","r") as f:
        for line in f:
            a=f.split()
            for word in a:
                 index(word, 1)

        
def main():
    writeInFile()
   
    for item in postingList.keys():
        print(item+':')
        print(postingList['हीरो'])
        print('\n')

main()