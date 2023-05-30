function getRandomInt(max) {
    return Math.floor(Math.random() * max);
}

fetch('https://baby-names-ma.glitch.me/names.json')
    .then((response) => response.json())
    .then((json) => {

        const names = json["name"]

        let n = getRandomInt(Object.keys(names).length)

        let name2show = names[n]

        let h1 = document.getElementById("name")

        h1.innerText = name2show
    });