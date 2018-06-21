ffmpeg -ss 00:01:03 -t 30 -i antartica1.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\antartica1.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\antartica1.avi" > "info/1.json"
ffmpeg -i tmp\\antartica1.avi -c:v libx264 -crf 0 cut_wogrey/1.mp4
del /q "tmp\\antartica1.avi"

ffmpeg -ss 00:01:40 -t 30 -i fireworks.mkv -c:v rawvideo -pix_fmt yuv420p tmp\\fireworks.avi
fprobe -v quiet -print_format json -show_format -show_streams "tmp\\fireworks.avi" > "info/2.json"
ffmpeg -i tmp\\fireworks.avi -c:v libx264 -crf 0 cut_wogrey/2.mp4
del /q "tmp\\fireworks.avi"

ffmpeg -ss 00:04:01 -t 30 -i antartica1.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\antartica1.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\antartica1.avi" > "info/3.json"
ffmpeg -i tmp\\antartica1.avi -c:v libx264 -crf 0 cut_wogrey/3.mp4
del /q "tmp\\antartica1.avi"

ffmpeg -ss 00:01:52 -t 30 -i hawaii.mkv -c:v rawvideo -pix_fmt yuv420p tmp\\hawaii.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\hawaii.avi" > "info/4.json"
ffmpeg -i tmp/hawaii.avi -c:v libx264 -crf 0 cut_wogrey/4.mp4
del /q "tmp\\hawaii.avi"

ffmpeg -ss 00:01:39 -t 30 -i antartica3.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\antartica3.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\antartica3.avi" > "info/5.json"
ffmpeg -i tmp\\antartica3.avi -c:v libx264 -crf 0 cut_wogrey/5.mp4
del /q "tmp\\antartica3.avi"

ffmpeg -ss 00:02:16 -t 30 -i antartica3.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\antartica3.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\antartica3.avi" > "info/6.json"
ffmpeg -i tmp\\antartica3.avi -c:v libx264 -crf 0 cut_wogrey/6.mp4
del /q "tmp\\antartica3.avi"

ffmpeg -ss 00:01:55 -t 30 -i colonie.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\colonie.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\colonie.avi" > "info/7.json"
ffmpeg -i tmp\\colonie.avi -c:v libx264 -crf 0 cut_wogrey/7.mp4
del /q "tmp\\colonie.avi"

ffmpeg -ss 00:01:18 -t 30 -i wasala.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\wasala.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\wasala.avi" > "info/8.json"
ffmpeg -i tmp\\wasala.avi -c:v libx264 -crf 0 cut_wogrey/8.mp4
del /q "tmp\\wasala.avi"

ffmpeg -ss 00:05:47 -t 30 -i wasala.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\wasala.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\wasala.avi" > "info/9.json"
ffmpeg -i tmp\\wasala.avi -c:v libx264 -crf 0 cut_wogrey/9.mp4
del /q "wasala.avi"
del /q "tmp\\wasala.avi"

ffmpeg -ss 00:02:07 -t 30 -i carrara.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\carrara.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\carrara.avi" > "info/10.json"
ffmpeg -i tmp\\carrara.avi -c:v libx264 -crf 0 cut_wogrey/10.mp4
del /q "tmp\\carrara.avi"

ffmpeg -ss 00:00:10 -t 30 -i edgeofspace.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\edgeofspace.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\edgeofspace.avi" > "info/11.json"
ffmpeg -i tmp\\edgeofspace.avi -c:v libx264 -crf 0 cut_wogrey/11.mp4
del /q "tmp\\edgeofspace.avi"

ffmpeg -ss 00:03:05 -t 30 -i arcachon.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\arcachon.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\arcachon.avi" > "info/12.json"
ffmpeg -i tmp\\arcachon.avi -c:v libx264 -crf 0 cut_wogrey/12.mp4
del /q "tmp\\arcachon.avi"

ffmpeg -ss 00:03:10 -t 30 -i lagrottechauvet.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\lagrottechauvet.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\lagrottechauvet.avi" > "info/13.json"
ffmpeg -i tmp\\lagrottechauvet.avi -c:v libx264 -crf 0 cut_wogrey/13.mp4
del /q "tmp\\lagrottechauvet.avi"

ffmpeg -ss 00:05:47 -t 30 -i aliens.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\aliens.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\aliens.avi" > "info/14.json"
ffmpeg -i tmp\\aliens.avi -c:v libx264 -crf 0 cut_wogrey/14.mp4
del /q "tmp\\aliens.avi"

ffmpeg -ss 00:01:50 -t 00:00:18.700 -i elisir.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\elisir1.avi
ffmpeg -ss 00:02:25 -t 00:00:11.300 -i elisir.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\elisir2.avi
ffmpeg -i tmp\\elisir1.avi -i tmp\\elisir2.avi -filter_complex "[0:v][1:v]concat=n=2:v=1:a=0[outv]" -map "[outv]" -c:v rawvideo -pix_fmt yuv420p tmp\\elisir.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\elisir.avi" > "info/15.json"
ffmpeg -i tmp\\elisir.avi -c:v libx264 -crf 0 cut_wogrey/15.mp4
del /q "tmp\\elisir.avi"
del /q "tmp\\elisir1.avi"
del /q "tmp\\elisir2.avi"

ffmpeg -ss 00:01:10 -t 30 -i spotlighthelp.mkv -c:v rawvideo -pix_fmt yuv420p tmp\\spotlighthelp.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\spotlighthelp.avi" > "info/16.json"
ffmpeg -i tmp\\spotlighthelp.avi -c:v libx264 -crf 0 cut_wogrey/16.mp4
del /q "tmp\\spotlighthelp.avi"

ffmpeg -ss 00:00:12 -t 30 -i angelfalls.mkv -c:v rawvideo -pix_fmt yuv420p tmp\\angelfalls.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\angelfalls.avi" > "info/17.json"
ffmpeg -i tmp\\angelfalls.avi -c:v libx264 -crf 0 cut_wogrey/17.mp4
del /q "tmp\\angelfalls.avi"

ffmpeg -ss 00:06:17 -t 30 -i wolfskinder.mp4 -c:v rawvideo -pix_fmt yuv420p tmp\\wolfskinder.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\wolfskinder.avi" > "info/18.json"
ffmpeg -i tmp\\wolfskinder.avi -c:v libx264 -crf 0 cut_wogrey/18.mp4
del /q "tmp\\wolfskinder.avi"

ffmpeg -ss 00:00:13 -t 30 -i nerfbattle.mkv -c:v rawvideo -pix_fmt yuv420p tmp\\nerfbattle.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\nerfbattle.avi" > "info/19.json"
ffmpeg -i tmp\\nerfbattle.avi -c:v libx264 -crf 0 cut_wogrey/19.mp4
del /q "tmp\\nerfbattle.avi"

ffmpeg -ss 00:00:16 -t 30 -i football.mkv -c:v rawvideo -pix_fmt yuv420p tmp\\football.avi
ffprobe -v quiet -print_format json -show_format -show_streams "tmp\\football.avi" > "info/20.json"
ffmpeg -i tmp\\football.avi -c:v libx264 -crf 0 cut_wogrey/20.mp4
del /q "tmp\\football.avi"
