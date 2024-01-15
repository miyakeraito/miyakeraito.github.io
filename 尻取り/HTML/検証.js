let n = 0;
function aaaa() {
    document.body.style.backgroundColor = `hsl(${n}deg 100%, 50%)`
    n += 100;
    n = n % 360
}
setInterval(aaaa,950);