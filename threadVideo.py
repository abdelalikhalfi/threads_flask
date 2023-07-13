import requests
import json
import urllib.request
from urllib.parse import urlparse



def getVideoUrl(threads_url):
	path_id = urlparse(threads_url).path  # get the path from the URL ("/t/CuVwNwcse5r")
	path_id = path_id[::-1].strip('/').split('/')[0][::-1]
	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789-_'
	thread_id = 0

	for letter in path_id:
		thread_id = (thread_id * 64) + alphabet.index(letter)

	URL = "https://www.threads.net/api/graphql"
	user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
	xigappid = '238260118697367'
	xfblsd = 'hi'
	ct = 'application/x-www-form-urlencoded'
	SecFetchSite = 'same-origin'

	headers = {
		'user_agent':user_agent,
		'X-Ig-App-Id':xigappid,
		'X-Fb-Lsd':xfblsd,
		'Content-Type':ct,
		'Sec-Fetch-Site':SecFetchSite
	}

	body = {
		'lsd':'hi',
		'variables':'{"postID":"'+str(thread_id)+'"}',
		'doc_id':'6456331934413506'
	}

	r = requests.post(url=URL, headers=headers, data=body)

	data = r.json()
	if  data['data'] == None or data['data']['data']['containing_thread']['thread_items'][0]['post']['video_versions'] == None:
		return {"success":"false", "msg":"video not found", "code":404}


	try:	
		return {
		"success":"true",
		"video_id":str(thread_id),
		"video_img":data['data']['data']['containing_thread']['thread_items'][0]['post']['image_versions2']['candidates'][6]['url'],
		"video_url":data['data']['data']['containing_thread']['thread_items'][0]['post']['video_versions'][0]['url'],
		"caption":data['data']['data']['containing_thread']['thread_items'][0]['post']['caption']
		}
	except:
		return {"success":"false", "msg":"something went wrong", "code":500}

def downloadVideo(video_data):
	urllib.request.urlretrieve(video_data['video_url'], './static/videos/'+video_data['video_id']+'.mp4')
	return {"caption":video_data['caption'],"success":"true","video_id":video_data['video_id'],"threads_img":video_data['video_img'], "download_link":'/static/videos/'+video_data['video_id']+'.mp4'}



