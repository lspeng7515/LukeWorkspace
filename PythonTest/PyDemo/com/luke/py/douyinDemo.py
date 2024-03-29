import douyin
from douyin.structures import Topic,Music
#定义视频下载，音频下载，MongoDB
video_file_handler=douyin.handlers.VideoFileHandler(folder='./videos')
music_file_handler=douyin.handlers.MusicFileHandler(folder='./musics')
mongo_handler=douyin.handlers.MongoHandler()
#定义下载器，并将三个处理器当做参数传递
downloader=douyin.downloaders.VideoDownloader([mongo_handler,video_file_handler,music_file_handler])
for result in douyin.hot.trend():
    for item in result.data:
        #爬取热门话题和热门音乐下面的所有视频，每个话题或音乐最多爬取100个相关视频
        downloader.download(item.videos(max=100))