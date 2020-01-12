
// credentials
var keys = {
  speechToText: [
    {
      name: 'virtual-shop---watso-speechtotext-1578734019631',
      credentials: {
        apikey: 'giWlFoTiwAuEWngH6QUdyskpPY52s8fJx-5OaEk2bMei',
        url: 'https://api.eu-de.speech-to-text.watson.cloud.ibm.com/instances/bf66765f-e5f1-4f4a-82ec-bdacd76a1af7'
      }
    }
  ]
}

// record voice
var recorder, gumStream
var recordButton = document.getElementById('recordButton')
recordButton.addEventListener('click', toggleRecording)

function toggleRecording () {
  if (recorder && recorder.state == 'recording') {
    recorder.stop()
    gumStream.getAudioTracks()[0].stop()
  } else {
    try {
      navigator.mediaDevices.getUserMedia({
        audio: true
      })
        .then(function (stream) {
          gumStream = stream
          recorder = new MediaRecorder(stream)
          recorder.ondataavailable = function (e) {
            var url = URL.createObjectURL(e.data)
            var preview = document.createElement('audio')
            preview.controls = true
            preview.src = url
            document.getElementById('Watson').appendChild(preview)
          }
          recorder.start()
        })
    } catch (error) {
      console.log(error)
    }
  }
}

// send to API
// 'audio/ogg' in Firefox

// Result + Logic

// return Output
