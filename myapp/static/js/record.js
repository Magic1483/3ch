const recordButton = document.querySelector('#startRecordButton');
    const stopButton = document.querySelector('#stopRecordButton');
    
    var rec_key = true
    
    navigator.mediaDevices.getUserMedia({
    audio: true
  })
    .then(function (stream) {
    
    recordButton.addEventListener('click', control);
    
    recorder = new MediaRecorder(stream);

    // listen to dataavailable, which gets triggered whenever we have
    // an audio blob available
    recorder.addEventListener('dataavailable', onRecordingReady);
  });

  function control() {
    if(rec_key==true){
      startRecording()
      console.log('start')
      rec_key=false
    }else{
      stopRecording()
      console.log('stop')
      rec_key=true
      
    }
  }
  function startRecording() {
    
    recorder.start();
  }
  
  function stopRecording() {
    
    recorder.stop();
  }
  
  function onRecordingReady(e) {
    var audio = document.getElementById('rec');
    // e.data contains a blob representing the recording
    // audio.src = URL.createObjectURL(e.data);
    // audio.play();
    let track = document.getElementById("track").files[0];
    let formData = new FormData();

    let data = new FormData();
    data.append('audio', e.data);;
    // add form input from hidden input elsewhere on the page
    data.append('csrfmiddlewaretoken', '{{ csrf_token }}');
    fetch("/notes/notes", {
        method: 'POST',
        body: data,
    })
    
  }