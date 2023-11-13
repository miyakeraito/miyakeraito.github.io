function aaaa() {
    document.body.style.backgroundColor = "#" + Math.floor(Math.random() * 0xffffff).toString(16).padStart(6,"0");
    requestAnimationFrame(aaaa);
}
aaaa();