// put attribute data-coldown in minutes in timerElement
function startCountdown(timerElement, elementEndTime, onFinishCallback) {
    var durationInSeconds = elementEndTime * 60;

    function updateTimerDisplay() {
        if (durationInSeconds > 0) {
            var minutes = Math.floor(durationInSeconds / 60);
            var seconds = durationInSeconds % 60;

            var minutesStr = String(minutes).padStart(2, '0');
            var secondsStr = String(seconds).split('.')[0].padStart(2, '0')

            timerElement.textContent = minutesStr + ":" + secondsStr;
            durationInSeconds--;

            // Stop the countdown when it hits zero
            if (durationInSeconds <= 0) {
                clearInterval(intervalId);
                timerElement.textContent = '00:00';
                if (typeof onFinishCallback === 'function') {
                    onFinishCallback();
                }
            }
        } else {
            clearInterval(intervalId);
            timerElement.textContent = '00:00';
            if (typeof onFinishCallback === 'function') {
                onFinishCallback();
            }
        }
    }

    var intervalId = setInterval(updateTimerDisplay, 1000);

    // Initial call to update the display immediately
    updateTimerDisplay();
}
