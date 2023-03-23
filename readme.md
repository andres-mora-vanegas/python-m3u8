# Download m3u8

Project to donwload videos from any m3u8 page that contains the videos in format ts

## How works

Is required get urls that ends with extension .m3u8 like the following

163
- Example URL:

'https://proxy-09.nyc.dailymotion.com/sec(06B2xrQvupyx3v5AXa2ZbVy_tOv87rG4aq_pO93r4OdvDd4v-Fz8KbiE1oBcCVe370uWVGKJImOTYAJKoYJnO-yCUj9Aqng51u3E62Tv79w)/video/167/842/512248761_mp4_h264_aac_hq.m3u8',

- Once is added to list_episodes variable it will download a ts file with all chapters of each link

- Then need to run the next command using ffmpeg, important change the xxx with the name of ts file and mp4 destination file

```sh
ffmpeg -i xxxx.ts -acodec copy -vcodec copy xxx.mp4
```

- Once is converted the video is ready to view.