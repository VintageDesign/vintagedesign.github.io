(function() {
    var contador = 0;


    function setDates() {
        var date = new Date;
        var months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"];
        var hour = date.getHours(),
            minutes = (date.getMinutes() < 10) ? '0' + String(date.getMinutes()):
            date.getMinutes();
        hourTitle = document.getElementById('hour');

        if (!contador) {
            hourTitle.textContent = hour + ':' + minutes;
            contador = 1;
        }
        else {
            hourTitle.innerHTML = hour + '<span class="hidden">:</span>' +
                minutes;
            contador = 0;
        }

        var day = date.getDate(),
            month = months[date.getMonth()],
            year = date.getFullYear(),
            dateSubtitle = document.getElementById("date");


        dateSubtitle.textContent = day + ' ' + month + ' ' + year;
    }

    setDates();
    setInterval(setDates, 1000);
})()
