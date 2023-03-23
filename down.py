import m3u8
import requests

list_episodes=(    
    'https://proxy-12.nyc.dailymotion.com/sec(q7wHNBo9zV_qod5lIeRMXCSv8sRsgkSvl8iAvoR-zwg4Qf41D-fwNcYLPutvMwRKTHcnBc7TppVqdTHAWtdqJCAokI-GsT5ogHj8TnvDaXE)/video/751/410/516014157_mp4_h264_aac_hq_1.m3u8',#182
)
auto=1
for url in list_episodes:
    base ='https://vod.cf.dmcdn.net'    
    req1=requests.get(url)
    m3u8_master=m3u8.loads(req1.text)
    playlist=m3u8_master.data['segments']
    with open(f"{auto}.ts",'wb') as f:
        auto2=1
        for segment in playlist:
            print(f"capitulo {auto} segmento {auto2} de {len(playlist)}")
            req2=requests.get(base+segment['uri'])
            auto2=auto2+1
            f.write(req2.content)
    
    auto=auto+1
