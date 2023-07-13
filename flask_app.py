from flask import Flask, request
from urllib.parse import urlparse
from threadVideo import getVideoUrl, downloadVideo
import json




app = Flask(__name__)

@app.route('/')
def hello():
    thread_url = request.args.get('thread_url')
    parsed_url = urlparse(thread_url).netloc
    if parsed_url not in ['threads.net','www.threads.net']:
        return json.dumps({'success':'false', 'msg':'error in url'}), 400, {'ContentType':'application/json'}

    video_url = getVideoUrl(thread_url)
    if video_url['success'] == 'false':
        return json.dumps(video_url), video_url['code']

    return json.dumps(downloadVideo(video_url)), 200, {'ContentType':'application/json'}
    

if __name__ == '__main__':
    app.run()