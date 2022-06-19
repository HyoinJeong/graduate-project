
#5초동안 사용자 목소리 입력 후 data폴더내에 저장
#colab 규정상 마이크 사용 금지 -> 브라우저를 이용하여 간접적으로 마이크 사용
from IPython.display import Javascript
from google.colab.output import eval_js
from base64 import b64decode
import io
import ffmpeg
import os

RECORD = """
const sleep  = time => new Promise(resolve => setTimeout(resolve, time))
const b2text = blob => new Promise(resolve => {
  const reader = new FileReader()
  reader.onloadend = e => resolve(e.srcElement.result)
  reader.readAsDataURL(blob)
})
var record = time => new Promise(async resolve => {
  stream = await navigator.mediaDevices.getUserMedia({ audio: true })
  recorder = new MediaRecorder(stream)
  chunks = []
  recorder.ondataavailable = e => chunks.push(e.data)
  recorder.start()
  await sleep(time)
  recorder.onstop = async ()=>{
    blob = new Blob(chunks)
    text = await b2text(blob)
    resolve(text)
  }
  recorder.stop()
})
"""


path="/content/gdrive//MyDrive/VoiceRecognition/static/Recording/"

#5초동안 녹음
def record(name,age,sex,sec=5):
  display(Javascript(RECORD))
  data = eval_js('record(%d)' % (sec*1000))
  binary = b64decode(data.split(',')[1])
  
  process = (ffmpeg
    .input('pipe:0')
    .output('pipe:1', format='wav')
    .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True, quiet=True, overwrite_output=True)
  )
  output, err = process.communicate(input=binary)
  
  riff_chunk_size = len(output) - 8
  q = riff_chunk_size
  b = []
  for i in range(4):
      q, r = divmod(q, 256)
      b.append(r)

  riff = output[:4] + bytes(b) + output[8:]
  
  count=0 #가지고있는 목소리파일 개수
  if not os.path.isdir(path+name+age+sex): #처음 목소리 등록할 때
    os.makedirs(path+name+age+sex)
    with open(path+name+age+sex+'/'+name+age+sex+'_'+str(count+1)+'.wav','wb') as f:
      f.write(riff)
  else:
    count=len(os.listdir(path+name+age+sex))
    with open(path+name+age+sex+'/'+name+age+sex+'_'+str(count+1)+'.wav','wb') as f:
      f.write(riff)

#5초동안 녹음
def recognition_record(sec=5):
  display(Javascript(RECORD))
  data = eval_js('record(%d)' % (sec*1000))
  binary = b64decode(data.split(',')[1])
  
  process = (ffmpeg
    .input('pipe:0')
    .output('pipe:1', format='wav')
    .run_async(pipe_stdin=True, pipe_stdout=True, pipe_stderr=True, quiet=True, overwrite_output=True)
  )
  output, err = process.communicate(input=binary)
  
  riff_chunk_size = len(output) - 8
  q = riff_chunk_size
  b = []
  for i in range(4):
      q, r = divmod(q, 256)
      b.append(r)

  riff = output[:4] + bytes(b) + output[8:]
  
  path="/content/gdrive//MyDrive/VoiceRecognition/static/Result_recording/"
  with open(path+'recognition_audio.wav','wb') as f:
      f.write(riff)

  return 'recognition_audio.wav'