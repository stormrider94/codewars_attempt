function speedListen(audioLength, playSpeed) {
    let AudioLengthInArray=audioLength.split(":")
    let AudioLengthInSec=parseInt(AudioLengthInArray[0])*3600 +parseInt(AudioLengthInArray[1])*60 +parseInt(AudioLengthInArray[2])
    let newAudioLength = Math.floor(AudioLengthInSec/playSpeed)
    //we need to return the new AudioLength in hh:mm:ss "time string" format
    let sec_num=parseInt(newAudioLength,10)
    var hours   = Math.floor(sec_num / 3600);
    var minutes = Math.floor((sec_num - (hours * 3600)) / 60)
    var seconds = sec_num - (hours * 3600) - (minutes * 60)
    if (hours   < 10) {hours   = "0"+hours}
    if (minutes < 10) {minutes = "0"+minutes}
    if (seconds < 10) {seconds = "0"+seconds}
    return hours+':'+minutes+':'+seconds
  }