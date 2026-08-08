const card = document.querySelector('.hud-card');
const reactorZone = document.querySelector('.reactor-3d-zone');


document.addEventListener('mousemove', (e) => {
    let xAxis = (window.innerWidth / 2 - e.pageX) / 30;
    let yAxis = (window.innerHeight / 2 - e.pageY) / 30;
    card.style.transform = `rotateY(${xAxis}deg) rotateX(${-yAxis}deg)`;
});

document.addEventListener('mouseleave', () => {
    card.style.transition = 'all 0.5s ease';
    card.style.transform = `rotateY(0deg) rotateX(0deg)`;
});

function updateJarvisStatus(statusText) {
    document.getElementById('jarvis-say').innerText = statusText.toUpperCase();
}

function setJarvisSpeaking(isSpeaking) {
    if (isSpeaking) {
        reactorZone.classList.add('speaking');
    } else {
        reactorZone.classList.remove('speaking');
    }
}


setInterval(() => {
    let randomCPU = Math.floor(Math.random() * (45 - 15 + 1)) + 15;
    let randomRAM = Math.floor(Math.random() * (65 - 55 + 1)) + 55;
    document.getElementById('cpu-val').innerText = randomCPU;
    document.getElementById('ram-val').innerText = randomRAM;
}, 1000);